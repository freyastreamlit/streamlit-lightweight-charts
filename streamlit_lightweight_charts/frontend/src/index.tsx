import React from "react"
import ReactDOM from "react-dom"
import { StreamlitProvider } from "streamlit-component-lib-react-hooks"
import LightweightCharts from "./LightweightCharts"

ReactDOM.render(
  <React.StrictMode>
    <StreamlitProvider>
      <LightweightCharts />
    </StreamlitProvider>
  </React.StrictMode>,
  document.getElementById("root")
)
