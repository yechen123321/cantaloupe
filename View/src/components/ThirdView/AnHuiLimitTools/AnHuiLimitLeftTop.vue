<script setup>
import {onMounted, ref} from 'vue';
import * as echarts from "echarts";

const echartsRef = ref(null);
let myChart74 = null;
let option74 = null;

onMounted(() => {
    myChart74 = echarts.init(echartsRef.value, 'dark');
    // Your echarts option setup here...
    // (Your existing option setup code)
    var colorList = [
        new echarts.graphic.LinearGradient(0, 0, 0, 1, [
            {offset: 0, color: '#fa3104'},
            {offset: 1, color: '#ff1212'},
        ]),
        new echarts.graphic.LinearGradient(0, 0, 0, 1, [
            {offset: 0, color: '#fd448c'},
            {offset: 1, color: '#fd0792'},
        ]),
        new echarts.graphic.LinearGradient(0, 0, 0, 1, [
            {offset: 0, color: '#fa7ae3'},
            {offset: 1, color: '#ff00d5'},
        ]),
        new echarts.graphic.LinearGradient(0, 0, 0, 1, [
            {offset: 0, color: '#dc90ea'},
            {offset: 1, color: '#c56ef1'},
        ]),

        new echarts.graphic.LinearGradient(0, 0, 0, 1, [
            {offset: 0, color: '#bf2adc'},
            {offset: 1, color: '#5003e3'},
        ]),
    ];
    option74 = {
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

        series: [
            {
                name: '地区开发',
                type: 'pie',
                radius: ['20%', '50%'],
                center: ['32%', '48%'],
                roseType: 'radius',
                itemStyle: {
                    borderRadius: 5,
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
                    {value: 45, name: '光伏'},
                    {value: 33, name: '水利'},
                    {value: 28, name: '风能'},
                    {value: 22, name: '质能'},
                    {value: 20, name: '其他'},
                ],
            }
        ]
    };
    option74 && myChart74.setOption(option74);

    const resizeObserver = new ResizeObserver(() => {
        myChart74.resize();
    });

    resizeObserver.observe(echartsRef.value);
});

</script>
<template>
    <div class="AnHuiLimitLeftTop">
        <div class="title">能源开发及供给结构</div>
        <div class="AnHuiLimitLeftTop-echarts" ref="echartsRef"></div>
    </div>
</template>

<style scoped lang="scss">
.AnHuiLimitLeftTop {
  width: 100%;
  height: 100%;

  .title {
    width: 24vw;
    //background: red;
    text-align: center;
    position: absolute;
    color: white;
    font-size: 1.2em;
    margin-left: 1vw;
    margin-top: -0.5vh;
    font-weight: bolder;
  }

  .AnHuiLimitLeftTop-echarts {
    width: 25.5vw;
    height: 22vh;

  }
}
</style>