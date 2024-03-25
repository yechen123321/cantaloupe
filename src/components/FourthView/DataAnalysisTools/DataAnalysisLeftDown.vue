<script setup>
import {onMounted, ref} from 'vue';
import * as echarts from "echarts";

const echartsRef = ref(null);
let myChart85 = null;
let option85 = null;

onMounted(() => {
    myChart85 = echarts.init(echartsRef.value, 'dark');
    // Your echarts option setup here...
    // (Your existing option setup code)
    var colorList = [
        // new echarts.graphic.LinearGradient(0, 0, 0, 1, [
        //     {offset: 0, color: '#bc4e9c'},
        //     {offset: 1, color: '#f80759'}
        // ]),
        new echarts.graphic.LinearGradient(0, 0, 0, 1, [
            {offset: 0, color: '#396afc'},
            {offset: 1, color: '#2948ff'}
        ]),
        new echarts.graphic.LinearGradient(0, 0, 0, 1, [
            {offset: 0, color: '#00C9FF'},
            {offset: 1, color: '#92FE9D'}
        ]),
        // 其他渐变色定义...
    ];
    option85 = {
        backgroundColor: 'rgba(1,1,1,0)',
        color: colorList,
        tooltip: {
            trigger: 'axis',
            // axisPointer: {
            //     type: 'cross'
            // }
        },
        legend: {
            top: "16%",
            left: '20%',
            textStyle: {
                color: 'white',
            }
        },
        grid: {
            top: 70,
            bottom: 50
        },
        xAxis: [
            {
                type: 'category',
                axisTick: {
                    alignWithLabel: true
                },
                axisLabel: {
                    textStyle: {
                        color: 'white' // 设置Y轴上数据的颜色为白色
                    }
                },
                axisLine: {
                    onZero: false,
                    lineStyle: {
                        color: colorList[1]
                    }
                },
                axisPointer: {
                    label: {
                        formatter: function (params) {
                            return (
                                params.value + ' 月份' + ' 单位/万千瓦时'
                            );
                        }
                    }
                },
                // prettier-ignore
                data: ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
            },
        ],
        yAxis: [
            {
                name: '单位/万千瓦时',
                type: 'value',
                nameTextStyle: {
                    color: 'white'
                },
                axisLabel: {
                    textStyle: {
                        color: 'white' // 设置Y轴上数据的颜色为白色
                    }
                },
            }
        ],
        series: [
            {
                name: '2020',
                type: 'line',
                smooth: true,
                emphasis: {
                    focus: 'series'
                },
                data: [
                    2.6, 5.9, 9.0, 26.4, 28.7, 70.7, 175.6, 182.2, 48.7, 18.8, 6.0, 2.3
                ]
            },
            {
                name: '2021',
                type: 'line',
                smooth: true,
                emphasis: {
                    focus: 'series'
                },
                data: [
                    3.9, 5.9, 11.1, 231.6, 46.6, 55.4, 18.4, 10.3, 0.7, 18.7, 48.3, 69.2,
                ]
            },
            {
                name: '2022',
                type: 'line',
                smooth: true,
                emphasis: {
                    focus: 'series'
                },
                data: [
                    69.2, 231.6, 46.6, 55.4, 18.4, 10.3, 0.7, 3.9, 5.9, 11.1, 18.7, 48.3,
                ]
            },
            {
                name: '2023',
                type: 'line',
                smooth: true,
                emphasis: {
                    focus: 'series'
                },
                data: [
                    3.9, 5.9, 11.1, 18.7, 48.3, 69.2, 231.6, 46.6, 55.4, 18.4, 10.3, 0.7
                ]
            }
        ]
    };
    option85 && myChart85.setOption(option85);

    const resizeObserver = new ResizeObserver(() => {
        myChart85.resize();
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
    width: 28vw;
    height: 30vh;
    margin-top: 4vh;
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