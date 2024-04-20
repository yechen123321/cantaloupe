<script setup>
import {onMounted, ref} from "vue";
import * as echarts from "echarts";
import {loadBMap} from "@/assets/map";
import "echarts/extension/bmap/bmap"
import router from "@/router";

const echartsRef = ref(null);
let myChart71 = null;
let option71 = null;

onMounted(() => {
    myChart71 = echarts.init(echartsRef.value, 'dark');
    myChart71.on('click', function (params) {
        if (params.componentType === 'series') {
            if (params.seriesType === 'scatter') {
                // 判断点击的是散点图
                if (params.data && params.data.value) {
                    // 获取点击的数据
                    // 在这里可以根据需要处理点击事件，比如获取数据信息，然后跳转到另一个页面
                    // 这里只是简单的示例，实际情况根据您的需求进行相应处理
                    // window.location.href = 'https://www.4399.com'
                    router.push('/thermalpower');
                }
            }
        }
    });
    loadBMap("EGlnrCfbkZCDlamN0ap6OPQpuQhUsdmt").then(() => {
        const data = [
            {name: '合肥', value: 200, thing: '一号火电厂'},
            {name: '马鞍山', value: 100, thing: '二号火电厂'},
        ];
        const geoCoordMap = {
            合肥: [117.17, 31.52],
            安庆: [117.02, 30.31],
            蚌埠: [117.21, 32.56],
            毫州: [115.47, 33.52],
            巢湖: [117.52, 31.36],
            滁州: [118.18, 32.18],
            阜阳: [115.48, 32.54],
            贵池: [117.28, 30.39],
            淮北: [116.47, 33.57],
            淮南: [116.58, 32.37],
            黄山: [118.18, 29.43],
            界首: [115.21, 33.15],
            六安: [116.28, 31.44],
            马鞍山: [118.28, 31.43],
            明光: [117.58, 32.47],
            宿州: [116.58, 33.38],
            天长: [118.59, 32.41],
            铜陵: [117.48, 30.56],
            芜湖: [118.22, 31.19],
            宣州: [118.44, 30.57],
        };
        const convertData = function (data) {
            var res = [];
            for (var i = 0; i < data.length; i++) {
                var geoCoord = geoCoordMap[data[i].name];
                if (geoCoord) {
                    res.push({
                        name: data[i].name,
                        value: geoCoord.concat(data[i].value),
                        thing: data[i].thing // 添加 thing 属性
                    });
                }
            }
            return res;
        };
        option71 = {
            backgroundColor: 'rgba(121,121,121,0)',
            tooltip: {
                trigger: 'item',
                formatter: function (params) {
                    return params.name + ': ' + params.data.thing; // 显示 name 和 thing
                }
            },
            bmap: {
                center: [117.7, 31.30], // 合肥的经纬度坐标
                zoom: 9,
                roam: true,
                mapStyle: {
                    styleJson: [
                        {
                            featureType: 'water',
                            elementType: 'all',
                            stylers: {
                                color: '#044161'
                            }
                        },
                        {
                            featureType: 'land',
                            elementType: 'all',
                            stylers: {
                                color: '#004981'
                            }
                        },
                        {
                            featureType: 'boundary',
                            elementType: 'geometry',
                            stylers: {
                                color: '#064f85'
                            }
                        },
                        {
                            featureType: 'railway',
                            elementType: 'all',
                            stylers: {
                                visibility: 'off'
                            }
                        },
                        {
                            featureType: 'highway',
                            elementType: 'geometry',
                            stylers: {
                                color: '#004981'
                            }
                        },
                        {
                            featureType: 'highway',
                            elementType: 'geometry.fill',
                            stylers: {
                                color: '#005b96',
                                lightness: 1
                            }
                        },
                        {
                            featureType: 'highway',
                            elementType: 'labels',
                            stylers: {
                                visibility: 'off'
                            }
                        },
                        {
                            featureType: 'arterial',
                            elementType: 'geometry',
                            stylers: {
                                color: '#004981'
                            }
                        },
                        {
                            featureType: 'arterial',
                            elementType: 'geometry.fill',
                            stylers: {
                                color: '#00508b'
                            }
                        },
                        {
                            featureType: 'poi',
                            elementType: 'all',
                            stylers: {
                                visibility: 'off'
                            }
                        },
                        {
                            featureType: 'green',
                            elementType: 'all',
                            stylers: {
                                color: '#056197',
                                visibility: 'off'
                            }
                        },
                        {
                            featureType: 'subway',
                            elementType: 'all',
                            stylers: {
                                visibility: 'off'
                            }
                        },
                        {
                            featureType: 'manmade',
                            elementType: 'all',
                            stylers: {
                                visibility: 'off'
                            }
                        },
                        {
                            featureType: 'local',
                            elementType: 'all',
                            stylers: {
                                visibility: 'off'
                            }
                        },
                        {
                            featureType: 'arterial',
                            elementType: 'labels',
                            stylers: {
                                visibility: 'off'
                            }
                        },
                        {
                            featureType: 'boundary',
                            elementType: 'geometry.fill',
                            stylers: {
                                color: '#029fd4'
                            }
                        },
                        {
                            featureType: 'building',
                            elementType: 'all',
                            stylers: {
                                color: '#1a5787'
                            }
                        },
                        {
                            featureType: 'label',
                            elementType: 'all',
                            stylers: {
                                visibility: 'off'
                            }
                        }
                    ]
                }
            },
            series: [
                {
                    name: 'pm2.5',
                    type: 'scatter',
                    coordinateSystem: 'bmap',
                    data: convertData(
                        data
                            .sort(function (a, b) {
                                return b.value - a.value;
                            })
                            .slice(0, 6)
                    ),
                    // symbolSize: function (val) {
                    //     return val[2] / 10;
                    // },
                    encode: {
                        value: 2
                    },

                    label: {
                        show: true, // 显示label
                        textStyle: {
                            color: 'white'
                        },
                        formatter: function (params) {
                            return params.data.name; // 显示地名
                        },
                        position: 'right'
                    },
                    itemStyle: {
                        normal: {
                            color: 'transparent'
                        },
                        emphasis: {
                            color: 'transparent'
                        }
                    },
                    symbol: 'image://' + require('../../../assets/火电.png'), // 使用 require 加载图片
                    symbolSize: 65, // 设置图片大小
                    emphasis: {
                        label: {
                            show: true
                        }
                    }
                }
            ],

        };
        option71 && myChart71.setOption(option71);
    });
    const resizeObserver = new ResizeObserver(() => {
        myChart71.resize();
    });

    resizeObserver.observe(echartsRef.value);
});
</script>

