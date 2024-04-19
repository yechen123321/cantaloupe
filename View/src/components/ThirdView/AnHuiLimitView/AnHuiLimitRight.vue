<script setup>
// import * as echarts from "echarts";
import {initK1} from "@/api";
import {ref, reactive, onBeforeUnmount, onUnmounted, nextTick,} from 'vue'
import {initKlist} from "@/api";

let timer = ref(null);
let roll = ref(null);
let listDatas = reactive([]);

onBeforeUnmount(() => {
    clearTimeout(timer.value);
});

onUnmounted(() => {
    clearTimeout(timer.value);
});

function testMove() {
    clearTimeout(timer.value);
}

function testMend() {
    start();
}

function start() {
    clearTimeout(timer.value);
    let speed = ref(100);
    timer.value = setInterval(MarqueeTest, speed.value);
}

function MarqueeTest() {
    let test1 = roll.value;

    if (test1 && test1.offsetHeight == 0) {
        test1 = roll.value;
    } else {
        test1.scrollTop += 1;

        if (test1.scrollTop >= (test1.scrollHeight - test1.clientHeight)) {
            test1.scrollTop = 0;
        }
    }

}

initKlist().then(data => {
    listDatas.splice(0, listDatas.length, ...data.data);
    nextTick(() => {
        start();
    });
}).catch(error => {
    console.error('Failed to fetch data:', error);
});

// const echartsRef = ref(null);
// let myChart72 = null;
// let option72 = null;

