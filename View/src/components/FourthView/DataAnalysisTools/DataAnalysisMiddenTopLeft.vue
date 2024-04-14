<script setup>
import {ref, onMounted} from "vue";
import * as echarts from "echarts";

const echartsRef = ref(null);
let myChart87 = null;
let option87 = null;
onMounted(() => {
    myChart87 = echarts.init(echartsRef.value, 'dark');
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
    option87 = {
        backgroundColor: "rgba(128,128,128,0)",
        color: colorList,
        tooltip: {
            trigger: 'axis',
        },
        legend: {

            textStyle: {
                color: 'white'
            },
            top: '15%',
            left: 'center',
            data: ['2021', '2022', '2023',],
            itemWidth: 20, // 标签宽度为20px
            itemHeight: 10, // 标签高度为10px
        },
        xAxis: [
            {
                type: 'category',
                data: ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'],
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
                name: '万吨',
                min: 0,
                // max: 250,
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
        ],
        series: [
            {
                name: '2021',
                type: 'line',
                tooltip: {
                    valueFormatter: function (value) {
                        return value + ' 万吨';
                    }
                },
                areaStyle: {
                    normal: {
                        color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
                            offset: 0,
                            color: 'rgba(57,106,252,0.5)' // 渐变色起始值
                        }, {
                            offset: 0.5,
                            color: 'rgba(41,72,255,0.1)' // 渐变色起始值
                        },
                        ])
                    }
                },
                data: [
                    176.7, 235.6, 262.2, 132.6, 262.2, 132.6, 176.7, 235.6, 262.2, 132.6, 176.7, 235.6,
                ]
            },
            {
                name: '2022',
                type: 'line',
                tooltip: {
                    valueFormatter: function (value) {
                        return value + ' 万吨';
                    }
                },
                areaStyle: {
                    normal: {
                        color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
                            offset: 0,
                            color: 'rgba(188,78,156,0.5)' // 渐变色起始值
                        }, {
                            offset: 0.5,
                            color: 'rgba(248,7,89,0.1)' // 渐变色起始值
                        },
                        ])
                    }
                },
                data: [
                    135.6, 162.2, 76.7, 135.6, 162.2, 32.6, 162.2, 32.6, 76.7, 135.6, 162.2, 162.2,
                ]
            },
            {
                name: '2023',
                type: 'line',
                tooltip: {
                    valueFormatter: function (value) {
                        return value + ' %';
                    }
                },
                areaStyle: {
                    normal: {
                        color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
                            offset: 0,
                            color: 'rgba(0,201,255,0.5)' // 渐变色起始值
                        }, {
                            offset: 0.5,
                            color: 'rgba(146,254,157,0.1)' // 渐变色起始值
                        },
                        ])
                    }
                },
                data: [
                    210.3, 123.4, 223.0, 126.5, 123.0, 136.5, 220.3, 120.3, 223.4, 123.0, 223.0, 126.5,
                ]
            },
        ]
    };


    option87 && myChart87.setOption(option87);

    const resizeObserver = new ResizeObserver(() => {
        myChart87.resize();
    });

    resizeObserver.observe(echartsRef.value);
});

</script>

<template>
    <div class="DataAnalysisMiddenTopLeft">
        <div class="TitleSecond">安徽省碳排放量统计</div>
        <div class="DataAnalysisMiddenTopLeft-down" ref="echartsRef"></div>
    </div>
</template>

<style scoped>
.DataAnalysisMiddenTopLeft {
    width: 100%;
    height: 100%;

    .TitleSecond {
        color: white;
        position: absolute;
        font-weight: bolder;
        margin-top: -5.5vh;
        width: 26vw;
        margin-left: -4vw;
        text-align: center;
        font-size: 1.3em;
    }

    .DataAnalysisMiddenTopLeft-down {
        width: 31vw;
        height: 29vh;
        position: absolute;
        margin-top: -4vh;
        margin-left: -2vw;
        z-index: 333;
    }
}
</style>