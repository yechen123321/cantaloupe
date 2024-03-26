<script setup>
import {ref, onMounted} from 'vue';
import * as echarts from 'echarts';
import 'echarts-gl';

const echartsRef = ref(null);
let myChart9 = null;
let option9 = null;

onMounted(() => {
    myChart9 = echarts.init(echartsRef.value);
    var colorList = [
        new echarts.graphic.LinearGradient(0, 0, 0, 1, [
            {offset: 0, color: '#396afc'},
            {offset: 1, color: '#2948ff'}
        ]),
        new echarts.graphic.LinearGradient(0, 0, 0, 1, [
            {offset: 0, color: '#bc4e9c'},
            {offset: 1, color: '#f80759'}
        ]),
        new echarts.graphic.LinearGradient(0, 0, 0, 1, [
            {offset: 0, color: '#00C9FF'},
            {offset: 1, color: '#92FE9D'}
        ]),
        // 其他渐变色定义...
    ];
    option9 = {
        color: colorList,
        tooltip: {
            trigger: 'axis',
            extraCssText: 'width: 15vw; height: 15vh;', // 设置tooltip框的宽度和高度，调整框的大小
            formatter: function (params) {
                let tooltipContent = '';
                let mineName = params[0].name;
                tooltipContent += '<span style="font-weight: bold;margin-right: 1vw; margin-top: -500px;">' + mineName + '</span>' + '单位/亿吨,亿元<br>' + '<br>'; // 设置矿地名字的样式为加粗并向上移动5px
                params.forEach(function (param) {
                    if (param.seriesName === '全国能耗降低率') {
                        tooltipContent += param.marker + param.seriesName + ': ' + '<span style="float: right; font-weight: bold;">' + param.value + '%</span>' + '<br>';
                    } else {
                        tooltipContent += param.marker + param.seriesName + ': ' + '<span style="float: right; font-weight: bold;">' + param.value + '</span>' + '<br>';
                    }
                });
                return tooltipContent;
            }
        },
        grid: {
            left: '5.3%', // 调整图表左边距
            right: '7%', // 调整图表右边距
            // top: '10%', // 调整图表上边距
            bottom: '15%', // 调整图表下边距
            containLabel: true,
        },
        legend: {
            // left:'0%',
            data: ['能源消耗', '全国GDP', '全国能耗降低率'],
            textStyle: {
                color: 'white'
            }
        },
        xAxis: [
            {
                type: 'category',
                axisTick: {
                    alignWithLabel: true
                }, axisLine: {
                    lineStyle: {
                        color: 'white',
                    },
                },
                axisLabel: {
                    textStyle: {
                        color: 'white' // 设置X轴上数据的颜色为白色
                    }
                },
                // prettier-ignore
                data: ['Aug', 'Sep', 'Oct', 'Nov', 'Dec']
            }
        ],
        yAxis: [
            {
                type: 'value',
                name: '万亿元',
                position: 'right',
                alignTicks: true,
                nameTextStyle: {
                    padding: [0, -30, 0, 0]
                },
                axisLine: {
                    lineStyle: {
                        color: 'white',
                    },
                },
                axisLabel: {
                    textStyle: {
                        color: 'white' // 设置X轴上数据的颜色为白色
                    }
                }
            },
            {
                type: 'value',
                name: '降低率',
                nameLocation: 'end', // 将名称显示在轴线末尾，即向右移动
                position: 'right',
                nameTextStyle: {
                    padding: [0, -38, 0, 0]
                },
                alignTicks: true,
                offset: 40,
                axisLine: {
                    lineStyle: {
                        color: 'white',
                    },
                },
                axisLabel: {
                    textStyle: {
                        color: 'white' // 设置X轴上数据的颜色为白色
                    }
                }
            },
            {
                type: 'value',
                name: '标准煤 / 万亿吨',
                position: 'left',
                alignTicks: true,
                axisLine: {
                    lineStyle: {
                        color: 'white',
                    },
                },
                axisLabel: {
                    textStyle: {
                        color: 'white' // 设置X轴上数据的颜色为白色
                    }
                }
            },
        ],
        series: [
            {
                name: '能源消耗',
                type: 'bar',
                yAxisIndex: 2,
                data: [
                    135.6, 162.2, 32.6, 20.0, 6.4,
                ]
            },
            {
                name: '全国GDP',
                type: 'bar',
                yAxisIndex: 0,
                data: [
                    175.6, 182.2, 48.7, 18.8, 6.0
                ]
            },
            {
                name: '全国能耗降低率',
                type: 'line',
                yAxisIndex: 1,
                data: [3.4, 2.0, 1.5, 1.0, 3.2]
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
        <Button class="GotoQ">全国能源消耗水平</Button>
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
    //cursor: pointer;
  }

  //
  //.GotoQ:hover {
  //  font-size: 1.3vw;
  //}
  //
  //.GotoQ:active {
  //  font-size: 1.2vw;
  //}

  #MainDownLeft-echarts {
    width: 26vw;
    height: 35vh;
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
