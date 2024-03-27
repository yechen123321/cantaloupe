
<script setup>
import {onMounted, ref} from 'vue';
import * as echarts from "echarts";
import SunEnergyMiddenDownThing from "@/components/SunEnergy/SunEnergyTools/SunEnergyMiddenDownThing.vue";
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
    <div class="SunEnergyMiddenDown">
        <div class="title">电场历史发电量</div>
        <div class="SunEnergyMiddenDown-echarts" ref="echartsRef"></div>
        <div class="right">
            <SunEnergyMiddenDownThing id="SunEnergyMiddenDownThing-out"></SunEnergyMiddenDownThing>
        </div>
        <img src="../../../assets/pic/border4.png" alt="" class="BackImg">
    </div>
</template>

<style scoped lang="scss">
.SunEnergyMiddenDown {
    width: 100%;
    height: 100%;
    .right{
        width: 15vw;
        height: 23vh;
        margin-top: 6vh;
        border-left: #0d87f6 2px solid;
        margin-right: 1vw;
        position: absolute;
        right: 0;
        #SunEnergyMiddenDownThing-out{
            width: 24vw;
            height: 24vh;
            margin-left: -1.5vw;
            position: absolute;
            z-index: 300;
        }
    }
    .SunEnergyMiddenDown-echarts{
        position: absolute;
        width: 29vw;
        height: 34vh;
        margin-left: 1vw;
        z-index: 300;
    }
    .title{
        color:white;
        position: absolute;
        font-weight: bolder;
        font-size: 1.5em;
        width: 20vw;
        text-align: center;
        margin-left: 3.6vw;
        margin-top: 1vh;
    }
    .BackImg {
        width: 43vw;
        height: 31vh;
    }
}
</style>