<script setup>

import router from "@/router";
import {ref, onMounted} from "vue";
import * as echarts from "echarts";

const echartsRef = ref(null);
let myChart86 = null;
let option86 = null;
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

onMounted(() => {
    myChart86 = echarts.init(echartsRef.value, 'dark');
    // Your echarts option setup here...
    // (Your existing option setup code)
    var colorList = [
        new echarts.graphic.LinearGradient(0, 0, 0, 1, [
            {offset: 0, color: '#396afc'},
            {offset: 1, color: '#2948ff'}
        ]),
        new echarts.graphic.LinearGradient(0, 0, 0, 1, [
            {offset: 0, color: '#bc4e9c'},
            {offset: 1, color: '#f80759'}
        ]),
        new echarts.graphic.LinearGradient(0, 0, 0, 1, [
            {offset: 0, color: '#00C9FF'},
            {offset: 1, color: '#92FE9D'}
        ]),
        // 其他渐变色定义...
    ];
    option86 = {
        backgroundColor: 'rgba(1,1,1,0)',
        color: colorList,
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
            top: '3%',
            data: ['能源消耗', '全国GDP', '全国能耗降低率'],
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
                name: '降低率',
                nameLocation: 'end', // 将名称显示在轴线末尾，即向右移动
                position: 'right',
                nameTextStyle: {
                    color: 'white',
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
                name: '标准煤 / 万亿吨',
                position: 'left',
                alignTicks: true,
                nameTextStyle: {
                    color: 'white',
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
        ],
        series: [
            {
                name: '能源消耗',
                type: 'bar',
                yAxisIndex: 2,
                data: [
                    135.6, 162.2, 32.6, 20.0, 6.4,
                ]
            },
            {
                name: '全国GDP',
                type: 'bar',
                yAxisIndex: 0,
                data: [
                    175.6, 182.2, 48.7, 18.8, 6.0
                ]
            },
            {
                name: '全国能耗降低率',
                type: 'line',
                yAxisIndex: 1,
                data: [3.4, 2.0, 1.5, 1.0, 3.2]
            },
        ]
    };

    option86 && myChart86.setOption(option86);

    const resizeObserver = new ResizeObserver(() => {
        myChart86.resize();
    });

    resizeObserver.observe(echartsRef.value);
});

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
    font-size: 1.4em;
    position: absolute;
    width: 42.5vw;
    text-align: center;
    margin-top: 0.8vh;
  }

  .DataAnalysisMiddenDown-echarts {
    width: 30vw;
    height: 28vh;
    margin-top: 4vh;
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