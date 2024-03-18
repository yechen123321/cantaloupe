<script setup>
import {onMounted, ref} from "vue";
import * as echarts from "echarts";

const echartsRef = ref(null);
let myChart37 = null;
let option37 = null;

onMounted(() => {
    myChart37 = echarts.init(echartsRef.value, 'dark');
    var colorList = [
        '#5470c6', '#91cc75', '#fac858', '#ee6666', '#73c0de', '#3ba272', '#fc8452', '#9a60b4', '#546570', '#ea7ccc'
    ];
    // Your echarts option setup here...
    // (Your existing option setup code)
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