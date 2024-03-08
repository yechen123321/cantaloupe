<script setup>
import {ref, onMounted} from 'vue';
import * as echarts from 'echarts';
import MainLeftMidden from "@/components/FirstView/FirstViewTools/MainLeftMidden.vue";
import MainLeftButtom from "@/components/FirstView/FirstViewTools/MainLeftButtom.vue";
import MainChinaLeft from "@/components/FirstView/MainChinaLeft.vue";

const echartsRef = ref(null);
let myChart1 = null;
let option1 = null;

onMounted(() => {
    myChart1 = echarts.init(echartsRef.value, 'dark');

    // Your echarts option setup here...
    // (Your existing option setup code)
    option1 = {
        backgroundColor:'rgba(128,128,128,0)',
        title: {
            text: '全国重要矿产开发产量',
            left: 'center',
            top: '0%',
            textStyle: {
                color: 'white',
            },
        },
        tooltip: {
            trigger: 'axis',
            extraCssText: 'width: 13vw',
            axisPointer: {
                type: 'shadow'
            },
            // textStyle: {
            //     fontWeight: 'bold'
            // },
            formatter: function (params) {
                let tooltipContent = '';
                let mineName = params[0].name;
                tooltipContent += '<span style="font-weight: bold; margin-top: -500px;">' + mineName + '</span>' + '<br>' ; // 设置矿地名字的样式为加粗并向上移动5px
                params.forEach(function (param) {
                    if (param.seriesName !== '趋势') {
                        tooltipContent += param.marker + param.seriesName + ': ' + '<span style="float: right; font-weight: bold;">' + param.value + '吨</span>' + '<br>';
                    }
                });
                return tooltipContent;
            }
        },
        legend: {
            width:'120%',
            top:'15%',
            itemWidth: 10, // 标签宽度为10px
            itemHeight: 10, // 标签高度为10px
            left:'center',
            textStyle: {
                color: 'white',
            },
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
                data: ['2017', '2018', '2019', '2020', '2021', '2022', '2023'],
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
        yAxis: [
            {
                type: 'value',

                axisLine: {
                    lineStyle: {
                        color: 'white',
                    }
                },
                axisLabel: {
                    textStyle: {
                        color: 'white' // 设置Y轴上数据的颜色为白色
                    }
                }
            }
        ],
        series: [
            {
                name: '铁矿',
                type: 'bar',
                emphasis: {
                    focus: 'series'
                },
                data: [320, 332, 301, 334, 390, 330, 320]
            },
            {
                name: '锰矿',
                type: 'bar',
                stack: 'Ad',
                emphasis: {
                    focus: 'series'
                },
                data: [120, 132, 101, 134, 90, 230, 210]
            },
            {
                name: '世伟矿',
                type: 'bar',
                stack: 'Ad',
                emphasis: {
                    focus: 'series'
                },
                data: [220, 182, 191, 234, 290, 330, 310]
            },
            {
                name: '超级矿',
                type: 'bar',
                stack: 'Ad',
                emphasis: {
                    focus: 'series'
                },
                data: [150, 232, 201, 154, 190, 330, 410]
            },
            {
                name: '基岩',
                type: 'bar',
                data: [862, 1018, 964, 1026, 1679, 1600, 1570],
                emphasis: {
                    focus: 'series'
                },
                markLine: {
                    lineStyle: {
                        type: 'dashed'

                    },
                    label: {
                        formatter: '{c} 吨', // 在数据后加上单位
                        textStyle: {
                            color: 'white' // 设置 markLine 文本颜色为白色
                        }
                    },
                    data: [[{type: 'min'}, {type: 'max'}]]
                }
            },
            // {
            //     name: 'Baidu',
            //     type: 'bar',
            //     barWidth: 5,
            //     stack: 'Search Engine',
            //     emphasis: {
            //         focus: 'series'
            //     },
            //     data: [620, 732, 701, 734, 1090, 1130, 1120]
            // },
            // {
            //     name: 'Google',
            //     type: 'bar',
            //     stack: 'Search Engine',
            //     emphasis: {
            //         focus: 'series'
            //     },
            //     data: [120, 132, 101, 134, 290, 230, 220]
            // },
            //
            // {
            //     name: 'Others',
            //     type: 'bar',
            //     stack: 'Search Engine',
            //     emphasis: {
            //         focus: 'series'
            //     },
            //     data: [62, 82, 91, 84, 109, 110, 120]
            // }
        ]
    };
    option1 && myChart1.setOption(option1);

    const resizeObserver = new ResizeObserver(() => {
        myChart1.resize();
    });

    resizeObserver.observe(echartsRef.value);
});
</script>


<template>
    <div class="MainLeftTable">
        <div id="MainTable-echarts" ref="echartsRef"></div>
<!--        <Button class="GoMinerals">全国重要矿产开发产量</Button>-->
        <MainLeftMidden id="MainLeftMidden-out"></MainLeftMidden>
        <MainChinaLeft id="MainChinaLeft-out"></MainChinaLeft>
        <img class="BackImg" src="../../assets/pic/border3.png" alt="">
        <MainLeftButtom id="MainLeftButtom-out"></MainLeftButtom>
    </div>
</template>

<style scoped lang="scss">
.MainLeftTable {
  width: 100vw;
  height: 100vh;

  .BackImg {
    width: 27vw;
    height: 84vh;
  }

  #MainTable-echarts {
    width: 23vw;
    height: 21.5vh;
    margin-left: 1.5vw;
    position: absolute;
    margin-top: 28vh;
    z-index: 999;
  }

  .GoMinerals {
    //cursor: pointer;
    position: absolute;
    //right: 0;
    text-align: center;
    width: 13vw;
    height: 2.5vh;
    font-size: 1.2vw;
    margin-top: 27.5vh;
    //margin-right: -2vw;
    margin-left: 6.8vw;
    font-weight: bolder;
    color: white;
    background: none;
    border: none;
    border-radius: 2px;
    z-index: 999;
  }

  //.GoMinerals:hover {
  //  width: 14vw;
  //  height: 3vh;
  //  font-size: 1.3vw;
  //  margin-top: 31vh;
  //  //margin-right: -2.4vw;
  //  margin-left: 6.3vw;
  //}
  //
  //.GoMinerals:active {
  //  font-size: 1.2vw;
  //  margin-top: 31vh;
  //  margin-left: 6.8vw;
  //  width: 13vw;
  //  height: 2.5vh;
  //}

  #MainLeftMidden-out {
    width: 25vw;
    height: 23.5vh;
    margin-left: 2.5vw;
    position: absolute;
    margin-top: 27.8vh;
  }

  #MainLeftButtom-out {
    width: 23vw;
    height: 32.5vh;
    margin-left: 2.5vw;
    position: absolute;
    margin-top: -16vh;
  }

  #MainChinaLeft-out {
    width: 15vw;
    height: 23.5vh;
    margin-left: 28vw;
    position: absolute;
    margin-top: 21.8vh;
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
