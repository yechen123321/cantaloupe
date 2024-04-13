<script setup>
import {ref, onMounted} from 'vue';
import * as echarts from 'echarts';


const echartsRef = ref(null);
let myChart21 = null;
let option21 = null;

onMounted(() => {
    myChart21 = echarts.init(echartsRef.value);
    var colorList = [
        new echarts.graphic.LinearGradient(0, 0, 0, 1, [
            {offset: 0, color: '#56CCF2'},
            {offset: 1, color: '#2948ff'}
        ]),
        new echarts.graphic.LinearGradient(0, 0, 0, 1, [
            {offset: 0, color: '#DCE35B'},
            {offset: 1, color: '#45B649'}
        ]),

        new echarts.graphic.LinearGradient(0, 0, 0, 1, [
            {offset: 0, color: '#4AC29A'},
            {offset: 1, color: '#BDFFF3'}
        ]),
        new echarts.graphic.LinearGradient(0, 0, 0, 1, [
            {offset: 0, color: '#00C9FF'},
            {offset: 1, color: '#92FE9D'}
        ]),
        new echarts.graphic.LinearGradient(0, 0, 0, 1, [
            {offset: 1, color: '#C6FFDD'},
            {offset: 0, color: '#FBD786'},
        ]),
        // 其他渐变色定义...
    ];
    option21 = {
        color:colorList,
        backgroundColor: 'rgba(128,128,128,0)',
        tooltip: {
            trigger: 'axis',
            extraCssText: 'width: 13vw',
            axisPointer: {
                type: 'shadow',
            },
            // textStyle: {
            //     fontWeight: 'bold'
            // },
            formatter: function (params) {
                let tooltipContent = '';
                let mineName = params[0].name;
                tooltipContent += '<span style="font-weight: bold; margin-right: 1vw">' + mineName + '</span>' + '单位/万千瓦时' + '<br>'; // 设置矿地名字的样式为加粗并向上移动5px
                params.forEach(function (param) {
                    if (param.seriesName !== '趋势') {
                        tooltipContent += param.marker + param.seriesName + ': ' + '<span style="float: right; font-weight: bold;">' + param.value + '</span>' + '<br>';
                    }
                });
                return tooltipContent;
            }
        },
        legend: {
            itemWidth: 9, // 标签宽度为20px
            itemHeight: 9, // 标签高度为10px
            top: '15%',
            // itemWidth: 10, // 标签宽度为10px
            // itemHeight: 10, // 标签高度为10px
            textStyle: {
                color: 'white',
            },
            left: 'center',
        },
        grid: {
            left: '3%',
            right: '4%',
            bottom: '3%',
            containLabel: true,
        },
        xAxis: [
            {
                type: 'category',
                data: ['2020', '2021', '2022', '2023'],
                axisLine: {
                    lineStyle: {
                        color: 'white',
                    },
                },
            },
        ],
        yAxis: [
            {
                type: 'value',
                axisLine: {
                    lineStyle: {
                        color: 'white',
                    },
                },
            },
        ],
        series: [
            {
                name: '光生发电',
                type: 'bar',
                emphasis: {
                    focus: 'series'
                },
                data: [ 334, 390, 330, 320],
                itemStyle: {
                    barBorderRadius: [5,5, 0, 0] // 设置柱子上方为圆角，数组中的四个值分别代表左上、右上、右下、左下的圆角半径
                }
            },
            {
                name: '水生发电',
                type: 'bar',
                emphasis: {
                    focus: 'series'
                },
                data: [ 132,134,230, 210],
                itemStyle: {
                    barBorderRadius: [5,5, 0, 0] // 设置柱子上方为圆角，数组中的四个值分别代表左上、右上、右下、左下的圆角半径
                }
            },
            {
                name: '风生发电',
                type: 'bar',
                data: [ 1026, 1679, 1600, 1570],
                emphasis: {
                    focus: 'series'
                },
                itemStyle: {
                    barBorderRadius: [5,5, 0, 0] // 设置柱子上方为圆角，数组中的四个值分别代表左上、右上、右下、左下的圆角半径
                }
            },
            {
                name: '氢能',
                type: 'bar',
                emphasis: {
                    focus: 'series'
                },
                data: [ 234, 290, 330, 310],
                itemStyle: {
                    barBorderRadius: [5,5, 0, 0] // 设置柱子上方为圆角，数组中的四个值分别代表左上、右上、右下、左下的圆角半径
                }
            },
            {
                name: '生物质能',
                type: 'bar',
                emphasis: {
                    focus: 'series'
                },
                data: [232, 201, 330, 410],
                itemStyle: {
                    barBorderRadius: [5,5, 0, 0] // 设置柱子上方为圆角，数组中的四个值分别代表左上、右上、右下、左下的圆角半径
                }
            },

            {
                name: '地热能',
                type: 'bar',
                stack: 'Search Engine',
                emphasis: {
                    focus: 'series'
                },
                data: [734, 1090, 1130, 1120],
                itemStyle: {
                    barBorderRadius: [5,5, 0, 0] // 设置柱子上方为圆角，数组中的四个值分别代表左上、右上、右下、左下的圆角半径
                }
            },
        ]
    };
    option21 && myChart21.setOption(option21);
    const resizeObserver = new ResizeObserver(() => {
        myChart21.resize();
    });

    resizeObserver.observe(echartsRef.value);

});
</script>

<template>
    <div className="SecondMiddenCenter">
        <img className="BackImg" src="../../../assets/pic/border4.png" alt="">
        <button class="GotoMore">安徽省再生能源产能图</button>
        <div id="SecondMiddenCenter-echarts" ref="echartsRef"></div>
    </div>
</template>

<style scoped lang="scss">
.SecondMiddenCenter {
  width: 100vw;
  height: 100vh;
  color: white;

  .GotoMore {
    position: absolute;
    width: 20vw;
    border: none;
    background: none;
    font-weight: bolder;
    font-size: 1.26em;
    color: white;
    margin-top: 1.3vh;
    margin-left: -30vw;
    cursor: pointer;
  }

  #SecondMiddenCenter-echarts {
    width: 26vw;
    height: 27vh;
    margin-left: 0.7vw;
    position: absolute;
    margin-top: -28vh;
    z-index: 1000;
  }

  .BackImg {
    width: 40vw;
    height: 29vh;
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
