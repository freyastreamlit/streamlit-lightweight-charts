import os
from typing import Dict
from typing import List
from enum import Enum
import streamlit.components.v1 as components
import examples.dataSamples as data

_COMPONENT_NAME = "renderLightweightChart"
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
    _component_func = components.declare_component(
        _COMPONENT_NAME,
        path=build_dir
    )


# Create a wrapper function for the component. This is an optional
# best practice - we could simply expose the component function returned by
# `declare_component` and call it done. The wrapper allows us to customize
# our component's API: we can pre-process its input args, post-process its
# output value, and add a docstring for users.
def renderLightweightChart(chartOptions: Dict, series: List, key: str = None):
    """Create a new instance of "renderLightweightChart".

    Parameters
    ----------

    chartOptions: <Dict>
        https://tradingview.github.io/lightweight-charts/docs/api/interfaces/ChartOptions

    series: <List of Dicts>
        https://tradingview.github.io/lightweight-charts/docs/series-types

        type: <str-enum>
            Area
            Bar
            Baseline
            Candlestick
            Histogram
            Line

        data: <List of Dicts> accordingly to series type

        options: <Dict> with style options

        priceScale: <Dict> optional

    key: str or None
        An optional key that uniquely identifies this component. If this is
        None, and the component's arguments are changed, the component will
        be re-mounted in the Streamlit frontend and lose its current state.

    """

    component_value = _component_func(
        chartOptions=chartOptions,
        series=series,
        key=key
    )
    return component_value


# app: `$ streamlit run renderLightweightChart/__init__.py`
if not _RELEASE:
    import streamlit as st

    chartOptions = {
        "layout": {
            "textColor": 'black',
            "background": {
                "type": 'solid',
                "color": 'white'
            }
        }
    }

    seriesAreaChart = [{
        "type": 'Area',
        "data": data.seriesSingleValueData,
        "options": {}
    }]
    st.subheader("Area Chart sample")
    renderLightweightChart( chartOptions, seriesAreaChart, 'area')
    st.markdown("---")

    seriesBaselineChart = [{
        "type": 'Baseline',
        "data": data.seriesBaselineChart,
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
    renderLightweightChart( chartOptions, seriesBaselineChart, 'baseline')
    st.markdown("---")

    seriesLineChart = [{
        "type": 'Line',
        "data": data.seriesSingleValueData,
        "options": {}
    }]
    st.subheader("Line Chart sample")
    renderLightweightChart(chartOptions, seriesLineChart, 'line')
    st.markdown("---")

    seriesHistogramChart = [{
        "type": 'Histogram',
        "data": data.seriesHistogramChart,
        "options": { "color": '#26a69a' }
    }]
    st.subheader("Histogram Chart sample")
    renderLightweightChart(chartOptions, seriesHistogramChart, 'histogram')
    st.markdown("---")

    seriesBarChart = [{
        "type": 'Bar',
        "data": data.seriesBarChart,
        "options": {
            "upColor": '#26a69a',
            "downColor": '#ef5350'
        }
    }]
    st.subheader("Bar Chart sample")
    renderLightweightChart(chartOptions, seriesBarChart, 'bar')
    st.markdown("---")

    seriesCandlestickChart = [{
        "type": 'Candlestick',
        "data": data.seriesCandlestickChart,
        "options": {
            "upColor": '#26a69a',
            "downColor": '#ef5350',
            "borderVisible": False,
            "wickUpColor": '#26a69a',
            "wickDownColor": '#ef5350'
        }
    }]
    st.subheader("Candlestick Chart sample")
    renderLightweightChart(chartOptions, seriesCandlestickChart, 'candlestick')
    st.markdown("---")

    overlaidAreaSeriesOptions = {
    	# "width": 600,
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

    seriesMultipleChart = [
        {
            "type": 'Area',
            "data": data.seriesMultipleChartArea01,
            "options": {
                "topColor": 'rgba(255, 192, 0, 0.7)',
                "bottomColor": 'rgba(255, 192, 0, 0.3)',
                "lineColor": 'rgba(255, 192, 0, 1)',
                "lineWidth": 2,
            }
        },
        {
            "type": 'Area',
            "data": data.seriesMultipleChartArea02,
            "options": {
                "topColor": 'rgba(67, 83, 254, 0.7)',
                "bottomColor": 'rgba(67, 83, 254, 0.3)',
                "lineColor": 'rgba(67, 83, 254, 1)',
                "lineWidth": 2,
            }
        }
    ]
    st.subheader("Overlaid Series Chart sample")
    renderLightweightChart(overlaidAreaSeriesOptions, seriesMultipleChart, 'multiple')

    st.markdown("---")

    priceVolumeChartOptions = {
    	# "width": 600,
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

    priceVolumeSeries = [
        {
            "type": 'Area',
            "data": data.priceVolumeSeriesArea,
            "options": {
                "topColor": 'rgba(38,198,218, 0.56)',
                "bottomColor": 'rgba(38,198,218, 0.04)',
                "lineColor": 'rgba(38,198,218, 1)',
                "lineWidth": 2,
            }
        },
        {
            "type": 'Histogram',
            "data": data.priceVolumeSeriesHistogram,
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
    st.subheader("Price and Volume Series Chart sample")
    renderLightweightChart(priceVolumeChartOptions, priceVolumeSeries)

