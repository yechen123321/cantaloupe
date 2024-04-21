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
        new echarts.graphic.LinearGradient(0, 0, 0, 1, [
            {offset: 0, color: '#396afc'},
            {offset: 1, color: '#2948ff'}
        ]),

        new echarts.graphic.LinearGradient(0, 0, 0, 1, [
            {offset: 0, color: '#00F260'},
            {offset: 1, color: '#0575E6'}
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
                areaStyle: {
                    normal: {
                        color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
                            offset: 0,
                            color: 'rgba(57,106,252,0.5)' // 渐变色起始值
                        }, {
                            offset: 1,
                            color: 'rgba(41,72,255,0.1)' // 渐变色起始值
                        },
                        ])
                    }
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
                areaStyle: {
                    normal: {
                        color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
                            offset: 0,
                            color: 'rgba(0,242,96,0.5)' // 渐变色起始值
                        }, {
                            offset: 1,
                            color: 'rgba(5,117,230,0.1)' // 渐变色起始值
                        },
                        ])
                    }
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
                areaStyle: {
                    normal: {
                        color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
                            offset: 0,
                            color: 'rgba(188,78,156,0.5)' // 渐变色起始值
                        }, {
                            offset: 1,
                            color: 'rgba(248,7,89,0.1)' // 渐变色起始值
                        },
                        ])
                    }
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
                areaStyle: {
                    normal: {
                        color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
                            offset: 0,
                            color: 'rgba(251,215,134,0.5)' // 渐变色起始值
                        }, {
                            offset: 1,
                            color: 'rgba(198,255,221,0.1)' // 渐变色起始值
                        },
                        ])
                    }
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
    <div class="DataAnalysisMiddenTopLeft">
        <div class="TitleFirst">安徽省能源发展统计</div>
        <div class="TitleSecond">安徽省耗能时间分布</div>
        <div class="AnHuiLeftTop-main">
            <div class="MainOne">
                <img src="../../../assets/为国内生产总值贡献.png" alt="" class="pic">
                <div class="number">
                    <div class="one">4.71</div>
                    <div class="up">万亿元</div>
                </div>
                <div class="tow">全省生产总值</div>
            </div>
            <div class="MainTow">
                <img src="../../../assets/装机容量.png" alt="" class="pic">
                <div class="number">
                    <div class="one" style="margin-left: 0.2vw">1.081</div>
                    <div class="up">亿千瓦</div>
                </div>
                <div class="tow">全省总装机容量</div>
            </div>
            <div class="MainThree">
                <img src="../../../assets/日用电量查询.png" alt="" class="pic" style="margin-top: 3vh">
                <div class="number">
                    <div class="one" style="margin-left: -0.2vw">3214</div>
                    <div class="up" style="margin-left: 5vw">亿千瓦时</div>
                </div>
                <div class="tow">全省社会用电</div>
            </div>
            <div class="MainFour">
                <img src="../../../assets/投资.png" style="margin-top: 3vh" alt="" class="pic">
                <div class="number">
                    <div class="one" style="margin-left: 0.3vw">14.33</div>
                    <div class="up">%</div>
                </div>
                <div class="tow">建设投资增长</div>
            </div>
        </div>
        <div class="DataAnalysisMiddenTopLeft-down" ref="echartsRef"></div>
    </div>
</template>

<style scoped>
.DataAnalysisMiddenTopLeft {
    width: 100%;
    height: 100%;

    .AnHuiLeftTop-main {
        position: absolute;
        width: 25vw;
        height: 18vh;
        margin-left: 1vw;
        margin-top: -3.5vh;
        color: white;

        .number {
            position: absolute;
            width: 8vw;
            height: 4vh;
            margin-top: 5.7vh;
            margin-left: 3vw;

            .up {
                position: absolute;
                width: 5vw;
                margin-left: 4.2vw;
                text-align: center;
                font-size: 0.8em;
                margin-top: 1vh;
                font-weight: bolder;
            }

            .one {
                position: absolute;
                font-size: 1.6em;
                margin-left: -0.6vw;
                line-height: 3.7vh;
                margin-top: -0.3vh;
                font-weight: bolder;
                width: 6vw;
                text-align: center;
                height: 3.7vh;
                color: #fac800;
                text-shadow: 0 0 1px #fac800, 0 0 1px #fac800, 0 0 2px #fac800;
            }
        }

        .tow {
            position: absolute;
            margin-left: 3vw;
            margin-top: 2vh;
            width: 8vw;
            font-size: 1em;
            font-weight: bolder;
            height: 3vh;
            border-bottom: 2px solid #00bfff;
            text-align: center;
        }

        .pic {
            position: absolute;
            width: 2.7vw;
            height: 5vh;
            margin-top: 2.4vh;
        }

        .MainOne {
            width: 11vw;
            height: 8vh;
            position: absolute;
        }

        .MainTow {
            width: 11vw;
            height: 8vh;
            position: absolute;
            margin-left: 13vw;
        }

        .MainThree {
            width: 11vw;
            height: 8vh;
            position: absolute;
            margin-top: 10vh;
        }

        .MainFour {
            width: 11vw;
            height: 8vh;
            position: absolute;
            margin-top: 10vh;
            margin-left: 13vw;
            z-index: 999;
        }
    }

    .TitleSecond {
        color: white;
        position: absolute;
        font-weight: bolder;
        margin-top: 17.5vh;
        width: 26vw;
        margin-left: -4vw;
        text-align: center;
        font-size: 1.25em;
    }

    .TitleFirst {
        color: white;
        position: absolute;
        font-weight: bolder;
        margin-top: -6vh;
        width: 26vw;
        margin-left: -4vw;
        text-align: center;
        font-size: 1.25em;
    }

    .DataAnalysisMiddenTopLeft-down {
        width: 28vw;
        height: 30vh;
        position: absolute;
        margin-top: 17vh;
        z-index: 999;
    }
}
</style>