// onMounted(() => {
//     myChart72 = echarts.init(echartsRef.value);
//     var colorList = [
//         new echarts.graphic.LinearGradient(0, 0, 0, 1, [
//             {offset: 0, color: '#ffc0cb'},
//             {offset: 1, color: '#de1dde'}
//         ]),
//         new echarts.graphic.LinearGradient(0, 0, 0, 1, [
//             {offset: 0, color: '#ea5fff'},
//             {offset: 1, color: '#7F00FF'}
//         ]),
//         new echarts.graphic.LinearGradient(0, 0, 0, 1, [
//             {offset: 0, color: '#FFB75E'},
//             {offset: 1, color: '#ED8F03'}
//         ]),
//         new echarts.graphic.LinearGradient(0, 0, 0, 1, [
//             {offset: 0, color: '#fc82ab'},
//             {offset: 1, color: '#d720a6'}
//         ]),
//         new echarts.graphic.LinearGradient(0, 0, 0, 1, [
//             {offset: 0, color: '#c98a08'},
//             {offset: 1, color: '#b0200f'}
//         ]),
//
//         // 其他渐变色定义...
//     ];
//     option72 = {
//         color: colorList,
//         tooltip: {
//             trigger: 'axis',
//             extraCssText: 'width: 15vw; height: 15vh;', // 设置tooltip框的宽度和高度，调整框的大小
//             formatter: function (params) {
//                 let tooltipContent = '';
//                 let mineName = params[0].name;
//                 tooltipContent += '<span style="font-weight: bold;margin-right: 1vw; margin-top: -500px;">' + mineName + '</span>' + '单位/亿吨,亿元<br>' + '<br>'; // 设置矿地名字的样式为加粗并向上移动5px
//                 params.forEach(function (param) {
//                     if (param.seriesName === '全国能耗降低率') {
//                         tooltipContent += param.marker + param.seriesName + ': ' + '<span style="float: right; font-weight: bold;">' + param.value + '%</span>' + '<br>';
//                     } else {
//                         tooltipContent += param.marker + param.seriesName + ': ' + '<span style="float: right; font-weight: bold;">' + param.value + '</span>' + '<br>';
//                     }
//                 });
//                 return tooltipContent;
//             }
//         },
//         grid: {
//             left: '5.3%', // 调整图表左边距
//             right: '7%', // 调整图表右边距
//             bottom: '15%', // 调整图表下边距
//             containLabel: true,
//         },
//         legend: {
//             itemWidth: 20, // 标签宽度为10px
//             itemHeight: 10, // 标签高度为10px
//             left: '13%',
//             top: '13%',
//             data: ['开采耗费', '获取能量', '降低率'],
//             textStyle: {
//                 color: 'white'
//             }
//         },
//         xAxis: [
//             {
//                 type: 'category',
//                 axisTick: {
//                     alignWithLabel: true
//                 }, axisLine: {
//                     lineStyle: {
//                         color: 'white',
//                     },
//                 },
//                 axisLabel: {
//                     textStyle: {
//                         color: 'white' // 设置X轴上数据的颜色为白色
//                     }
//                 },
//                 // prettier-ignore
//                 data: ['2019', '2020', '2021', '2022', '2023']
//             }
//         ],
//         yAxis: [
//             {
//                 type: 'value',
//                 name: '万亿元',
//                 position: 'right',
//                 alignTicks: true,
//                 nameTextStyle: {
//                     padding: [0, -30, 0, 0]
//                 },
//                 axisLine: {
//                     lineStyle: {
//                         color: 'white',
//                     },
//                 },
//                 axisLabel: {
//                     textStyle: {
//                         color: 'white' // 设置X轴上数据的颜色为白色
//                     }
//                 }
//             },
//             {
//                 type: 'value',
//                 name: '降低率',
//                 nameLocation: 'end', // 将名称显示在轴线末尾，即向右移动
//                 position: 'right',
//                 nameTextStyle: {
//                     padding: [0, -38, 0, 0]
//                 },
//                 alignTicks: true,
//                 offset: 40,
//                 axisLine: {
//                     lineStyle: {
//                         color: 'white',
//                     },
//                 },
//                 axisLabel: {
//                     textStyle: {
//                         color: 'white' // 设置X轴上数据的颜色为白色
//                     }
//                 }
//             },
//             {
//                 type: 'value',
//                 name: '标准煤',
//                 nameTextStyle: {
//                     padding: [0, 36, 0, 0],
//                 },
//                 alignTicks: true,
//                 axisLine: {
//                     lineStyle: {
//                         color: 'white',
//                     },
//                 },
//                 axisLabel: {
//                     textStyle: {
//                         color: 'white' // 设置X轴上数据的颜色为白色
//                     }
//                 }
//             },
//         ],
//         series: [
//             {
//                 name: '开采耗费',
//                 type: 'bar',
//                 yAxisIndex: 2,
//                 data: [
//                     35.6, 32.2, 32.6, 20.0, 36.4,
//                 ]
//             },
//             {
//                 name: '获取能量',
//                 type: 'bar',
//                 yAxisIndex: 0,
//                 data: [
//                     175.6, 182.2, 148.7, 138.8, 146.0
//                 ]
//             },
//             {
//                 name: '降低率',
//                 type: 'line',
//                 yAxisIndex: 1,
//                 data: [3.4, 2.0, 1.5, 1.0, 3.2]
//             },
//         ]
//     };
//
//     option72 && myChart72.setOption(option72);
//
//     const resizeObserver = new ResizeObserver(() => {
//         myChart72.resize();
//     });
//
//     resizeObserver.observe(echartsRef.value);
// });
const datas = ref([]);
const listData = ref({});

initK1().then(response => {
    Object.assign(listData.value, response.data);
    for (var i = 0; i < 2; i++) {
        const newData = {
            name: listData.value["name"][i],
            number: listData.value["number"][i],
            up: listData.value["up"][i],
            num: listData.value["num"][i]
        };
        datas.value.push(newData);
    }
}).catch(error => {
    console.error('Error fetching data:', error);
});
</script>

