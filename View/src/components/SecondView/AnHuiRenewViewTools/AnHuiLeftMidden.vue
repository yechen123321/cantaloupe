<script setup>
import {onMounted, ref} from "vue";
import * as echarts from "echarts";
import {initKlist2} from "@/api";

const echartsRef = ref(null);
let myChart37 = null;
let option37 = null;

onMounted(async () => {
    myChart37 = echarts.init(echartsRef.value, 'dark');
    var colorList = [
        new echarts.graphic.LinearGradient(0, 0, 0, 1, [
            {offset: 0, color: '#56CCF2'},
            {offset: 1, color: '#2948ff'}
        ]),
        new echarts.graphic.LinearGradient(0, 0, 0, 1, [
            {offset: 0, color: '#DCE35B'},
            {offset: 1, color: '#45B649'}
        ]),

        new echarts.graphic.LinearGradient(0, 0, 0, 1, [
            {offset: 0, color: '#4AC29A'},
            {offset: 1, color: '#BDFFF3'}
        ]),
        new echarts.graphic.LinearGradient(0, 0, 0, 1, [
            {offset: 0, color: '#00C9FF'},
            {offset: 1, color: '#92FE9D'}
        ]),
        new echarts.graphic.LinearGradient(0, 0, 0, 1, [
            {offset: 1, color: '#C6FFDD'},
            {offset: 0, color: '#FBD786'},
        ]),
        // 其他渐变色定义...
    ];
    try {
        const data = await initKlist2(); // 使用initlandlist函数获取数据
        // 处理从initlandlist获取的数据，例如更新echarts图表
        if (data) {
            option37 = {
                backgroundColor: 'rgba(128,128,128,0)',
                color: colorList,
                tooltip: {
                    trigger: 'item',
                    textStyle: {
                        fontWeight: 'bold',
                    },
                    // formatter: '{a} <br/>{b} : {c} 吨 ({d}%)',
                    formatter: '{a} <br/>{b} : {d}%'
                },
                legend: {
                    left: 'center',
                    top: 'bottom',
                    data: [
                        '光伏',
                        '水利',
                        '风能',
                        '质能',
                        '其他',
                    ],
                    textStyle: {
                        color: 'white',
                    },
                },
                // toolbox: {
                //     show: true,
                //     feature: {
                //         mark: { show: true },
                //         dataView: { show: true, readOnly: false },
                //         restore: { show: true },
                //         saveAsImage: { show: true }
                //     }
                // },
                series: [
                    {
                        name: '地区开发',
                        type: 'pie',
                        radius: ['20%', '50%'],
                        center: ['32%', '48%'],
                        roseType: 'radius',
                        itemStyle: {
                            borderRadius: 3,
                        },
                        label: {
                            show: true,
                            fontWeight: 'bold',
                            color: 'white'
                        },
                        emphasis: {
                            label: {
                                show: true,
                                fontSize: 16,
                                color: 'white',
                                fontWeight: 'bold'
                            }
                        },
                        data: [
                            {value: 45, name: '光伏'},
                            {value: 33, name: '水利'},
                            {value: 28, name: '风能'},
                            {value: 22, name: '质能'},
                            {value: 20, name: '其他'},
                        ]
                    },

                    {
                        name: '地区消耗',
                        type: 'pie',
                        radius: ['20%', '50%'],
                        center: ['70%', '48%'],
                        roseType: 'area',
                        itemStyle: {
                            borderRadius: 5
                        },
                        label: {
                            show: true,
                            fontWeight: 'bold',
                            color: 'white'
                        },
                        data: [
                            {value: 30, name: '光伏'},
                            {value: 28, name: '水利'},
                            {value: 26, name: '风能'},
                            {value: 24, name: '质能'},
                            {value: 22, name: '其他'},
                        ],
                    }
                ]
            };
        } else {
            console.error('Failed to fetch data from initlandlist');
        }
    } catch (error) {
        console.error('Error fetching data:', error);
    }

    // Your echarts option setup here...
    // (Your existing option setup code)

    option37 && myChart37.setOption(option37);

    const resizeObserver = new ResizeObserver(() => {
        myChart37.resize();
    });

    resizeObserver.observe(echartsRef.value);
});
</script>

<template>
    <div class="AnHuiLeftMidden">
        <div class="AnHuiLeftMidden-title">安徽省再生能源结构</div>
        <div class="AnHuiLeftMidden-echarts" ref="echartsRef"></div>
    </div>
</template>

<style scoped lang="scss">
.AnHuiLeftMidden {
  width: 100%;
  height: 100%;

  .AnHuiLeftMidden-title {
    width: 23vw;
    color: white;
    font-weight: bolder;
    font-size: 1.3vw;
    text-align: center;
    position: absolute;
    //background: red;
  }

  .AnHuiLeftMidden-echarts {
    width: 27vw;
    height: 23vh;
    margin-left: -2vw;
  }
}
</style>