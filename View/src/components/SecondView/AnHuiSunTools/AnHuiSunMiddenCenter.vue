<script setup>
import {onMounted, ref} from "vue";
import * as echarts from "echarts";
import AnHuiSunMiddenCenterThing from "@/components/SecondView/AnHuiSunTools/AnHuiSunMiddenCenterThing.vue";

const echartsRef = ref(null);
let myChart43 = null;
let option43 = null;

onMounted(() => {
    myChart43 = echarts.init(echartsRef.value, 'dark');
    var colorList = [
        new echarts.graphic.LinearGradient(0, 0, 0, 1, [
            {offset: 0, color: '#396afc'},
            {offset: 1, color: '#2948ff'}
        ]),
        new echarts.graphic.LinearGradient(0, 0, 0, 1, [
            {offset: 0, color: '#bc4e9c'},
            {offset: 1, color: '#f80759'}
        ]),

        // 其他渐变色定义...
    ];
    // Your echarts option setup here...
    // (Your existing option setup code)
    option43 = {
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
                data: ['2019', '2020', '2021', '2022', '2023'],
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
                    color:'white',
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
                    color:'white',
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
                        return value + ' ml';
                    }
                },
                data: [
                    76.7, 135.6, 162.2, 32.6, 162.2,
                ]
            },
            {
                name: '增长量',
                type: 'bar',
                tooltip: {
                    valueFormatter: function (value) {
                        return value + ' ml';
                    }
                },
                data: [
                    70.7, 175.6, 182.2, 48.7, 182.2,
                ]
            },
            {
                name: '增长率',
                type: 'line',
                yAxisIndex: 1,
                tooltip: {
                    valueFormatter: function (value) {
                        return value + ' °C';
                    }
                },
                data: [20.3, 23.4, 23.0, 16.5, 23.0,]
            }
        ]
    };
    option43 && myChart43.setOption(option43);

    const resizeObserver = new ResizeObserver(() => {
        myChart43.resize();
    });

    resizeObserver.observe(echartsRef.value);
});
</script>
<template>
    <div class="AnHuiSunMiddenCenter">
        <div class="title">安徽省光伏发电装机容量</div>
        <img src="../../../assets/pic/border4.png" alt="" class="BackImg">
        <div class="AnHuiSunMiddenCenter-echarts" ref="echartsRef"></div>
        <AnHuiSunMiddenCenterThing id="AnHuiSunMiddenCenterThing"></AnHuiSunMiddenCenterThing>
    </div>
</template>

<style scoped lang="scss">
.AnHuiSunMiddenCenter {
  width: 100%;
  height: 100%;

  #AnHuiSunMiddenCenterThing {
    width: 20vw;
    height: 20vh;
    //background: red;
    position: absolute;
    margin-left: 25.5vw;
    margin-top: -24vh;
    border-left: 2px solid #0d87f6;
  }

  .title {
    position: absolute;
    color: white;
    width: 40vw;
    font-weight: bolder;
    font-size: 1.26em;
    text-align: center;
    margin-top: 1vh;
    //background: red;
  }

  .AnHuiSunMiddenCenter-echarts {
    width: 27vw;
    height: 33vh;
    position: absolute;
    margin-top: -28.5vh;
    margin-left: -1vw;
  }

  .BackImg {
    width: 40vw;
    height: 29vh;
  }
}
</style>