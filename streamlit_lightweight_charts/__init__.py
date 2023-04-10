import os
from typing import Dict
from enum import Enum
import streamlit.components.v1 as components

_COMPONENT_NAME = "streamlit_lightweight_charts"
_RELEASE = True

class Chart(str, Enum):
    Area = 'addAreaSeries'
    Baseline = 'addBaselineSeries'
    Histogram = 'addHistogramSeries'
    Line = 'addLineSeries'
    Bar = 'addBarSeries'
    Candlestick = 'addCandlestickSeries'

parent_dir = os.path.dirname(os.path.abspath(__file__))
build_dir = os.path.join(parent_dir, "frontend","build")

if not _RELEASE:
    _component_func = components.declare_component(
        _COMPONENT_NAME,
        # path=build_dir,
        url="http://localhost:3001",
    )
else:
    _component_func = components.declare_component(
        _COMPONENT_NAME,
        path=build_dir
    )

# Create a wrapper function for the component. This is an optional
# best practice - we could simply expose the component function returned by
# `declare_component` and call it done. The wrapper allows us to customize
# our component's API: we can pre-process its input args, post-process its
# output value, and add a docstring for users.
def renderLightweightCharts(charts: Dict, key: str = None):
    """Create a new instance of "renderLightweightCharts".

    Parameters
    ----------
    charts: <List of Dicts>

        chart: <Dict>
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

    return _component_func(
        charts=charts,
        key=key
    )


if not _RELEASE:
    import streamlit as st
    import dataSamples as data

    chartOptions = {
        "width": 600,
        "layout": {
            "textColor": 'black',
            "background": {
                "type": 'solid',
                "color": 'white'
            }
        }
    }

    # AREA chart
    seriesAreaChart = [{
        "type": 'Area',
        "data": data.seriesSingleValueData,
        "options": {}
    }]
    st.subheader("Area Chart")
    renderLightweightCharts( [
        {
            "chart": chartOptions,
            "series": seriesAreaChart,
        }
    ], 'area')
    st.markdown("---")

    # BASELINE chart
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
    st.subheader("Baseline Chart")
    renderLightweightCharts([
        {
            "chart": chartOptions,
            "series": seriesBaselineChart
        }
    ], 'baseline')
    st.markdown("---")

    # LINE charts
    seriesLineChart = [{
        "type": 'Line',
        "data": data.seriesSingleValueData,
        "options": {}
    }]
    st.subheader("Line Chart")
    renderLightweightCharts([
        {
            "chart": chartOptions,
            "series": seriesLineChart
        }
    ], 'line')
    st.markdown("---")

    # HISTOGRAM chart
    seriesHistogramChart = [{
        "type": 'Histogram',
        "data": data.seriesHistogramChart,
        "options": { "color": '#26a69a' }
    }]
    st.subheader("Histogram Chart")
    renderLightweightCharts([
        {
            "chart": chartOptions,
            "series": seriesHistogramChart
        }
    ], 'histogram')
    st.markdown("---")

    # BAR chart
    seriesBarChart = [{
        "type": 'Bar',
        "data": data.seriesBarChart,
        "options": {
            "upColor": '#26a69a',
            "downColor": '#ef5350'
        }
    }]
    st.subheader("Bar Chart")
    renderLightweightCharts([
        {
            "chart": chartOptions,
            "series": seriesBarChart
        }
    ], 'bar')
    st.markdown("---")

    # CANDLESTICK chart
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
    st.subheader("Candlestick Chart")
    renderLightweightCharts([
        {
            "chart": chartOptions,
            "series": seriesCandlestickChart
        }
    ], 'candlestick')
    st.markdown("---")

    # OVERLAID AREA chart
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

    st.markdown("---")

    # PRICE AND VOLUME chart
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
    st.subheader("Price and Volume Series Chart")
    renderLightweightCharts([
        {
            "chart": priceVolumeChartOptions,
            "series": priceVolumeSeries
        }
    ], 'priceAndVolume')
    st.markdown("---")

    # MULTIPANE charts
    chartMultipaneOptions = [
        {
            "width": 600,
            "height": 400,
            "layout": {
                "background": {
                    "type": "solid",
                    "color": 'white'
                },
                "textColor": "black"
            },
            "grid": {
                "vertLines": {
                    "color": "rgba(197, 203, 206, 0.5)"
                    },
                "horzLines": {
                    "color": "rgba(197, 203, 206, 0.5)"
                }
            },
            "crosshair": {
                "mode": 0
            },
            "priceScale": {
                "borderColor": "rgba(197, 203, 206, 0.8)"
            },
            "timeScale": {
                "borderColor": "rgba(197, 203, 206, 0.8)",
                "barSpacing": 15
                # "fixLeftEdge": True,
            },
            "watermark": {
                "visible": True,
                "fontSize": 48,
                "horzAlign": 'center',
                "vertAlign": 'center',
                "color": 'rgba(171, 71, 188, 0.3)',
                "text": 'Watermark Price',
            },
        },
        {
            "width": 600,
            "height": 100,
            "crosshair": {
                "mode": 0
            },
            "layout": {
                "background": {
                    "type": 'solid',
                    "color": 'transparent'
                },
                "textColor": 'black',
            },
            "grid": {
                "vertLines": {
                    "color": 'rgba(42, 46, 57, 0)',
                },
                "horzLines": {
                    "color": 'rgba(42, 46, 57, 0.6)',
                }
            },
            "timeScale": {
                "visible": False,
            }
        },
        {
            "width": 600,
            "height": 200,
            "layout": {
                "background": {
                    "type": "solid",
                    "color": 'white'
                },
                "textColor": "black"
            },
            "timeScale": {
                "visible": False,
            }
        }

    ]

    seriesCandlestickChart = [
        {
            "type": 'Candlestick',
            "data": data.priceCandlestickMultipane,
            "options": {
                "upColor": '#26a69a',
                "downColor": '#ef5350',
                "borderVisible": False,
                "wickUpColor": '#26a69a',
                "wickDownColor": '#ef5350'
            }
        }
    ]
    
    seriesAreaChart = [
        {
            "type": 'Baseline',
            "data": data.priceBaselineMultipane,
            "options": {
                "baseValue": { "type": "price", "price": 180 },
                "topLineColor": 'rgba( 38, 166, 154, 1)',
                "topFillColor1": 'rgba( 38, 166, 154, 0.28)',
                "topFillColor2": 'rgba( 38, 166, 154, 0.05)',
                "bottomLineColor": 'rgba( 239, 83, 80, 1)',
                "bottomFillColor1": 'rgba( 239, 83, 80, 0.05)',
                "bottomFillColor2": 'rgba( 239, 83, 80, 0.28)'
            }
        }
    ]

    seriesHistogramChart = [
        {
            "type": 'Histogram',
            "data": data.priceVolumeMultipane,
            "options": {
                "color": '#26a69a',
                "priceFormat": {
                    "type": 'volume',
                },
                "priceScaleId": "" # set as an overlay setting,
            },
            "priceScale": {
                "scaleMargins": {
                    "top": 0,
                    "bottom": 0,
                },
                "alignLabels": False
            }
        }
    ]

    st.subheader("Multipane Chart with Watermark")
    renderLightweightCharts([
        {
            "chart": chartMultipaneOptions[0],
            "series": seriesCandlestickChart
        },
        {
            "chart": chartMultipaneOptions[1],
            "series": seriesHistogramChart
        },
                {
            "chart": chartMultipaneOptions[2],
            "series": seriesAreaChart
        }
    ], 'multipane')
    st.markdown("---")
