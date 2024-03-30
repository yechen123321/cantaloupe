<script setup>
import {ref, onMounted} from "vue";
import * as echarts from "echarts";

const datas = ref([
    {name: '碳排放增率', number: -2.6, up: '%'},
    {name: '能源增产率', number: 3.2, up: '%'},
]);

const echartsRef = ref(null);
let myChart89 = null;
let option89 = null;
onMounted(() => {
    myChart89 = echarts.init(echartsRef.value, 'dark');
    // Your echarts option setup here...
    // (Your existing option setup code)
    var colorList = [
        // new echarts.graphic.LinearGradient(0, 0, 0, 1, [
        //     {offset: 0, color: '#bc4e9c'},
        //     {offset: 1, color: '#f80759'}
        // ]),
        new echarts.graphic.LinearGradient(0, 0, 0, 1, [
            {offset: 0, color: '#396afc'},
            {offset: 1, color: '#2948ff'}
        ]),
        new echarts.graphic.LinearGradient(0, 0, 0, 1, [
            {offset: 0, color: '#00C9FF'},
            {offset: 1, color: '#92FE9D'}
        ]),
        // 其他渐变色定义...
    ];
    option89 = {
        color: colorList,
        backgroundColor: 'rgba(128, 128, 128, 0)',
        legend: {
            itemWidth: 15, // 标签宽度为10px
            itemHeight: 10, // 标签高度为10px
            width: '10vw',
            left: '25%',
            top: '8%',
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
                {name: '产能', max: 65000},
                {name: '碳排放', max: 40000},
                {name: '清洁比重', max: 30000},
                {name: '能耗', max: 38000},
                {name: '采集效率', max: 52000},
                {name: '建设投资', max: 30000},
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
                            color: colorList[0]
                        },
                    },
                    {
                        value: [42000, 30000, 20000, 35000, 45000, 25000, 18000, 0],
                        name: '省内总量',
                        areaStyle: {
                            color: colorList[1]
                        },

                    },

                ]
            }
        ]
    };
    option89 && myChart89.setOption(option89);

    const resizeObserver = new ResizeObserver(() => {
        myChart89.resize();
    });

    resizeObserver.observe(echartsRef.value);
});
</script>

<template>
    <div class="DataAnalysisMiddenTopRight">
        <ul>
            <li v-for="(item,index) in datas" :class="{ 'li-active': index === 0 }" :key="index">
                <div class="name">{{ item.name }}：</div>
                <div class="thing">{{ item.number }}</div>
                <div class="up">{{ item.up }}</div>
            </li>
        </ul>
        <div class="title">安徽能源发展指标</div>
        <div class="DataAnalysisMiddenTopRight-echarts" ref="echartsRef"></div>
    </div>
</template>

<style scoped>
.DataAnalysisMiddenTopRight {
    width: 100%;
    height: 100%;

    .title {
        color: white;
        font-weight: bolder;
        font-size: 1.3em;
        position: absolute;
        margin-top: 10.5vh;
        width: 16vw;
        text-align: center;
    }

    .DataAnalysisMiddenTopRight-echarts {
        width: 30vw;
        height: 30vh;
        position: absolute;
        margin-top: 13vh;
        margin-left: -7vw;
        z-index: 300;
    }

    ul {
        width: 13.5vw;
        height: 15vh;
        margin-top: -1vh;
        position: absolute;
        color: white;
        font-weight: bolder;

        li {
            width: 15vw;
            margin-left: -2vw;
            height: 6vh;
            list-style: none;

            .name {
                position: absolute;
                font-size: 1.4em;
                color: #83fcf3;
                text-shadow: 0 0 1px #5bfff4, 0 0 2px #69e8df;
            }

            .thing {
                position: absolute;
                margin-top: -0.4vh;
                font-size: 1.8em;
                right: 0;
                margin-right: 2.8vw;
            //margin-left: 9vw; color: yellow;
            }

            .up {
                position: absolute;
                margin-top: 0.4vh;
                font-size: 1.4em;
                margin-left: 13.5vw;
                color: yellow;
            }
        }
    }
}
</style>