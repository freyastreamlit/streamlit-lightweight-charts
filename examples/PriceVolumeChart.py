import streamlit as st
from streamlit_lightweight_charts import renderLightweightCharts

priceVolumeChartOptions = {
    "height": 400,
    "rightPriceScale": {
        "scaleMargins": {
            "top": 0.2,
            "bottom": 0.25,
        },
        "borderVisible": False,
    },
    "overlayPriceScales": {
        "scaleMargins": {
            "top": 0.7,
            "bottom": 0,
        }
    },
    "layout": {
        "background": {
            "type": 'solid',
            "color": '#131722'
        },
        "textColor": '#d1d4dc',
    },
    "grid": {
        "vertLines": {
            "color": 'rgba(42, 46, 57, 0)',
        },
        "horzLines": {
            "color": 'rgba(42, 46, 57, 0.6)',
        }
    }
}

priceVolumeSeriesArea = [
    { "time": '2019-03-01', "value": 56.96 },
    { "time": '2019-03-04', "value": 56.24 },
    { "time": '2019-03-05', "value": 56.08 },
    { "time": '2019-03-06', "value": 55.68 },
    { "time": '2019-03-07', "value": 56.30 },
    { "time": '2019-03-08', "value": 56.53 },
    { "time": '2019-03-11', "value": 57.58 },
    { "time": '2019-03-12', "value": 57.43 },
    { "time": '2019-03-13', "value": 57.66 },
    { "time": '2019-03-14', "value": 57.95 },
    { "time": '2019-03-15', "value": 58.39 },
    { "time": '2019-03-18', "value": 58.07 },
    { "time": '2019-03-19', "value": 57.50 },
    { "time": '2019-03-20', "value": 57.67 },
    { "time": '2019-03-21', "value": 58.29 },
    { "time": '2019-03-22', "value": 59.76 },
    { "time": '2019-03-25', "value": 60.08 },
    { "time": '2019-03-26', "value": 60.63 },
    { "time": '2019-03-27', "value": 60.88 },
    { "time": '2019-03-28', "value": 59.08 },
    { "time": '2019-03-29', "value": 59.13 },
    { "time": '2019-04-01', "value": 59.09 },
    { "time": '2019-04-02', "value": 58.53 },
    { "time": '2019-04-03', "value": 58.87 },
    { "time": '2019-04-04', "value": 58.99 },
    { "time": '2019-04-05', "value": 59.09 },
    { "time": '2019-04-08', "value": 59.13 },
    { "time": '2019-04-09', "value": 58.40 },
    { "time": '2019-04-10', "value": 58.61 },
    { "time": '2019-04-11', "value": 58.56 },
    { "time": '2019-04-12', "value": 58.74 },
    { "time": '2019-04-15', "value": 58.71 },
    { "time": '2019-04-16', "value": 58.79 },
    { "time": '2019-04-17', "value": 57.78 },
    { "time": '2019-04-18', "value": 58.04 },
    { "time": '2019-04-22', "value": 58.37 },
    { "time": '2019-04-23', "value": 57.15 },
    { "time": '2019-04-24', "value": 57.08 },
    { "time": '2019-04-25', "value": 55.85 },
    { "time": '2019-04-26', "value": 56.58 },
    { "time": '2019-04-29', "value": 56.84 },
    { "time": '2019-04-30', "value": 57.19 },
    { "time": '2019-05-01', "value": 56.52 },
    { "time": '2019-05-02', "value": 56.99 },
    { "time": '2019-05-03', "value": 57.24 },
    { "time": '2019-05-06', "value": 56.91 },
    { "time": '2019-05-07', "value": 56.63 },
    { "time": '2019-05-08', "value": 56.38 },
    { "time": '2019-05-09', "value": 56.48 },
    { "time": '2019-05-10', "value": 56.91 },
    { "time": '2019-05-13', "value": 56.75 },
    { "time": '2019-05-14', "value": 56.55 },
    { "time": '2019-05-15', "value": 56.81 },
    { "time": '2019-05-16', "value": 57.38 },
    { "time": '2019-05-17', "value": 58.09 },
    { "time": '2019-05-20', "value": 59.01 },
    { "time": '2019-05-21', "value": 59.50 },
    { "time": '2019-05-22', "value": 59.25 },
    { "time": '2019-05-23', "value": 58.87 },
    { "time": '2019-05-24', "value": 59.32 },
    { "time": '2019-05-28', "value": 59.57 },
]

