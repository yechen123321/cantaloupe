<script setup>
import {ref, onMounted} from 'vue';
import * as echarts from 'echarts';
import AnHuiMiddenDownThing from "@/components/SecondView/AnHuiRenewViewTools/AnHuiMiddenDownThing.vue";

const echartsRef = ref(null);
let myChart22 = null;
let option22 = null;

onMounted(() => {
    myChart22 = echarts.init(echartsRef.value);
    var colorList = [
        new echarts.graphic.LinearGradient(0, 0, 0, 1, [
            {offset: 1, color: '#00C9FF'},
            {offset: 0, color: '#92FE9D'}
        ]),
        new echarts.graphic.LinearGradient(0, 0, 0, 1, [
            {offset: 1, color: '#C6FFDD'},
            {offset: 0, color: '#FBD786'},
        ]),
        new echarts.graphic.LinearGradient(0, 0, 0, 1, [
            {offset: 0, color: '#56CCF2'},
            {offset: 1, color: '#2948ff'}
        ]),
        // 其他渐变色定义...
    ];
    option22 = {
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
            top: '10%',
            data: ['现有量', '增长量', '增长率'],
            itemWidth: 20, // 标签宽度为20px
            itemHeight: 10, // 标签高度为10px
        },
        xAxis: [
            {
                type: 'category',
                data: ['2020', '2021', '2022', '2023'],
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
                name: '万千瓦',
                min: 0,
                max: 250,
                nameTextStyle: {
                    padding: [0, 10, 0, 0]
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
            {
                type: 'value',
                name: '百分比',
                min: 0,
                max: 25,
                nameTextStyle: {
                    padding: [0, -25, 0, 0]
                },
                interval: 5,
                axisLabel: {
                    textStyle: {
                        color: 'white' // 设置Y轴上数据的颜色为白色
                    }, formatter: '{value} %'

                },
                axisLine: {
                    lineStyle: {
                        color: 'white',
                    },
                },
            }
        ],
        series: [
            {
                name: '现有量',
                type: 'bar',
                tooltip: {
                    valueFormatter: function (value) {
                        return value + ' 万千瓦';
                    }
                },
                data: [
                    176.7, 135.6, 162.2, 132.6,
                ],
                itemStyle: {
                    barBorderRadius: [10,10, 0, 0] // 设置柱子上方为圆角，数组中的四个值分别代表左上、右上、右下、左下的圆角半径
                }
            },
            {
                name: '增长量',
                type: 'bar',
                tooltip: {
                    valueFormatter: function (value) {
                        return value + ' 万千瓦';
                    }
                },
                data: [
                    70.7,75.6, 82.2, 48.7,
                ],
                itemStyle: {
                    barBorderRadius: [10, 10, 0, 0] // 设置柱子上方为圆角，数组中的四个值分别代表左上、右上、右下、左下的圆角半径
                }
            },
            {
                name: '增长率',
                type: 'line',
                yAxisIndex: 1,
                tooltip: {
                    valueFormatter: function (value) {
                        return value + ' %';
                    }
                },
                data: [20.3, 23.4, 23.0, 16.5,],
            }
        ]
    };

    option22 && myChart22.setOption(option22);
    const resizeObserver = new ResizeObserver(() => {
        myChart22.resize();
    });

    resizeObserver.observe(echartsRef.value);

});
</script>

<template>
    <div class="AnHuiMiddenDown">
        <img class="BackImg" src="../../../assets/pic/border4.png" alt="">
        <div class="AnHuiMiddenDown-title">安徽省再生能源装机容量</div>
        <div class="AnHuiMiddenDown-echarts" ref="echartsRef"></div>
        <AnHuiMiddenDownThing class="AnHuiMiddenDownThing-out"></AnHuiMiddenDownThing>
    </div>
</template>

<style scoped lang="scss">
.AnHuiMiddenDown {
  width: 100%;
  height: 100%;
  //background: red;
  .BackImg {
    width: 40vw;
    height: 29vh;
    position: absolute;
  }

  .AnHuiMiddenDown-title {
    color: white;
    position: absolute;
    width: 100%;
    //background: red;
    text-align: center;
    font-weight: bolder;
    margin-top: 1vh;
    font-size: 1.26em;
  }

  .AnHuiMiddenDownThing-out {
    width: 14vw;
    height: 22vh;
    position: absolute;
    //background: red;
    right: 0;
    margin-top: 5.5vh;
    margin-right: -0.7vw;
    border-left: 2px solid #0d87f6;
  }

  .AnHuiMiddenDown-echarts {
    width: 28vw;
    height: 32vh;
    margin-top: 1.5vh;
    margin-left: -1vw;
    position: absolute;
    z-index: 999;
    //background: red;
  }


}
</style>
