<script setup>
import {ref, onMounted} from 'vue';
import * as echarts from 'echarts';
import {useRouter} from 'vue-router';

const router = useRouter();

const handleRouteChange = () => {
    // 在这里添加您的路由切换逻辑，下面是一个示例，实际根据您的路由配置进行修改
    router.push('/'); // 替换'/new-route'为您要跳转的路由路径
};
const echartsRef = ref(null);
let myChart22 = null;
let option22 = null;

onMounted(() => {
    myChart22 = echarts.init(echartsRef.value);
    const yearCount = 7;
    const categoryCount = 30;
    const xAxisData = [];
    const customData = [];
    const legendData = [];
    const dataList = [];
    legendData.push('trend');
    const encodeY = [];
    for (var i = 0; i < yearCount; i++) {
        legendData.push(2017 + i + '');
        dataList.push([]);
        encodeY.push(1 + i);
    }
    for (var i = 0; i < categoryCount; i++) {
        var val = Math.random(1, 100) * 1000;
        xAxisData.push('矿场' + i + '\t单位 / 吨');
        var customVal = [i];
        customData.push(customVal);
        for (var j = 0; j < dataList.length; j++) {
            var value =
                j === 0
                    ? echarts.number.round(val, 2)
                    : echarts.number.round(
                        Math.max(0, dataList[j - 1][i] + (Math.random(1, 100) - 0.5) * 200),
                        2
                    );
            dataList[j].push(value);
            customVal.push(value);
        }
    }
    option22 = {
        title: {
            left: 'center',
            top: '10%',
            text: '安徽省矿场产量总览',
            textStyle: {
                color: 'white',
            },
        },
        tooltip: {
            trigger: 'axis'
        },
        legend: {
            data: legendData,
            textStyle: {
                color: 'white'
            }
        },
        dataZoom: [
            {
                type: 'slider',
                start: 50,
                end: 70
            },
            {
                type: 'inside',
                start: 50,
                end: 70
            }
        ],
        xAxis: {
            data: xAxisData,

            axisLine: {
                lineStyle: {
                    color: 'white',
                }
            },
        },
        yAxis: {

            axisLine: {
                lineStyle: {
                    color: 'white',
                }
            },
        },
        series: [
            {
                type: 'custom',
                name: 'trend',
                renderItem: function (params, api) {
                    var xValue = api.value(0);
                    var currentSeriesIndices = api.currentSeriesIndices();
                    var barLayout = api.barLayout({
                        barGap: '30%',
                        barCategoryGap: '20%',
                        count: currentSeriesIndices.length - 1
                    });
                    var points = [];
                    for (var i = 0; i < currentSeriesIndices.length; i++) {
                        var seriesIndex = currentSeriesIndices[i];
                        if (seriesIndex !== params.seriesIndex) {
                            var point = api.coord([xValue, api.value(seriesIndex)]);
                            point[0] += barLayout[i - 1].offsetCenter;
                            point[1] -= 20;
                            points.push(point);
                        }
                    }
                    var style = api.style({
                        stroke: api.visual('color'),
                        fill: 'none'
                    });
                    return {
                        type: 'polyline',
                        shape: {
                            points: points
                        },
                        style: style
                    };
                },
                itemStyle: {
                    borderWidth: 2
                },
                encode: {
                    x: 0,
                    y: encodeY
                },
                data: customData,
                z: 100
            },
            ...dataList.map(function (data, index) {
                return {
                    type: 'bar',
                    animation: false,
                    name: legendData[index + 1],
                    itemStyle: {
                        opacity: 1
                    },
                    data: data
                };
            })
        ]
    };

    option22 && myChart22.setOption(option22);
    const resizeObserver = new ResizeObserver(() => {
        myChart22.resize();
    });

    resizeObserver.observe(echartsRef.value);
});
</script>

<template>
    <div className="SecondMiddenCenter">
        <img className="BackImg" src="../../../assets/pic/border4.png" alt="">
        <div id="SecondMiddenCenter-echarts" ref="echartsRef"></div>
        <Button class="GotoOre" @click="handleRouteChange">矿场详情</Button>
    </div>
</template>

<style scoped lang="scss">
.SecondMiddenCenter {
  width: 100vw;
  height: 100vh;
  color: white;

  #SecondMiddenCenter-echarts {
    width: 44vw;
    height: 27vh;
    margin-left: -1.5vw;
    position: absolute;
    margin-top: -27.5vh;
    z-index: 166;
  }

  .GotoOre {
    position: absolute;
    margin-left: -8vw;
    margin-top: 4.5vh;
    width: 6vw;
    height: 2.5vh;
    color: white;
    font-size: 0.8vw;
    font-weight: bolder;
    border-radius: 5px;
    z-index: 999;
    cursor: pointer;
    border: none;
    background: #0d87f6;
  }

  .GotoOre:hover {
    width: 6.5vw;
    height: 3vh;
    margin-top: 4.3vh;
    margin-left: -8.3vw;
    font-size: 1vw;
  }

  .GotoOre:active {
    margin-left: -8vw;
    margin-top: 4.5vh;
    width: 6vw;
    height: 2.5vh;
    color: white;
    font-size: 0.8vw;
  }

  .BackImg {
    width: 40vw;
    height: 29vh;
    //margin-top: -20vh;
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