<template>
    <div class="AnHuiLimitMidden">
        <div class="title">安徽省火电基地分布</div>
        <div class="echarts">
            <div class="AnHuiLimitRight-echarts" ref="echartsRef"></div>
        </div>
        <div class="top">
            <div class="topOne">
                <div class="topHead">当前统计基地数</div>
                <div class="topMain">1276</div>
                <div class="up">座</div>
            </div>
            <div class="topTow">
                <div class="topHead">发电装机总容量</div>
                <div class="topMain" style="margin-left: -2.4vw">3245</div>
                <div class="up">万千瓦</div>
            </div>
            <div class="topFour">
                <div class="oneOne">
                    <div class="topTitle">在线</div>
                    <div class="topNumber">1232</div>
                </div>
                <div class="towTow">
                    <div class="topTitle">离线</div>
                    <div class="topNumber">32</div>
                </div>
                <div class="threeThree">
                    <div class="topTitle">停运</div>
                    <div class="topNumber">12</div>
                </div>
            </div>
        </div>
        <div class="right">
            <div class="right-one">
                <div class="oneTop">月平均发电量</div>
                <div class="oneCenter">
                    <div class="centerLeft">234</div>
                    <div class="centerRight">万千瓦</div>
                </div>
                <div class="oneDown">
                    <div class="num">2.34%</div>
                    <img src="../../../assets/上升.png" alt="" class="Out">
                </div>
            </div>
            <div class="right-tow">
                <div class="oneTop">月平均损耗标准煤</div>
                <div class="oneCenter">
                    <div class="centerLeft">34</div>
                    <div class="centerRight">万吨</div>
                </div>
                <div class="oneDown">
                    <div class="num">4.5%</div>
                    <img src="../../../assets/下降.png" alt="" class="Out">
                </div>
            </div>
        </div>
        <img src="../../../assets/pic/midden.png" alt="" class="BackImg">
    </div>
</template>

