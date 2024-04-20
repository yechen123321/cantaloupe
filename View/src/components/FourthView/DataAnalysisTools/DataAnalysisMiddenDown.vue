<script setup>

import router from "@/router";
import {ref, onMounted} from "vue";
import * as echarts from "echarts";

const echartsRef = ref(null);
let myChart83 = null;
let option83 = null;

onMounted(() => {
    myChart83 = echarts.init(echartsRef.value, 'dark');
    // Your echarts option setup here...
    // (Your existing option setup code)
    var colorList = [
        new echarts.graphic.LinearGradient(0, 0, 0, 1, [
            {offset: 0, color: '#56CCF2'},
            {offset: 1, color: '#2948ff'}
        ]),
        new echarts.graphic.LinearGradient(0, 0, 0, 1, [

            {offset: 0, color: '#fc8cd9'},
            {offset: 1, color: '#f80759'}
        ]),
        new echarts.graphic.LinearGradient(0, 0, 0, 1, [
            {offset: 0, color: '#00C9FF'},
            {offset: 1, color: '#92FE9D'}
        ]),
        // 其他渐变色定义...
    ];
    option83 = {
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
            data: ['产量', '产量增量', '产量增长率',],
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
                max: 450,
                nameTextStyle: {
                    color: 'white',
                    padding: [0, 25, 0, 0]
                },
                interval: 90,
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
                name: '产量',
                type: 'bar',
                tooltip: {
                    valueFormatter: function (value) {
                        return value + ' 万千瓦';
                    }
                },
                data: [
                    176.7, 215.6, 252.2, 302.6, 333.2, 382.6, 406.7,
                ],
                itemStyle: {
                    barBorderRadius: [10, 10, 0, 0] // 设置柱子上方为圆角，数组中的四个值分别代表左上、右上、右下、左下的圆角半径
                }
            },
            {
                name: '产量增量',
                type: 'bar',
                tooltip: {
                    valueFormatter: function (value) {
                        return value + ' 万千瓦';
                    }
                },
                data: [
                    30.7, 45.6, 32.2, 48.7, 32.2, 48.7, 20.7,
                ],
                itemStyle: {
                    barBorderRadius: [10, 10, 0, 0] // 设置柱子上方为圆角，数组中的四个值分别代表左上、右上、右下、左下的圆角半径
                }
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
        ]
    };
    option83 && myChart83.setOption(option83);

    const resizeObserver = new ResizeObserver(() => {
        myChart83.resize();
    });

    resizeObserver.observe(echartsRef.value);
});


const handleRouteChange = () => {
    // 在这里添加您的路由切换逻辑，下面是一个示例，实际根据您的路由配置进行修改
    router.push('/dataanalysis'); // 替换'/new-route'为您要跳转的路由路径
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

</script>

<template>
    <div class="DataAnalysisMiddenTop">
        <div class="title">安徽省能源消耗水平</div>
        <div class="DataAnalysisMiddenDown-echarts" ref="echartsRef"></div>
        <div class="MySelect">
            <select style="font-weight: bolder" class="SelectBox">
                <option style="font-weight: bolder" class="options" v-for="(option, index) in options" :key="index">
                    {{ option.where }}
                </option>
            </select>
            <button class="SelectGo" @click="handleRouteChange">切换</button>
        </div>
        <img src="../../../assets/pic/border4.png" alt="" class="BackImg">
    </div>
</template>

<style scoped lang="scss">
.DataAnalysisMiddenTop {
  width: 100%;
  height: 100%;

  .title {
    color: white;
    font-weight: bolder;
    font-size: 1.25em;
    position: absolute;
    width: 42.5vw;
    text-align: center;
    margin-top: 1vh;
  }

  .DataAnalysisMiddenDown-echarts {
    width: 33vw;
    height: 32vh;
    margin-left: -2vw;
    margin-top: 1.2vh;
    position: absolute;
  }

  .MySelect {
    width: 12vw;
    height: 18vh;
    margin-left: 30vw;
    margin-top: 7vh;
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

  .BackImg {
    width: 42.5vw;
    height: 28vh;
  }
}
</style>