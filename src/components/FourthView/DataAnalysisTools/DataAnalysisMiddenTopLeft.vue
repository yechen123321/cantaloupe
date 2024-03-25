<script setup>
import {ref, onMounted} from "vue";
import * as echarts from "echarts";

const echartsRef = ref(null);
let myChart87 = null;
let option87 = null;
const echartsRef2 = ref(null);
let myChart88 = null;
let option88 = null;
onMounted(() => {
    myChart87 = echarts.init(echartsRef.value, 'dark');
    myChart88 = echarts.init(echartsRef2.value, 'dark');
    // Your echarts option setup here...
    // (Your existing option setup code)
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
    option87 = {
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
            top: '15%',
            left: 'center',
            data: ['2021', '2022', '2023',],
            itemWidth: 20, // 标签宽度为20px
            itemHeight: 10, // 标签高度为10px
        },
        xAxis: [
            {
                type: 'category',
                data: ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'],
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
                name: '万吨',
                min: 0,
                // max: 250,
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
        ],
        series: [
            {
                name: '2021',
                type: 'line',
                tooltip: {
                    valueFormatter: function (value) {
                        return value + ' ml';
                    }
                },
                data: [
                    176.7, 235.6, 262.2, 132.6, 262.2, 132.6, 176.7, 235.6, 262.2, 132.6, 176.7, 235.6,
                ]
            },
            {
                name: '2022',
                type: 'line',
                tooltip: {
                    valueFormatter: function (value) {
                        return value + ' ml';
                    }
                },
                data: [
                    135.6, 162.2, 76.7, 135.6, 162.2, 32.6, 162.2, 32.6, 76.7, 135.6, 162.2, 162.2,
                ]
            },
            {
                name: '2023',
                type: 'line',
                tooltip: {
                    valueFormatter: function (value) {
                        return value + ' %';
                    }
                },
                data: [
                    210.3, 123.4, 223.0, 126.5, 123.0, 136.5, 220.3, 120.3, 223.4, 123.0, 223.0, 126.5,
                ]
            },
        ]
    };

    option88 = {
        color: colorList,
        backgroundColor: 'rgba(1,1,1,0)',
        // toolbox: {
        //     iconStyle: {
        //         borderColor: "#fff",
        //     },
        //     showTitle:false,
        //     right:'3%',
        //     feature: {
        //         dataView: { show: true, readOnly: false },
        //         // magicType: { show: true, type: ['line', 'bar'] },
        //         restore: { show: true },
        //         saveAsImage: { show: true }
        //     }
        // },
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
            top: '3%',
            itemWidth: 10, // 标签宽度为10px
            itemHeight: 10, // 标签高度为10px
            data: ['开采耗费', '获取能量', '能耗降低率'],
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
                    color: 'white',
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
                    color: 'white',
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
                nameTextStyle: {
                    color: 'white',
                    padding: [0, 10, 0, 0]
                },
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
                name: '开采耗费',
                type: 'bar',
                yAxisIndex: 2,
                data: [
                    135.6, 162.2, 32.6, 20.0, 6.4,
                ]
            },
            {
                name: '获取能量',
                type: 'bar',
                yAxisIndex: 0,
                data: [
                    175.6, 182.2, 48.7, 18.8, 6.0
                ]
            },
            {
                name: '能耗降低率',
                type: 'line',
                yAxisIndex: 1,
                data: [3.4, 2.0, 1.5, 1.0, 3.2]
            },
        ]
    };

    option87 && myChart87.setOption(option87);
    option88 && myChart88.setOption(option88);

    const resizeObserver = new ResizeObserver(() => {
        myChart87.resize();
        myChart88.resize();
    });

    resizeObserver.observe(echartsRef.value);
});

</script>

<template>
    <div class="DataAnalysisMiddenTopLeft">
        <div class="TitleFirst">安徽省能源采集效率</div>
        <div class="DataAnalysisMiddenTopLeft-top" ref="echartsRef2"></div>
        <div class="TitleSecond">安徽省碳排放量统计</div>
        <div class="DataAnalysisMiddenTopLeft-down" ref="echartsRef"></div>
    </div>
</template>

<style scoped>
.DataAnalysisMiddenTopLeft {
    width: 100%;
    height: 100%;

    .TitleFirst {
        color: white;
        position: absolute;
        font-weight: bolder;
        margin-top: -6vh;
        width: 26vw;
        margin-left: -2vw;
        text-align: center;
        font-size: 1.3em;
    }

    .TitleSecond {
        color: white;
        position: absolute;
        font-weight: bolder;
        margin-top: 21vh;
        width: 26vw;
        margin-left: -2vw;
        text-align: center;
        font-size: 1.3em;
    }

    .DataAnalysisMiddenTopLeft-down {
        width: 31vw;
        height: 29vh;
        position: absolute;
        margin-top: 21vh;
        margin-left: -2vw;
        z-index: 333;
    }

    .DataAnalysisMiddenTopLeft-top {
        width: 25.5vw;
        height: 28vh;
        margin-top: -3vh;
        z-index: 333;
        position: absolute;
    }
}
</style>