<script setup>
import {onMounted, ref} from 'vue';
import * as echarts from "echarts";

const echartsRef = ref(null);
let myChart75 = null;
let option75 = null;

onMounted(() => {
    myChart75 = echarts.init(echartsRef.value, 'dark');
    // Your echarts option setup here...
    // (Your existing option setup code)
    var colorList = [
        new echarts.graphic.LinearGradient(0, 0, 0, 1, [
            {offset: 0, color: '#dc90ea'},
            {offset: 1, color: '#763aee'},
        ]),
        new echarts.graphic.LinearGradient(0, 0, 0, 1, [
            {offset: 0, color: '#ef98d0'},
            {offset: 1, color: '#fd0792'},
        ]),
    ];
    option75 = {
        color: colorList,
        backgroundColor: 'rgba(128, 128, 128, 0)',
        legend: {
            itemWidth: 15, // 标签宽度为10px
            itemHeight: 10, // 标签高度为10px
            width: '10vw',
            left: '18%',
            top: '-2%',
            data: ['全国平均', '省内总量'],
            textStyle: {
                color: 'white',
                fontWeight: 'bold',
            }
        },
        radar: {
            // shape: 'circle',
            center: ['44%', '42%'], // 调整雷达图的位置，这里设置为图表中心
            radius: '55%', // 调整雷达图的大小
            indicator: [
                {name: '效率', max: 65000},
                {name: '产能', max: 40000},
                {name: '储能', max: 30000},
                {name: '容量', max: 38000},
                {name: '效益', max: 52000},
                {name: '稳定', max: 30000},
            ],

            splitNumber: 4, // 分割的圈数
            axisLine: {
                // show: false, // 隐藏雷达图的轴线
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
                // symbol: 'none', // 去掉每个角的小点
                data: [
                    {
                        value: [50000, 35000, 28000, 26000, 42000, 23200, ],
                        name: '全国平均',
                        areaStyle: {
                            color: colorList[0] // 粉红色，与深蓝色相呼应
                        },
                    },
                    {
                        value: [42000, 30000, 20000, 35000, 45000, 0, ],
                        name: '省内总量',
                        areaStyle: {
                            color: colorList[1] // 橙色，与深蓝色相呼应
                        },
                    },
                ]
            }
        ]
    };
    option75 && myChart75.setOption(option75);

    const resizeObserver = new ResizeObserver(() => {
        myChart75.resize();
    });

    resizeObserver.observe(echartsRef.value);
});

</script>
<template>
    <div class="AnHuiLimitLeftDown">
        <div class="title">安徽省有限能源发展概况图</div>
        <div class="AnHuiLimitLeftDown-echarts" ref="echartsRef"></div>
        <div class="AnHuiLimitLeftDown-thing">
            <div class="AnHuiLimitLeftDown-name">75%</div>
            <img src="../../../assets/pic/pic-4.png" alt="">
            <div class="AnHuiLimitLeftDown-down">发展指标</div>
        </div>
    </div>
</template>

<style scoped lang="scss">
.AnHuiLimitLeftDown {
  width: 100%;
  height: 100%;

  .AnHuiLimitLeftDown-thing {
    margin-top: -6vh;
    margin-right: -1vw;
    position: absolute;
    right: 0;

    .AnHuiLimitLeftDown-down {
      color: white;
      position: absolute;
      font-weight: bolder;
      width: 6vw;
      right: 0;
      margin-top: -2.7vh;
      margin-right: 1vw;
    }

    .AnHuiLimitLeftDown-name {
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

  .title {
    width: 24vw;
    //background: red;
    text-align: center;
    position: absolute;
    color: white;
    font-size: 1.15em;
    margin-left: 1vw;
    font-weight: bolder;
  }

  .AnHuiLimitLeftDown-echarts {
    width: 28vw;
    height: 28vh;
    margin-top: 4vh;
    margin-left: -3vw;
  }
}
</style>