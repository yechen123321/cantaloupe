<script setup>
import {onMounted, ref} from "vue";
import * as echarts from "echarts";

const echartsRef = ref(null);
let myChart49 = null;
let option49 = null;

onMounted(() => {
    myChart49 = echarts.init(echartsRef.value, 'dark');

    // Your echarts option setup here...
    // (Your existing option setup code)
    option49 = {
        color: ['#73C0DE', '#FAC858'],
        backgroundColor: 'rgba(128, 128, 128, 0)',
        legend: {
            itemWidth: 15, // 标签宽度为10px
            itemHeight: 10, // 标签高度为10px
            width: '10vw',
            top:'-1%',
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
                {name: '效率', max: 65000},
                {name: '产能', max: 40000},
                {name: '储能', max: 30000},
                {name: '稳定', max: 38000},
                {name: '效益', max: 50000},
                {name: '容量', max: 32000},
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
                            color: '#73C0DE' // 粉红色，与深蓝色相呼应
                        },
                    },
                    {
                        value: [42000, 30000, 20000, 35000, 45000, 25000, 18000, 0],
                        name: '省内总量',
                        areaStyle: {
                            color: '#FAC858' // 橙色，与深蓝色相呼应
                        },

                    },

                ]
            }
        ]
    };
    option49 && myChart49.setOption(option49);

    const resizeObserver = new ResizeObserver(() => {
        myChart49.resize();
    });

    resizeObserver.observe(echartsRef.value);
});
</script>


<template>
    <div class="AnHuiSunLeftCenter">
        <div class="AnHuiSunLeftCenter-title">安徽省光伏能源发展概况图</div>
        <div class="AnHuiSunLeftCenter-echarts" ref="echartsRef"></div>
        <div class="AnHuiSunLeftCenter-thing">
            <div class="AnHuiSunLeftCenter-name">75%</div>
            <img src="../../../assets/pic/pic-4.png" alt="">
            <div class="AnHuiSunLeftCenter-down">发展占比</div>
        </div>
    </div>
</template>

<style scoped lang="scss">
.AnHuiSunLeftCenter {
    width: 100%;
    height: 100%;

    .AnHuiSunLeftCenter-thing {
        margin-top: 25vh;
        .AnHuiSunLeftCenter-down {
            color: white;
            position: absolute;
            font-weight: bolder;
            right: 0;
            margin-top: -2.7vh;
            margin-right: 4.1vw;
        }

        .AnHuiSunLeftCenter-name {
            color: white;
            position: absolute;
            right: 0;
            margin-top: -17vh;
            font-size: 2vw;
            margin-right: 4.1vw;
            z-index: 199;

        }

        img {
            width: 8vw;
            height: 18vh;
            right: 0;
            margin-right: 2.2vw;
            margin-top: -21.5vh;
            position: absolute;
        }
    }

    .AnHuiSunLeftCenter-title {
        color: white;
        //background: red;
        margin-top: -0.6vh;
        width: 24vw;
        margin-left: 1vw;
        text-align: center;
        position: absolute;
        font-weight: bolder;
        font-size: 1.26em;
    }

    .AnHuiSunLeftCenter-echarts {
        width: 23vw;
        height: 23vh;
        margin-left: -2vw;
        position: absolute;
        margin-top: 4vh;
        z-index: 399;
    }

}
</style>