<script setup>
import {ref, onMounted} from 'vue';
import * as echarts from 'echarts';

const echartsRef = ref(null);
let myChart5 = null;
let option5 = null;

onMounted(() => {
    myChart5 = echarts.init(echartsRef.value);

    // Your echarts option setup here...
    // (Your existing option setup code)
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
                ['光伏发电', 43, 23, 43, 23, 56, 54],
                ['风能发电', 56.5, 82.1, 88.7, 70.1, 53.4, 85.1],
                ['水力发电', 51.1, 51.4, 55.1, 53.3, 73.8, 68.7],
                ['火力发电', 40.1, 62.2, 69.5, 36.4, 45.2, 32.5],
                ['核能发电', 25.2, 37.1, 41.2, 18, 33.9, 49.1]
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
                    formatter: '{b}数据为：{@2018} ({d}%)',
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
                    ['光伏发电', 43, 23, 43, 23, 56, 54],
                    ['风能发电', 56.5, 82.1, 88.7, 70.1, 53.4, 85.1],
                    ['水力发电', 51.1, 51.4, 55.1, 53.3, 73.8, 68.7],
                    ['火力发电', 40.1, 62.2, 69.5, 36.4, 45.2, 32.5],
                    ['核能发电', 25.2, 37.1, 41.2, 18, 33.9, 49.1]
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
                    center: ['50%', '30%'],
                    animationType: 'scale',
                    emphasis: {
                        focus: 'self'
                    },
                    label: {
                        // show:'false',
                        formatter: '数据为：{@2018} ({d}%)'
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
                            formatter: `{b}: {@${dimension}} ({d}%)`
                        },
                        encode: {
                            value: dimension,
                            tooltip: dimension
                        }
                    }
                });
            }
        });
    });

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
        <div id="MainLeftButtom-echarts" ref="echartsRef"></div>
    </div>
</template>

<style scoped lang="scss">
.MainLeftButtom {
  width: 100vw;
  height: 100vh;
  color: white;

  #MainLeftButtom-echarts {
    width: 24vw;
    height: 32vh;
    margin-left: -0.5vw;
    position: absolute;
    margin-top: -18.5vh;
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
