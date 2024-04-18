<script setup>
import {onMounted, ref} from "vue";
import * as echarts from "echarts";

const echartsRef = ref(null);
let myChart55 = null;
let option55 = null;

onMounted(() => {
    myChart55 = echarts.init(echartsRef.value, 'dark');
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
    // Your echarts option setup here...
    // (Your existing option setup code)
    option55 ={
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
                center: ['29%', '48%'],
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
                center: ['68%', '48%'],
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
    option55 && myChart55.setOption(option55);

    const resizeObserver = new ResizeObserver(() => {
        myChart55.resize();
    });

    resizeObserver.observe(echartsRef.value);
});
</script>

<template>
    <div class="AnHuiWaterLeftCenter">
        <div class="title">安徽省水利能源结构</div>
        <div class="AnHuiWaterLeftCenter-echarts" ref="echartsRef"></div>
    </div>
</template>

<style scoped lang="scss">
.AnHuiWaterLeftCenter{
  width: 100%;
  height: 100%;
  .title{
    position: absolute;
    color: white;
    font-weight: bolder;
    text-align: center;
    font-size: 1.15em;
    margin-top: -2vh;
    width: 24vw;
    margin-left: 1vw;
  }
  .AnHuiWaterLeftCenter-echarts{
    width: 27vw;
    height: 27vh;
    margin-top: -3vh;
  }
}
</style>