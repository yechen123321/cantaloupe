<script setup>
import {ref, onMounted, onBeforeUnmount} from 'vue';
import * as echarts from 'echarts';
import {
    initK11,
    initK12,
    initK13,
    initK14,
    initK15,
    initKlist21,
    initKlist22,
    initKlist23,
    initKlist24,
    initKlist25,
    initKlist26,
    initKlist27,
    initKlist28,
    initKlist29,
    initKlist30,
    initKlist31
} from '@/api'
const echartsRef = ref(null);
let myChart30 = null;
let option30 = null;
// let currentIndex = 0;
let highlightTimer = null;

onMounted(() => {
    // myChart30 = echarts.init(echartsRef.value);
    myChart30 = echarts.init(echartsRef.value, 'dark');
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
    // Your echarts option setup here...
    // (Your existing option setup code)
    option30 = {
        backgroundColor: 'rgba(128,128,128,0)',
        color: colorList,
        // title: {
        //     text: 'Stacked Area Chart'
        // },
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
            data: ['风能', '水利', '光伏', '质能', '其他']
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
                offset: 5, // 负值表示向左偏移，这里设置为向左移动 10px
                type: 'value',
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
                name: '其他',
                type: 'line',
                stack: 'Total',
                areaStyle: {
                    normal: {
                        color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
                            offset: 0,
                            color: 'rgba(234,212,124,0.7)' // 渐变色起始值
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
                name: '质能',
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
                name: '风能',
                type: 'line',
                stack: 'Total',
                areaStyle: {
                    normal: {
                        color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
                            offset: 0,
                            color: 'rgba(88,250,250,0.7)' // 渐变色起始值
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
                name: '水利',
                type: 'line',
                stack: 'Total',
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
                data: [320, 332, 301, 334, 390, 330, 320]
            },
            {
                name: '光伏',
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
                            color: 'rgba(115,192,222,0.3)' // 渐变色起始值
                        }, {
                            offset: 1,
                            color: 'rgba(115,192,222,0)' // 渐变色起始值
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


    option30 && myChart30.setOption(option30);

    const resizeObserver = new ResizeObserver(() => {
        myChart30.resize();
    });

    resizeObserver.observe(echartsRef.value);
});

// 组件销毁时清除定时器
onBeforeUnmount(() => {
    clearInterval(highlightTimer);
});
</script>

<template>
    <div class="AnHuiRightTop">
        <div class="AnHuiRightTop-title">北京市再生能源储量</div>
        <div class="AnHuiRightTop-echarts" ref="echartsRef"></div>
        <img class="BackImg" src="../../../assets/pic/border4.png" alt="">
    </div>
</template>

<style scoped lang="scss">
.AnHuiRightTop {
    width: 100%;
    height: 100%;

    .AnHuiRightTop-title {
        font-size: 1.15em;
        width: 24vw;
        //background: red;
        color: white;
        text-align: center;
        position: absolute;
        font-weight: bolder;
        //background: none;
        margin-top: -9.5vh;
        margin-left: 13vw;
    }

    .AnHuiRightTop-echarts {
        position: absolute;
        width: 24vw;
        height: 23vh;
        margin-left: 12vw;
        margin-top: -10vh;
    }

    .BackImg {
        width: 25vw;
        height: 23vh;
        margin-left: 12vw;
        margin-top: -10vh;
    }
}
</style>