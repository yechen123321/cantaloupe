<script setup>
import {onMounted, ref} from "vue";
import * as echarts from "echarts";

const echartsRef = ref(null);
let myChart39 = null;
let option39 = null;

onMounted(() => {
    myChart39 = echarts.init(echartsRef.value, 'dark');

    // Your echarts option setup here...
    // (Your existing option setup code)
    var colorList = [
        new echarts.graphic.LinearGradient(0, 0, 0, 1, [
            {offset: 0, color: '#56CCF2'},
            {offset: 1, color: '#2948ff'}
        ]),
        new echarts.graphic.LinearGradient(0, 0, 0, 1, [
            {offset: 1, color: '#00C9FF'},
            {offset: 0, color: '#92FE9D'}
        ]),
    ];
    option39 = {
        color:colorList,
        backgroundColor: 'rgba(128, 128, 128, 0)',
        legend: {
            itemWidth: 15, // 标签宽度为10px
            itemHeight: 10, // 标签高度为10px
            width: '10vw',
            left: '18%',
            data: ['全国平均', '省内总量'],
            textStyle: {
                color: 'white',
                fontWeight: 'bold',
            }
        },
        radar: {
            // shape: 'circle',
            center: ['50%', '50%'], // 调整雷达图的位置，这里设置为图表中心
            radius: '55%', // 调整雷达图的大小
            indicator: [
                {name: '光伏', max: 65000},
                {name: '水利', max: 40000},
                {name: '风力', max: 30000},
                {name: '地热', max: 38000},
                {name: '氢能', max: 52000},
                {name: '潮汐', max: 30000},
                {name: '核能', max: 30000},
                {name: '海洋', max: 30000},
            ],

            splitNumber: 4, // 分割的圈数
            axisLine: {
                show: false, // 隐藏雷达图的轴线
                lineStyle: {
                    color: 'white'
                }
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
                symbol: 'none', // 去掉每个角的小点
                data: [
                    {
                        value: [50000, 35000, 28000, 26000, 42000, 23200, 21000, 28000],
                        name: '全国平均',
                        areaStyle: {
                        },
                    },
                    {
                        value: [42000, 30000, 20000, 35000, 45000, 25000, 18000, 0],
                        name: '省内总量',
                        areaStyle: {
                        },

                    },

                ]
            }
        ]
    };
    option39 && myChart39.setOption(option39);

    const resizeObserver = new ResizeObserver(() => {
        myChart39.resize();
    });

    resizeObserver.observe(echartsRef.value);
});
</script>


<template>
    <div class="AnHuiRightDownFirst">
        <div class="AnHuiRightDownFirst-title">安徽省再生能源储量概况图</div>
        <div class="AnHuiRightDownFirst-echarts" ref="echartsRef"></div>
        <div class="AnHuiRightDownFirst-thing">
            <div class="AnHuiRightDownFirst-name">75%</div>
            <img src="../../../assets/pic/pic-4.png" alt="">
            <div class="AnHuiRightDownFirst-down">发展占比</div>
        </div>
    </div>
</template>

<style scoped lang="scss">
.AnHuiRightDownFirst {
  width: 100%;
  height: 100%;

  .AnHuiRightDownFirst-thing {
    margin-top: 25vh;

    .AnHuiRightDownFirst-down {
      color: white;
      position: absolute;
      font-weight: bolder;
      right: 0;
      margin-top: -2.7vh;
      margin-right: 2.8vw;
    }

    .AnHuiRightDownFirst-name {
      color: white;
      position: absolute;
      right: 0;
      margin-top: -17vh;
      font-size: 2vw;
      margin-right: 3vw;
      z-index: 199;

    }

    img {
      width: 8vw;
      height: 18vh;
      right: 0;
      margin-right: 0.9vw;
      margin-top: -21.5vh;
      position: absolute;
    }
  }

  .AnHuiRightDownFirst-title {
    color: white;
    //background: red;
    margin-top: -0.6vh;
    width: 21vw;
    text-align: center;
    position: absolute;
    font-weight: bolder;
    font-size: 1.26em;
  }

  .AnHuiRightDownFirst-echarts {
    width: 23vw;
    height: 25vh;
    margin-left: -5vw;
    position: absolute;
    margin-top: 3vh;
    z-index: 399;
  }

}
</style>