priceVolumeSeriesHistogram = [
    { "time": '2019-03-01', "value": 10942737.00, "color": 'rgba(0, 150, 136, 0.8)' },
    { "time": '2019-03-04', "value": 13674737.00, "color": 'rgba(255,82,82, 0.8)' },
    { "time": '2019-03-05', "value": 15749545.00, "color": 'rgba(255,82,82, 0.8)' },
    { "time": '2019-03-06', "value": 13935530.00, "color": 'rgba(255,82,82, 0.8)' },
    { "time": '2019-03-07', "value": 12644171.00, "color": 'rgba(0, 150, 136, 0.8)' },
    { "time": '2019-03-08', "value": 10646710.00, "color": 'rgba(0, 150, 136, 0.8)' },
    { "time": '2019-03-11', "value": 13627431.00, "color": 'rgba(0, 150, 136, 0.8)' },
    { "time": '2019-03-12', "value": 12812980.00, "color": 'rgba(255,82,82, 0.8)' },
    { "time": '2019-03-13', "value": 14168350.00, "color": 'rgba(0, 150, 136, 0.8)' },
    { "time": '2019-03-14', "value": 12148349.00, "color": 'rgba(0, 150, 136, 0.8)' },
    { "time": '2019-03-15', "value": 23715337.00, "color": 'rgba(0, 150, 136, 0.8)' },
    { "time": '2019-03-18', "value": 12168133.00, "color": 'rgba(255,82,82, 0.8)' },
    { "time": '2019-03-19', "value": 13462686.00, "color": 'rgba(255,82,82, 0.8)' },
    { "time": '2019-03-20', "value": 11903104.00, "color": 'rgba(0, 150, 136, 0.8)' },
    { "time": '2019-03-21', "value": 10920129.00, "color": 'rgba(0, 150, 136, 0.8)' },
    { "time": '2019-03-22', "value": 25125385.00, "color": 'rgba(0, 150, 136, 0.8)' },
    { "time": '2019-03-25', "value": 15463411.00, "color": 'rgba(0, 150, 136, 0.8)' },
    { "time": '2019-03-26', "value": 12316901.00, "color": 'rgba(0, 150, 136, 0.8)' },
    { "time": '2019-03-27', "value": 13290298.00, "color": 'rgba(0, 150, 136, 0.8)' },
    { "time": '2019-03-28', "value": 20547060.00, "color": 'rgba(255,82,82, 0.8)' },
    { "time": '2019-03-29', "value": 17283871.00, "color": 'rgba(0, 150, 136, 0.8)' },
    { "time": '2019-04-01', "value": 16331140.00, "color": 'rgba(255,82,82, 0.8)' },
    { "time": '2019-04-02', "value": 11408146.00, "color": 'rgba(255,82,82, 0.8)' },
    { "time": '2019-04-03', "value": 15491724.00, "color": 'rgba(0, 150, 136, 0.8)' },
    { "time": '2019-04-04', "value": 8776028.00, "color": 'rgba(0, 150, 136, 0.8)' },
    { "time": '2019-04-05', "value": 11497780.00, "color": 'rgba(0, 150, 136, 0.8)' },
    { "time": '2019-04-08', "value": 11680538.00, "color": 'rgba(0, 150, 136, 0.8)' },
    { "time": '2019-04-09', "value": 10414416.00, "color": 'rgba(255,82,82, 0.8)' },
    { "time": '2019-04-10', "value": 8782061.00, "color": 'rgba(0, 150, 136, 0.8)' },
    { "time": '2019-04-11', "value": 9219930.00, "color": 'rgba(255,82,82, 0.8)' },
    { "time": '2019-04-12', "value": 10847504.00, "color": 'rgba(0, 150, 136, 0.8)' },
    { "time": '2019-04-15', "value": 7741472.00, "color": 'rgba(255,82,82, 0.8)' },
    { "time": '2019-04-16', "value": 10239261.00, "color": 'rgba(0, 150, 136, 0.8)' },
    { "time": '2019-04-17', "value": 15498037.00, "color": 'rgba(255,82,82, 0.8)' },
    { "time": '2019-04-18', "value": 13189013.00, "color": 'rgba(0, 150, 136, 0.8)' },
    { "time": '2019-04-22', "value": 11950365.00, "color": 'rgba(0, 150, 136, 0.8)' },
    { "time": '2019-04-23', "value": 23488682.00, "color": 'rgba(255,82,82, 0.8)' },
    { "time": '2019-04-24', "value": 13227084.00, "color": 'rgba(255,82,82, 0.8)' },
    { "time": '2019-04-25', "value": 17425466.00, "color": 'rgba(255,82,82, 0.8)' },
    { "time": '2019-04-26', "value": 16329727.00, "color": 'rgba(0, 150, 136, 0.8)' },
    { "time": '2019-04-29', "value": 13984965.00, "color": 'rgba(0, 150, 136, 0.8)' },
    { "time": '2019-04-30', "value": 15469002.00, "color": 'rgba(0, 150, 136, 0.8)' },
    { "time": '2019-05-01', "value": 11627436.00, "color": 'rgba(255,82,82, 0.8)' },
    { "time": '2019-05-02', "value": 14435436.00, "color": 'rgba(0, 150, 136, 0.8)' },
    { "time": '2019-05-03', "value": 9388228.00, "color": 'rgba(0, 150, 136, 0.8)' },
    { "time": '2019-05-06', "value": 10066145.00, "color": 'rgba(255,82,82, 0.8)' },
    { "time": '2019-05-07', "value": 12963827.00, "color": 'rgba(255,82,82, 0.8)' },
    { "time": '2019-05-08', "value": 12086743.00, "color": 'rgba(255,82,82, 0.8)' },
    { "time": '2019-05-09', "value": 14835326.00, "color": 'rgba(0, 150, 136, 0.8)' },
    { "time": '2019-05-10', "value": 10707335.00, "color": 'rgba(0, 150, 136, 0.8)' },
    { "time": '2019-05-13', "value": 13759350.00, "color": 'rgba(255,82,82, 0.8)' },
    { "time": '2019-05-14', "value": 12776175.00, "color": 'rgba(255,82,82, 0.8)' },
    { "time": '2019-05-15', "value": 10806379.00, "color": 'rgba(0, 150, 136, 0.8)' },
    { "time": '2019-05-16', "value": 11695064.00, "color": 'rgba(0, 150, 136, 0.8)' },
    { "time": '2019-05-17', "value": 14436662.00, "color": 'rgba(0, 150, 136, 0.8)' },
    { "time": '2019-05-20', "value": 20910590.00, "color": 'rgba(0, 150, 136, 0.8)' },
    { "time": '2019-05-21', "value": 14016315.00, "color": 'rgba(0, 150, 136, 0.8)' },
    { "time": '2019-05-22', "value": 11487448.00, "color": 'rgba(255,82,82, 0.8)' },
    { "time": '2019-05-23', "value": 11707083.00, "color": 'rgba(255,82,82, 0.8)' },
    { "time": '2019-05-24', "value": 8755506.00, "color": 'rgba(0, 150, 136, 0.8)' },
    { "time": '2019-05-28', "value": 3097125.00, "color": 'rgba(0, 150, 136, 0.8)' }
]

priceVolumeSeries = [
    {
        "type": 'Area',
        "data": priceVolumeSeriesArea,
        "options": {
            "topColor": 'rgba(38,198,218, 0.56)',
            "bottomColor": 'rgba(38,198,218, 0.04)',
            "lineColor": 'rgba(38,198,218, 1)',
            "lineWidth": 2,
        }
    },
    {
        "type": 'Histogram',
        "data": priceVolumeSeriesHistogram,
        "options": {
            "color": '#26a69a',
            "priceFormat": {
                "type": 'volume',
            },
            "priceScaleId": "" # set as an overlay setting,
        },
        "priceScale": {
            "scaleMargins": {
                "top": 0.7,
                "bottom": 0,
            }
        }
    }
]
st.subheader("Price with Volume Series Chart sample")

renderLightweightCharts([
    {
        "chart": priceVolumeChartOptions,
        "series": priceVolumeSeries
    }
], 'priceAndVolume')

