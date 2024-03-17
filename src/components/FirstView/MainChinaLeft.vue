<script setup>
import {ref, onMounted} from 'vue';
import * as echarts from 'echarts';
// import {initlandlist} from "@/api";
const echartsRef = ref(null)
let myChart8 = null;
let option8 = null;

onMounted(async () => {

    myChart8 = echarts.init(echartsRef.value);
    // try {
    //     const data = await initlandlist(); // 使用initlandlist函数获取数据
    //     console.log(data.data);
    //
    //     // 处理从initlandlist获取的数据，例如更新echarts图表
    //     if (data) {
    //
    //         // console.log(a[1][1])
    //         option8 = {
    //
    //             tooltip: {
    //                 trigger: 'axis',[p,
    //                 extraCssText: 'width: 10vw; height: 16vh;', // 设置tooltip框的宽度和高度，调整框的大小
    //                 axisPointer: {
    //                     type: 'shadow' // 'shadow' as default; can also be 'line' or 'shadow'
    //                 },
    //                 formatter: function (params) {
    //                     let tooltipContent = '';
    //                     let mineName = params[0].name;
    //                     tooltipContent += '<span style="font-weight: bold; margin-top: -500px;">' + mineName + '</span>' + '<br>' ; // 设置矿地名字的样式为加粗并向上移动5px
    //                     params.forEach(function (param) {
    //                         if (param.seriesName !== '趋势') {
    //                             tooltipContent += param.marker + param.seriesName + ': ' + '<span style="float: right; font-weight: bold;">' + param.value + '吨</span>' + '<br>';
    //                         }
    //                     });
    //                     return tooltipContent;
    //                 }
    //             },
    //             legend: {
    //                 top:'15%',
    //                 width:'100%',
    //                 itemWidth: 10, // 标签宽度为20px
    //                 itemHeight: 10, // 标签高度为10px
    //                 left: '1%',
    //                 textStyle: {
    //                     color: 'white'
    //                 },
    //             },
    //             grid: {
    //                 top: '25%',
    //                 left: '3%',
    //                 right: '4%',
    //                 bottom: '3%',
    //                 containLabel: true
    //             },
    //             xAxis: {
    //                 type: 'value',
    //                 axisLabel: {
    //                     formatter: '{value}%'
    //                 },
    //                 axisLine: {
    //                     lineStyle: {
    //                         color: 'white',
    //                     }
    //                 }
    //             },
    //             yAxis: {
    //                 type: 'category',
    //                 data: ['2019年', '2020年', '2021年', '2022年'],
    //
    //                 axisLine: {
    //                     lineStyle: {
    //                         color: 'white',
    //                     }
    //                 }
    //             },
    //             series: [
    //                 {
    //                     name: '牧草地',
    //                     type: 'bar',
    //                     stack: 'total',
    //                     label: {
    //                         show: true,
    //                         formatter: '{c}%'
    //                     },
    //                     emphasis: {
    //                         focus: 'series'
    //                     },
    //                     data: data.data.data[1]
    //                 },
    //                 {
    //                     name: '耕地',
    //                     type: 'bar',
    //                     stack: 'total',
    //                     label: {
    //                         show: true,
    //                         formatter: '{c}%'
    //                     },
    //                     emphasis: {
    //                         focus: 'series'
    //                     },
    //                     data: data.data[1]
    //                 },
    //                 {
    //                     name: '园地',
    //                     type: 'bar',
    //                     stack: 'total',
    //                     label: {
    //                         show: true,
    //                         formatter: '{c}%'
    //                     },
    //                     emphasis: {
    //                         focus: 'series'
    //                     },
    //                     data: data.data[1]
    //                 },
    //                 {
    //                     name: '林地',
    //                     type: 'bar',
    //                     stack: 'total',
    //                     label: {
    //                         show: true,
    //                         formatter: '{c}%'
    //                     },
    //                     emphasis: {
    //                         focus: 'series'
    //                     },
    //                     data: data.data[1]
    //                 },
    //                 {
    //                     name: '其他农用地',
    //                     type: 'bar',
    //                     stack: 'total',
    //                     label: {
    //                         show: true,
    //                         // formatter: '{c}%'
    //                     },
    //                     emphasis: {
    //                         focus: 'series'
    //                     },
    //                     data: data.data[1]
    //                 }
    //             ]
    //         };
    //     } else {
    //         console.error('Failed to fetch data from initlandlist');
    //     }
    // } catch (error) {
    //     console.error('Error fetching data:', error);
    // }

    var colorList = [
        new echarts.graphic.LinearGradient(0, 0, 0, 1, [
            {offset: 0, color: '#bc4e9c'},
            {offset: 1, color: '#f80759'}
        ]),
        new echarts.graphic.LinearGradient(0, 0, 0, 1, [
            {offset: 0, color: '#2980B9'},
            {offset: 1, color: '#6DD5FA'}
        ]),
        new echarts.graphic.LinearGradient(0, 0, 0, 1, [
            {offset: 0, color: '#00C9FF'},
            {offset: 1, color: '#92FE9D'}
        ]),
        // 其他渐变色定义...
    ];
    option8 = {
        color:colorList,
        tooltip: {
            trigger: 'axis',
            // axisPointer: {
            //     type: 'cross',
            //     crossStyle: {
            //         color: '#999'
            //     }
            // }
        },
        // toolbox: {
        //     iconStyle: {
        //         borderColor: "#fff",
        //     },
        //     showTitle:false,
        //     top:'82%',
        //     // itemSize:'10',
        //     right:'3%',
        //     feature: {
        //         dataView: { show: true, readOnly: false },
        //         magicType: { show: true, type: ['line', 'bar'] },
        //         restore: { show: true },
        //         saveAsImage: { show: true }
        //     }
        // },
        // toolbox: {
        //     feature: {
        //         dataView: { show: true, readOnly: false },
        //         magicType: { show: true, type: ['line', 'bar'] },
        //         restore: { show: true },
        //         saveAsImage: { show: true }
        //     }
        // },
        legend: {
            textStyle:{
              color:'white'
            },
            top:'3%',
            data: ['产量', '存量', '产量增长率'],
            itemWidth: 20, // 标签宽度为20px
            itemHeight: 10, // 标签高度为10px
        },
        xAxis: [
            {
                type: 'category',
                data: [ '2020', '2021', '2022', '2023'],
                axisPointer: {
                    type: 'shadow'
                },
                axisLabel: {
                    textStyle: {
                        color: 'white' // 设置Y轴上数据的颜色为白色
                    }
                },
                axisLine: {
                    lineStyle: {
                        color: 'white',
                    },
                },
            }
        ],
        grid:{
            left:'15%',
            right:"13%"
        },
        yAxis: [
            {
                type: 'value',
                name: '标准煤 / 万吨',
                min: 0,
                max: 250,
                nameTextStyle: {
                    padding:[0,-10,0,0]
                },
                interval: 50,
                axisLabel: {
                    textStyle: {
                        color: 'white' // 设置Y轴上数据的颜色为白色
                    }, formatter: '{value} '

                },
                axisLine: {
                    lineStyle: {
                        color: 'white',
                    },
                },
            },
            {
                type: 'value',
                name: '百分比',
                min: 0,
                max: 25,
                nameTextStyle: {
                    padding:[0,-25,0,0]
                },
                interval: 5,
                axisLabel: {
                    textStyle: {
                        color: 'white' // 设置Y轴上数据的颜色为白色
                    }, formatter: '{value} %'

                },
                axisLine: {
                    lineStyle: {
                        color: 'white',
                    },
                },
            }
        ],
        series: [
            {
                name: '产量',
                type: 'bar',
                tooltip: {
                    valueFormatter: function (value) {
                        return value + ' ml';
                    }
                },
                data: [
                    76.7, 135.6, 162.2, 32.6,
                ]
            },
            {
                name: '存量',
                type: 'bar',
                tooltip: {
                    valueFormatter: function (value) {
                        return value + ' ml';
                    }
                },
                data: [
                   70.7, 175.6, 182.2, 48.7,
                ]
            },
            {
                name: '产量增长率',
                type: 'line',
                yAxisIndex: 1,
                tooltip: {
                    valueFormatter: function (value) {
                        return value + ' °C';
                    }
                },
                data: [20.3, 23.4, 23.0, 16.5, ]
            }
        ]
    };

    option8 && myChart8.setOption(option8);
    const resizeObserver = new ResizeObserver(() => {
        myChart8.resize();
    });

    resizeObserver.observe(echartsRef.value);
});
</script>

<template>
    <div className="MainChinaLeft">
        <img class="BackImg" src="../../assets/pic/border3.png" alt="">
        <Button class="GotoGrounds">全国能源产量及库存</Button>
        <div id="MainChinaLeft-echarts" ref="echartsRef"></div>
    </div>
</template>

<style scoped lang="scss">
.MainChinaLeft {
  width: 100vw;
  height: 100vh;
  color: white;

  .GotoGrounds {
    position: absolute;
    margin-top: -38.5vh;
    width: 19vw;
    margin-left: 0.6vw;
    border: none;
    background: none;
    color: white;
    font-weight: bolder;
    //cursor: pointer;
    font-size: 1.2vw;
    z-index: 999;
  }

  //.GotoGrounds:hover {
  //  font-size: 1.3vw;
  //  margin-top: -32.3vh;
  //}
  //
  //.GotoGrounds:active {
  //  margin-top: -32vh;
  //  font-size: 1.2vw;
  //}

  #MainChinaLeft-echarts {
    width: 19vw;
    height: 39vh;
    margin-left: 0.2vw;
    position: absolute;
    margin-top: -36vh;
  }

  .BackImg {
    width: 20.2vw;
    height: 40vh;
    margin-top: -20vh;
  }

}
</style>
