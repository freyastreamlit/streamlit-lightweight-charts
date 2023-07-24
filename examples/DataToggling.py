import streamlit as st
from streamlit_lightweight_charts import renderLightweightCharts
import streamlit_lightweight_charts.dataSamples as data

chartOptions = {
    "layout": {
        "textColor": 'black',
        "background": {
            "type": 'solid',
            "color": 'white'
        }
    }
}

def render():
    st.subheader("Data Toggling for an Area Chart")

    data_select = st.radio('Select data source:', ('Area 01', 'Area 02'))

    if data_select == 'Area 01':
        renderLightweightCharts( [
            {
                "chart": chartOptions,
                "series": [{
                    "type": 'Area',
                    "data": data.seriesMultipleChartArea01,
                    "options": {}
                }],
            }
        ], 'area')
    else:
        renderLightweightCharts( [
            {
                "chart": chartOptions,
                "series": [{
                    "type": 'Area',
                    "data": data.seriesMultipleChartArea02,
                    "options": {}
                }],
            }
        ], 'area')
