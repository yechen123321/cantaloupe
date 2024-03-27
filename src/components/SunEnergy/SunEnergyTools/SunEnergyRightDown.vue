<script setup>
import {ref, onMounted} from "vue";
import * as echarts from "echarts";

const echartsRef = ref(null);
let myChart87 = null;
let option87 = null;
const echartsRef2 = ref(null);
let myChart88 = null;
let option88 = null;
var app = {};
onMounted(() => {
    myChart87 = echarts.init(echartsRef.value, 'dark');
    myChart88 = echarts.init(echartsRef2.value, 'dark');
    // Your echarts option setup here...
    // (Your existing option setup code)
    var colorList = [
        new echarts.graphic.LinearGradient(0, 0, 0, 1, [
            {offset: 0, color: '#8E2DE2'},
            {offset: 1, color: '#4A00E0'}
        ]),


        new echarts.graphic.LinearGradient(0, 0, 0, 1, [
            {offset: 0, color: '#00C9FF'},
            {offset: 1, color: '#92FE9D'}
        ]),
        new echarts.graphic.LinearGradient(0, 0, 0, 1, [
            {offset: 0, color: '#ee9ca7'},
            {offset: 1, color: '#ffdde1'}
        ]),
        new echarts.graphic.LinearGradient(0, 0, 0, 1, [
            {offset: 0, color: '#bc4e9c'},
            {offset: 1, color: '#f80759'}
        ]),
        new echarts.graphic.LinearGradient(0, 0, 0, 1, [
            {offset: 0, color: '#396afc'},
            {offset: 1, color: '#2948ff'}
        ]),
        new echarts.graphic.LinearGradient(0, 0, 0, 1, [
            {offset: 0, color: '#FBD786'},
            {offset: 1, color: '#C6FFDD'}
        ])
    ]
    const categories = (function () {
        let now = new Date();
        let res = [];
        let len = 10;
        while (len--) {
            res.unshift(now.toLocaleTimeString().replace(/^\D*/, ""));
            now = new Date(+now - 2000);
        }
        return res;
    })();
    const categories2 = (function () {
        let res = [];
        let len = 10;
        while (len--) {
            res.push(10 - len - 1);
        }
        return res;
    })();
    const getRandomNumber = (min, max) => {
        return parseInt(Math.random() * (max - min + 1) + min);
    };

    const data = (function () {
        let res = [];
        let len = 10;
        while (len--) {
            res.push(Number(getRandomNumber(110, 220).toFixed(1)));
        }
        return res;
    })();

    const data2 = (function () {
        let res = [];
        let len = 0;
        while (len < 10) {
            res.push(Number(getRandomNumber(60, 90).toFixed(1)));
            len++;
        }
        return res;
    })();

    option87 = {
        color: colorList,
        backgroundColor: "rgba(128, 128, 128, 0)",
        tooltip: {
            trigger: "axis",
            axisPointer: {
                type: "cross",
                label: {
                    backgroundColor: "#283b56",
                },
            },
        },
        grid:{
            right:'12%'
        },
        legend: {
            top: "14%",
            textStyle: {
                color: "white",
            },
        },
        dataZoom: {
            show: false,
            start: 0,
            end: 100,
        },
        xAxis: [
            {
                type: "category",
                boundaryGap: true,
                data: categories,
                axisLabel: {
                    textStyle: {
                        color: "white", // 设置Y轴上数据的颜色为白色
                    },
                },
                axisLine: {
                    lineStyle: {
                        color: "white",
                    },
                },
            },
            {
                type: "category",
                boundaryGap: true,
                data: categories,
                axisLabel: {
                    show: false,
                    textStyle: {
                        color: "white", // 设置Y轴上数据的颜色为白色
                    },
                },
                axisLine: {
                    lineStyle: {
                        color: "white",
                    },
                },
            },
        ],
        yAxis: [
            {
                type: "value",
                scale: true,
                name: "千瓦时/平方米",
                nameTextStyle: {
                    padding: [0, -20, 0, 0],
                    color: "white",
                },
                axisLabel: {
                    textStyle: {
                        color: "white", // 设置Y轴上数据的颜色为白色
                    },
                },
                axisLine: {
                    lineStyle: {
                        color: "white",
                    },
                },
                max: 220,
                min: 60,
                interval: 40, // 设置Y轴刻度间隔为20
                splitNumber: 4, // 设置Y轴线条数量为4
                boundaryGap: [0.2, 0.2],
            },
            {
                type: "value",
                scale: true,
                name: "百分比",
                nameTextStyle: {
                    color: "white",
                    padding: [0, -40, 0, 0],
                },
                axisLabel: {
                    formatter: "{value}%", // 在每个数据后面添加%
                    textStyle: {
                        color: "white", // 设置Y轴上数据的颜色为白色
                    },
                },
                axisLine: {
                    lineStyle: {
                        color: "white",
                    },
                },
                max: 100,
                min: 0,
                interval: 25, // 设置Y轴刻度间隔为20
                splitNumber: 4, // 设置Y轴线条数量为4
                boundaryGap: [0.2, 0.2],
            },
        ],
        series: [
            {
                name: "日照量",
                type: "bar",

                data: data,
            },
            {
                name: "利用率",
                type: "line",
                xAxisIndex: 1,
                yAxisIndex: 1,
                data: data2,
            },
        ],
    };
    app.count = 11;
    setInterval(function () {
        let axisData = new Date().toLocaleTimeString().replace(/^\D*/, "");
        data.shift();
        data.push(Number(getRandomNumber(110, 220).toFixed(1)));
        data2.shift();
        data2.push(+Number(getRandomNumber(60, 90).toFixed(1)));
        categories.shift();
        categories.push(axisData);
        categories2.shift();
        categories2.push(app.count++);
        myChart87.setOption({
            xAxis: [
                {
                    data: categories,
                },
                {
                    data: categories,
                },
            ],
            series: [
                {
                    data: data,
                },
                {
                    data: data2,
                },
            ],
        });
    }, 2100);

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
            data: ['运营耗资', '能源获取', '开发效率'],
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
                    padding: [0, -10, 0, 0]
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
                    padding: [0, -18, 0, 0]
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
                    padding: [0, -25, 0, 0]
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
                name: '运营耗资',
                type: 'bar',
                yAxisIndex: 2,
                data: [
                    135.6, 162.2, 32.6, 20.0, 6.4,
                ]
            },
            {
                name: '能源获取',
                type: 'bar',
                yAxisIndex: 0,
                data: [
                    175.6, 182.2, 48.7, 18.8, 6.0
                ]
            },
            {
                name: '开发效率',
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
    <div class="ThermalPowerRightDown">
        <div class="title">光伏数据图</div>
        <div class="title2">能源开发效率</div>
        <div class="ThermalPowerRightDown-echarts" ref="echartsRef"></div>
        <div class="ThermalPowerRightDown-echarts2" ref="echartsRef2"></div>
        <img src="../../../assets/pic/border3.png" alt="" class="BackImg">
    </div>
</template>

<style scoped lang="scss">
.ThermalPowerRightDown {
    width: 100%;
    height: 100%;

    .ThermalPowerRightDown-echarts {
        position: absolute;
        width: 25vw;
        height: 30.5vh;
        margin-left: 0.5vw;
        margin-top: 2vh;
    }

    .ThermalPowerRightDown-echarts2 {
        position: absolute;
        width: 26vw;
        height: 30vh;
        margin-top: 30vh;
        z-index: 300;
    }

    .title2 {
        color: white;
        position: absolute;
        font-weight: bolder;
        font-size: 1.2em;
        margin-left: 2vw;
        width: 21.7vw;
        text-align: center;
        margin-top: 27.3vh;
    }

    .title {
        color: white;
        position: absolute;
        font-weight: bolder;
        font-size: 1.2em;
        margin-left: 2vw;
        width: 21.7vw;
        text-align: center;
        margin-top: 3vh;
    }

    .BackImg {
        width: 26vw;
        height: 57vh;
    }
}
</style>