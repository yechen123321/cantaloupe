<script setup>
import {ref, onMounted} from 'vue';
import * as echarts from 'echarts';
import 'echarts-gl';

const echartsRef = ref(null);
let myChart7 = null;
let option7 = null;

onMounted(() => {
    myChart7 = echarts.init(echartsRef.value);
    var colorList = [
        new echarts.graphic.LinearGradient(0, 0, 0, 1, [
            {offset: 0, color: '#ec38bc'},
            {offset: 1, color: '#fdeff9'}
        ]),
        new echarts.graphic.LinearGradient(0, 0, 0, 1, [
            {offset: 0, color: '#FC5C7D'},
            {offset: 1, color: '#6A82FB'}
        ]),
        new echarts.graphic.LinearGradient(0, 0, 0, 1, [
            {offset: 0, color: '#bc4e9c'},
            {offset: 1, color: '#f80759'}
        ]),

        new echarts.graphic.LinearGradient(0, 0, 0, 1, [
            {offset: 0, color: '#FBD786'},
            {offset: 1, color: '#C6FFDD'}
        ]),

        // 其他渐变色定义...
        new echarts.graphic.LinearGradient(0, 0, 0, 1, [
            {offset: 0, color: '#396afc'},
            {offset: 1, color: '#2948ff'}
        ]),

    ];
    option7 = {
        color:colorList,
        legend: {
            top: "10%",
            data: ['水电', '火电', '核电', '风电', '太阳能'],
            textStyle: {
                color: 'white'
            }
        },
        tooltip: {
            trigger: 'axis',
            extraCssText: 'width: 10vw; height: 20vh;', // 设置tooltip框的宽度和高度，调整框的大小
            formatter: function (params) {
                let tooltipContent = '';
                let mineName = params[0].name;
                tooltipContent += '<span style="font-weight: bold;margin-right: 1vw; margin-top: -500px;">' + mineName + '</span>' + '单位 / 万千瓦<br>' + '<br>'; // 设置矿地名字的样式为加粗并向上移动5px
                params.forEach(function (param) {
                    if (param.seriesName !== '趋势') {
                        tooltipContent += param.marker + param.seriesName + ': ' + '<span style="float: right; font-weight: bold;">' + param.value + '</span>' + '<br>';
                    }
                });
                return tooltipContent;
            }
        },
        grid: {
            left: '3%',
            right: '5%',
            bottom: '3%',
            containLabel: true
        },
        xAxis: [
            {
                type: 'category',
                boundaryGap: false,
                data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
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
            }
        ],
        yAxis: [
            {
                type: 'value',
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
            }
        ],
        series: [
            {
                name: '水电',
                type: 'line',
                stack: 'Total',
                areaStyle: {
                    normal: {
                        color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
                            offset: 0,
                            color: 'rgba(236,56,188,0.5)' // 渐变色起始值
                        }, {
                            offset: 1,
                            color: 'rgba(253,239,249,0.5)' // 渐变色起始值
                        },
                        ])
                    }
                },
                emphasis: {
                    focus: 'series'
                },
                data: [120, 132, 101, 134, 90, 230, 210]
            },
            {
                name: '火电',
                type: 'line',
                stack: 'Total',
                areaStyle: {
                    normal: {
                        color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
                            offset: 0,
                            color: 'rgba(252,92,125,0.5)' // 渐变色起始值
                        }, {
                            offset: 1,
                            color: 'rgba(106,130,251,0.5)' // 渐变色起始值
                        },
                        ])
                    }
                },
                emphasis: {
                    focus: 'series'
                },
                data: [220, 182, 191, 234, 290, 330, 310]
            },
            {
                name: '核电',
                type: 'line',
                stack: 'Total',
                areaStyle: {
                    normal: {
                        color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
                            offset: 0,
                            color: 'rgba(188,78,156,0.05)' // 渐变色起始值
                        }, {
                            offset: 1,
                            color: 'rgba(248,7,89,0.5)' // 渐变色起始值
                        },
                        ])
                    }
                },
                emphasis: {
                    focus: 'series'
                },
                data: [150, 232, 201, 154, 190, 330, 410]
            },
            {
                name: '风电',
                type: 'line',
                stack: 'Total',
                areaStyle: {
                    normal: {
                        color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
                            offset: 0,
                            color: 'rgba(251,215,134,0.5)' // 渐变色起始值
                        }, {
                            offset: 1,
                            color: 'rgba(198,255,221,0.5)' // 渐变色起始值
                        },
                        ])
                    }
                },
                emphasis: {
                    focus: 'series'
                },
                data: [320, 332, 301, 334, 390, 330, 320]
            },
            {
                name: '太阳能',
                type: 'line',
                stack: 'Total',
                // label: {
                //     show: true,
                //     position: 'top'
                // },
                areaStyle: {
                    normal: {
                        color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
                            offset: 0,
                            color: 'rgba(57,106,252,0.5)' // 渐变色起始值
                        }, {
                            offset: 1,
                            color: 'rgba(41,72,255,0.5)' // 渐变色起始值
                        },
                        ])
                    }
                },
                emphasis: {
                    focus: 'series'
                },
                data: [820, 932, 901, 934, 1290, 1330, 1320]
            }
        ]
    };


    option7 && myChart7.setOption(option7);

    const resizeObserver = new ResizeObserver(() => {
        myChart7.resize();
    });

    resizeObserver.observe(echartsRef.value);
});
</script>


<template>
    <div className="MainDownSea">
        <Button class="GotoSea">全国发电装机容量</Button>
        <div id="MainDownSea-echarts" ref="echartsRef"></div>
    </div>
</template>

<style scoped lang="scss">
.MainDownSea {
  width: 100vw;
  height: 100vh;
  color: white;

  .GotoSea {
    position: absolute;
    margin-top: -26vh;
    border: none;
    background: none;
    color: white;
    font-weight: bolder;
    font-size: 1.2vw;
    margin-left: 7vw;
    //cursor: pointer;
  }

  //.GotoSea:hover {
  //  font-size: 1.3vw;
  //  margin-left: 6.7vw;
  //  margin-top: -26.1vh;
  //}
  //
  //.GotoSea:active {
  //  margin-top: -26vh;
  //  font-size: 1.2vw;
  //  margin-left: 7vw;
  //}

  #MainDownSea-echarts {
    width: 23vw;
    height: 32vh;
    margin-left: 0.6vw;
    position: absolute;
    margin-top: -25.5vh;
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
