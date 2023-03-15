import os
import streamlit.components.v1 as components
from enum import Enum

_COMPONENT_NAME = "streamlit-lightweight-charts"
_RELEASE = False

class Chart(str, Enum):
    area = 'addAreaSeries'
    baseline = 'addBaselineSeries'
    histogram = 'addHistogramSeries'
    line = 'addLineSeries'
    bar = 'addBarSeries'
    candlestick = 'addCandlestickSeries'

if not _RELEASE:
    _component_func = components.declare_component(
        _COMPONENT_NAME,
        url="http://localhost:3001",
    )
else:
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(parent_dir, "frontend","build")
    _component_func = components.declare_component(_COMPONENT_NAME, path=build_dir)


# Create a wrapper function for the component. This is an optional
# best practice - we could simply expose the component function returned by
# `declare_component` and call it done. The wrapper allows us to customize
# our component's API: we can pre-process its input args, post-process its
# output value, and add a docstring for users.
def streamlit_lightweight_charts(chart:Chart, chartOptions={}, series=[], seriesOptions={}, key=None):
    """Create a new instance of "streamlit_lightweight_charts".

    Parameters
    ----------
    data: list of dictionaries
        Timeseries in format...
    colors: dictionary
        Colors...
    key: str or None
        An optional key that uniquely identifies this component. If this is
        None, and the component's arguments are changed, the component will
        be re-mounted in the Streamlit frontend and lose its current state.

    Returns
    -------
    int
        Not sure

    """

    # "default" is a special argument that specifies the initial return
    # value of the component before the user has interacted with it.
    component_value = _component_func(
        chart=chart,
        chartOptions=chartOptions,
        series=series,
        seriesOptions=seriesOptions,
        key=key,
        default=0
    )
    return component_value


# Add some test code to play with the component while it's in development.
# During development, we can run this just as we would any other Streamlit
# app: `$ streamlit run streamlit_lightweight_charts/__init__.py`
if not _RELEASE:
    import streamlit as st

    chartOptions = {
        "layout": {
            "background": {
                "color": "white"
            }
        }
    }

    seriesSingleValueData = [
        { "time": '2018-12-22', "value": 32.51 },
        { "time": '2018-12-23', "value": 31.11 },
        { "time": '2018-12-24', "value": 27.02 },
        { "time": '2018-12-25', "value": 27.32 },
        { "time": '2018-12-26', "value": 25.17 },
        { "time": '2018-12-27', "value": 28.89 },
        { "time": '2018-12-28', "value": 25.46 },
        { "time": '2018-12-29', "value": 23.92 },
        { "time": '2018-12-30', "value": 22.68 },
        { "time": '2018-12-31', "value": 22.67 },
    ];

    seriesBarData = [
        { "open": 10, "high": 10.63, "low": 9.49, "close": 9.55, "time": 1642427876 },
        { "open": 9.55, "high": 10.30, "low": 9.42, "close": 9.94, "time": 1642514276 },
        { "open": 9.94, "high": 10.17, "low": 9.92, "close": 9.78, "time": 1642600676 },
        { "open": 9.78, "high": 10.59, "low": 9.18, "close": 9.51, "time": 1642687076 },
        { "open": 9.51, "high": 10.46, "low": 9.10, "close": 10.17, "time": 1642773476 },
        { "open": 10.17, "high": 10.96, "low": 10.16, "close": 10.47, "time": 1642859876 },
        { "open": 10.47, "high": 11.39, "low": 10.40, "close": 10.81, "time": 1642946276 },
        { "open": 10.81, "high": 11.60, "low": 10.30, "close": 10.75, "time": 1643032676 },
        { "open": 10.75, "high": 11.60, "low": 10.49, "close": 10.93, "time": 1643119076 },
        { "open": 10.93, "high": 11.53, "low": 10.76, "close": 10.96, "time": 1643205476 }
    ];

    seriesHistogramData = [
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
    ];

    seriesBaselineData = [
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
    ];

    seriesOptions = {

    }

    seriesBaselineOptions = {
        "baseValue": { "type": 'price', "price": 25 },
        "topLineColor": 'rgba( 38, 166, 154, 1)',
        "topFillColor1": 'rgba( 38, 166, 154, 0.28)',
        "topFillColor2": 'rgba( 38, 166, 154, 0.05)',
        "bottomLineColor": 'rgba( 239, 83, 80, 1)',
        "bottomFillColor1": 'rgba( 239, 83, 80, 0.05)',
        "bottomFillColor2": 'rgba( 239, 83, 80, 0.28)'
    }

    st.subheader("Area Chart sample")
    return_value = streamlit_lightweight_charts(Chart.area, chartOptions, seriesSingleValueData, seriesOptions, 'area')
    st.markdown("Returned value: %s" % int(return_value))

    st.markdown("---")

    st.subheader("Baseline Chart sample")
    return_value = streamlit_lightweight_charts(Chart.baseline, chartOptions, seriesBaselineData, seriesBaselineOptions, 'baseline')
    st.markdown("Returned value: %s" % int(return_value))

    st.markdown("---")

    st.subheader("Line Chart sample")
    return_value = streamlit_lightweight_charts(Chart.line, chartOptions, seriesSingleValueData, seriesOptions, 'line')
    st.markdown("Returned value: %s" % int(return_value))

    st.markdown("---")

    st.subheader("Histogram Chart sample")
    return_value = streamlit_lightweight_charts(Chart.histogram, chartOptions, seriesHistogramData, { "color": '#26a69a' }, 'histogram')
    st.markdown("Returned value: %s" % int(return_value))

    st.markdown("---")

    st.subheader("Bar Chart sample")
    return_value = streamlit_lightweight_charts(Chart.bar, chartOptions, seriesBarData, { "upColor": '#26a69a', "downColor": '#ef5350' }, 'bar')
    st.markdown("Returned value: %s" % int(return_value))

    st.markdown("---")

    st.subheader("Candlestick Chart sample")
    return_value = streamlit_lightweight_charts(Chart.candlestick, chartOptions, seriesBarData, { "upColor": '#26a69a', "downColor": '#ef5350', "borderVisible": False, "wickUpColor": '#26a69a', "wickDownColor": '#ef5350' }, 'candlestick')
    st.markdown("Returned value: %s" % int(return_value))
