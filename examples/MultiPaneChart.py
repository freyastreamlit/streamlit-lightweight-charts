import streamlit as st
from streamlit_lightweight_charts import renderLightweightCharts

import json
import numpy as np
import yfinance as yf
import pandas as pd
import pandas_ta as ta

# Request historic pricing data via finance.yahoo.com API
df = yf.Ticker('AAPL').history(period='4mo')[['Open', 'High', 'Low', 'Close', 'Volume']]

# Some data wrangling to match required format
df = df.reset_index()
df.columns = ['time','open','high','low','close','volume']                  # rename columns
df['time'] = df['time'].dt.strftime('%Y-%m-%d')                             # Date to string
df['color'] = np.where(  df['open'] > df['close'], '#ef5350', '#26a69a')    # bull or bear
df.ta.macd(close='close', fast=6, slow=12, signal=5, append=True)          # calculate macd

# extract to JSON format
candles = json.loads(df.to_json(orient = "records"))
volume = json.loads(df.rename(columns={"volume": "value",}).to_json(orient = "records"))
macd_fast = json.loads(df.rename(columns={"MACDh_6_12_5": "value"}).to_json(orient = "records"))
macd_slow = json.loads(df.rename(columns={"MACDs_6_12_5": "value"}).to_json(orient = "records"))
df['color'] = np.where(  df['MACD_6_12_5'] > 0, '#26a69a', '#ef5350')  # MACD histogram color
macd_hist = json.loads(df.rename(columns={"MACD_6_12_5": "value"}).to_json(orient = "records"))


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
        },
        "watermark": {
            "visible": True,
            "fontSize": 48,
            "horzAlign": 'center',
            "vertAlign": 'center',
            "color": 'rgba(171, 71, 188, 0.3)',
            "text": 'AAPL - D1',
        }
    },
    {
        "width": 600,
        "height": 100,
        # "crosshair": {
        #     "mode": 0
        # },
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
        },
        "watermark": {
            "visible": True,
            "fontSize": 18,
            "horzAlign": 'left',
            "vertAlign": 'top',
            "color": 'rgba(171, 71, 188, 0.7)',
            "text": 'Volume',
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
        },
        "watermark": {
            "visible": True,
            "fontSize": 18,
            "horzAlign": 'left',
            "vertAlign": 'center',
            "color": 'rgba(171, 71, 188, 0.7)',
            "text": 'MACD',
        }
    }

]

seriesCandlestickChart = [
    {
        "type": 'Candlestick',
        "data": candles,
        "options": {
            "upColor": '#26a69a',
            "downColor": '#ef5350',
            "borderVisible": False,
            "wickUpColor": '#26a69a',
            "wickDownColor": '#ef5350'
        }
    }
]

seriesMACDchart = [
    {
        "type": 'Line',
        "data": macd_fast,
        "options": {
            "color": 'blue',
            "lineWidth": 2
        }
    },
    {
        "type": 'Line',
        "data": macd_slow,
        "options": {
            "color": 'green',
            "lineWidth": 2
        }
    },
    {
        "type": 'Histogram',
        "data": macd_hist,
        "options": {
            "color": 'red',
            "lineWidth": 1
        }
    }
]


seriesVolumeChart = [
    {
        "type": 'Histogram',
        "data": volume,
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

st.subheader("Multipane Chart with Pandas")

renderLightweightCharts([
    {
        "chart": chartMultipaneOptions[0],
        "series": seriesCandlestickChart
    },
    {
        "chart": chartMultipaneOptions[1],
        "series": seriesVolumeChart
    },
    {
        "chart": chartMultipaneOptions[2],
        "series": seriesMACDchart
    }
], 'multipane')