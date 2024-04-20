<script setup>
import {ref, onMounted} from 'vue'
import * as echarts from "echarts";

const echartsRef2 = ref(null);
let myChart88 = null;
let option88 = null;

onMounted(() => {
    myChart88 = echarts.init(echartsRef2.value, 'dark');
    // Your echarts option setup here...
    // (Your existing option setup code)
    var colorList = [

        new echarts.graphic.LinearGradient(0, 0, 0, 1, [
            {offset: 0, color: '#fab300'},
            {offset: 1, color: '#ff0000'},
        ]),
        new echarts.graphic.LinearGradient(0, 0, 0, 1, [
            {offset: 0, color: '#ef98d0'},
            {offset: 1, color: '#fd0792'},
        ]),
    ];
    option88 = {
        color: colorList,
        backgroundColor: 'rgba(1,1,1,0)',
        tooltip: {
            trigger: 'axis',
            extraCssText: 'width: 15vw; height: 15vh;', // 设置tooltip框的宽度和高度，调整框的大小
            formatter: function (params) {
                let tooltipContent = '';
                let mineName = params[0].name;
                tooltipContent += '<span style="font-weight: bold;margin-right: 1vw; margin-top: -500px;">' + mineName + '</span>' + '单位/万亿吨, 亿元<br>' + '<br>'; // 设置矿地名字的样式为加粗并向上移动5px
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
            left: '17%',
            top: '12%',
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
                data: ['2月', '4月', '6月', '8月', '10月']
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
                name: '百分比',
                max: 100,
                min: 30,
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
                name: '标准煤',
                nameTextStyle: {
                    color: 'white',
                    padding: [0, 20, 0, 0]
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
                    35.6, 62.2, 32.6, 20.0, 46.4,
                ],
                itemStyle: {
                    barBorderRadius: [10, 10, 0, 0] // 设置柱子上方为圆角，数组中的四个值分别代表左上、右上、右下、左下的圆角半径
                },
            },
            {
                name: '能源获取',
                type: 'bar',
                yAxisIndex: 0,
                data: [
                    175.6, 182.2, 148.7, 138.8, 146.0
                ],
                itemStyle: {
                    barBorderRadius: [10, 10, 0, 0] // 设置柱子上方为圆角，数组中的四个值分别代表左上、右上、右下、左下的圆角半径
                },
            },
            {
                name: '开发效率',
                type: 'line',
                yAxisIndex: 1,
                data: [83.4, 82.0, 89.5, 91.0, 83.2]
            },
        ]
    };


    option88 && myChart88.setOption(option88);

    const resizeObserver = new ResizeObserver(() => {
        myChart88.resize();
    });

    resizeObserver.observe(echartsRef2.value);
});

</script>
<template>
    <div class="ThermalPowerRightDown">
        <div class="title">能源开发效率</div>
        <div class="ThermalPowerRightDown-echarts" ref="echartsRef2"></div>
        <div class="title2">室内环境数据</div>
        <div class="main">
            <ul>
                <li>
                    <img src="../../../assets/大气温度.png" alt="">
                    <div class="number">26.4</div>
                    <div class="up">(℃)</div>
                    <div class="what">室内温度</div>
                </li>
                <li>
                    <img src="../../../assets/露点温度.png" alt="">
                    <div class="number">11.7</div>
                    <div class="up">(%RH)</div>
                    <div class="what">空气湿度</div>
                </li>
                <li>
                    <img src="../../../assets/空气质量置灰.png" alt="">
                    <div class="number">21.1</div>
                    <div class="up">(AQI)</div>
                    <div class="what">空气质量</div>
                </li>
                <li>
                    <img src="../../../assets/空气质一般.png" alt="">
                    <div class="number">3.2</div>
                    <div class="up">(M/s)</div>
                    <div class="what">空气流速</div>
                </li>
            </ul>
        </div>
        <img src="../../../assets/pic/border3.png" alt="" class="BackImg">
    </div>
</template>

<style scoped lang="scss">
.ThermalPowerRightDown {
  width: 100%;
  height: 100%;

  .main {
    width: 24vw;
    margin-left: 1vw;
    height: 22vh;
    position: absolute;
    margin-top: 33vh;

    ul {
      position: absolute;
      width: 30vw;
      height: 20vh;
      margin-top: -2vh;
      margin-left: -4.4vw;

      li {
        color: white;
        font-weight: bolder;
        font-size: 1em;
        width: 10vw;
        height: 8vh;
        float: left;
        margin-top: 3vh;
        margin-left: 2vw;
        list-style: none;

        img {
          width: 4vw;
          position: absolute;
        }

        .number {
          position: absolute;
          margin-left: 4.4vw;
          margin-top: 3.5vh;
          font-size: 1.6em;
          width: 4vw;
          text-align: center;
        }

        .up {
          margin-left: 8.5vw;
          margin-top: 4.7vh;
          position: absolute;
          color: #0ca6e0;
        }

        .what {
          position: absolute;
          margin-left: 5vw;
          color: #3de9fa;
          margin-top: 0.5vh;
        }
      }
    }
  }

  .ThermalPowerRightDown-echarts {
    position: absolute;
    width: 26vw;
    height: 30vh;
    margin-top: 3.2vh;
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
    font-size: 1.15em;
    margin-left: 2vw;
    width: 21.7vw;
    text-align: center;
    margin-top: 29.3vh;
  }

  .title {
    color: white;
    position: absolute;
    font-weight: bolder;
    font-size: 1.15em;
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