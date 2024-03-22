<script setup>
import {onMounted, ref} from "vue";
import * as echarts from "echarts";

const datas = ref([
    {name: '全国能源投资建设', number: 28000, up: '亿', num: 1.6},
    {name: '全国能源投资建设', number: 28000, up: '亿', num: 1.6},
]);

const echartsRef = ref(null);
let myChart72 = null;
let option72 = null;

onMounted(() => {
    myChart72 = echarts.init(echartsRef.value);
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
    option72 = {
        color: colorList,
        // toolbox: {
        //     iconStyle: {
        //         borderColor: "#fff",
        //     },
        //     showTitle:false,
        //     right:'3%',
        //     feature: {
        //         dataView: { show: true, readOnly: false },
        //         // magicType: { show: true, type: ['line', 'bar'] },
        //         restore: { show: true },
        //         saveAsImage: { show: true }
        //     }
        // },
        tooltip: {
            trigger: 'axis',
            extraCssText: 'width: 15vw; height: 15vh;', // 设置tooltip框的宽度和高度，调整框的大小
            formatter: function (params) {
                let tooltipContent = '';
                let mineName = params[0].name;
                tooltipContent += '<span style="font-weight: bold;margin-right: 1vw; margin-top: -500px;">' + mineName + '</span>' + '单位/亿吨,亿元<br>' + '<br>'; // 设置矿地名字的样式为加粗并向上移动5px
                params.forEach(function (param) {
                    if (param.seriesName === '全国能耗降低率') {
                        tooltipContent += param.marker + param.seriesName + ': ' + '<span style="float: right; font-weight: bold;">' + param.value + '%</span>' + '<br>';
                    } else {
                        tooltipContent += param.marker + param.seriesName + ': ' + '<span style="float: right; font-weight: bold;">' + param.value + '</span>' + '<br>';
                    }
                });
                return tooltipContent;
            }
        },
        grid: {
            left: '5.3%', // 调整图表左边距
            right: '7%', // 调整图表右边距
            // top: '10%', // 调整图表上边距
            bottom: '15%', // 调整图表下边距
            containLabel: true,
        },
        legend: {
            // left:'0%',
            data: ['开采耗费', '获取能量', '全国能耗降低率'],
            textStyle: {
                color: 'white'
            }
        },
        xAxis: [
            {
                type: 'category',
                axisTick: {
                    alignWithLabel: true
                }, axisLine: {
                    lineStyle: {
                        color: 'white',
                    },
                },
                axisLabel: {
                    textStyle: {
                        color: 'white' // 设置X轴上数据的颜色为白色
                    }
                },
                // prettier-ignore
                data: ['Aug', 'Sep', 'Oct', 'Nov', 'Dec']
            }
        ],
        yAxis: [
            {
                type: 'value',
                name: '万亿元',
                position: 'right',
                alignTicks: true,
                nameTextStyle: {
                    padding: [0, -30, 0, 0]
                },
                axisLine: {
                    lineStyle: {
                        color: 'white',
                    },
                },
                axisLabel: {
                    textStyle: {
                        color: 'white' // 设置X轴上数据的颜色为白色
                    }
                }
            },
            {
                type: 'value',
                name: '降低率',
                nameLocation: 'end', // 将名称显示在轴线末尾，即向右移动
                position: 'right',
                nameTextStyle: {
                    padding: [0, -38, 0, 0]
                },
                alignTicks: true,
                offset: 40,
                axisLine: {
                    lineStyle: {
                        color: 'white',
                    },
                },
                axisLabel: {
                    textStyle: {
                        color: 'white' // 设置X轴上数据的颜色为白色
                    }
                }
            },
            {
                type: 'value',
                name: '标准煤 / 万亿吨',
                position: 'left',
                alignTicks: true,
                axisLine: {
                    lineStyle: {
                        color: 'white',
                    },
                },
                axisLabel: {
                    textStyle: {
                        color: 'white' // 设置X轴上数据的颜色为白色
                    }
                }
            },
        ],
        series: [
            {
                name: '开采耗费',
                type: 'bar',
                yAxisIndex: 2,
                data: [
                    135.6, 162.2, 32.6, 20.0, 6.4,
                ]
            },
            {
                name: '获取能量',
                type: 'bar',
                yAxisIndex: 0,
                data: [
                    175.6, 182.2, 48.7, 18.8, 6.0
                ]
            },
            {
                name: '全国能耗降低率',
                type: 'line',
                yAxisIndex: 1,
                data: [3.4, 2.0, 1.5, 1.0, 3.2]
            },
        ]
    };

    option72 && myChart72.setOption(option72);

    const resizeObserver = new ResizeObserver(() => {
        myChart72.resize();
    });

    resizeObserver.observe(echartsRef.value);
});
</script>

