<script setup>
import {ref, onMounted} from 'vue';
import * as echarts from 'echarts';
import {initadd} from "@/api";

const echartsRef = ref(null)
let myChart8 = null;
let option8 = null;

onMounted(async () => {
    var colorList = [
        new echarts.graphic.LinearGradient(0, 0, 0, 1, [
            {offset: 0, color: '#bc4e9c'},
            {offset: 1, color: '#f80759'}
        ]),
        new echarts.graphic.LinearGradient(0, 0, 0, 1, [
            {offset: 0, color: '#2980B9'},
            {offset: 1, color: '#6DD5FA'}
        ]),
        new echarts.graphic.LinearGradient(0, 0, 0, 1, [
            {offset: 0, color: '#00C9FF'},
            {offset: 1, color: '#92FE9D'}
        ]),
        // 其他渐变色定义...
    ];
    myChart8 = echarts.init(echartsRef.value);
    try {
        const data = await initadd(); // 使用initlandlist函数获取数据
        const datas = data.data.data;
        console.log(datas)
        // 处理从initlandlist获取的数据，例如更新echarts图表
        if (data) {
            option8 = {
                color: colorList,
                tooltip: {
                    trigger: 'axis',
                },

                legend: {
                    textStyle: {
                        color: 'white'
                    },
                    top: '3%',
                    data: ['产量', '存量', '产量增长率'],
                    itemWidth: 20, // 标签宽度为20px
                    itemHeight: 10, // 标签高度为10px
                },
                xAxis: [
                    {
                        type: 'category',
                        data: data.data['name'],
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
                        name: '标准煤 / 千万吨',
                        // min: 0,
                        // max: 50000,
                        nameTextStyle: {
                            padding: [0, -10, 0, 0]
                        },
                        interval: 100,
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
                        // max: 5,
                        nameTextStyle: {
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
                                return value + ' 千万吨';
                            }
                        },
                        data: datas['产量']
                    },
                    {
                        name: '存量',
                        type: 'bar',
                        tooltip: {
                            valueFormatter: function (value) {
                                return value + ' 千万吨';
                            }
                        },
                        data: datas['存量']
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
                        data: datas['产量增长率']
                    }
                ]
            };
            // console.log(a[1][1]
        } else {
            console.error('Failed to fetch data from initlandlist');
        }
    } catch (error) {
        console.error('Error fetching data:', error);
    }


    option8 && myChart8.setOption(option8);
    const resizeObserver = new ResizeObserver(() => {
        myChart8.resize();
    });

    resizeObserver.observe(echartsRef.value);
});
</script>

<template>
    <div className="MainChinaLeft">
        <img class="BackImg" src="../../assets/pic/border3.png" alt="">
        <Button class="GotoGrounds">全国能源产量及库存</Button>
        <div id="MainChinaLeft-echarts" ref="echartsRef"></div>
    </div>
</template>

<style scoped lang="scss">
.MainChinaLeft {
  width: 100vw;
  height: 100vh;
  color: white;

  .GotoGrounds {
    position: absolute;
    margin-top: -38.5vh;
    width: 19vw;
    margin-left: 0.6vw;
    border: none;
    background: none;
    color: white;
    font-weight: bolder;
    //cursor: pointer;
    font-size: 1.2vw;
    z-index: 999;
  }

  //.GotoGrounds:hover {
  //  font-size: 1.3vw;
  //  margin-top: -32.3vh;
  //}
  //
  //.GotoGrounds:active {
  //  margin-top: -32vh;
  //  font-size: 1.2vw;
  //}

  #MainChinaLeft-echarts {
    width: 19vw;
    height: 39vh;
    margin-left: 0.2vw;
    position: absolute;
    margin-top: -36vh;
  }

  .BackImg {
    width: 20.2vw;
    height: 40vh;
    margin-top: -20vh;
  }

}
</style>