<template>
    <div class="AnHuiLimitRight">
        <div class="second">
            <img src="../../../assets/pic/midden.png" alt="" class="BackImg">
            <div class="roll">
                <div class="top">
                    <div class="name">设施</div>
                    <div class="do">工作</div>
                    <div class="number">数目</div>
                    <div class="up">单位</div>
                    <div class="when">时间</div>
                </div>
                <div class="roll-in" ref="roll">
                    <div class="roll-main" v-for="item in listDatas" :key="item.id">
                        <div @mousemove="testMove" @mouseleave="testMend" class="name">
                            <div class="name">{{ item.name }}</div>
                            <div class="do">{{ item.do }}</div>
                            <div class="number">{{ item.number }}</div>
                            <div class="up">{{ item.up }}</div>
                            <div class="when">{{ item.when }}</div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div class="first">
            <div class="title1">能源发展概览</div>
            <div class="title2">设施信息概览</div>
            <div class="AnHuiLeftTop-main">
                <div class="MainOne">
                    <img src="../../../assets/可再生能源.png" alt="" class="pic">
                    <div class="number">
                        <div class="one">4232</div>
                        <div class="up">亿万千瓦</div>
                    </div>
                    <div class="tow">再生能源总产量</div>
                </div>
                <div class="MainTow">
                    <img src="../../../assets/装机容量.png" alt="" class="pic">
                    <div class="number">
                        <div class="one" style="margin-left: 0.2vw">13.44</div>
                        <div class="up">%</div>
                    </div>
                    <div class="tow">装机容量提升率</div>
                </div>
                <div class="MainThree">
                    <img src="../../../assets/投资.png" alt="" class="pic">
                    <div class="number">
                        <div class="one">3789</div>
                        <div class="up">亿元</div>
                    </div>
                    <div class="tow">能源建设投资</div>
                </div>
                <div class="MainFour">
                    <img src="../../../assets/GenericChart.png" style="margin-top: 3vh" alt="" class="pic">
                    <div class="number">
                        <div class="one" style="margin-left: 0.3vw">1.33</div>
                        <div class="up">%</div>
                    </div>
                    <div class="tow">发展指标增长</div>
                </div>
            </div>
        </div>

        <img src="../../../assets/pic/midden.png" alt="" class="BackImg" style="margin-top: 0.3vh">
    </div>
</template>

