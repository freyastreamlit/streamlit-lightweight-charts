import streamlit as st
from streamlit_lightweight_charts import renderLightweightCharts
import streamlit_lightweight_charts.dataSamples as data

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

seriesOverlaidChart = [
    {
        "type": 'Area',
        "data": data.seriesMultipleChartArea01,
        "options": {
            "topColor": 'rgba(255, 192, 0, 0.7)',
            "bottomColor": 'rgba(255, 192, 0, 0.3)',
            "lineColor": 'rgba(255, 192, 0, 1)',
            "lineWidth": 2,
        },
        "markers": [
            {
                "time": '2019-04-08',
                "position": 'aboveBar',
                "color": 'rgba(255, 192, 0, 1)',
                "shape": 'arrowDown',
                "text": 'H',
                "size": 3
            },
            {
                "time": '2019-05-13',
                "position": 'belowBar',
                "color": 'rgba(255, 192, 0, 1)',
                "shape": 'arrowUp',
                "text": 'L',
                "size": 3
            },
        ]
    },
    {
        "type": 'Area',
        "data": data.seriesMultipleChartArea02,
        "options": {
            "topColor": 'rgba(67, 83, 254, 0.7)',
            "bottomColor": 'rgba(67, 83, 254, 0.3)',
            "lineColor": 'rgba(67, 83, 254, 1)',
            "lineWidth": 2,
        },
        "markers": [
            {
                "time": '2019-05-03',
                "position": 'aboveBar',
                "color": 'rgba(67, 83, 254, 1)',
                "shape": 'arrowDown',
                "text": 'PEAK',
                "size": 3
            },
        ]
    }
]
st.subheader("Overlaid Series with Markers")

renderLightweightCharts([
    {
        "chart": overlaidAreaSeriesOptions,
        "series": seriesOverlaidChart
    }
], 'overlaid')
