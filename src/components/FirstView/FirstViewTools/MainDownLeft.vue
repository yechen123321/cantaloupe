<script setup>
import {ref, onMounted} from 'vue';
import * as echarts from 'echarts';
import 'echarts-gl';

const echartsRef = ref(null);
let myChart9 = null;
let option9 = null;

onMounted(() => {
    myChart9 = echarts.init(echartsRef.value);


    option9 = {

        tooltip: {
            trigger: 'axis',
            // axisPointer: {
            //     type: 'cross',
            //     // label: {
            //     //     backgroundColor: '#6a7985'
            //     // }
            //
            // }
        },
        legend: {
            data: ['煤炭', '石油', '天然气', '页岩气', '页岩油', '煤层气', '油页岩'],
            textStyle: {
                color: 'white'
            }
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
                    },
                }
            }
        ],
        yAxis: [
            {
                type: 'value',
                axisLine: {
                    lineStyle: {
                        color: 'white',
                    },
                }
            }
        ],
        series: [
            {
                name: '煤炭',
                type: 'line',
                stack: 'Total',
                areaStyle: {},
                emphasis: {
                    focus: 'series'
                },
                data: [120, 132, 101, 134, 90, 230, 210]
            },
            {
                name: '石油',
                type: 'line',
                stack: 'Total',
                areaStyle: {},
                emphasis: {
                    focus: 'series'
                },
                data: [220, 182, 191, 234, 290, 330, 310]
            },
            {
                name: '天然气',
                type: 'line',
                stack: 'Total',
                areaStyle: {},
                emphasis: {
                    focus: 'series'
                },
                data: [150, 232, 201, 154, 190, 330, 410]
            },
            {
                name: '页岩气',
                type: 'line',
                stack: 'Total',
                areaStyle: {},
                emphasis: {
                    focus: 'series'
                },
                data: [320, 332, 301, 334, 390, 330, 320]
            },
            {
                name: '页岩油',
                type: 'line',
                stack: 'Total',
                areaStyle: {},
                emphasis: {
                    focus: 'series'
                },
                data: [820, 932, 901, 934, 1290, 1330, 1320]
            },
            {
                name: '煤层气',
                type: 'line',
                stack: 'Total',

                areaStyle: {},
                emphasis: {
                    focus: 'series'
                },
                data: [820, 932, 901, 934, 1290, 1330, 1320]
            },
            {
                name: '油页岩',
                type: 'line',
                stack: 'Total',

                areaStyle: {},
                emphasis: {
                    focus: 'series'
                },
                data: [820, 932, 901, 934, 1290, 1330, 1320]
            },
        ]
    };
    option9 && myChart9.setOption(option9);

    const resizeObserver = new ResizeObserver(() => {
        myChart9.resize();
    });

    resizeObserver.observe(echartsRef.value);
});
</script>


<template>
    <div className="MainDownLeft">
        <Button class="GotoQ">全国化石能源产量结构占比</Button>
        <div id="MainDownLeft-echarts" ref="echartsRef"></div>
    </div>
</template>

<style scoped lang="scss">
.MainDownLeft {
  width: 100vw;
  height: 100vh;
  color: white;

  .GotoQ {
    position: absolute;
    margin-top: -25.5vh;
    width: 23vw;
    margin-left: 0.6vw;
    background: none;
    border: none;
    color: white;
    font-weight: bolder;
    font-size: 1.2vw;
    cursor: pointer;
  }

  .GotoQ:hover {
    font-size: 1.3vw;
  }

  .GotoQ:active {
    font-size: 1.2vw;
  }

  #MainDownLeft-echarts {
    width: 23vw;
    height: 30vh;
    margin-left: 0.5vw;
    position: absolute;
    margin-top: -21.5vh;
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
