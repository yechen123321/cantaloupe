<script setup>
import {ref, onMounted} from 'vue';
import * as echarts from 'echarts';


const echartsRef = ref(null);
let myChart21 = null;
let option21 = null;

onMounted(() => {
    myChart21 = echarts.init(echartsRef.value);
    option21 = {
        title: {
            text: '你好不好我不好',
            left: 'center',
            top: '10%',
            textStyle: {
                color: 'white',
            },
        },
        tooltip: {
            trigger: 'axis',
            axisPointer: {
                type: 'shadow'
            },
        },
        legend: {
            textStyle: {
                color: 'white',
            },
            left: '5%',
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
                data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
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
                    }
                }
            }
        ],
        series: [
            {
                name: 'Direct',
                type: 'bar',
                emphasis: {
                    focus: 'series'
                },
                data: [320, 332, 301, 334, 390, 330, 320]
            },
            {
                name: 'Email',
                type: 'bar',
                stack: 'Ad',
                emphasis: {
                    focus: 'series'
                },
                data: [120, 132, 101, 134, 90, 230, 210]
            },
            {
                name: 'Union Ads',
                type: 'bar',
                stack: 'Ad',
                emphasis: {
                    focus: 'series'
                },
                data: [220, 182, 191, 234, 290, 330, 310]
            },
            {
                name: 'Video Ads',
                type: 'bar',
                stack: 'Ad',
                emphasis: {
                    focus: 'series'
                },
                data: [150, 232, 201, 154, 190, 330, 410]
            },
            {
                name: 'Search Engine',
                type: 'bar',
                data: [862, 1018, 964, 1026, 1679, 1600, 1570],
                emphasis: {
                    focus: 'series'
                },
                markLine: {
                    lineStyle: {
                        type: 'dashed'
                    },
                    data: [[{type: 'min'}, {type: 'max'}]]
                }
            },
            {
                name: 'Baidu',
                type: 'bar',
                barWidth: 5,
                stack: 'Search Engine',
                emphasis: {
                    focus: 'series'
                },
                data: [620, 732, 701, 734, 1090, 1130, 1120]
            },
            {
                name: 'Google',
                type: 'bar',
                stack: 'Search Engine',
                emphasis: {
                    focus: 'series'
                },
                data: [120, 132, 101, 134, 290, 230, 220]
            },

            {
                name: 'Others',
                type: 'bar',
                stack: 'Search Engine',
                emphasis: {
                    focus: 'series'
                },
                data: [62, 82, 91, 84, 109, 110, 120]
            }
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
        <div id="SecondMiddenCenter-echarts" ref="echartsRef"></div>
    </div>
</template>

<style scoped lang="scss">
.SecondMiddenCenter {
  width: 100vw;
  height: 100vh;
  color: white;

  #SecondMiddenCenter-echarts {
    width: 40vw;
    height: 25vh;
    margin-left: -0.5vw;
    position: absolute;
    margin-top: -27.5vh;
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
