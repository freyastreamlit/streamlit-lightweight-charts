import { Streamlit } from "streamlit-component-lib"
import { useRenderData } from "streamlit-component-lib-react-hooks"
import {
  ChartOptions,
  createChart,
  IChartApi,
  MouseEventParams,
} from "lightweight-charts"

import React, { useRef, useEffect } from "react"

interface ChartsDataItems {
  chart: ChartOptions;
  series: any;
}

enum Chart{
    Area = 'addAreaSeries',
    Baseline = 'addBaselineSeries',
    Histogram = 'addHistogramSeries',
    Line = 'addLineSeries',
    Bar = 'addBarSeries',
    Candlestick = 'addCandlestickSeries',
}

const LightweightChartsMultiplePanes: React.VFC = () => {

  // returns the renderData passed from Python
  // { args: object, disabled: boolean, theme: object }
  const renderData = useRenderData()
  const chartsData = renderData.args["charts"]

  const chartsContainerRef = useRef<HTMLDivElement>(null)
  const chartElRefs = Array(chartsData.length).fill(useRef<HTMLDivElement>(null))
  const chartRefs = useRef<IChartApi[]>([])

    useEffect(() => {
      if (chartElRefs.find((ref) => !ref.current)) return;

      chartElRefs.forEach((ref, i) => {
        const chart: IChartApi = chartRefs.current[i] = createChart(
          ref.current as HTMLDivElement,{
            height: 300,
            width: chartElRefs[i].current.clientWidth,
            ...chartsData[i].chart,
          }
        );

        for (const series of chartsData[i].series){

          // @ts-ignore - dynamic access to IChartApi methods (e.g.: chart.addLineSeries() )
          const chartSeries = chart[Chart[series.type]](series.options)

          if(series.priceScale)
            chart.priceScale(series.options.priceScaleId || '').applyOptions(series.priceScale)

          chartSeries.setData(series.data)

          if(series.markers)
            chartSeries.setMarkers(series.markers)

        }

        // user clicked the 'mouse/pointer'
        chart.subscribeClick((param: MouseEventParams) => {
          if (!param.point || !param.time) { return }

          const prices: any[] = []

          chartsData.forEach((el: ChartsDataItems) => {
            el.series.forEach((series: any, idx: number) => {
              // @ts-ignore - get the whole series by idx and remove `time` and `color`
              const { time, color, ...values } = [ ...param.seriesData.values() ][idx]
              prices.push({
                'title': series.title,
                'type': series.type,
                values
              })
            })
          })

          Streamlit.setComponentValue({
            'time': param.time,
            prices
          })

        })

        // user moved the 'pointer'
        // chart.subscribeCrosshairMove(param => {
        //   console.log('CrossHair',param)
        // })

        // chart.timeScale().subscribeVisibleTimeRangeChange(param => {
        //   console.log('TimeRangeChange',param)
        // });

        chart.timeScale().fitContent();

      })
  
      const charts = chartRefs.current.map((c) => c as IChartApi);
      
      if(chartsData.length > 1){ // sync charts
        charts.forEach((chart) => {
          if (!chart) return;

          chart.timeScale().subscribeVisibleTimeRangeChange((e) => {
            charts
              .filter((c) => c !== chart)
              .forEach((c) => {
                c.timeScale().applyOptions({
                  rightOffset: chart.timeScale().scrollPosition()
          }) }) })

          chart.timeScale().subscribeVisibleLogicalRangeChange((range) => {
            if (range) {
              charts
                .filter((c) => c !== chart)
                .forEach((c) => {
                  c.timeScale().setVisibleLogicalRange({
                    from: range?.from,
                    to: range?.to
          }) }) } })

          // chart.subscribeCrosshairMove((handler) => {
          //   charts
          //     .filter((c) => c !== chart)
          //     .forEach((c) => {
          //       // if (handler.time !== undefined) {
          //       //   var xx = c.timeScale().timeToCoordinate(handler.time);
          //       //   c.setCrossHairXY(xx,50,true);
          //       // } else if (handler.point !== undefined){
          //       //   c.setCrossHairXY(handler.point.x,10,false);
          //       // }
          //       // c.timeScale().applyOptions({
          //       //   rightOffset: chart.timeScale().scrollPosition()
          //       // })
          //       console.log('handler',handler)
          //       if (handler.time !== undefined) {
          //         const xx = c.timeScale().timeToCoordinate(handler.time);
          //         if(xx) c.timeScale().scrollToPosition(xx,true)
          //         console.log('const xx',xx)
          //       }
          //     })
          // })

      }) }

      // const handleResize = () => {
      //   chart.applyOptions({ width: chartsContainerRef?.current?.clientWidth })
      // }
      // window.addEventListener('resize', handleResize)
      return () => { // required because how useEffect() works
        charts.forEach((chart) => {
          chart.remove()
        })
      }

    }, [ chartsData, chartElRefs, chartRefs])


    return (
      <div ref={chartsContainerRef}>
        {chartElRefs.map((ref, i) => (
          <div
            ref={ref}
            id={`lightweight-charts-${i}`}
            key={`lightweight-charts-${i}`}
          />
        ))}
      </div>
    )

}

export default LightweightChartsMultiplePanes
