const COLORS = ['#1a73e8','#f44336','#4caf50','#ff9800','#9c27b0','#00bcd4','#ff5722','#607d8b','#cddc39','#e91e63'];
const OWSERVER_DEVICE_PATTERN = /^sensor\.(ds18b20|ds18s20|ds1822|ds1820|ds2438|ds2406|ds2408|ds2423|ds2450|eds)[a-z0-9]*_[0-9a-f]{16}_temperature$/i;

class OWServerPanel extends HTMLElement {
  connectedCallback() {
    this.attachShadow({ mode: "open" });
    this.shadowRoot.innerHTML = `
      <style>
        :host { display: block; padding: 20px; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; color: var(--primary-text-color, #e0e0e0); }
        h1 { font-size: 1.5rem; margin-bottom: 20px; display: flex; align-items: center; gap: 10px; }
        h1 small { font-size: 0.8rem; opacity: 0.6; font-weight: normal; }
        .controls { display: flex; gap: 10px; align-items: center; margin-bottom: 20px; flex-wrap: wrap; }
        .controls select, .controls button {
          background: var(--card-background-color, #1e1e1e); color: var(--primary-text-color, #e0e0e0); border: 1px solid var(--divider-color, #333); padding: 8px 14px; border-radius: 6px; font-size: 0.9rem;
        }
        .controls button { background: var(--primary-color, #1a73e8); color: #fff; border: none; cursor: pointer; }
        .controls button:hover { opacity: 0.8; }
        .chart-container { background: var(--card-background-color, #1e1e1e); border-radius: 10px; padding: 16px; margin-bottom: 16px; }
        .chart-container canvas { width: 100% !important; }
        .error { padding: 20px; text-align: center; }
        .loading { text-align: center; padding: 40px; }
        .spinner { width: 40px; height: 40px; border: 3px solid var(--divider-color, #333); border-top-color: var(--primary-color, #1a73e8); border-radius: 50%; animation: spin 0.8s linear infinite; margin: 20px auto; }
        @keyframes spin { to { transform: rotate(360deg); } }
        .stats { display: flex; gap: 20px; flex-wrap: wrap; margin-bottom: 20px; }
        .stat-card { background: var(--card-background-color, #1e1e1e); border-radius: 10px; padding: 16px 24px; flex: 1; min-width: 120px; }
        .stat-card .value { font-size: 1.8rem; font-weight: bold; color: var(--primary-text-color, #fff); }
        .stat-card .label { font-size: 0.8rem; opacity: 0.6; margin-top: 4px; }
      </style>
      <h1>
        <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2a3 3 0 0 0-3 3v7.5a5 5 0 1 0 6 0V5a3 3 0 0 0-3-3z"/><circle cx="12" cy="17" r="2" fill="currentColor" stroke="none"/></svg>
        OW-SERVER Temperature History
        <small id="updateInfo"></small>
      </h1>
      <div class="controls">
        <select id="rangeSelect">
          <option value="1">Last hour</option>
          <option value="6" selected>Last 6 hours</option>
          <option value="12">Last 12 hours</option>
          <option value="24">Last 24 hours</option>
          <option value="72">Last 3 days</option>
          <option value="168">Last week</option>
        </select>
        <button id="refreshBtn">&#x21bb; Refresh</button>
        <span id="sensorCount"></span>
      </div>
      <div class="stats" id="stats"></div>
      <div id="charts"></div>
      <div id="loading" class="loading"><div class="spinner"></div>Loading sensor data...</div>
    `;

    this.shadowRoot.getElementById('refreshBtn').addEventListener('click', () => this.loadData());
    this.shadowRoot.getElementById('rangeSelect').addEventListener('change', () => this.loadData());

    this._loadChartJS();
  }

  async _loadChartJS() {
    if (window.Chart) { this.loadData(); return; }
    const script = document.createElement('script');
    script.src = 'https://cdn.jsdelivr.net/npm/chart.js@4/dist/chart.umd.min.js';
    script.onload = () => {
      const script2 = document.createElement('script');
      script2.src = 'https://cdn.jsdelivr.net/npm/chartjs-adapter-date-fns@3/dist/chartjs-adapter-date-fns.bundle.min.js';
      script2.onload = () => this.loadData();
      document.head.appendChild(script2);
    };
    document.head.appendChild(script);
  }

