<script setup>
import {onMounted, ref} from 'vue';
import router from "@/router";
import * as echarts from "echarts";

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
let myChart70 = null;
let option70 = null;

onMounted(() => {
    myChart70 = echarts.init(echartsRef.value, 'dark');
    // Your echarts option setup here...
    // (Your existing option setup code)
    var colorList = [
        // new echarts.graphic.LinearGradient(0, 0, 0, 1, [
        //     {offset: 0, color: '#bc4e9c'},
        //     {offset: 1, color: '#f80759'}
        // ]),
        new echarts.graphic.LinearGradient(0, 0, 0, 1, [
            {offset: 0, color: '#396afc'},
            {offset: 1, color: '#2948ff'}
        ]),
        new echarts.graphic.LinearGradient(0, 0, 0, 1, [
            {offset: 0, color: '#00C9FF'},
            {offset: 1, color: '#92FE9D'}
        ]),
        // 其他渐变色定义...
    ];
    option70 = {
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
            left: 'center',
            data: ['储量', '供量', '储量增长率', '供量增长率'],
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
                    padding: [0, 25, 0, 0]
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
                name: '储量',
                type: 'bar',
                tooltip: {
                    valueFormatter: function (value) {
                        return value + ' ml';
                    }
                },
                data: [
                    76.7, 135.6, 162.2, 32.6, 162.2, 32.6, 76.7,
                ]
            },
            {
                name: '供量',
                type: 'bar',
                tooltip: {
                    valueFormatter: function (value) {
                        return value + ' ml';
                    }
                },
                data: [
                    70.7, 175.6, 182.2, 48.7, 182.2, 48.7, 70.7,
                ]
            },
            {
                name: '储量增长率',
                type: 'line',
                yAxisIndex: 1,
                tooltip: {
                    valueFormatter: function (value) {
                        return value + ' °C';
                    }
                },
                data: [20.3, 23.4, 23.0, 16.5, 23.0, 16.5, 20.3,]
            },
            {
                name: '供量增长率',
                type: 'line',
                yAxisIndex: 1,
                tooltip: {
                    valueFormatter: function (value) {
                        return value + ' °C';
                    }
                },
                data: [16.5, 23.0, 20.3, 23.4, 23.0, 20.3, 16.5,]
            }
        ]
    };
    option70 && myChart70.setOption(option70);

    const resizeObserver = new ResizeObserver(() => {
        myChart70.resize();
    });

    resizeObserver.observe(echartsRef.value);
});

</script>

<template>
    <div class="AnHuiLimitTop">
        <div class="title">安徽省有限资源储能图</div>
        <img src="../../../assets/pic/border4.png" alt="" class="BackImg">
        <div class="AnHuiLimitTop-echarts" ref="echartsRef"></div>
        <div class="MySelect">
            <select class="SelectBox">
                <option class="options" v-for="(option, index) in options" :key="index">
                    {{ option.where }}
                </option>
            </select>
            <button class="SelectGo" @click="handleRouteChange">切换</button>
        </div>
    </div>
</template>

<style scoped lang="scss">
.AnHuiLimitTop {
  width: 100%;
  height: 100%;

  .AnHuiLimitTop-echarts {
    width: 32vw;
    height: 32vh;
    margin-top: -27vh;
    margin-left: -1.5vw;
    position: absolute;
  }

  .MySelect {
    width: 12vw;
    height: 18vh;
    //background: red;
    margin-left: 30vw;
    margin-top: -22vh;
    position: absolute;
    //margin-top: 6vh;
    z-index: 222;
    border-left: 2px solid #0d87f6;
    //margin-right: -1vw;

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
    //background: red;
    text-align: center;
    font-size: 1.4em;
    margin-left: 1.2vw;
    margin-top: 1vh;
    font-weight: bolder;
  }

  .BackImg {
    width: 42.5vw;
    height: 28vh;
    //position: absolute;
  }
}
</style>