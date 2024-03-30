<script setup>
import {onMounted, ref} from "vue";
import * as echarts from "echarts";

const echartsRef = ref(null);
let myChart48 = null;
let option48 = null;

onMounted(() => {
    myChart48 = echarts.init(echartsRef.value, 'dark');
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
            left: '4%',
            itemWidth: 20, // 标签宽度为10px
            itemHeight: 10, // 标签高度为10px
            top: '80%',
            width:'120%',
            data: [
                '合肥',
                '芜湖',
                '马鞍山',
                '淮南',
                '蚌埠',
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
                    {value: 45, name: '合肥'},
                    {value: 33, name: '芜湖'},
                    {value: 28, name: '马鞍山'},
                    {value: 22, name: '淮南'},
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
                    {value: 30, name: '合肥'},
                    {value: 28, name: '芜湖'},
                    {value: 26, name: '马鞍山'},
                    {value: 24, name: '蚌埠'},
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