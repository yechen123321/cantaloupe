<script setup>
import {onMounted, ref} from 'vue';
import * as echarts from "echarts";

const echartsRef = ref(null);
let myChart76 = null;
let option76 = null;

onMounted(() => {
    myChart76 = echarts.init(echartsRef.value, 'dark');
    // Your echarts option setup here...
    // (Your existing option setup code)
    var colorList = [
        new echarts.graphic.LinearGradient(0, 0, 0, 1, [
            {offset: 0, color: '#ffc0cb'},
            {offset: 1, color: '#de1dde'}
        ]),
        new echarts.graphic.LinearGradient(0, 0, 0, 1, [
            {offset: 0, color: '#fc82ab'},
            {offset: 1, color: '#d720a6'}
        ]),
        new echarts.graphic.LinearGradient(0, 0, 0, 1, [
            {offset: 0, color: '#ea5fff'},
            {offset: 1, color: '#7F00FF'}
        ]),
        new echarts.graphic.LinearGradient(0, 0, 0, 1, [
            {offset: 0, color: '#c98a08'},
            {offset: 1, color: '#b0200f'}
        ]),
        new echarts.graphic.LinearGradient(0, 0, 0, 1, [
            {offset: 0, color: '#FFB75E'},
            {offset: 1, color: '#ED8F03'}
        ]),
        // 其他渐变色定义...
    ];

    option76 = {
        backgroundColor: "rgba(128,128,128,0)",
        color: colorList,
        tooltip: {
            trigger: 'axis',
        },
        legend: {
            textStyle: {
                color: 'white'
            },
            top: '12%',
            left: '5%',
            data: ['产量','储量', '供量', '储量增长率', '供量增长率'],
            itemWidth: 20, // 标签宽度为20px
            itemHeight: 10, // 标签高度为10px
        },
        xAxis: [
            {
                type: 'category',
                data: [ '2020', '2021', '2022', '2023'],
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
                min: 0,
                max: 250,
                nameTextStyle: {
                    color: 'white',
                    padding: [0, 25, 0, 0]
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
                        return value + ' 万千瓦';
                    }
                },
                data: [
                    176.7, 135.6, 162.2, 132.6, 162.2, 132.6, 176.7,
                ]
            },
            {
                name: '储量',
                type: 'bar',
                tooltip: {
                    valueFormatter: function (value) {
                        return value + ' 万千瓦';
                    }
                },
                data: [
                    176.7, 135.6, 162.2, 132.6, 162.2, 132.6, 176.7,
                ]
            },
            {
                name: '供量',
                type: 'bar',
                tooltip: {
                    valueFormatter: function (value) {
                        return value + ' 万千瓦';
                    }
                },
                data: [
                    170.7, 175.6, 182.2, 148.7, 182.2, 148.7, 170.7,
                ]
            },
            {
                name: '储量增长率',
                type: 'line',
                yAxisIndex: 1,
                tooltip: {
                    valueFormatter: function (value) {
                        return value + ' %';
                    }
                },
                data: [20.3, 23.4, 23.0, 16.5, 23.0, 16.5, 20.3,]
            },
            {
                name: '供量增长率',
                type: 'line',
                yAxisIndex: 1,
                tooltip: {
                    valueFormatter: function (value) {
                        return value + ' °C';
                    }
                },
                data: [16.5, 23.0, 20.3, 23.4, 23.0, 20.3, 16.5,]
            }
        ]
    };

    option76 && myChart76.setOption(option76);

    const resizeObserver = new ResizeObserver(() => {
        myChart76.resize();
    });

    resizeObserver.observe(echartsRef.value);
});

</script>
<template>
    <div class="AnHuiLimitLeftDown">
        <div class="title">安徽省有限资源产能图</div>
        <div class="AnHuiLimitLeftDown-echarts" ref="echartsRef"></div>
    </div>
</template>

<style scoped lang="scss">
.AnHuiLimitLeftDown {
  width: 100%;
  height: 100%;

  .title {
    width: 24vw;
    text-align: center;
    position: absolute;
    color: white;
    font-size: 1.15em;
    margin-left: 1vw;
    font-weight: bolder;
  }

  .AnHuiLimitLeftDown-echarts {
    width: 26vw;
    height: 32vh;
      margin-left: -0.4vw;
  }
}
</style>