<script setup>
import {ref, onMounted} from 'vue';
import * as echarts from 'echarts';

const echartsRef = ref(null);
let myChart8 = null;
let option8 = null;

onMounted(() => {
    myChart8 = echarts.init(echartsRef.value);

    option8 = {
        // title: {
        //     text: '全国土地利用情况',
        //     // subtext: 'Fake Data',
        //     top: '15%',
        //     left: 'center',
        //     textStyle: {
        //         color: 'white',
        //     },
        // },
        tooltip: {
            trigger: 'axis',
            axisPointer: {
                // Use axis to trigger tooltip
                type: 'shadow' // 'shadow' as default; can also be 'line' or 'shadow'
            }
        },
        legend: {
            left: 'center',
            textStyle: {
                color: 'white'
            },
        },
        grid: {
            top: '25%',
            left: '3%',
            right: '4%',
            bottom: '3%',
            containLabel: true
        },
        xAxis: {
            type: 'value',
            axisLabel: {
                formatter: '{value}%'
            },
            axisLine: {
                lineStyle: {
                    color: 'white',
                }
            }
        },
        yAxis: {
            type: 'category',
            data: ['2017年', '2018年', '2019年', '2020年', '2021年', '2022年', '2023年'],

            axisLine: {
                lineStyle: {
                    color: 'white',
                }
            }
        },
        series: [
            {
                name: '牧草地',
                type: 'bar',
                stack: 'total',
                label: {
                    show: true,
                    formatter: '{c}%'
                },
                emphasis: {
                    focus: 'series'
                },
                data: [20, 24, 20, 29, 15, 12, 25]
            },
            {
                name: '耕地',
                type: 'bar',
                stack: 'total',
                label: {
                    show: true,
                    formatter: '{c}%'
                },
                emphasis: {
                    focus: 'series'
                },
                data: [11, 26, 20, 22, 22, 13, 25]
            },
            {
                name: '园地',
                type: 'bar',
                stack: 'total',
                label: {
                    show: true,
                    formatter: '{c}%'
                },
                emphasis: {
                    focus: 'series'
                },
                data: [19, 11, 16, 20, 33, 25, 25]
            },
            {
                name: '林地',
                type: 'bar',
                stack: 'total',
                label: {
                    show: true,
                    formatter: '{c}%'
                },
                emphasis: {
                    focus: 'series'
                },
                data: [27, 22, 22, 11, 19, 27, 22]
            },
            {
                name: '其他农用地',
                type: 'bar',
                stack: 'total',
                label: {
                    show: true,
                    formatter: '{c}%'
                },
                emphasis: {
                    focus: 'series'
                },
                data: [23, 17, 22, 18, 11, 23, 3]
            }
        ]
    };
    option8 && myChart8.setOption(option8);
    const resizeObserver = new ResizeObserver(() => {
        myChart8.resize();
    });

    resizeObserver.observe(echartsRef.value);
});
</script>

<template>
    <div className="MainChinaLeft">
        <img class="BackImg" src="../../assets/pic/border3.png" alt="">
        <Button class="GotoGrounds">全国土地利用情况</Button>
        <div id="MainChinaLeft-echarts" ref="echartsRef"></div>
    </div>
</template>

<style scoped lang="scss">
.MainChinaLeft {
  width: 100vw;
  height: 100vh;
  color: white;

  .GotoGrounds {
    position: absolute;
    margin-top: -32vh;
    width: 19vw;
    margin-left: 0.6vw;
    border: none;
    background: none;
    color: white;
    font-weight: bolder;
    cursor: pointer;
    font-size: 1.2vw;
    z-index: 999;
  }

  .GotoGrounds:hover {
    font-size: 1.3vw;
    margin-top: -32.3vh;
  }

  .GotoGrounds:active {
    margin-top: -32vh;
    font-size: 1.2vw;
  }

  #MainChinaLeft-echarts {
    width: 19vw;
    height: 37vh;
    margin-left: 0.2vw;
    position: absolute;
    margin-top: -38vh;
  }

  .BackImg {
    width: 20.2vw;
    height: 40vh;
    margin-top: -20vh;
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
