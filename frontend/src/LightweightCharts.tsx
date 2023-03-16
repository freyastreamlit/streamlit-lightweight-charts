import { useRenderData } from "streamlit-component-lib-react-hooks"
import { createChart } from "lightweight-charts"
import React, { useRef, useEffect } from "react"

const LightweightCharts: React.VFC = () => {

  // returns the renderData passed from Python
  // { args: object, disabled: boolean, theme: object }
  const renderData = useRenderData()  
  const chartOptions = renderData.args["chartOptions"]
  const series = renderData.args["series"]

  const chartContainerRef = useRef<HTMLDivElement>(null)
  
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

        for (const seriesObject of series){
          
          let newSeries
          switch(seriesObject.type) {
            case 'Area':
              newSeries = chart.addAreaSeries(seriesObject.seriesOptions)
              break
            case 'Bar':
              newSeries = chart.addBarSeries(seriesObject.seriesOptions )
              break
            case 'Baseline':
              newSeries = chart.addBaselineSeries(seriesObject.options)
              break
            case 'Candlestick':
              newSeries = chart.addCandlestickSeries(seriesObject.seriesOptions)
              break
            case 'Histogram':
              newSeries = chart.addHistogramSeries(seriesObject.seriesOptions)
              break
            case 'Line':
              newSeries = chart.addLineSeries(seriesObject.seriesOptions)
              break
            default:
                return
          }

          newSeries.setData(seriesObject.data)
        }

        window.addEventListener('resize', handleResize)
        return () => { // required because how useEffect() works 
          window.removeEventListener('resize', handleResize)
          chart.remove()
        }
      }
		},
		[series, chartOptions]
	)

	return (
		<div ref={chartContainerRef} />
	)
}

export default LightweightCharts
