import React from "react"
import ReactDOM from "react-dom"
import { StreamlitProvider } from "streamlit-component-lib-react-hooks"
import LightweightCharts from "./LightweightCharts"
import LightweightChartsMultiplePanes from "./LightweightChartsMultiplePanes"

ReactDOM.render(
  <React.StrictMode>
    <StreamlitProvider>
      {/* <LightweightCharts /> */}
      <LightweightChartsMultiplePanes />
    </StreamlitProvider>
  </React.StrictMode>,
  document.getElementById("root")
)
