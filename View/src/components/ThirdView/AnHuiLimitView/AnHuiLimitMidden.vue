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
            安庆 : [117.02, 30.31],
            蚌埠: [117.21,32.56 ],
            毫州: [115.47, 33.52],
            巢湖 : [117.52, 31.36],
            滁州: [118.18, 32.18 ],
            阜阳: [115.48,32.54 ],
            贵池: [117.28, 30.39 ],
            淮北: [116.47, 33.57 ],
            淮南: [116.58,32.37 ],
            黄山: [118.18,29.43 ],
            界首: [115.21,33.15 ],
            六安 : [116.28, 31.44 ],
            马鞍山: [118.28, 31.43 ],
            明光: [117.58, 32.47 ],
            宿州: [116.58, 33.38 ],
            天长: [118.59, 32.41 ],
            铜陵 : [117.48, 30.56 ],
            芜湖: [118.22, 31.19 ],
            宣州: [118.44, 30.57 ],
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
        <img src="../../../assets/pic/midden.png" alt="" class="BackImg">
    </div>
</template>

<style scoped lang="scss">
.AnHuiLimitMidden {
  width: 100%;
  height: 100%;

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
    height: 34vh;
    position: absolute;
    overflow: hidden;
    margin-left: 3.75vw;
    margin-top: 20.5vh;
    border-radius: 8px;

    .AnHuiLimitRight-echarts {
      position: absolute;
      width: 30vw;
      height: 50vh;
      z-index: 999;
    }
  }

  .BackImg {
    width: 47.5vw;
    height: 62vh;
  }
}
</style>