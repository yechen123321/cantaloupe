<script setup>
import {ref, onMounted} from 'vue';
import * as echarts from 'echarts';
import 'echarts-gl';

const echartsRef = ref(null);
let myChart9 = null;
let option9 = null;

onMounted(() => {
    myChart9 = echarts.init(echartsRef.value);

    // Your echarts option setup here...
    // (Your existing option setup code)
    // prettier-ignore
    var hours = ['沿海滩涂', '内陆滩涂', '沼泽地', '红树林地', '森林沼泽', '灌丛沼泽', '沼泽草地',];
// prettier-ignore
    var years = ['2017', '2018', '2019',
        '2020', '2021', '2022', '2023'];
// prettier-ignore
    var data = [[0, 0, 0.45], [0, 1, 0.14], [0, 2, 0.15], [0, 3, 0.19], [0, 4, 0.14], [0, 5, 0.11], [0, 6, 0.15],
        [1, 0, 0.42], [1, 1, 0.14], [1, 2, 0.15], [1, 3, 0.19], [1, 4, 0.14], [1, 5, 0.11], [1, 6, 0.15],
        [2, 0, 0.34], [2, 1, 0.14], [2, 2, 0.15], [2, 3, 0.19], [2, 4, 0.14], [2, 5, 0.11], [2, 6, 0.15],
        [3, 0, 0.43], [3, 1, 0.14], [3, 2, 0.15], [3, 3, 0.19], [3, 4, 0.14], [3, 5, 0.11], [3, 6, 0.15],
        [4, 0, 0.34], [4, 1, 0.14], [4, 2, 0.15], [4, 3, 0.19], [4, 4, 0.14], [4, 5, 0.11], [4, 6, 0.15],
        [5, 0, 0.29], [5, 1, 0.14], [5, 2, 0.15], [5, 3, 0.19], [5, 4, 0.14], [5, 5, 0.11], [5, 6, 0.15],
        [6, 0, 0.31], [6, 1, 0.14], [6, 2, 0.15], [6, 3, 0.19], [6, 4, 0.14], [6, 5, 0.11], [6, 6, 0.15],]
    option9 = {
        title: {
            text: '全国湿地资源结构示意图',
            top: '1%',
            left: '25.5%',
            textStyle: {
                color: 'white'
            }
        },
        tooltip: {
            formatter: function (params) {
                return '年份：' + years[params.value[1]] + '<br>' + '结构类型：' + hours[params.value[0]] + '<br>' + '结构占比：' + (params.value[2] * 100).toFixed(2) + '%';// 使用当前数据点的索引来获取对应的 hours 和 years 值
            },
        },
        visualMap: {
            max: 0.5,
            inRange: {
                color: [
                    '#abd9e9',
                    '#fdae61',
                    '#d73027',
                ]
            }
        },
        xAxis3D: {
            type: 'category',
            data: hours,
            axisLine: {
                lineStyle: {
                    color: 'white',
                }
            }
        },
        yAxis3D: {
            type: 'category',
            data: years,
            axisLine: {
                lineStyle: {
                    color: 'white',
                }
            }
        },
        zAxis3D: {
            type: 'value',
            max: 1,
            axisLine: {
                lineStyle: {
                    color: 'white',
                },

            }
        },
        grid3D: {
            boxWidth: 200,
            boxDepth: 80,
            viewControl: {
                autoRotate: true, // 自动旋转
                // distance: 100, // 初始视角距离
                // minBeta: -360, // 最小仰角
                // maxBeta: 360, // 最大仰角
                // alpha: 45, // 初始方位角
                // beta: 10, // 初始仰角
            },

            light: {
                main: {
                    intensity: 1.2,
                    shadow: true
                },
                ambient: {
                    intensity: 0.3
                }
            }
        },
        series: [
            {
                type: 'bar3D',
                data: data.map(function (item) {
                    return {
                        value: [item[1], item[0], item[2]]
                    };
                }),
                shading: 'lambert',
                label: {
                    fontSize: 16,
                    borderWidth: 1
                },
                emphasis: {
                    label: {
                        fontSize: 20,
                        color: '#900'
                    },
                    itemStyle: {
                        color: '#900'
                    }
                }
            }
        ]
    };

    option9 && myChart9.setOption(option9);

    const resizeObserver = new ResizeObserver(() => {
        myChart9.resize();
    });

    resizeObserver.observe(echartsRef.value);
});
</script>


<template>
    <div className="MainDownLeft">
        <div id="MainDownLeft-echarts" ref="echartsRef"></div>
    </div>
</template>

<style scoped lang="scss">
.MainDownLeft {
  width: 100vw;
  height: 100vh;
  color: white;

  #MainDownLeft-echarts {
    width: 23vw;
    height: 26vh;
    margin-left: 1vw;
    position: absolute;
    margin-top: -21.5vh;
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
