<script setup>
import {ref, onMounted} from 'vue';
import * as echarts from 'echarts';
import {initcdd} from '@/api'
const echartsRef = ref(null);
let myChart2 = null;
let option2 = null;

onMounted(async () => {
    myChart2 = echarts.init(echartsRef.value);

    // Your echarts option setup here...
    // (Your existing option setup code)
    var colorList = [
        new echarts.graphic.LinearGradient(0, 0, 0, 1, [
            {offset: 0, color: '#396afc'},
            {offset: 1, color: '#2948ff'}
        ]),
        new echarts.graphic.LinearGradient(0, 0, 0, 1, [
            {offset: 0, color: '#00C9FF'},
            {offset: 1, color: '#92FE9D'}
        ]),
        new echarts.graphic.LinearGradient(0, 0, 0, 1, [
            {offset: 0, color: '#bc4e9c'},
            {offset: 1, color: '#f80759'}
        ]),

        new echarts.graphic.LinearGradient(0, 0, 0, 1, [
            {offset: 0, color: '#FBD786'},
            {offset: 1, color: '#C6FFDD'}
        ]),
        new echarts.graphic.LinearGradient(0, 0, 0, 1, [
            {offset: 0, color: '#8E2DE2'},
            {offset: 1, color: '#4A00E0'}
        ]),
        // 其他渐变色定义...
        new echarts.graphic.LinearGradient(0, 0, 0, 1, [
            {offset: 0, color: '#ee9ca7'},
            {offset: 1, color: '#ffdde1'}
        ]),
    ];
    try {
        const data = await initcdd(); // 使用initlandlist函数获取数据
        // 处理从initlandlist获取的数据，例如更新echarts图表
        if (data) {
            option2 = {
                backgroundColor: 'rgba(128,128,128,0)',
                color: colorList,
                // title: {
                //     top:'-2%',
                //     text: '全国资源开发与消耗占比',
                //     // subtext: 'Fake Data',
                //     left: 'center',
                //     textStyle: {
                //         color: 'white',
                //     },
                // },
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
                        '东北',
                        '华北',
                        '华东',
                        '中南',
                        '西南',
                        '西北',
                    ],
                    textStyle: {
                        color: 'white',
                    }
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
                        center: ['28%', '48%'],
                        roseType: 'radius',
                        itemStyle: {
                            borderRadius: 3
                        },
                        label: {
                            show: true,
                            fontWeight: 'bold',
                            color: 'white'
                        },
                        emphasis: {
                            label: {
                                show: true,
                            }
                        },
                        data: data.data.data["地区开发"]
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
                            color: 'white',
                            fontWeight: 'bold',
                        },
                        data:data.data.data["地区消耗"]
                    },
                ]
            };
            option2 && myChart2.setOption(option2);
        } else {
            console.error('Failed to fetch data from initlandlist');
        }
    } catch (error) {
        console.error('Error fetching data:', error);
    }

    const resizeObserver = new ResizeObserver(() => {
        myChart2.resize();
    });

    resizeObserver.observe(echartsRef.value);
});
</script>

<template>
    <div className="MainLeftMidden">
        <div class="MainLeftMidden-title">全国能源开发与需求占比</div>
        <div id="MainLeftMidden-echarts" ref="echartsRef"></div>
    </div>
</template>

<style scoped lang="scss">
.MainLeftMidden {
  width: 100vw;
  height: 100vh;
  color: white;

  .MainLeftMidden-title {
    position: absolute;
    margin-top: -23vh;
    width: 22vw;
    font-weight: bolder;
    font-size: 1.2vw;
    text-align: center;
  }

  #MainLeftMidden-echarts {
    width: 26vw;
    height: 22vh;
    margin-left: -2vw;
    position: absolute;
    margin-top: -22.5vh;
  }

}
</style>