<style scoped lang="scss">
.AnHuiLimitMidden {
  width: 100%;
  height: 100%;

  .right {
    width: 10vw;
    height: 34vh;
    position: absolute;
    margin-left: 34.2vw;
    margin-top: 22.5vh;
    color: white;
    font-weight: bolder;

    .num {
      width: 5.5vw;
      text-align: center;
      margin-left: 1vw;
      margin-top: -0.5vh;
    }

    .Out {
      width: 2vw;
      position: absolute;
      margin-left: 6.5vw;
      margin-top: -3.5vh;
    }

    .oneTop {
      width: 10vw;
      height: 4.5vh;
      position: absolute;
      margin-top: 1.2vh;
      color: #00bfff;
      text-shadow: 0 0 0.5px #00bfff, 0 0 1px #00bfff, 0 0 1px #00bfff;
    }

    .oneCenter {
      width: 10vw;
      height: 6vh;
      position: absolute;
      margin-top: 4.5vh;
      line-height: 6vh;
      border-top: 2px solid #0a8cf8;
      border-bottom: 2px solid #0a8cf8;
      text-align: center;

      .centerLeft {
        width: 6vw;
        position: absolute;
        height: 7vh;
        color: #fac800;
        text-shadow: 0 0 1px #fac800, 0 0 1px #fac800, 0 0 2px #fac800;
        font-size: 1.8em;
      }

      .centerRight {
        position: absolute;
        width: 4vw;
        height: 7vh;
        right: 0;
        margin-top: 0.6vh;
      }
    }

    .oneDown {
      width: 10vw;
      height: 4.5vh;
      position: absolute;
      margin-top: 11.5vh;
      font-size: 1.3em;

    }

    .right-one {
      width: 10vw;
      height: 16vh;
      position: absolute;
      margin-top: 0.7vh;
    }

    .right-tow {
      width: 10vw;
      height: 16vh;
      position: absolute;
      margin-top: 16vh;
    }
  }

  .top {
    position: absolute;
    width: 42vw;
    height: 10vh;
    margin-top: 11vh;
    margin-left: 3vw;

    div {
      float: left;
    }

    .up {
      width: 5vw;
      height: 5vh;
      position: absolute;
      color: #00bfff;
      text-shadow: 0 0 0.5px #00bfff, 0 0 1px #00bfff, 0 0 1px #00bfff;
      margin-left: 5vw;
      margin-top: 4.8vh;
      font-size: 1.3em;
    }

    .topHead {
      width: 10vw;
      height: 4vh;
      color: #d851f3;
      text-shadow: 0 0 0.5px #d851f3, 0 0 0.5px #d851f3, 0 0 0.5px #d851f3;
      font-size: 1.2em;
    }

    .topMain {
      width: 10vw;
      height: 6vh;
      color: #00bfff;
      text-shadow: 0 0 0.5px #00bfff, 0 0 1px #00bfff, 0 0 1px #00bfff;
      margin-left: -1vw;
      font-size: 1.8em;
    }

    .topOne {
      width: 10vw;
      height: 10vh;
      margin-left: 1vw;
      margin-top: 1vh;
      text-align: center;
      color: #fff;
      font-weight: bolder;
    }

    .topTow {
      width: 10vw;
      height: 10vh;
      margin-top: 1vh;
      margin-left: 2.5vw;

      text-align: center;
      color: #fff;
      font-weight: bolder;
    }

    .topFour {
      width: 14vw;
      height: 11.5vh;
      margin-top: -1.5vh;
      border-radius: 5px;
      margin-left: 3vw;
      font-weight: bolder;
      border: 1px solid #0a8cf8;
      background: rgb(7, 22, 33, .7);

      .topNumber {
        width: 4.6vw;
        text-align: center;
        font-size: 1.3em;
        margin-top: 2vh;
      }

      .topTitle {
        text-align: center;
        width: 4.6vw;
      }

      .oneOne {
        width: 4.8vw;
        height: 9vh;
        margin-top: 1.2vh;
        position: absolute;
        color: white;
        border-right: 2px solid #0a8cf8;
      }

      .towTow {
        width: 4.6vw;
        height: 9vh;
        margin-top: 1.2vh;
        margin-left: 4.8vw;
        position: absolute;
        color: #0a8cf8;
        border-right: 2px solid #0a8cf8;
      }

      .threeThree {
        width: 4.6vw;
        height: 9vh;
        margin-top: 1.2vh;
        margin-left: 9.4vw;
        position: absolute;
        color: #ff2d00;
        text-shadow: 0 0 1px #ff2d00;
      }
    }
  }

  .title {
    width: 20vw;
    color: white;
    font-weight: bolder;
    font-size: 1.3em;
    position: absolute;
    margin-top: 7vh;
    margin-left: 5vw;
  }

  .echarts {
    width: 30vw;
    height: 32vh;
    position: absolute;
    overflow: hidden;
    margin-left: 3.75vw;
    margin-top: 22.5vh;
    border-radius: 8px;

    .AnHuiLimitRight-echarts {
      position: absolute;
      width: 30vw;
      height: 48vh;
      z-index: 999;
    }
  }

  .BackImg {
    width: 47.5vw;
    height: 62vh;
  }
}
</style>