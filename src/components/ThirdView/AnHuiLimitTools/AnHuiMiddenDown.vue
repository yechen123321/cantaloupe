<script setup>
import {ref, onMounted, onBeforeUnmount} from 'vue';
import * as echarts from 'echarts';
import AnHuiMiddenDownThing from "@/components/ThirdView/AnHuiLimitTools/AnHuiMiddenDownThing.vue";

const echartsRef = ref(null);
let myChart22 = null;
let option22 = null;

onMounted(() => {
    myChart22 = echarts.init(echartsRef.value);
    var colorList = [
        '#ea7ccc', '#73c0de', '#3ba272', '#fc8452',
    ];
    const yearCount = 3;
    const categoryCount = 30;
    const xAxisData = [];
    const customData = [];
    const legendData = [];
    const dataList = [];
    legendData.push('趋势');
    const encodeY = [];
    for (var i = 0; i < yearCount; i++) {
        legendData.push(2021 + i + '');
        dataList.push([]);
        encodeY.push(1 + i);
    }
    for (var i = 0; i < categoryCount; i++) {
        var val = Math.random(1, 100) * 1000;
        xAxisData.push('矿场' + i);
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
        backgroundColor: 'rgba(128,128,128,0)',
        color: colorList,
        // title: {
        //     left: 'center',
        //     top: '-1%',
        //     text: '安徽省矿场产量总览',
        //     textStyle: {
        //         color: 'white',
        //     },
        tooltip: {
            trigger: 'axis',
            extraCssText: 'width: 10vw; height: 14vh;', // 设置tooltip框的宽度和高度，调整框的大小
            formatter: function (params) {
                let tooltipContent = '';
                let mineName = params[0].name; // 获取矿地的名字
                tooltipContent += '<span style="font-weight: bold; margin-right: 1vw; margin-top: -500px;">' + mineName + '</span>' + '单位/万吨' + '<br>' + '<br>'; // 设置矿地名字的样式为加粗并向上移动5px
                params.forEach(function (param) {
                    if (param.seriesName !== '趋势') {
                        tooltipContent += param.marker + param.seriesName + ': ' + '<span style="float: right; font-weight: bold;">' + param.value + '</span>' + '<br>';
                    }
                });
                return tooltipContent;
            }

        },
        legend: {
            data: legendData,
            top: '12%',
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
                name: '趋势',
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

    let start = -1; // 初始数据区域缩放起始位置
    let end = 2; // 初始数据区域缩放结束位置
    let step = 1; // 每次轮播的步长
    let direction = 1; // 方向，1表示向前，-1表示向后

    const timer = setInterval(() => {
        start += step * direction;
        end += step * direction;

        if (start < 0) {
            start = 0;
            end = 2;
            direction = 1; // 改变方向为向前
        } else if (end >= 30) {
            start = 0;
            end = 2;
            direction = 1; // 改变方向为向前
        }

        myChart22.dispatchAction({
            type: 'dataZoom',
            startValue: start,
            endValue: end
        });
    }, 2000); // 设置轮播间隔时间，单位为毫秒

    // 监听组件销毁事件，清除定时器
    onBeforeUnmount(() => {
        clearInterval(timer);
    });
    const resizeObserver = new ResizeObserver(() => {
        myChart22.resize();
    });

    resizeObserver.observe(echartsRef.value);
});
</script>

<template>
    <div className="SecondMiddenCenter">
        <img className="BackImg" src="../../../assets/pic/border4.png" alt="">
        <div class="SecondMiddenCenter-title">安徽省矿场产量总览</div>
        <div id="SecondMiddenCenter-echarts" ref="echartsRef"></div>
        <AnHuiMiddenDownThing id="AnHuiMiddenDownThing-out"></AnHuiMiddenDownThing>
        <!--        <Button class="GotoOre" @click="handleRouteChange">矿场详情</Button>-->
    </div>
</template>

<style scoped lang="scss">
.SecondMiddenCenter {
  width: 100vw;
  height: 100vh;
  color: white;

  .SecondMiddenCenter-title {
    position: absolute;
    margin-top: -28.7vh;
    margin-left: 14vw;
    font-size: 1.3vw;
    font-weight: bolder;
  }

  #AnHuiMiddenDownThing-out {
    width: 12vw;
    height: 18vh;
    position: absolute;
    right: 0;
    //background: red;
    margin-right: 0.8vw;
    margin-top: -24vh;
    z-index: 199;
    border-left: 1.5px solid #0d87f6;
  }

  #SecondMiddenCenter-echarts {
    width: 28vw;
    height: 27vh;
    //margin-left: 0vw;
    position: absolute;
    margin-top: -28.2vh;
    z-index: 166;
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