<style scoped lang="scss">
.AnHuiLimitRight {
  width: 100%;
  height: 100%;

  .AnHuiLeftTop-main {
    position: absolute;
    width: 25vw;
    height: 18vh;
    margin-left: 2vw;
    color: white;
    margin-top: -23vh;

    .number {
      position: absolute;
      width: 8vw;
      height: 4vh;
      margin-top: 1.6vh;
      margin-left: 3vw;
      border-bottom: 2px solid #0a8cf8;

      .up {
        position: absolute;
        width: 5vw;
        margin-left: 4.2vw;
        text-align: center;
        font-size: 0.8em;
        margin-top: 1.3vh;
        font-weight: bolder;
      }

      .one {
        position: absolute;
        font-size: 1.6em;
        margin-left: -0.6vw;
        line-height: 3.7vh;
        margin-top: -0.3vh;
        font-weight: bolder;
        width: 6vw;
        text-align: center;
        height: 3.7vh;
        color: #fac800;
        text-shadow: 0 0 1px #fac800, 0 0 1px #fac800, 0 0 2px #fac800;
      }
    }

    .tow {
      position: absolute;
      margin-left: 3vw;
      margin-top: 6vh;
      width: 8vw;
      font-size: 0.95em;
      font-weight: 400;
      height: 3vh;
      text-align: center;
    }

    .pic {
      position: absolute;
      width: 2.7vw;
      height: 5vh;
      margin-top: 2.4vh;
    }

    .MainOne {
      width: 11vw;
      height: 8vh;
      position: absolute;
    }

    .MainTow {
      width: 11vw;
      height: 8vh;
      position: absolute;
      margin-left: 13vw;
    }

    .MainThree {
      width: 11vw;
      height: 8vh;
      position: absolute;
      margin-top: 9vh;
    }

    .MainFour {
      width: 11vw;
      height: 8vh;
      position: absolute;
      margin-top: 9vh;
      margin-left: 13vw;
      z-index: 999;
    }
  }

  .roll {
    color: white;
    width: 23vw;
    margin-top: 35vh;
    height: 40vh;
    margin-left: 2.5vw;

    .top {
      width: 100%;
      height: 3.5vh;
      background: rgba(255, 255, 255, .2);
      margin-top: -1vh;

      .name {
        float: left;
        margin-left: 1.3vw;
        margin-top: 0.3vh;

      }

      .do {
        float: left;
        margin-top: 0.3vh;
        margin-left: 2.3vw;
      }

      .number {
        float: left;
        margin-top: 0.3vh;
        margin-left: 1.9vw;
      }

      .up {
        float: left;
        margin-top: 0.3vh;
        margin-left: 2vw;
      }

      .when {
        float: left;
        margin-top: 0.3vh;
        margin-left: 2.7vw;
      }
    }

    .roll-in {
      width: 23vw;
      height: 20.5vh;
      overflow: hidden;
      margin-right: 2vw;
      margin-top: 1vh;

      .roll-main {
        width: 100%;
        height: 5vh;
        background: rgba(13, 135, 246, 0.1);
        margin-top: 1vh;

        .name {
          float: left;
          margin-left: 0.1vw;
          margin-top: 0.3vh;
          text-align: center;
        }

        .number {
          float: left;
          margin-top: 0.3vh;
          text-align: center;
          margin-left: 1.2vw;
          width: 4vw;
        }

        .when {
          float: left;
          margin-top: 0.3vh;
          text-align: center;
          margin-left: 1vw;
        }

        .up {
          float: left;
          width: 5vw;
          margin-top: 0.3vh;
          text-align: center;
          margin-left: -0.3vw;
          margin-right: -1.1vw;
        }

        .do {
          float: left;
          margin-top: 0.3vh;
          text-align: center;
          margin-left: 0.3vw;
          margin-right: -1.3vw;
          width: 4vw;
        }
      }
    }
  }

  .year-on-year::-webkit-scrollbar {
    display: none;
  }

  .year-on-year {
    height: 10vh;
    position: absolute;
    z-index: 10;
    width: 100%;
    margin-top: 5vh;

    li {
      list-style-type: none;
      width: 100%;
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
        color: #fc82ab;
        width: 30%;
        font-weight: bolder;
        text-shadow: 0 0 1px #fc82ab, 0 0 2px #fc82ab, 0 0 3px #fc82ab;
        font-size: 2em;
      }

      .li-up {
        float: left;
        margin-left: -1vw;
        font-size: 1em;
        margin-top: 1.3%;
        color: #ffc0cb;
        text-shadow: 0 0 1px #ffc0cb, 0 0 1px #ffc0cb, 0 0 1.5px #ffc0cb;
      }

      .li-midden {
        float: left;
        margin-left: 1vw;
        margin-top: 1.3%;
        font-size: 1em;
        color: #ffc0cb;
        text-shadow: 0 0 1px #ffc0cb, 0 0 1px #ffc0cb, 0 0 1.5px #ffc0cb;
      }

      .li-num {
        float: left;
        width: 8vw;
        text-align: center;
        font-size: 2em;
        color: #FFB75E;
        font-weight: bolder;
      }
    }
  }

  .second {
    width: 24vw;
    height: 20vh;
    position: absolute;
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
      margin-top: -26vh;
      margin-left: -3.5vw;
      text-align: center;
      font-size: 1.15em;
    }

    .title2 {
      position: absolute;
      color: white;
      font-weight: bolder;
      width: 20vw;
      margin-left: -3.5vw;
      text-align: center;
      font-size: 1.15em;
    }


  }

  .BackImg {
    width: 28vw;
    height: 40vh;
  }
}
</style>