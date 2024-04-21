<script setup>
import * as echarts from "echarts";
import {ref, onMounted} from 'vue'
import router from "@/router";

const handleRouteChange = () => {
    // 在这里添加您的路由切换逻辑，下面是一个示例，实际根据您的路由配置进行修改
    router.push('/anhuilimit'); // 替换'/new-route'为您要跳转的路由路径
};
const options = ref([
    {where: '安徽', value: 1},
    {where: '北京', value: 2},
    {where: '浙江', value: 3},
    {where: '重庆', value: 4},
    {where: '西藏', value: 5},
    {where: '四川', value: 6},
    {where: '山东', value: 7},
    {where: '上海', value: 8},
    {where: '广东', value: 9},
    {where: '广西', value: 10},
]);


const echartsRef = ref(null);
let myChart72 = null;
let option72 = null;

onMounted(() => {
    myChart72 = echarts.init(echartsRef.value);
    var colorList = [
        new echarts.graphic.LinearGradient(0, 0, 0, 1, [
            {offset: 0, color: '#dc90ea'},
            {offset: 1, color: '#5907fd'},
        ]),
        new echarts.graphic.LinearGradient(0, 0, 0, 1, [
            {offset: 0, color: '#fab300'},
            {offset: 1, color: '#ff0000'},
        ]),
        new echarts.graphic.LinearGradient(0, 0, 0, 1, [
            {offset: 0, color: '#ef98d0'},
            {offset: 1, color: '#fd0792'},
        ]),
        new echarts.graphic.LinearGradient(0, 0, 0, 1, [
            {offset: 0, color: '#074dfd'},
            {offset: 1, color: '#5907fd'},
        ]),
    ];
    option72 = {
        color: colorList,
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
            bottom: '15%', // 调整图表下边距
            containLabel: true,
        },
        legend: {
            itemWidth: 20, // 标签宽度为10px
            itemHeight: 10, // 标签高度为10px
            left: '13%',
            top: '13%',
            data: ['开发耗费', '获取能量', '百分比'],
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
                data: ['2019', '2020', '2021', '2022', '2023']
            }
        ],
        yAxis: [
            {
                type: 'value',
                name: '万亿元',
                position: 'right',
                alignTicks: true,
                nameTextStyle: {
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
                name: '百分比',
                max: 100,
                min: 30,
                nameLocation: 'end', // 将名称显示在轴线末尾，即向右移动
                position: 'right',
                nameTextStyle: {
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
                name: '标准煤',
                nameTextStyle: {
                    padding: [0, 36, 0, 0],
                },
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
                name: '开发耗费',
                type: 'bar',
                yAxisIndex: 2,
                data: [
                    35.6, 32.2, 32.6, 20.0, 36.4,
                ],
                itemStyle: {
                    barBorderRadius: [10, 10, 0, 0] // 设置柱子上方为圆角，数组中的四个值分别代表左上、右上、右下、左下的圆角半径
                }
            },
            {
                name: '获取能量',
                type: 'bar',
                yAxisIndex: 0,
                data: [
                    175.6, 182.2, 148.7, 138.8, 146.0
                ],
                itemStyle: {
                    barBorderRadius: [10, 10, 0, 0] // 设置柱子上方为圆角，数组中的四个值分别代表左上、右上、右下、左下的圆角半径
                }
            },
            {
                name: '百分比',
                type: 'line',
                yAxisIndex: 1,
                data: [83.4, 94.0, 91.5, 86.0, 83.2]
            },
        ]
    };

    option72 && myChart72.setOption(option72);

    const resizeObserver = new ResizeObserver(() => {
        myChart72.resize();
    });

    resizeObserver.observe(echartsRef.value);
});

</script>

<template>
    <div class="AnHuiLimitTop">
        <div class="title">安徽省有限能源开发</div>
        <img src="../../../assets/pic/border4.png" alt="" class="BackImg">
        <div class="MySelect">
            <select class="SelectBox">
                <option class="options" v-for="(option, index) in options" :key="index">
                    {{ option.where }}
                </option>
            </select>
            <button class="SelectGo" @click="handleRouteChange">切换</button>
        </div>
        <div class="AnHuiLimitRight-echarts" ref="echartsRef"></div>
    </div>
</template>

<style scoped lang="scss">
.AnHuiLimitTop {
  width: 100%;
  height: 100%;

  .AnHuiLimitRight-echarts {
    width: 30vw;
    height: 30vh;
    position: absolute;
    margin-top: -27vh;
  }

  .MySelect {
    width: 12vw;
    height: 18vh;
    margin-left: 30vw;
    margin-top: -22vh;
    position: absolute;
    z-index: 222;
    border-left: 2px solid #0d87f6;

    .SelectBox {
      width: 7vw;
      margin-left: 2.5vw;
      margin-top: 2vh;
      height: 4vh;
      cursor: pointer;
      overflow: hidden;
      font-size: 1vw;
      background: #4d70cd;
      color: white;
      border: none;
      text-align: center;
      border-radius: 6px;

    }

    .SelectGo {
      width: 7vw;
      height: 4vh;
      right: 0;
      margin-top: 9vh;
      margin-right: 2.5vw;
      position: absolute;
      cursor: pointer;
      font-size: 1vw;
      font-weight: bolder;
      color: white;
      border: none;
      border-radius: 6px;
      background: #0d87f6;
      z-index: 222;
    }

    .SelectGo:hover {
      width: 7.5vw;
      height: 5vh;
      margin-top: 8.5vh;
      margin-right: 2.15vw;
      font-size: 1.4vw;
    }

    .SelectGo:active {
      width: 7vw;
      height: 4vh;
      margin-top: 9vh;
      margin-right: 2.5vw;
      font-size: 1vw;
    }
  }

  .title {
    position: absolute;
    color: white;
    width: 40vw;
    text-align: center;
    font-size: 1.3em;
    margin-left: 1.2vw;
    margin-top: 1vh;
    font-weight: bolder;
  }

  .BackImg {
    width: 42.5vw;
    height: 28vh;
  }
}
</style>