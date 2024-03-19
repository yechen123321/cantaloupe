

<script setup>
import {onMounted, ref} from "vue";
import * as echarts from "echarts";

const echartsRef = ref(null);
let myChart48 = null;
let option48 = null;

onMounted(() => {
    myChart48 = echarts.init(echartsRef.value, 'dark');
    var colorList = [
        '#5470c6', '#91cc75', '#fac858', '#ee6666', '#73c0de', '#3ba272', '#fc8452', '#9a60b4', '#546570', '#ea7ccc'
    ];
    // Your echarts option setup here...
    // (Your existing option setup code)
    option48 ={
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
            top: '80%',
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
                radius: ['20%', '40%'],
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
                radius: ['20%', '40%'],
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
    option48 && myChart48.setOption(option48);

    const resizeObserver = new ResizeObserver(() => {
        myChart48.resize();
    });

    resizeObserver.observe(echartsRef.value);
});
</script>
<template>
    <div class="AnHuiSunLeftTop">
        <div class="title">安徽省光伏能源结构</div>
        <div class="AnHuiSunLeftTop-echarts" ref="echartsRef"></div>
    </div>

</template>

<style scoped lang="scss">
.AnHuiSunLeftTop{
  width: 100%;
  height: 100%;
  .title{
    position: absolute;
    color: white;
    font-weight: bolder;
    text-align: center;
    font-size: 1.26em;
    margin-top: 0.2vh;
    width: 24vw;
    margin-left: 1vw;
  }
  .AnHuiSunLeftTop-echarts{
    width: 25vw;
    height: 25vh;
    margin-top: -1vh;
  }
}
</style>