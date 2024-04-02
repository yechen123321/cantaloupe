<script setup>
import {ref, onMounted} from 'vue';
import * as echarts from 'echarts';
import {initKlist2} from "@/api";

const echartsRef = ref(null);
let myChart5 = null;
let option5 = null;

onMounted(async () => {
    myChart5 = echarts.init(echartsRef.value);
    var colorList = [
        new echarts.graphic.LinearGradient(0, 0, 0, 1, [
            {offset: 0, color: '#396afc'},
            {offset: 1, color: '#2948ff'}
        ]),
        new echarts.graphic.LinearGradient(0, 0, 0, 1, [
            {offset: 0, color: '#00C9FF'},
            {offset: 1, color: '#92FE9D'}
        ]),



        new echarts.graphic.LinearGradient(0, 0, 0, 1, [
            {offset: 0, color: '#bc4e9c'},
            {offset: 1, color: '#f80759'}
        ]),

        new echarts.graphic.LinearGradient(0, 0, 0, 1, [
            {offset: 0, color: '#FBD786'},
            {offset: 1, color: '#C6FFDD'}
        ]),
        new echarts.graphic.LinearGradient(0, 0, 0, 1, [
            {offset: 0, color: '#8E2DE2'},
            {offset: 1, color: '#4A00E0'}
        ]),
        // 其他渐变色定义...
        new echarts.graphic.LinearGradient(0, 0, 0, 1, [
            {offset: 0, color: '#ee9ca7'},
            {offset: 1, color: '#ffdde1'}
        ]),
    ];
    // Your echarts option setup here...
    // (Your existing option setup code)
    try {
        const data = await initKlist2(); // 使用initlandlist函数获取数据
        console.log(data);

        // 处理从initlandlist获取的数据，例如更新echarts图表
        if (data) {
            option5 = {
                color:colorList,
                legend: {
                    itemWidth: 2, // 标签宽度为20px
                    itemHeight: 10, // 标签高度为10px

                    textStyle: {
                        color: 'white'
                    },
                    inactiveColor: '#ccc',
                },
                tooltip: {
                    trigger: 'axis',
                    showContent: false,
                },
                dataset: {
                    source: [
                        ['年份', '2018', '2019', '2020', '2021', '2022', '2023'],
                        ['太阳能源', 51.1, 51.4, 55.1, 53.3, 73.8, 68.7],
                        ['风力能源', 40.1, 62.2, 69.5, 36.4, 45.2, 32.5],
                        ['水利能源', 25.2, 37.1, 41.2, 18, 33.9, 49.1],
                        ['生物质能', 43, 23, 43, 23, 56, 54],
                        ['其他能源', 56.5, 82.1, 88.7, 70.1, 53.4, 85.1],
                    ]
                },
                xAxis: {
                    type: 'category',
                    axisLine: {
                        lineStyle: {
                            color: 'white',
                        }
                    }
                },
                yAxis: {
                    gridIndex: 0,
                    axisLine: {
                        lineStyle: {
                            color: 'white',
                        }
                    }
                },
                grid: {
                    top: '53%',
                },
                series: [
                    {
                        type: 'line',
                        smooth: true,
                        seriesLayoutBy: 'row',
                        emphasis: {focus: 'series'}
                    },
                    {
                        type: 'line',
                        smooth: true,
                        seriesLayoutBy: 'row',
                        emphasis: {focus: 'series'}
                    },
                    {
                        type: 'line',
                        smooth: true,
                        seriesLayoutBy: 'row',
                        emphasis: {focus: 'series'}
                    },
                    {
                        type: 'line',
                        smooth: true,
                        seriesLayoutBy: 'row',
                        emphasis: {focus: 'series'}
                    },
                    {
                        type: 'line',
                        smooth: true,
                        seriesLayoutBy: 'row',
                        emphasis: {focus: 'series'}
                    },
                    {
                        type: 'pie',
                        id: 'pie',
                        radius: '30%',
                        center: ['50%', '30%'],
                        emphasis: {
                            focus: 'self'
                        },
                        label: {
                            // show:'false',
                            formatter: `占比为：{d}%`,
                            color: 'white',
                        },
                        encode: {
                            itemName: 'product',
                            value: '2018',
                            tooltip: '2018'
                        }
                    }
                ]
            };
            setTimeout(() => {
                myChart5.setOption(option5);
                option5 = {
                    legend: {
                        textStyle: {
                            color: 'white'
                        },
                        inactiveColor: '#ccc',
                    },
                    tooltip: {
                        trigger: 'axis',
                        showContent: false,
                    },
                    dataset: {
                        source: [
                            ['年份', '2018', '2019', '2020', '2021', '2022', '2023'],
                            ['太阳能源', 51.1, 51.4, 55.1, 53.3, 73.8, 68.7],
                            ['风力能源', 40.1, 62.2, 69.5, 36.4, 45.2, 32.5],
                            ['水利能源', 25.2, 37.1, 41.2, 18, 33.9, 49.1],
                            ['生物质能', 43, 23, 43, 23, 56, 54],
                            ['其他能源', 56.5, 82.1, 88.7, 70.1, 53.4, 85.1],
                        ]
                    },
                    xAxis: {
                        type: 'category',
                        axisLine: {
                            lineStyle: {
                                color: 'white',
                            }
                        }
                    },
                    yAxis: {
                        gridIndex: 0,
                        axisLine: {
                            lineStyle: {
                                color: 'white',
                            }
                        }
                    },
                    grid: {
                        top: '53%',
                    },
                    series: [
                        {
                            type: 'line',
                            smooth: true,
                            seriesLayoutBy: 'row',
                            animation: true, // 启用动画效果
                            emphasis: {focus: 'series'}
                        },
                        {
                            type: 'line',
                            smooth: true,
                            seriesLayoutBy: 'row',
                            animation: true, // 启用动画效果
                            emphasis: {focus: 'series'}
                        },
                        {
                            type: 'line',
                            smooth: true,
                            seriesLayoutBy: 'row',
                            animation: true, // 启用动画效果
                            emphasis: {focus: 'series'}
                        },
                        {
                            type: 'line',
                            smooth: true,
                            seriesLayoutBy: 'row',
                            animation: true, // 启用动画效果
                            emphasis: {focus: 'series'}
                        },
                        {
                            type: 'line',
                            smooth: true,
                            seriesLayoutBy: 'row',
                            animation: true, // 启用动画效果
                            emphasis: {focus: 'series'}
                        },
                        {
                            type: 'pie',
                            id: 'pie',
                            radius: '30%',
                            center: ['50%', '40%'],
                            animationType: 'scale',
                            emphasis: {
                                focus: 'self'
                            },
                            label: {
                                // show:'false',
                                formatter: '数据为：{d}%'
                            },
                            encode: {
                                itemName: 'product',
                                value: '2018',
                                tooltip: '2018'
                            }
                        }
                    ]
                };
                myChart5.on('updateAxisPointer', (event) => {
                    const xAxisInfo = event.axesInfo[0];
                    if (xAxisInfo) {
                        const dimension = xAxisInfo.value + 1;
                        myChart5.setOption({
                            series: {
                                id: 'pie',
                                label: {
                                    show: true,
                                    // formatter: `数据为： {@${dimension}} ({d}%)`
                                    formatter: `占比为：{d}%`
                                },
                                encode: {
                                    value: dimension,
                                    tooltip: dimension
                                },
                            }
                        });
                    }
                });
            });
        } else {
            console.error('Failed to fetch data from initlandlist');
        }
    } catch (error) {
        console.error('Error fetching data:', error);
    }


    const resizeObserver = new ResizeObserver(() => {
        myChart5.resize();
    });
    let currentIndex = -1;
    setInterval(() => {
        const dataLen = option5.dataset.source[0].length;
        // 取消之前高亮
        myChart5.dispatchAction({
            type: 'downplay',
            seriesIndex: 0,
            dataIndex: currentIndex
        });
        currentIndex = (currentIndex + 1) % dataLen;
        // 高亮当前数据
        myChart5.dispatchAction({
            type: 'highlight',
            seriesIndex: 0,
            dataIndex: currentIndex
        });
        // 显示 tooltip
        myChart5.dispatchAction({
            type: 'showTip',
            seriesIndex: 0,
            dataIndex: currentIndex
        });
    }, 2000); // 每隔 2 秒切换一次
    resizeObserver.observe(echartsRef.value);
});
</script>

<template>
    <div class="MainLeftButtom">
        <button class="GoEnergy-title">全国新能源结构及趋势</button>
        <div id="MainLeftButtom-echarts" ref="echartsRef"></div>
    </div>
</template>

<style scoped lang="scss">
.MainLeftButtom {
  width: 100vw;
  height: 100vh;
  color: white;

  .GoEnergy-title {
    position: absolute;
    margin-left: 2vw;
    width: 18vw;
    height: 2.5vh;
    font-size: 1.2vw;
    font-weight: bolder;
    color: white;
    border: none;
    margin-top: -17vh;
    background: none;
    border-radius: 2px;
    z-index: 999;
  }

  #MainLeftButtom-echarts {
    width: 26vw;
    height: 32vh;
    margin-left: -2.4vw;
    position: absolute;
    margin-top: -13.5vh;
  }

  @keyframes glow {
    from {
      box-shadow: 0px 0px 3px 3px #00bfff, 0px 0px 5px 3px #0d0d0d, 0px 0px 7px 5px #00bfff;
    }
    to {
      box-shadow: 0px 0px 5px 3px #00bfff, 0px 0px 7px 5px #0d0d0d, 0px 0px 9px 7px #00bfff;
    }
  }
}
</style>
