import { CrosshairMode, ColorType } from "lightweight-charts";

export interface ChartOptions {
    width?: number;
    height?: number;
    layout?: {
      backgroundColor?: string;
      background?: {
        type?: ColorType;
        color?: string;
      },
      textColor?: string;
    },
    grid?: {
      vertLines?: {
        color?: string;
      },
      horzLines?: {
        color?: string;
      }
    },
    crosshair?: {
      mode?: CrosshairMode;
    },
    priceScale?: {
      borderColor?: string;
    },
    timeScale?: {
      borderColor?: string;
    },
    watermark?: {
      text?: string;
      fontSize?: number;
      color?: string;
      visible?: boolean
    }
}

export interface SeriesOptions {


}