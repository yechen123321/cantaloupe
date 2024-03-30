<script setup>
import {onMounted, ref} from 'vue';
import * as echarts from "echarts";

const echartsRef = ref(null);
let myChart83 = null;
let option83 = null;

onMounted(() => {
    myChart83 = echarts.init(echartsRef.value, 'dark');
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
    option83 = {
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
                name: '产量',
                type: 'bar',
                tooltip: {
                    valueFormatter: function (value) {
                        return value + ' 万千瓦';
                    }
                },
                data: [
                    176.7, 135.6, 162.2, 132.6, 162.2, 132.6, 176.7,
                ]
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
                    170.7, 175.6, 182.2, 148.7, 182.2, 148.7, 170.7,
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
        ]
    };
    option83 && myChart83.setOption(option83);

    const resizeObserver = new ResizeObserver(() => {
        myChart83.resize();
    });

    resizeObserver.observe(echartsRef.value);
});

</script>
<template>
    <div class="DataAnalysisLeftTop">
        <div class="title">安徽能源总产能</div>
        <div class="DataAnalysisLeftTop-echarts" ref="echartsRef"></div>
        <img src="../../../assets/pic/midden.png" alt="" class="BackImg">
    </div>

</template>

<style scoped lang="scss">
.DataAnalysisLeftTop {
  width: 100%;
  height: 100%;

  .DataAnalysisLeftTop-echarts {
    width: 29.3vw;
    height: 31vh;
    margin-top: 5.2vh;
    position: absolute;
  }

  .title {
    position: absolute;
    color: white;
    font-size: 1.4em;
    font-weight: bolder;
    margin-top: 4vh;
    margin-left: 3vw;
  }

  .BackImg {
    width: 30vw;
    height: 34vh;
  }
}
</style>