  async loadData() {
    const root = this.shadowRoot;
    const chartsDiv = root.getElementById('charts');
    const loadingDiv = root.getElementById('loading');
    const statsDiv = root.getElementById('stats');
    const sensorCount = root.getElementById('sensorCount');
    const updateInfo = root.getElementById('updateInfo');

    loadingDiv.style.display = 'block';
    chartsDiv.innerHTML = '';
    statsDiv.innerHTML = '';

    try {
      const resp = await fetch('/api/states');
      if (!resp.ok) throw new Error(`API error: ${resp.status}`);
      const states = await resp.json();

      const sensors = states.filter(s => OWSERVER_DEVICE_PATTERN.test(s.entity_id));
      sensorCount.textContent = `${sensors.length} sensor${sensors.length > 1 ? 's' : ''}`;

      if (sensors.length === 0) {
        loadingDiv.style.display = 'none';
        chartsDiv.innerHTML = '<div class="error">No OW-SERVER temperature sensors found.</div>';
        return;
      }

      const hours = parseInt(root.getElementById('rangeSelect').value);
      const start = new Date(Date.now() - hours * 3600000);

      updateInfo.textContent = 'updated just now';

      const entityIds = sensors.map(s => s.entity_id);
      const histResp = await fetch(`/api/history/period/${start.toISOString()}?filter_entity_id=${entityIds.join(',')}&minimal_response&no_attributes`);
      if (!histResp.ok) throw new Error(`History API error: ${histResp.status}`);
      const history = await histResp.json();

      const historyMap = {};
      history.forEach(h => {
        h.forEach(entry => {
          if (!historyMap[entry.entity_id]) historyMap[entry.entity_id] = [];
          historyMap[entry.entity_id].push(entry);
        });
      });

      let currentTemps = sensors.map(s => ({
        name: s.attributes?.friendly_name || s.entity_id,
        temp: s.state !== 'unavailable' && s.state !== 'unknown' ? parseFloat(s.state) : null,
        entity_id: s.entity_id,
        history: historyMap[s.entity_id] || []
      }));
      currentTemps.sort((a, b) => (a.temp ?? -Infinity) > (b.temp ?? -Infinity) ? -1 : 1);

      statsDiv.innerHTML = currentTemps.map(s => {
        const cls = s.temp !== null ? (s.temp < 10 ? 'color:#42a5f5' : s.temp < 25 ? 'color:#ff9800' : 'color:#f44336') : '';
        return `<div class="stat-card"><div class="value" style="${cls}">${s.temp !== null ? s.temp.toFixed(1) + '°C' : '--'}</div><div class="label" title="${s.entity_id}">${s.name.replace('OW-SERVER ', '')}</div></div>`;
      }).join('');

      sensors.forEach((sensor, idx) => {
        const entityHistory = historyMap[sensor.entity_id] || [];
        const data = entityHistory
          .filter(e => e.state !== 'unavailable' && e.state !== 'unknown' && !isNaN(parseFloat(e.state)))
          .map(e => ({ x: new Date(e.last_changed || e.last_updated), y: parseFloat(e.state) }));

        const container = document.createElement('div');
        container.className = 'chart-container';
        container.innerHTML = `
          <div style="display:flex;justify-content:space-between;margin-bottom:10px">
            <strong>${sensor.attributes?.friendly_name || sensor.entity_id}</strong>
            <span style="opacity:0.6;font-size:0.9rem">${sensor.entity_id}</span>
          </div>
          <canvas id="chart-${idx}"></canvas>
        `;
        chartsDiv.appendChild(container);

        const ctx = container.querySelector(`#chart-${idx}`).getContext('2d');
        new Chart(ctx, {
          type: 'line',
          data: {
            datasets: [{
              label: sensor.attributes?.friendly_name || sensor.entity_id,
              data: data,
              borderColor: COLORS[idx % COLORS.length],
              backgroundColor: COLORS[idx % COLORS.length] + '20',
              fill: true,
              tension: 0.3,
              pointRadius: 0,
              borderWidth: 2,
            }]
          },
          options: {
            responsive: true,
            maintainAspectRatio: false,
            animation: false,
            plugins: { legend: { display: false } },
            scales: {
              x: { type: 'time', time: { tooltipFormat: 'MMM d, HH:mm', displayFormats: { hour: 'HH:mm', day: 'MMM d' } }, grid: { color: '#333' }, ticks: { color: '#888', maxTicksLimit: 8 } },
              y: { grid: { color: '#333' }, ticks: { color: '#888', callback: v => v + '°C' } }
            },
            interaction: { intersect: false, mode: 'nearest' }
          }
        });
      });

    } catch (err) {
      chartsDiv.innerHTML = `<div class="error">Error: ${err.message}</div>`;
    } finally {
      loadingDiv.style.display = 'none';
    }
  }
}
customElements.define("owserver-panel", OWServerPanel);
