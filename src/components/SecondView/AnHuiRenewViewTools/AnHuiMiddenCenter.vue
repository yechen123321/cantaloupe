<script setup>
import {ref, onMounted} from 'vue';
import * as echarts from 'echarts';


const echartsRef = ref(null);
let myChart21 = null;
let option21 = null;

onMounted(() => {
    myChart21 = echarts.init(echartsRef.value);
    option21 = {
        // toolbox: {
        //     iconStyle: {
        //         borderColor: "#fff",
        //     },
        //     showTitle:false,
        //     right:'3%',
        //     feature: {
        //         dataView: { show: true, readOnly: false },
        //         magicType: { show: true, type: ['line', 'bar'] },
        //         restore: { show: true },
        //         saveAsImage: { show: true }
        //     }
        // },
        // title: {
        //     text: '你好不好我不好',
        //     left: 'center',
        //     top: '10%',
        //     textStyle: {
        //         color: 'white',
        //     },
        // },
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
                data: ['2018', '2019', '2020', '2021', '2022', '2023'],
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
                data: [320, 332, 301, 334, 390, 330, 320]
            },
            {
                name: '水生发电',
                type: 'bar',
                stack: 'Ad',
                emphasis: {
                    focus: 'series'
                },
                data: [120, 132, 101, 134, 90, 230, 210]
            },
            {
                name: '风生发电',
                type: 'bar',
                stack: 'Ad',
                emphasis: {
                    focus: 'series'
                },
                data: [220, 182, 191, 234, 290, 330, 310]
            },
            {
                name: '生物质能',
                type: 'bar',
                stack: 'Ad',
                emphasis: {
                    focus: 'series'
                },
                data: [150, 232, 201, 154, 190, 330, 410]
            },
            {
                name: '氢能',
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
                name: '风能',
                type: 'bar',
                barWidth: 5,
                stack: 'Search Engine',
                emphasis: {
                    focus: 'series'
                },
                data: [620, 732, 701, 734, 1090, 1130, 1120]
            },
            {
                name: '氢能源',
                type: 'bar',
                stack: 'Search Engine',
                emphasis: {
                    focus: 'series'
                },
                data: [120, 132, 101, 134, 290, 230, 220]
            },
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
        <Button class="GotoMore">安徽省再生能源产能图</Button>
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
    //z-index: 999;
  }

  //.GotoMore:hover {
  //  font-size: 1.3vw;
  //  margin-top: 4.9vh;
  //}
  //
  //.GotoMore:active {
  //  margin-top: 5vh;
  //  font-size: 1.2vw;
  //
  //}

  #SecondMiddenCenter-echarts {
    width: 40vw;
    height: 25vh;
    margin-left: -0.5vw;
    position: absolute;
    margin-top: -27.5vh;
    z-index: 200;
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
