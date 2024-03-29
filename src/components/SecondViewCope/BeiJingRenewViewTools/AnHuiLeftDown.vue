<script setup>
import {onMounted, ref} from "vue";
import * as echarts from "echarts";

const echartsRef = ref(null);
let myChart36 = null;
let option36 = null;

onMounted(() => {
    myChart36 = echarts.init(echartsRef.value, 'dark');

    // Your echarts option setup here...
    // (Your existing option setup code)
    var colorList = [
        new echarts.graphic.LinearGradient(0, 0, 0, 1, [
            {offset: 0, color: '#396afc'},
            {offset: 1, color: '#2948ff'},
        ]),
        new echarts.graphic.LinearGradient(0, 0, 0, 1, [
            {offset: 0, color: '#bc4e9c'},
            {offset: 1, color: '#f80759'},
        ]),
        new echarts.graphic.LinearGradient(0, 0, 0, 1, [
            {offset: 0, color: '#00C9FF'},
            {offset: 1, color: '#92FE9D'},
        ]),
        // 其他渐变色定义...
    ];
    option36 = {
        backgroundColor: "rgba(128,128,128,0)",
        color: colorList,
        tooltip: {
            trigger: 'axis',
            // axisPointer: {
            //     type: 'cross',
            //     crossStyle: {
            //         color: '#999'
            //     }
            // }
        },
        // toolbox: {
        //     feature: {
        //         dataView: { show: true, readOnly: false },
        //         magicType: { show: true, type: ['line', 'bar'] },
        //         restore: { show: true },
        //         saveAsImage: { show: true }
        //     }
        // },
        legend: {
            textStyle: {
                color: 'white'
            },
            top: '10%',
            data: ['产量', '存量', '产量增长率'],
            itemWidth: 20, // 标签宽度为20px
            itemHeight: 10, // 标签高度为10px
        },
        xAxis: [
            {
                type: 'category',
                data: ['2020', '2021', '2022', '2023'],
                axisPointer: {
                    type: 'shadow'
                },
                axisLabel: {
                    textStyle: {
                        color: 'white' // 设置Y轴上数据的颜色为白色
                    }
                },
                axisLine: {
                    lineStyle: {
                        color: 'white',
                    },
                },
            }
        ],
        grid: {
            left: '15%',
            right: "13%"
        },
        yAxis: [
            {
                type: 'value',
                name: '亿元',
                min: 0,
                max: 250,
                nameTextStyle: {
                    color: 'white',
                    padding: [0, 30, 0, 0]
                },
                interval: 50,
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
            {
                type: 'value',
                name: '百分比',
                min: 0,
                max: 25,
                nameTextStyle: {
                    color: 'white',
                    padding: [0, -25, 0, 0]
                },
                interval: 5,
                axisLabel: {
                    textStyle: {
                        color: 'white' // 设置Y轴上数据的颜色为白色
                    }, formatter: '{value} %'

                },
                axisLine: {
                    lineStyle: {
                        color: 'white',
                    },
                },
            }
        ],
        series: [
            {
                name: '产量',
                type: 'bar',
                tooltip: {
                    valueFormatter: function (value) {
                        return value + ' ml';
                    }
                },
                data: [
                    162.2, 132.6,176.7, 135.6,
                ]
            },
            {
                name: '存量',
                type: 'bar',
                tooltip: {
                    valueFormatter: function (value) {
                        return value + ' ml';
                    }
                },
                data: [
                    182.2, 148.7,170.7, 175.6,
                ]
            },
            {
                name: '产量增长率',
                type: 'line',
                yAxisIndex: 1,
                tooltip: {
                    valueFormatter: function (value) {
                        return value + ' °C';
                    }
                },
                data: [23.0, 16.5,20.3, 23.4, ]
            }
        ]
    };

    option36 && myChart36.setOption(option36);

    const resizeObserver = new ResizeObserver(() => {
        myChart36.resize();
    });

    resizeObserver.observe(echartsRef.value);
})
;
</script>

<template>
    <div class="AnHuiLeftDown">
        <div class="AnHuiLeftDown-title">北京再生能源建设投资</div>
        <div class="AnHuiLeftDown-echarts" ref="echartsRef"></div>
    </div>
</template>

<style scoped lang="scss">
.AnHuiLeftDown {
  width: 100%;
  height: 100%;

  .AnHuiLeftDown-title {
    width: 23vw;
    color: white;
    //background: red;
    margin-left: 1.5vw;
    font-weight: bolder;
    font-size: 1.3vw;
    margin-top: 1.5vh;
    position: absolute;
    text-align: center;
  }

  .AnHuiLeftDown-echarts {
    width: 25vw;
    height: 33vh;
    margin-top: 2vh;
    position: absolute;
    z-index: 999;
  }
}
</style>