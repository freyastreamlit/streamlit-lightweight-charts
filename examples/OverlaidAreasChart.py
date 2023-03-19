import streamlit as st
from streamlit_lightweight_charts import renderLightweightCharts

overlaidAreaSeriesOptions = {
    "height": 400,
    "rightPriceScale": {
        "scaleMargins": {
            "top": 0.1,
            "bottom": 0.1,
        },
        "mode": 2, # PriceScaleMode: 0-Normal, 1-Logarithmic, 2-Percentage, 3-IndexedTo100
        "borderColor": 'rgba(197, 203, 206, 0.4)',
    },
    "timeScale": {
        "borderColor": 'rgba(197, 203, 206, 0.4)',
    },
    "layout": {
        "background": {
            "type": 'solid',
            "color": '#100841'
        },
        "textColor": '#ffffff',
    },
    "grid": {
        "vertLines": {
            "color": 'rgba(197, 203, 206, 0.4)',
            "style": 1, # LineStyle: 0-Solid, 1-Dotted, 2-Dashed, 3-LargeDashed
        },
        "horzLines": {
            "color": 'rgba(197, 203, 206, 0.4)',
            "style": 1, # LineStyle: 0-Solid, 1-Dotted, 2-Dashed, 3-LargeDashed
        }
    }
}

seriesMultipleChartArea01 = [
    { "time": '2019-03-01', "value": 42.58 },
    { "time": '2019-03-04', "value": 42.64 },
    { "time": '2019-03-05', "value": 42.74 },
    { "time": '2019-03-06', "value": 42.7 },
    { "time": '2019-03-07', "value": 42.63 },
    { "time": '2019-03-08', "value": 42.25 },
    { "time": '2019-03-11', "value": 42.33 },
    { "time": '2019-03-12', "value": 42.46 },
    { "time": '2019-03-13', "value": 43.83 },
    { "time": '2019-03-14', "value": 43.95 },
    { "time": '2019-03-15', "value": 43.87 },
    { "time": '2019-03-18', "value": 44.24 },
    { "time": '2019-03-19', "value": 44.47 },
    { "time": '2019-03-20', "value": 44.53 },
    { "time": '2019-03-21', "value": 44.53 },
    { "time": '2019-03-22', "value": 43.95 },
    { "time": '2019-03-25', "value": 43.53 },
    { "time": '2019-03-26', "value": 43.82 },
    { "time": '2019-03-27', "value": 43.59 },
    { "time": '2019-03-28', "value": 43.63 },
    { "time": '2019-03-29', "value": 43.72 },
    { "time": '2019-04-01', "value": 44.09 },
    { "time": '2019-04-02', "value": 44.23 },
    { "time": '2019-04-03', "value": 44.23 },
    { "time": '2019-04-04', "value": 44.15 },
    { "time": '2019-04-05', "value": 44.53 },
    { "time": '2019-04-08', "value": 45.23 },
    { "time": '2019-04-09', "value": 44.99 },
    { "time": '2019-04-10', "value": 45.04 },
    { "time": '2019-04-11', "value": 44.87 },
    { "time": '2019-04-12', "value": 44.67 },
    { "time": '2019-04-15', "value": 44.67 },
    { "time": '2019-04-16', "value": 44.48 },
    { "time": '2019-04-17', "value": 44.62 },
    { "time": '2019-04-18', "value": 44.39 },
    { "time": '2019-04-22', "value": 45.04 },
    { "time": '2019-04-23', "value": 45.02 },
    { "time": '2019-04-24', "value": 44.13 },
    { "time": '2019-04-25', "value": 43.96 },
    { "time": '2019-04-26', "value": 43.31 },
    { "time": '2019-04-29', "value": 43.02 },
    { "time": '2019-04-30', "value": 43.73 },
    { "time": '2019-05-01', "value": 43.08 },
    { "time": '2019-05-02', "value": 42.63 },
    { "time": '2019-05-03', "value": 43.08 },
    { "time": '2019-05-06', "value": 42.93 },
    { "time": '2019-05-07', "value": 42.22 },
    { "time": '2019-05-08', "value": 42.28 },
    { "time": '2019-05-09', "value": 41.65 },
    { "time": '2019-05-10', "value": 41.5 },
    { "time": '2019-05-13', "value": 41.23 },
    { "time": '2019-05-14', "value": 41.55 },
    { "time": '2019-05-15', "value": 41.77 },
    { "time": '2019-05-16', "value": 42.28 },
    { "time": '2019-05-17', "value": 42.34 },
    { "time": '2019-05-20', "value": 42.58 },
    { "time": '2019-05-21', "value": 42.75 },
    { "time": '2019-05-22', "value": 42.34 },
    { "time": '2019-05-23', "value": 41.34 },
    { "time": '2019-05-24', "value": 41.76 },
    { "time": '2019-05-28', "value": 41.625 },
]

