<script setup>
import {ref, onMounted} from "vue";
import * as echarts from "echarts";

const echartsRef = ref(null);
let myChart87 = null;
let option87 = null;
onMounted(() => {
    myChart87 = echarts.init(echartsRef.value, 'dark');
    const dataBJ = [
        [1, 55, 9, 56, 0.46, 18, 6, '良'],
        [2, 25, 11, 21, 0.65, 34, 9, '优'],
        [3, 56, 7, 63, 0.3, 14, 5, '良'],
        [4, 33, 7, 29, 0.33, 16, 6, '优'],
        [5, 42, 24, 44, 0.76, 40, 16, '优'],
        [6, 82, 58, 90, 1.77, 68, 33, '良'],
        [7, 74, 49, 77, 1.46, 48, 27, '良'],
        [8, 78, 55, 80, 1.29, 59, 29, '良'],
        [9, 267, 216, 280, 4.8, 108, 64, '重度污染'],
        [10, 185, 127, 216, 2.52, 61, 27, '中度污染'],
        [11, 39, 19, 38, 0.57, 31, 15, '优'],
        [12, 41, 11, 40, 0.43, 21, 7, '优'],
    ];
    const dataGZ = [
        [1, 26, 37, 27, 1.163, 27, 13, '优'],
        [2, 85, 62, 71, 1.195, 60, 8, '良'],
        [3, 78, 38, 74, 1.363, 37, 7, '良'],
        [4, 21, 21, 36, 0.634, 40, 9, '优'],
        [5, 93, 77, 104, 1.165, 53, 7, '良'],
        [6, 99, 130, 227, 3.97, 55, 15, '良'],
        [7, 146, 84, 139, 1.094, 40, 17, '轻度污染'],
        [8, 113, 108, 137, 1.481, 48, 15, '轻度污染'],
        [9, 81, 48, 62, 1.619, 26, 3, '良'],
        [10, 56, 48, 68, 1.336, 37, 9, '良'],
        [11, 82, 92, 174, 3.29, 0, 13, '良'],
        [12, 106, 116, 188, 3.628, 101, 16, '轻度污染'],
    ];
    // const dataSH = [
    //     [1, 116, 87, 131, 1.47, 84, 40, '轻度污染'],
    //     [2, 108, 80, 121, 1.3, 85, 37, '轻度污染'],
    //     [3, 134, 83, 167, 1.16, 57, 43, '轻度污染'],
    //     [4, 79, 43, 107, 1.05, 59, 37, '良'],
    //     [5, 71, 46, 89, 0.86, 64, 25, '良'],
    //     [6, 97, 71, 113, 1.17, 88, 31, '良'],
    //     [7, 84, 57, 91, 0.85, 55, 31, '良'],
    //     [8, 87, 63, 101, 0.9, 56, 41, '良'],
    //     [9, 104, 77, 119, 1.09, 73, 48, '轻度污染'],
    //     [10, 87, 62, 100, 1, 72, 28, '良'],
    //     [11, 168, 128, 172, 1.49, 97, 56, '中度污染'],
    //     [12, 65, 45, 51, 0.74, 39, 17, '良'],
    // ];
    const schema = [
        { name: 'date', index: 0, text: '月' },
        { name: 'AQIindex', index: 1, text: '平均AQI指数' },
        { name: 'PM25', index: 2, text: 'PM2.5' },
        { name: 'PM10', index: 3, text: 'PM10' },
        { name: 'CO', index: 4, text: '一氧化碳（CO）' },
        { name: 'NO2', index: 5, text: '二氧化氮（NO2）' },
        { name: 'SO2', index: 6, text: '二氧化硫（SO2）' }
    ];

    const itemStyle = {
        opacity: 0.8,
        shadowBlur: 10,
        shadowOffsetX: 0,
        shadowOffsetY: 0,
        shadowColor: 'rgba(0,0,0,0.3)'
    };
    option87 = {
        backgroundColor: 'rgba(1,1,1,0)',
        legend: {
            top: '3%',
            left:'24%',
            data: ['2021','2022',  '2023'],
            textStyle: {
                fontSize: 16,
                color:'white',
            }
        },
        grid: {
            left: '10%',
            right: 150,
            top: '24%',
            bottom: '10%'
        },
        tooltip: {
            position:'right',
            backgroundColor: 'rgba(255,255,255,1)',
            formatter: function (param) {
                var value = param.value;
                // prettier-ignore
                return '<div style="border-bottom: 1px solid rgba(255,255,255,.3); font-size: 18px;padding-bottom: 7px;margin-bottom: 7px">'
                    + param.seriesName + ' ' + value[0] + '月：'
                    + value[7]
                    + '</div>'
                    + schema[1].text + '：' + value[1] + '<br>'
                    + schema[2].text + '：' + value[2] + '<br>'
                    + schema[3].text + '：' + value[3] + '<br>'
                    + schema[4].text + '：' + value[4] + '<br>'
                    + schema[5].text + '：' + value[5] + '<br>'
                    + schema[6].text + '：' + value[6] + '<br>';
            }
        },
        xAxis: {
            type: 'value',
            // name: '日期',
            nameGap: 16,
            nameTextStyle: {
                fontSize: 16
            },
            max: 12,
            splitLine: {
                show: false
            },
            axisLabel: {
                textStyle: {
                    color: 'white' // 设置Y轴上数据的颜色为白色
                }, formatter: '{value} '

            },
            axisLine: {
                lineStyle: {
                    color: 'white',
                },
            },
        },
        yAxis: {
            type: 'value',
            name: '平均AQI指数',
            nameLocation: 'end',
            nameGap: 20,
            nameTextStyle: {
                fontSize: 16,
                color:'white',
            },
            axisLabel: {
                textStyle: {
                    color: 'white' // 设置Y轴上数据的颜色为白色
                }, formatter: '{value} '
            },
            axisLine: {
                lineStyle: {
                    color: 'white',
                },
            },
            splitLine: {
                show: false
            }
        },
        visualMap: [
            {
                left: '70%',
                top: '10%',
                dimension: 2,
                min: 0,
                max: 250,
                textStyle:{
                    color:'white',
                },
                itemWidth: 13,
                itemHeight: 50,
                calculable: true,
                precision: 0.1,
                // text: ['圆形大小：PM2.5'],
                textGap: 30,
                inRange: {
                    symbolSize: [10, 40]
                },
                outOfRange: {
                    symbolSize: [10, 40],
                    color: ['rgba(255,255,255,0.4)']
                },
                controller: {
                    inRange: {
                        color: ['#c23531']
                    },
                    outOfRange: {
                        color: ['#999']
                    }
                }
            },
            {
                left: '75%',
                dimension: 6,
                min: 0,
                max: 50,
                itemWidth: 15,
                itemHeight: 60,
                // text: ['明暗：二氧化硫'],
                textGap: 30,
                inRange: {
                    colorLightness: [0.9, 0.5]
                },
                outOfRange: {
                    color: ['rgba(255,255,255,0.4)']
                },
                controller: {
                    inRange: {
                        color: ['#c23531']
                    },
                    outOfRange: {
                        color: ['#999']
                    }
                }
            }
        ],
        series: [
            {
                name: '2023',
                type: 'scatter',
                itemStyle: itemStyle,
                data: dataBJ
            },
            {
                name: '2022',
                type: 'scatter',
                itemStyle: itemStyle,
                data: dataGZ
            },
            // {
            //     name: '2021',
            //     type: 'scatter',
            //     itemStyle: itemStyle,
            //     data: dataSH
            // },
        ]
    };
    option87 && myChart87.setOption(option87);

    const resizeObserver = new ResizeObserver(() => {
        myChart87.resize();
    });

    resizeObserver.observe(echartsRef.value);
});

</script>

<template>
    <div class="DataAnalysisLeftDown">
        <div class="title">安徽耗能时间分布</div>
        <div class="DataAnalysisLeftDown-echarts" ref="echartsRef"></div>
        <img src="../../../assets/pic/midden.png" alt="" class="BackImg">
    </div>
</template>

<style scoped lang="scss">
.DataAnalysisLeftDown {
  width: 100%;
  height: 100%;

  .DataAnalysisLeftDown-echarts {
    width: 32vw;
    height: 22vh;
    margin-top: 8vh;
    margin-left: 2vw;
    position: absolute;
  }

  .title {
    position: absolute;
    color: white;
    font-size: 1.4em;
    font-weight: bolder;
    margin-top: 4.5vh;
    margin-left: 3vw;
  }

  .BackImg {
    width: 30vw;
    height: 34vh;
  }
}
</style>