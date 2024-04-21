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
            {offset: 0, color: '#6cd7fa'},
            {offset: 1, color: '#2948ff'}
        ]),
        new echarts.graphic.LinearGradient(0, 0, 0, 1, [
            {offset: 1, color: '#00C9FF'},
            {offset: 0, color: '#92FE9D'}
        ]),
        new echarts.graphic.LinearGradient(0, 0, 0, 1, [
            {offset: 0, color: '#FBD786'},
            {offset: 1, color: '#C6FFDD'}
        ]),
        // 其他渐变色定义...
    ];
    option36 = {
        backgroundColor: "rgba(128,128,128,0)",
        color: colorList,
        tooltip: {
            trigger: 'axis',
        },

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
                    }, formatter: '{value} %'

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
                        return value + ' 亿元';
                    }
                },
                data: [
                    176.7, 135.6, 162.2, 132.6,
                ],
                itemStyle: {
                    barBorderRadius: [10, 10, 0, 0] // 设置柱子上方为圆角，数组中的四个值分别代表左上、右上、右下、左下的圆角半径
                }
            },
            {
                name: '存量',
                type: 'bar',
                tooltip: {
                    valueFormatter: function (value) {
                        return value + ' 亿元';
                    }
                },
                data: [
                    170.7, 175.6, 182.2, 148.7,
                ],
                itemStyle: {
                    barBorderRadius: [10, 10, 0, 0] // 设置柱子上方为圆角，数组中的四个值分别代表左上、右上、右下、左下的圆角半径
                }
            },
            {
                name: '产量增长率',
                type: 'line',
                yAxisIndex: 1,
                tooltip: {
                    valueFormatter: function (value) {
                        return value + ' %';
                    }
                },
                data: [20.3, 23.4, 23.0, 16.5,],

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
    <div className="AnHuiLeftDown">
        <div className="AnHuiLeftDown-title">北京市再生能源建设投资</div>
        <div className="AnHuiLeftDown-echarts" ref="echartsRef"></div>
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
        font-size: 1.15em;
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