seriesMultipleChartArea02 = [
    { "time": '2019-03-01', "value": 174.97 },
    { "time": '2019-03-04', "value": 175.85 },
    { "time": '2019-03-05', "value": 175.53 },
    { "time": '2019-03-06', "value": 174.52 },
    { "time": '2019-03-07', "value": 172.5 },
    { "time": '2019-03-08', "value": 172.91 },
    { "time": '2019-03-11', "value": 178.9 },
    { "time": '2019-03-12', "value": 180.91 },
    { "time": '2019-03-13', "value": 181.71 },
    { "time": '2019-03-14', "value": 183.73 },
    { "time": '2019-03-15', "value": 186.12 },
    { "time": '2019-03-18', "value": 188.02 },
    { "time": '2019-03-19', "value": 186.53 },
    { "time": '2019-03-20', "value": 188.16 },
    { "time": '2019-03-21', "value": 195.09 },
    { "time": '2019-03-22', "value": 191.05 },
    { "time": '2019-03-25', "value": 188.74 },
    { "time": '2019-03-26', "value": 186.79 },
    { "time": '2019-03-27', "value": 188.47 },
    { "time": '2019-03-28', "value": 188.72 },
    { "time": '2019-03-29', "value": 189.95 },
    { "time": '2019-04-01', "value": 191.24 },
    { "time": '2019-04-02', "value": 194.02 },
    { "time": '2019-04-03', "value": 195.35 },
    { "time": '2019-04-04', "value": 195.69 },
    { "time": '2019-04-05', "value": 197 },
    { "time": '2019-04-08', "value": 200.1 },
    { "time": '2019-04-09', "value": 199.5 },
    { "time": '2019-04-10', "value": 200.62 },
    { "time": '2019-04-11', "value": 198.95 },
    { "time": '2019-04-12', "value": 198.87 },
    { "time": '2019-04-15', "value": 199.23 },
    { "time": '2019-04-16', "value": 199.25 },
    { "time": '2019-04-17', "value": 203.13 },
    { "time": '2019-04-18', "value": 203.86 },
    { "time": '2019-04-22', "value": 204.53 },
    { "time": '2019-04-23', "value": 207.48 },
    { "time": '2019-04-24', "value": 207.16 },
    { "time": '2019-04-25', "value": 205.28 },
    { "time": '2019-04-26', "value": 204.3 },
    { "time": '2019-04-29', "value": 204.61 },
    { "time": '2019-04-30', "value": 200.67 },
    { "time": '2019-05-01', "value": 210.52 },
    { "time": '2019-05-02', "value": 209.15 },
    { "time": '2019-05-03', "value": 211.75 },
    { "time": '2019-05-06', "value": 208.48 },
    { "time": '2019-05-07', "value": 202.86 },
    { "time": '2019-05-08', "value": 202.9 },
    { "time": '2019-05-09', "value": 200.72 },
    { "time": '2019-05-10', "value": 197.18 },
    { "time": '2019-05-13', "value": 185.72 },
    { "time": '2019-05-14', "value": 188.66 },
    { "time": '2019-05-15', "value": 190.92 },
    { "time": '2019-05-16', "value": 190.08 },
    { "time": '2019-05-17', "value": 189 },
    { "time": '2019-05-20', "value": 183.09 },
    { "time": '2019-05-21', "value": 186.6 },
    { "time": '2019-05-22', "value": 182.78 },
    { "time": '2019-05-23', "value": 179.66 },
    { "time": '2019-05-24', "value": 178.97 },
    { "time": '2019-05-28', "value": 179.07 },
]

seriesOverlaidChart = [
    {
        "type": 'Area',
        "data": seriesMultipleChartArea01,
        "options": {
            "topColor": 'rgba(255, 192, 0, 0.7)',
            "bottomColor": 'rgba(255, 192, 0, 0.3)',
            "lineColor": 'rgba(255, 192, 0, 1)',
            "lineWidth": 2,
        }
    },
    {
        "type": 'Area',
        "data": seriesMultipleChartArea02,
        "options": {
            "topColor": 'rgba(67, 83, 254, 0.7)',
            "bottomColor": 'rgba(67, 83, 254, 0.3)',
            "lineColor": 'rgba(67, 83, 254, 1)',
            "lineWidth": 2,
        }
    }
]
st.subheader("Overlaid Series Chart sample")

renderLightweightCharts([
    {
        "chart": overlaidAreaSeriesOptions,
        "series": seriesOverlaidChart
    }
], 'overlaid')
