import { useRenderData } from "streamlit-component-lib-react-hooks"
import { createChart } from "lightweight-charts"
import React, { useRef, useEffect } from "react"
// import { ChartOptions, SeriesOptions } from "./Types"

const LightweightCharts: React.VFC = () => {

  // returns the renderData passed from Python
  // { args: object, disabled: boolean, theme: object }
  const renderData = useRenderData() 
  console.log('renderData',renderData)
  
  const type = renderData.args["chart"]
  const chartOptions = renderData.args["chartOptions"]
  const series = renderData.args["series"]
  const seriesOptions = renderData.args["cseriesOptions"]

  const chartContainerRef = useRef<HTMLDivElement>(null);
  
  console.log('chart',type)
  useEffect(
		() => {
      if(chartContainerRef.current){
        const handleResize = () => {
          chart.applyOptions({ width: chartContainerRef?.current?.clientWidth })
        }

        const chart = createChart(chartContainerRef?.current, {
          height: 300,
          ...chartOptions,
          width: chartContainerRef?.current?.clientWidth
        })

        chart.timeScale().fitContent();

        let newSeries
        switch(type) {
          case 'addAreaSeries':
            newSeries = chart.addAreaSeries({...seriesOptions })
            break
          case 'addBarSeries':
            newSeries = chart.addBarSeries({...seriesOptions })
            break
          case 'addBaselineSeries':
            newSeries = chart.addBaselineSeries({...seriesOptions })
            break
          case 'addCandlestickSeries':
            newSeries = chart.addCandlestickSeries({...seriesOptions })
            break
          case 'addHistogramSeries':
            newSeries = chart.addHistogramSeries({...seriesOptions })
            break
          default:
            newSeries = chart.addLineSeries({...seriesOptions })
        }

        // const newSeries = chart[series]({...seriesOptions })
        newSeries.setData(series)

        window.addEventListener('resize', handleResize)

        return () => { // required because how useEffect() works 
          window.removeEventListener('resize', handleResize)
          chart.remove()
        };
      }
		},
		[type, chartOptions, series, seriesOptions]
	);

	return (
		<div
			ref={chartContainerRef}
		/>
	);
}

export default LightweightCharts
