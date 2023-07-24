import streamlit as st
import inspect
import textwrap

import examples.OverlaidAreaHistogram as OverlaidAreaHistogram
import examples.OverlaidAreas as OverlaidAreas
import examples.DataToggling as DataToggling
import examples.MultiPaneWithPandas as MultiPaneWithPandas
import examples.MultiPaneFromCSV as MultiPaneFromCSV
import examples.LineChart as LineChart
import examples.AreaChart as AreaChart
import examples.HistogramChart as HistogramChart
import examples.CandlestickChart as CandlestickChart
import examples.BaselineChart as BaselineChart

import examples.AreaChart as AreaChart

charts = [
    "OverlaidAreaHistogram",
    "OverlaidAreas",
    "DataToggling",
    "MultiPaneWithPandas",
    "MultiPaneFromCSV",
    "LineChart",
    "AreaChart",
    "HistogramChart",
    "CandlestickChart",
    "BaselineChart",
]

params = st.experimental_get_query_params() # To get params from URL
if 'chart' not in st.session_state:
    url_param = params.get('chart', charts)[0] # get chart from URL or default
    st.session_state.chart = url_param if url_param in charts else charts[0]

current = locals()[st.session_state.chart]
current.render()

sourcelines, _ = inspect.getsourcelines(current)
with st.expander("Source Code", expanded=True):
    st.code(textwrap.dedent("".join(sourcelines[1:])))

st.sidebar.radio( 'CHARTS', charts, key='chart' )

