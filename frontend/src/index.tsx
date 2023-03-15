import React from "react"
import ReactDOM from "react-dom"
import { StreamlitProvider } from "streamlit-component-lib-react-hooks"
import StreamlitLightweightCharts from "./StreamlitLightweightCharts"

ReactDOM.render(
  <React.StrictMode>
    <StreamlitProvider>
      <StreamlitLightweightCharts />
    </StreamlitProvider>
  </React.StrictMode>,
  document.getElementById("root")
)
