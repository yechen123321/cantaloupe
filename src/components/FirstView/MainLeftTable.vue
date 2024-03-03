<script setup>
import {ref, onMounted} from 'vue';
import * as echarts from 'echarts';
import MainLeftMidden from "@/components/FirstView/FirstViewTools/MainLeftMidden.vue";
import MainLeftButtom from "@/components/FirstView/FirstViewTools/MainLeftButtom.vue";
import MainChinaLeft from "@/components/FirstView/MainChinaLeft.vue";

const echartsRef = ref(null);
let myChart1 = null;
let option1 = null;

onMounted(() => {
    myChart1 = echarts.init(echartsRef.value, 'dark');

    // Your echarts option setup here...
    // (Your existing option setup code)
    option1 = {
        backgroundColor: 'rgba(128, 128, 128, 0)',
        color: ['#80FFA5', '#00DDFF', '#37A2FF', '#FF0087', '#FFBF00'],
        title: {
            text: '全国重要矿产开发投入资金',
            top: '28vh',
            left: 'center',
        },
        tooltip: {
            trigger: 'axis',
            axisPointer: {
                type: 'cross',
                label: {
                    backgroundColor: '#6a7985'
                }
            }
        },
        legend: {
            textStyle: {
                color: 'white'
            },
            data: ['锰矿', '钨矿', '铀矿', '铅锌矿', '硫铁矿']
        },
        // toolbox: {
        //     feature: {
        //         saveAsImage: {}
        //     }
        // },
        grid: {
            left: '3%',
            right: '4%',

            bottom: '3%',
            containLabel: true
        },
        xAxis: [
            {
                type: 'category',
                boundaryGap: false,
                data: ['2017', '2018', '2019', '2020', '2021', '2022', '2023'],
                axisLine: {
                    lineStyle: {
                        color: 'white',
                    }
                }
            }

        ],
        yAxis: [
            {
                type: 'value',
                axisLine: {
                    lineStyle: {
                        color: 'white',
                    }
                }
            }
        ],
        series: [
            {
                name: '锰矿',
                type: 'line',
                stack: 'Total',
                smooth: true,
                lineStyle: {
                    width: 0
                },
                showSymbol: false,
                areaStyle: {
                    opacity: 0.8,
                    color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
                        {
                            offset: 0,
                            color: 'rgb(128, 255, 165)'
                        },
                        {
                            offset: 1,
                            color: 'rgb(1, 191, 236)'
                        }
                    ])
                },
                emphasis: {
                    focus: 'series'
                },
                data: [140, 232, 101, 264, 90, 340, 250]
            },
            {
                name: '钨矿',
                type: 'line',
                stack: 'Total',
                smooth: true,
                lineStyle: {
                    width: 0
                },
                axisLine: {
                    lineStyle: {
                        color: 'white',
                    }
                },
                showSymbol: false,
                areaStyle: {
                    opacity: 0.8,
                    color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
                        {
                            offset: 0,
                            color: 'rgb(0, 221, 255)'
                        },
                        {
                            offset: 1,
                            color: 'rgb(77, 119, 255)'
                        }
                    ])
                },
                emphasis: {
                    focus: 'series'
                },
                data: [120, 282, 111, 234, 220, 340, 310]
            },
            {
                name: '铀矿',
                type: 'line',
                stack: 'Total',
                smooth: true,
                lineStyle: {
                    width: 0
                },
                showSymbol: false,
                areaStyle: {
                    opacity: 0.8,
                    color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
                        {
                            offset: 0,
                            color: 'rgb(55, 162, 255)'
                        },
                        {
                            offset: 1,
                            color: 'rgb(116, 21, 219)'
                        }
                    ])
                },
                emphasis: {
                    focus: 'series'
                },
                data: [320, 132, 201, 334, 190, 130, 220]
            },
            {
                name: '铅锌矿',
                type: 'line',
                stack: 'Total',
                smooth: true,
                lineStyle: {
                    width: 0
                },
                showSymbol: false,
                areaStyle: {
                    opacity: 0.8,
                    color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
                        {
                            offset: 0,
                            color: 'rgb(255, 0, 135)'
                        },
                        {
                            offset: 1,
                            color: 'rgb(135, 0, 157)'
                        }
                    ])
                },
                emphasis: {
                    focus: 'series'
                },
                data: [220, 402, 231, 134, 190, 230, 120],

            },
            {
                name: '硫铁矿',
                type: 'line',
                stack: 'Total',
                smooth: true,
                lineStyle: {
                    width: 0,
                },
                showSymbol: false,
                label: {
                    show: true,
                    position: 'top'

                },
                areaStyle: {
                    opacity: 0.8,
                    color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
                        {
                            offset: 0,
                            color: 'rgb(255, 191, 0)'
                        },
                        {
                            offset: 1,
                            color: 'rgb(224, 62, 76)'
                        }
                    ])
                },
                emphasis: {
                    focus: 'series'
                },
                data: [220, 302, 181, 234, 210, 290, 150]
            }
        ]
    }
    option1 && myChart1.setOption(option1);

    const resizeObserver = new ResizeObserver(() => {
        myChart1.resize();
    });

    resizeObserver.observe(echartsRef.value);
});
</script>


<template>
    <div class="MainLeftTable">
        <div id="MainTable-echarts" ref="echartsRef"></div>
        <MainLeftMidden id="MainLeftMidden-out"></MainLeftMidden>
        <MainChinaLeft id="MainChinaLeft-out"></MainChinaLeft>
        <img class="BackImg" src="../../assets/pic/border3.png" alt="">
        <MainLeftButtom id="MainLeftButtom-out"></MainLeftButtom>
    </div>
</template>

<style scoped lang="scss">
.MainLeftTable {
  width: 100vw;
  height: 100vh;

  .BackImg {
    width: 27vw;
    height: 80vh;
  }

  #MainTable-echarts {
    width: 23vw;
    height: 21.5vh;
    margin-left: 1.5vw;
    position: absolute;
    margin-top: 4vh;
  }

  #MainLeftMidden-out {
    width: 25vw;
    height: 23.5vh;
    margin-left: 2.5vw;
    position: absolute;
    margin-top: 48.8vh;
  }

  #MainLeftButtom-out {
    width: 23vw;
    height: 32.5vh;
    margin-left: 2.5vw;
    position: absolute;
    margin-top: -14vh;
  }

  #MainChinaLeft-out {
    width: 25vw;
    height: 23.5vh;
    margin-left: 28vw;
    position: absolute;
    margin-top: 21.8vh;
  }

  @keyframes glow {
    from {
      box-shadow: 0px 0px 3px 3px #00bfff, 0px 0px 5px 3px #0d0d0d, 0px 0px 7px 5px #00bfff;
    }

    to {
      box-shadow: 0px 0px 5px 3px #00bfff, 0px 0px 7px 5px #0d0d0d, 0px 0px 9px 7px #00bfff;
    }
  }
}
</style>
