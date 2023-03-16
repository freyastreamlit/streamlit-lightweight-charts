import streamlit as st
import streamlit_lightweight_charts

chartOptions = {
    "layout": {
        "textColor": 'black',
        "background": {
            "type": 'solid',
            "color": 'white'
        }
    }
}

seriesBaselineChart = [{
    "type": 'Baseline',
    "data": [
        { "value": 1, "time": 1642425322 },
        { "value": 8, "time": 1642511722 },
        { "value": 10, "time": 1642598122 },
        { "value": 20, "time": 1642684522 },
        { "value": 3, "time": 1642770922 },
        { "value": 43, "time": 1642857322 },
        { "value": 41, "time": 1642943722 },
        { "value": 43, "time": 1643030122 },
        { "value": 56, "time": 1643116522 },
        { "value": 46, "time": 1643202922 }
    ],
    "options": {
        "baseValue": { "type": "price", "price": 25 },
        "topLineColor": 'rgba( 38, 166, 154, 1)',
        "topFillColor1": 'rgba( 38, 166, 154, 0.28)',
        "topFillColor2": 'rgba( 38, 166, 154, 0.05)',
        "bottomLineColor": 'rgba( 239, 83, 80, 1)',
        "bottomFillColor1": 'rgba( 239, 83, 80, 0.05)',
        "bottomFillColor2": 'rgba( 239, 83, 80, 0.28)'
    }
}]

st.subheader("Baseline Chart sample")
streamlit_lightweight_charts( chartOptions, seriesBaselineChart, 'baseline')