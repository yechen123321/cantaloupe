<script setup>
import {onMounted, ref} from "vue";
import * as echarts from "echarts";

const echartsRef = ref(null);
let myChart53 = null;
let option53 = null;

onMounted(() => {
    myChart53 = echarts.init(echartsRef.value, 'dark');
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
            {offset: 0, color: '#4AC29A'},
            {offset: 1, color: '#BDFFF3'}
        ]),
        new echarts.graphic.LinearGradient(0, 0, 0, 1, [
            {offset: 1, color: '#C6FFDD'},
            {offset: 0, color: '#FBD786'},
        ]),

        // 其他渐变色定义...
    ];
    // Your echarts option setup here...
    // (Your existing option setup code)
    option53 = {
        backgroundColor: "rgba(128,128,128,0)",
        color: colorList,
        tooltip: {
            trigger: 'axis',
        },
        legend: {
            textStyle: {
                color: 'white'
            },
            top: '12%',
            left: 'center',
            data: ['储量', '产量', '产量增长率', '储量增长率'],
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
                max: 200,
                nameTextStyle: {
                    color: 'white',
                    padding: [0, 35, 0, 0]
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
                max: 30,
                nameTextStyle: {
                    color: 'white',
                    padding: [0, -25, 0, 0]
                },
                interval: 7.5,
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
                name: '储量',
                type: 'bar',
                tooltip: {
                    valueFormatter: function (value) {
                        return value + ' 万千瓦';
                    }
                },
                itemStyle: {
                    barBorderRadius: [10, 10, 0, 0] // 设置柱子上方为圆角，数组中的四个值分别代表左上、右上、右下、左下的圆角半径
                },
                data: [
                    176.7, 135.6, 162.2, 132.6, 162.2, 132.6, 176.7,
                ]
            },
            {
                name: '产量',
                type: 'bar',
                tooltip: {
                    valueFormatter: function (value) {
                        return value + ' 万千瓦';
                    }
                },
                itemStyle: {
                    barBorderRadius: [10, 10, 0, 0] // 设置柱子上方为圆角，数组中的四个值分别代表左上、右上、右下、左下的圆角半径
                },
                data: [
                    70.7, 75.6, 82.2, 48.7, 82.2, 48.7, 70.7,
                ]
            },
            {
                name: '产量增长率',
                type: 'line',
                yAxisIndex: 1,
                tooltip: {
                    valueFormatter: function (value) {
                        return value + ' %';
                    }
                },
                data: [20.3, 23.4, 23.0, 16.5, 23.0, 16.5, 20.3,]
            },
            {
                name: '储量增长率',
                type: 'line',
                yAxisIndex: 1,
                tooltip: {
                    valueFormatter: function (value) {
                        return value + ' %';
                    }
                },
                data: [12.3, 13.4, 14.0, 6.5, 3.0, 10.5, 12.3,]
            }
        ]
    };
    option53 && myChart53.setOption(option53);

    const resizeObserver = new ResizeObserver(() => {
        myChart53.resize();
    });

    resizeObserver.observe(echartsRef.value);
});
</script>
<template>
    <div className="AnHuiWaterMiddenDown">
        <div className="title">安徽省水利发电储能图</div>
        <img src="../../../assets/pic/border4.png" alt="" className="BackImg">
        <div className="AnHuiWaterMiddenDown-echarts" ref="echartsRef"></div>
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
.AnHuiWaterMiddenDown {
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

  .title {
    position: absolute;
    color: white;
    width: 40vw;
    font-weight: bolder;
    font-size: 1.15em;
    text-align: center;
    margin-top: 1vh;
    //background: red;
  }

  .AnHuiWaterMiddenDown-echarts {
    width: 29.2vw;
    height: 33vh;
    margin-left: -1.5vw;
    position: absolute;
    margin-top: -28.5vh;
    z-index: 555;
  }

  .BackImg {
    width: 40vw;
    height: 29vh;
  }
}
</style>