<template>
    <div class="AnHuiLimitRight">
        <div class="second">
            <img src="../../../assets/pic/ca1.png" alt="" class="BackImg">
            <ul class="year-on-year">
                <li v-for="(item,index) in datas" :class="{ 'li-active': index === 0 }" :key="index">
                    <div class="li-title">{{ item.name }}</div>
                    <div class="li-number">{{ item.number }}</div>
                    <div class="li-up">{{ item.up }}</div>
                    <div class="li-midden">同比增长</div>
                    <div class="li-num">{{ item.num }}%</div>
                </li>
            </ul>
        </div>
        <div class="first">
            <div class="title1">能源开采效率</div>
            <div class="AnHuiLimitRight-echarts" ref="echartsRef"></div>
        </div>

        <img src="../../../assets/pic/ca1.png" alt="" class="BackImg">
    </div>
</template>

<style scoped lang="scss">
.AnHuiLimitRight {
  width: 100%;
  height: 100%;

  .year-on-year::-webkit-scrollbar {
    display: none;
  }

  .year-on-year {
    height: 10vh;
    position: absolute;
    z-index: 10;
    //overflow-y: auto;
    width: 100%;
    margin-top: 5vh;
    //background: red;
    li {
      list-style-type: none;
      width: 100%;
      //margin-top: 2%;
      line-height: 4.5vh;
      color: white;
      height: 100%;

      .li-title {
        float: left;
        width: 18vw;
        font-size: 1.4em;
        font-weight: bolder;
        margin-bottom: 1vh;
      }

      .li-number {
        float: left;
        color: #1cd7cd;
        text-align: center;
        margin-left: 2vw;
        width: 30%;
        font-weight: bolder;
        text-shadow: 0 0 1px #1cd7cd, 0 0 2px #1cd7cd, 0 0 3px #1cd7cd;
        font-size: 2em;
      }

      .li-up {
        float: left;
        margin-left: 4.5%;
        font-size: 1em;
        margin-top: 1.3%;
        color: #01bae4;
        text-shadow: 0 0 1px #1cd7cd, 0 0 1px #1cd7cd, 0 0 1.5px #1cd7cd;
      }

      .li-midden {
        float: left;
        margin-left: 4%;
        margin-top: 1.3%;
        font-size: 1em;
        color: #01bae4;
        text-shadow: 0 0 1px #1cd7cd, 0 0 1px #1cd7cd, 0 0 1.5px #1cd7cd;
      }

      .li-num {
        float: left;
        margin-left: 5%;
        font-size: 2em;
        color: yellow;
        font-weight: bolder;
      }
    }
  }

  .second {
    width: 24vw;
    height: 20vh;
    position: absolute;
    //background: red;
    margin-top: -24.87vh;

    .BackImg {
      width: 28vw;
      height: 30vh;
      position: absolute;
    }
  }

  .first {
    margin-top: 5vh;
    position: absolute;

    .title1 {
      position: absolute;
      color: white;
      font-weight: bolder;
      width: 20vw;
      margin-top: 1vh;
      margin-left: -3vw;
      //background: red;
      text-align: center;
      font-size: 1.26em;
    }

    .AnHuiLimitRight-echarts {
      width: 25vw;
      height: 15vw;
      margin-top: 5vh;
      margin-left: 1.4vw;
      position: absolute;
      //background: black;
    }
  }

  //.AnHuiLimitRight-echarts2{
  //  width: 20vw;
  //  height: 15vw;
  //  margin-top: 20vh;
  //  position: absolute;
  //  background: red;
  //}
  .BackImg {
    width: 28vw;
    height: 40vh;
  }
}
</style>