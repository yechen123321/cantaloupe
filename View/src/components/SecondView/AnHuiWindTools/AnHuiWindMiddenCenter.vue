<script setup>
import {onMounted, ref} from "vue";
import * as echarts from "echarts";

const echartsRef = ref(null);
let myChart62 = null;
let option62 = null;

onMounted(() => {
    myChart62 = echarts.init(echartsRef.value, 'dark');
    // Your echarts option setup here...
    // (Your existing option setup code)
    var colorList = [
        new echarts.graphic.LinearGradient(0, 0, 0, 1, [
            {offset: 0, color: '#6cd7fa'},
            {offset: 1, color: '#2948ff'}
        ]),
        new echarts.graphic.LinearGradient(0, 0, 0, 1, [
            {offset: 1, color: '#00C9FF'},
            {offset: 0, color: '#92FE9D'}
        ]),
        new echarts.graphic.LinearGradient(0, 0, 0, 1, [
            {offset: 0, color: '#FBD786'},
            {offset: 1, color: '#C6FFDD'}
        ]),
        // 其他渐变色定义...
    ];
    option62 = {
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
    option62 && myChart62.setOption(option62);

    const resizeObserver = new ResizeObserver(() => {
        myChart62.resize();
    });

    resizeObserver.observe(echartsRef.value);
});
</script>

<template>
    <div class="AnHuiWindMiddenCenter">
        <div class="title">安徽省风能发电产能图</div>
        <img src="../../../assets/pic/border4.png" alt="" class="BackImg">
        <div class="AnHuiWindMiddenCenter-echarts" ref="echartsRef"></div>
        <div class="right">
            <div class="rightOne">
                <div class="left">产能增率：</div>
                <div class="thing">15.32%</div>
            </div>
            <div class="rightTow">
                <div class="left">投资增率：</div>
                <div class="thing">3.32%</div>
            </div>
            <div class="rightThree">
                <div class="left">储量增率：</div>
                <div class="thing">9.32%</div>
            </div>
            <div class="out">
                <img src="../../../assets/pic/1.png" alt="" class="down">
            </div>

        </div>
    </div>
</template>

<style scoped lang="scss">
.AnHuiWindMiddenCenter {
  width: 100%;
  height: 100%;

  .right {
    position: absolute;
    width: 13vw;
    height: 28vh;
    margin-left: 27.2vw;
    margin-top: -26.3vh;
    color: white;

    .left {
      margin-top: 2vh;
      position: absolute;
      font-weight: bolder;
      margin-left: 1vw;
      font-size: 1.15em;
    }

    .thing {
      margin-top: 1.8vh;
      position: absolute;
      font-weight: bolder;
      margin-left: 7vw;
      width: 6vw;
      text-align: center;
      font-size: 1.4em;
      color: #2bfff1;
      text-shadow: 0 0 1px #1cd7cd, 0 0 2px #1cd7cd, 0 0 3px #1cd7cd;
    }

    .out {
      width: 16vw;
      height: 10vh;
      position: absolute;
      margin-top: 16.5vh;

      .down {
        position: absolute;
        width: 16vw;
        margin-left: -2.5vw;
        height: 5vh;
      }
    }

    .rightOne {
      width: 13vw;
      height: 8vh;
      position: absolute;
      right: 0;
      margin-top: 1vh;
      margin-right: 1vw;
    }

    .rightTow {
      width: 13vw;
      height: 12vh;
      position: absolute;
      right: 0;
      margin-right: 1vw;
      margin-top: 6vh;

    }

    .rightThree {
      width: 13vw;
      height: 12vh;
      position: absolute;
      right: 0;
      margin-right: 1vw;
      margin-top: 11vh;

    }
  }

  .AnHuiWindMiddenCenter-echarts {
    width: 29.5vw;
    height: 33vh;
    margin-left: -1.5vw;
    position: absolute;
    margin-top: -28vh;
    z-index: 399;
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

  .BackImg {
    width: 40vw;
    height: 29vh;
  }
}
</style>