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
            {offset: 0, color: '#bc4e9c'},
            {offset: 1, color: '#f80759'}
        ]),
        new echarts.graphic.LinearGradient(0, 0, 0, 1, [
            {offset: 0, color: '#2980B9'},
            {offset: 1, color: '#6DD5FA'}
        ]),
        new echarts.graphic.LinearGradient(0, 0, 0, 1, [
            {offset: 0, color: '#00C9FF'},
            {offset: 1, color: '#92FE9D'}
        ]),
        // 其他渐变色定义...
    ];

    option76 = {
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
            top: '12%',
            left: 'center',
            data: ['储量', '供量', '储量增长率', '供量增长率'],
            itemWidth: 20, // 标签宽度为20px
            itemHeight: 10, // 标签高度为10px
        },
        xAxis: [
            {
                type: 'category',
                data: ['2017', '2018', '2019', '2020', '2021', '2022', '2023'],
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
                name: '万千瓦',
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
                name: '储量',
                type: 'bar',
                tooltip: {
                    valueFormatter: function (value) {
                        return value + ' ml';
                    }
                },
                data: [
                    76.7, 135.6, 162.2, 32.6, 162.2, 32.6, 76.7,
                ]
            },
            {
                name: '供量',
                type: 'bar',
                tooltip: {
                    valueFormatter: function (value) {
                        return value + ' ml';
                    }
                },
                data: [
                    70.7, 175.6, 182.2, 48.7, 182.2, 48.7, 70.7,
                ]
            },
            {
                name: '储量增长率',
                type: 'line',
                yAxisIndex: 1,
                tooltip: {
                    valueFormatter: function (value) {
                        return value + ' °C';
                    }
                },
                data: [20.3, 23.4, 23.0, 16.5, 23.0, 16.5, 20.3,]
            },
            // {
            //     name: '供量增长率',
            //     type: 'line',
            //     yAxisIndex: 1,
            //     tooltip: {
            //         valueFormatter: function (value) {
            //             return value + ' °C';
            //         }
            //     },
            //     data: [16.5, 23.0, 20.3, 23.4, 23.0, 20.3, 16.5,]
            // }
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
    margin-top: -0.5vh;
    //background: red;
    text-align: center;
    position: absolute;
    color: white;
    font-size: 1.3em;
    margin-left: 1vw;
    font-weight: bolder;
  }

  .AnHuiLimitLeftDown-echarts {
    width: 26vw;
    height: 32vh;

  }
}
</style>