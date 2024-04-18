<script setup>
import {onMounted, ref} from "vue";
import * as echarts from "echarts";
import AnHuiWindMiddenDownThing from "@/components/SecondView/AnHuiWindTools/AnHuiWindMiddenDownThing.vue";

const echartsRef = ref(null);
let myChart54 = null;
let option54 = null;

onMounted(() => {
    myChart54 = echarts.init(echartsRef.value, 'dark');
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
    // Your echarts option setup here...
    // (Your existing option setup code)
    option54 = {
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
            top: '12%',
            data: ['现有量', '增长量', '增长率'],
            itemWidth: 20, // 标签宽度为20px
            itemHeight: 10, // 标签高度为10px
        },
        xAxis: [
            {
                type: 'category',
                data: ['2017', '2018', '2019', '2020', '2021', '2022', '2023'],
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
                    color: 'white',
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
                    color: 'white',
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
                    176.7, 135.6, 162.2, 132.6, 162.2, 132.6, 176.7,
                ],
                itemStyle: {
                    barBorderRadius: [8, 8, 0, 0] // 设置柱子上方为圆角，数组中的四个值分别代表左上、右上、右下、左下的圆角半径
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
                    70.7, 75.6, 82.2, 48.7, 82.2, 48.7, 70.7,
                ],
                itemStyle: {
                    barBorderRadius: [8, 8, 0, 0] // 设置柱子上方为圆角，数组中的四个值分别代表左上、右上、右下、左下的圆角半径
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
                data: [20.3, 23.4, 23.0, 16.5, 23.0, 16.5, 20.3,]
            }
        ]
    };
    option54 && myChart54.setOption(option54);

    const resizeObserver = new ResizeObserver(() => {
        myChart54.resize();
    });

    resizeObserver.observe(echartsRef.value);
});
</script>
<template>
    <div class="AnHuiWindMiddenDown">
        <div class="title">安徽省风能发电装机容量</div>
        <img src="../../../assets/pic/border4.png" alt="" class="BackImg">
        <div class="AnHuiWindMiddenDown-echarts" ref="echartsRef"></div>
        <AnHuiWindMiddenDownThing id="AnHuiWindMiddenDownThing"></AnHuiWindMiddenDownThing>
    </div>
</template>

<style scoped lang="scss">
.AnHuiWindMiddenDown {
  width: 100%;
  height: 100%;

  #AnHuiWindMiddenDownThing {
    width: 16vw;
    height: 20vh;
    position: absolute;
    margin-left: 27vw;
    margin-top: -24vh;
    border-left: 2px solid #0d87f6;
  }

  .title {
    position: absolute;
    color: white;
    width: 40vw;
    font-weight: bolder;
    font-size: 1.15em;
    text-align: center;
    margin-top: 1vh;
  }

  .AnHuiWindMiddenDown-echarts {
    width: 28vw;
    height: 33vh;
    position: absolute;
    margin-top: -28.5vh;
    margin-left: -1vw;
    z-index: 555;
  }

  .BackImg {
    width: 40vw;
    height: 29vh;
  }
}
</style>