<script setup>
import {ref, onMounted} from 'vue';
import * as echarts from 'echarts';
import {initsdd} from '@/api'

const echartsRef = ref(null);
let myChart11 = null;
let option11 = null;

onMounted(async () => {
    myChart11 = echarts.init(echartsRef.value);
    var colorList = [
        new echarts.graphic.LinearGradient(0, 0, 0, 1, [
            {offset: 0, color: '#56CCF2'},
            {offset: 1, color: '#2948ff'}
        ]),
        new echarts.graphic.LinearGradient(0, 0, 0, 1, [

            {offset: 0, color: '#fc8cd9'},
            {offset: 1, color: '#f80759'}
        ]),

    ];

    try {
        const data = await initsdd(); // 使用initlandlist函数获取数据

        // 处理从initlandlist获取的数据，例如更新echarts图表
        if (data) {
            option11 = {
                color: colorList,
                backgroundColor: 'rgba(128, 128, 128, 0)',
                legend: {
                    itemWidth: 15, // 标签宽度为10px
                    itemHeight: 10, // 标签高度为10px
                    width: '10vw',
                    left: '60%',
                    top: '30vh',
                    data: ['国内总量', '世界平均'],
                    textStyle: {
                        color: 'white',
                    }
                },
                radar: {
                    // shape: 'circle',
                    center: ['50%', '50%'], // 调整雷达图的位置，这里设置为图表中心
                    radius: '55%', // 调整雷达图的大小
                    indicator: [
                        {name: '煤炭', max: 9000},
                        {name: '石油', max: 14000},
                        {name: '天然气', max: 180},
                        {name: '地热', max: 16000},
                        {name: '风能', max: 20},
                        {name: '太阳能 ', max: 50},
                    ],

                    splitNumber: 4, // 分割的圈数
                    axisLine: {
                        // show: false, // 隐藏雷达图的轴线
                        lineStyle: {
                            color: 'white',
                        },
                    },
                    splitLine: {
                        lineStyle: {
                            color: ['#B8B8B8'], // 设置分隔线的颜色
                            width: 1 // 设置分隔线的宽度
                        }
                    },
                    name: {
                        textStyle: {
                            fontWeight: 'bold',
                            color: '#fff' // 设置雷达图每一个角的文字颜色为白色
                        }
                    },
                },
                series: [
                    {
                        name: 'Budget vs spending',
                        type: 'radar',
                        // symbol: 'none', // 去掉每个角的小点
                        data: [

                            {
                                value: data.data.data["世界平均"],
                                name: '世界平均',
                                areaStyle: {},
                            },
                            {
                                value: data.data.data["国内总量"],
                                name: '国内总量',
                                areaStyle: {},
                            },
                        ]
                    }
                ]
            };
        } else {
            console.error('Failed to fetch data from initlandlist');
        }
    } catch (error) {
        console.error('Error fetching data:', error);
    }


    option11 && myChart11.setOption(option11);

    const resizeObserver = new ResizeObserver(() => {
        myChart11.resize();
    });

    resizeObserver.observe(echartsRef.value);
});
</script>


<template>
    <div className="MainDownRight">
        <button class="GotoForest">全国能源储量统计</button>
        <div id="MainDownRight-echarts" ref="echartsRef"></div>
    </div>
</template>

<style scoped lang="scss">
.MainDownRight {
  width: 100vw;
  height: 100vh;
  color: white;

  .GotoForest {
    position: absolute;
    font-size: 1.2vw;
    font-weight: bolder;
    margin-top: -22.5vh;
    border: none;
    background: none;
    color: white;
    margin-left: 9.3vw;
    z-index: 999;
    //cursor: pointer;
  }

  //.GotoForest:hover {
  //  font-size: 1.3vw;
  //  margin-left: 7.5vw;
  //  margin-top: -19.2vh;
  //}
  //
  //.GotoForest:active {
  //  font-size: 1.2vw;
  //  margin-top: -19vh;
  //  margin-left: 7.7vw;
  //}

  #MainDownRight-echarts {
    width: 26vw;
    height: 35vh;
    //margin-left: 0vw;
    position: absolute;
    margin-top: -21.5vh;
    margin-left: 1.5vw;
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
