<script setup>
import {onMounted, ref} from "vue";
import * as echarts from "echarts";
import {loadBMap} from "@/assets/map";
import "echarts/extension/bmap/bmap"
import {initK} from "@/api";

const echartsRef = ref(null);
let myChart90 = null;
let option90 = null;

onMounted(async () => {
    myChart90 = echarts.init(echartsRef.value, 'dark');

    // Your echarts option setup here...
    // (Your existing option setup code)
    try {
        const datas = await initK(); // 使用initlandlist函数获取数据
        // 处理从initlandlist获取的数据，例如更新echarts图表
        if (datas) {
            loadBMap("EGlnrCfbkZCDlamN0ap6OPQpuQhUsdmt").then(() => {
                const data = datas.data
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
                const convertDataForHeatmap = function (data) {
                    var res = [];
                    for (var i = 0; i < data.length; i++) {
                        var geoCoord = geoCoordMap[data[i].name];
                        if (geoCoord) {
                            res.push({
                                name: data[i].name,
                                value: geoCoord.concat(data[i].value)
                            });
                        }
                    }
                    return res;
                };
                option90 = {
                    backgroundColor: 'rgba(121,121,121,0)',
                    // tooltip: {
                    //     trigger: 'item',
                    //     formatter: function (params) {
                    //         return params.name + ': ' + params.data.thing; // 显示 name 和 thing
                    //     }
                    // },
                    bmap: {
                        center: [117.27, 31.70], // 合肥的经纬度坐标
                        zoom: 7,
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
                    visualMap: {
                        min: 0,
                        max: 60000,
                        show: false,
                        calculable: true,
                        inRange: {
                            color: ['yellow', 'red']
                        },
                        range: [0, 60000], // 设置热力图数值的覆盖范围，这里假设为 200000 到 4000000
                        textStyle: {
                            color: '#fff'
                        }
                    },
                    series: [
                        {
                            type: 'heatmap',
                            coordinateSystem: 'bmap',
                            data: convertDataForHeatmap(data)
                        }
                    ]
                };
                option90 && myChart90.setOption(option90);
            });
        } else {
            console.error('Failed to fetch data from initlandlist');
        }
    } catch (error) {
        console.error('Error fetching data:', error);
    }


    const resizeObserver = new ResizeObserver(() => {
        myChart90.resize();
    });

    resizeObserver.observe(echartsRef.value);

});
const downloadLocalWordDoc = () => {
    // 本地 Word 文档的文件路径
    const localDocPath = 'https://student-portrait-1314223587.cos.ap-nanjing.myqcloud.com/City.docx';

    // 创建一个链接元素并设置下载属性
    const a = document.createElement('a');
    a.href = localDocPath;
    a.download = 'local-doc.docx';
    document.body.appendChild(a);

    // 模拟点击链接进行下载
    a.click();

    // 清理链接元素
    document.body.removeChild(a);
};
const reportGenerated = ref(false);

const updateReport = () => {
    reportGenerated.value = true;
};

const showReport = () => {
    // 这里可以添加显示报告的逻辑
};
</script>

<template>
    <div class="DataAnalysisRightDown">
        <div class="title">安徽省能源发展适宜区</div>
        <button class="update" @click="updateReport" v-show="!reportGenerated">生成报告</button>
        <button class="done" @click="showReport" v-show="reportGenerated">已生成报告</button>
        <button @click="downloadLocalWordDoc" class="goto" :disabled="!reportGenerated">导出报告</button>
        <div class="echarts">
            <div class="DataAnalysisRightDown-echarts" ref="echartsRef"></div>
        </div>
        <img src="../../../assets/pic/border3.png" alt="" class="BackImg">
    </div>
</template>

<style scoped lang="scss">
.DataAnalysisRightDown {
  width: 100%;
  height: 100%;

  .all {
    position: absolute;
    background: none;
    border: none;
    right: 0;
    margin-top: 7.6vh;
    margin-right: 1vw;

    img {
      width: 2.2vw;
      height: 4vh;
    }
  }

  .all:hover {
    cursor: pointer;
  }

  .goto {
    width: 6vw;
    height: 3.5vh;
    line-height: 3vh;
    text-align: center;
    position: absolute;
    border-radius: 3px;
    margin-top: 8vh;
    margin-left: 13vw;
    font-size: 1em;
    color: white;
    background: rgb(25, 83, 206);
    border: none;
    font-weight: bolder;
  }

  .goto:disabled {
    background: #b6d4df;
    color: white;
    cursor: no-drop;
  }

  .goto:hover {
    cursor: pointer;
  }

  .done {
    width: 6vw;
    height: 3.5vh;
    line-height: 3vh;
    text-align: center;
    position: absolute;
    border-radius: 3px;
    margin-top: 8vh;
    margin-left: 5vw;
    font-size: 1em;
    color: white;
    background: rgb(25, 83, 206);
    border: none;
    font-weight: bolder;
  }

  .update {
    width: 6vw;
    height: 3.5vh;
    line-height: 3vh;
    text-align: center;
    position: absolute;
    border-radius: 3px;
    margin-top: 8vh;
    margin-left: 5vw;
    font-size: 1em;
    color: white;
    background: rgb(25, 83, 206);
    border: none;
    font-weight: bolder;
  }

  .done:hover {
    cursor: pointer;
  }

  .update:hover {
    cursor: pointer;
  }

  .echarts {
    width: 23vw;
    height: 42vh;
    position: absolute;
    margin-left: 1.5vw;
    margin-top: 13vh;
    border-radius: 20px;
    //margin-top: -51.5vh;
    overflow: hidden;

    .DataAnalysisRightDown-echarts {
      width: 23vw;
      height: 50vh;
      z-index: 999;
      position: absolute;

    }
  }

  .title {
    position: absolute;
    font-size: 1.4em;
    font-weight: bolder;
    color: white;
    margin-top: 3vh;
    width: 24vw;
    margin-left: 1vw;
    text-align: center;
  }

  .BackImg {
    width: 26vw;
    height: 58vh;
  }
}
</style>