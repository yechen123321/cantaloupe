<script setup>
import {onMounted, ref} from "vue";
import * as echarts from "echarts";

const echartsRef = ref(null);
let myChart47 = null;
let option47 = null;

onMounted(() => {
    myChart47 = echarts.init(echartsRef.value, 'dark');
    var colorList = [
        new echarts.graphic.LinearGradient(0, 0, 0, 1, [
            {offset: 1, color: '#C6FFDD'},
            {offset: 0, color: '#FBD786'},
        ]),
        new echarts.graphic.LinearGradient(0, 0, 0, 1, [
            {offset: 0, color: '#00C9FF'},
            {offset: 1, color: '#92FE9D'}
        ]),
        new echarts.graphic.LinearGradient(0, 0, 0, 1, [
            {offset: 0, color: '#4AC29A'},
            {offset: 1, color: '#BDFFF3'}
        ]),
        new echarts.graphic.LinearGradient(0, 0, 0, 1, [
            {offset: 0, color: '#DCE35B'},
            {offset: 1, color: '#45B649'}
        ]),
        new echarts.graphic.LinearGradient(0, 0, 0, 1, [
            {offset: 0, color: '#56CCF2'},
            {offset: 1, color: '#2948ff'}
        ]),
        // 其他渐变色定义...
    ];

    option47 = {
        backgroundColor: 'rgba(128,128,128,0)',
        color: colorList,

        tooltip: {
            trigger: 'axis',
            extraCssText: 'width: 10vw; height: 15vh;', // 设置tooltip框的宽度和高度，调整框的大小
            formatter: function (params) {
                let tooltipContent = '';
                let mineName = params[0].name;
                tooltipContent += '<span style="font-weight: bold; margin-top: -500px; margin-right: 2vw">' + mineName + '</span>' + '单位/万千瓦' + '<br>'; // 设置矿地名字的样式为加粗并向上移动5px
                params.forEach(function (param) {
                    if (param.seriesName !== '趋势') {
                        tooltipContent += param.marker + param.seriesName + ': ' + '<span style="float: right; font-weight: bold;">' + param.value + '</span>' + '<br>';
                    }
                });
                return tooltipContent;
            }
        },
        legend: {
            top: '15%',
            textStyle: {
                color: 'white'
            },
            data: ['合肥', '马鞍山', '芜湖', '阜阳', '其他']
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
                axisLine: {
                    lineStyle: {
                        color: 'white',
                    },
                },
                axisLabel: {
                    color: 'white' // 设置轴标签文字颜色为白色
                },
                boundaryGap: false,
                data: ['2017', '2018', '2019', '2020', '2021', '2022', '2023']
            }
        ],
        yAxis: [
            {
                type: 'value',
                offset: 5, // 负值表示向左偏移，这里设置为向左移动 10px
                axisLine: {
                    lineStyle: {
                        color: 'white', // 设置轴线颜色为白色
                    },
                },
                axisLabel: {
                    color: 'white' // 设置轴标签文字颜色为白色
                }
            }
        ],
        series: [
            {
                name: '合肥',
                type: 'line',
                stack: 'Total',
                areaStyle: {
                    normal: {
                        color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
                            offset: 0,
                            color: 'rgba(234,124,204,0.7)' // 渐变色起始值
                        }, {
                            offset: 1,
                            color: 'rgba(234,124,204,0.1)' // 渐变色起始值
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
                name: '马鞍山',
                type: 'line',
                stack: 'Total',
                areaStyle: {
                    normal: {
                        color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
                            offset: 0,
                            color: 'rgba(145,204,117,0.7)' // 渐变色起始值
                        }, {
                            offset: 1,
                            color: 'rgba(145,204,117,0.1)' // 渐变色起始值
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
                name: '阜阳',
                type: 'line',
                stack: 'Total',
                areaStyle: {
                    normal: {
                        color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
                            offset: 0,
                            color: 'rgba(250,200,88,0.7)' // 渐变色起始值
                        }, {
                            offset: 1,
                            color: 'rgba(250,200,88,0.1)' // 渐变色起始值
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
                name: '芜湖',
                type: 'line',
                stack: 'Total',
                areaStyle: {
                    normal: {
                        color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
                            offset: 0,
                            color: 'rgba(238,102,102,0.7)' // 渐变色起始值
                        }, {
                            offset: 1,
                            color: 'rgba(238,102,102,0.1)' // 渐变色起始值
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
                name: '其他',
                type: 'line',
                stack: 'Total',
                label: {
                    show: true,
                    position: 'top',
                    color: 'white'
                },
                areaStyle: {
                    normal: {
                        color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
                            offset: 0,
                            color: 'rgba(115,192,222,0.7)' // 渐变色起始值
                        }, {
                            offset: 1,
                            color: 'rgba(115,192,222,0.1)' // 渐变色起始值
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
    }


    option47 && myChart47.setOption(option47);

    const resizeObserver = new ResizeObserver(() => {
        myChart47.resize();
    });

    resizeObserver.observe(echartsRef.value);
});
</script>


<template>
    <div class="AnHuiSunLeftDown">
        <div class="title">安徽省光伏能源储能</div>
        <div class="AnHuiSunLeftDown-echarts" ref="echartsRef"></div>
    </div>
</template>

<style scoped lang="scss">
.AnHuiSunLeftDown {
  width: 100%;
  height: 100%;

  .title {
    position: absolute;
    color: white;
    font-weight: bolder;
    text-align: center;
    font-size: 1.15em;
    margin-top: 0.2vh;
    width: 24vw;
    margin-left: 1vw;
  }

  .AnHuiSunLeftDown-echarts {
    width: 24vw;
    height: 27vh;
    margin-top: 0.6vh;
    margin-left: 1.3vw;
    z-index: 555;
  }
}
</style>

