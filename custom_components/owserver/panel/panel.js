class OWServerPanel extends HTMLElement {
  connectedCallback() {
    this.attachShadow({ mode: "open" });
    this.shadowRoot.innerHTML = `
      <style>
        :host { display: block; height: 100%; }
        iframe { width: 100%; height: 100%; border: none; }
      </style>
      <iframe src="/api/owserver/panel"></iframe>
    `;
  }
}
customElements.define("owserver-panel", OWServerPanel);
