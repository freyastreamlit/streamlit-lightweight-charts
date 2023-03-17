import streamlit as st
from streamlit_lightweight_charts import renderLightweightChart

chartOptions = {
    "layout": {
        "textColor": 'black',
        "background": {
            "type": 'solid',
            "color": 'white'
        }
    }
}

seriesHistogramChart = [{
    "type": 'Histogram',
    "data": [
        { "value": 1, "time": 1642425322 },
        { "value": 8, "time": 1642511722 },
        { "value": 10, "time": 1642598122 },
        { "value": 20, "time": 1642684522 },
        { "value": 3, "time": 1642770922, "color": 'red' },
        { "value": 43, "time": 1642857322 },
        { "value": 41, "time": 1642943722, "color": 'red' },
        { "value": 43, "time": 1643030122 },
        { "value": 56, "time": 1643116522 },
        { "value": 46, "time": 1643202922, "color": 'red' }
    ],
    "options": { "color": '#26a69a' }
}]

st.subheader("Histogram Chart sample")
renderLightweightChart( chartOptions, seriesHistogramChart, 'histogram')