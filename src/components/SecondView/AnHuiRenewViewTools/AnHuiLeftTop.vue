<script setup>
import {onMounted, ref} from "vue";
import * as echarts from "echarts";

const echartsRef = ref(null);
let myChart38 = null;
let option38 = null;

onMounted(() => {
    myChart38 = echarts.init(echartsRef.value, 'dark');
    var colorList = [
        '#5470c6', '#91cc75', '#fac858', '#ee6666', '#73c0de', '#3ba272', '#fc8452', '#9a60b4', '#546570', '#ea7ccc'
    ];
    // Your echarts option setup here...
    // (Your existing option setup code)
    option38 ={
        backgroundColor:'rgba(128,128,128,0)',
        color: colorList,
        tooltip: {
            trigger: 'item',
            textStyle:{
                fontWeight:'bold',
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
                center: ['33%', '48%'],
                roseType: 'radius',
                itemStyle: {
                    borderRadius: 3,
                },
                label: {
                    show: true,
                    fontWeight: 'bold',
                    color:'white'
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
                    {value: 40, name: '光伏'},
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
                center: ['72%', '48%'],
                roseType: 'area',
                itemStyle: {
                    borderRadius: 5
                },
                label: {
                    show: true,
                    fontWeight: 'bold',
                    color:'white'
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
    option38 && myChart38.setOption(option38);

    const resizeObserver = new ResizeObserver(() => {
        myChart38.resize();
    });

    resizeObserver.observe(echartsRef.value);
});
</script>

<template>
  <div class="AnHuiLeftTop">
      <div class="AnHuiLeftTop-title">安徽省再生能源结构</div>
    <div class="AnHuiLeftTop-echarts" ref="echartsRef"></div>
  </div>
</template>

<style scoped lang="scss">
  .AnHuiLeftTop{
    width: 100%;
    height: 100%;
    color:white;
    .AnHuiLeftTop-title{
      position: absolute;
      color: white;
      margin-top: -0.3vh;
      text-align: center;
      //background: red;
      width: 23vw;
      margin-left: 3.5vw;
      font-weight: bolder;
      font-size: 1.3vw;
    }
    .AnHuiLeftTop-echarts{
      width: 29vw;
      height: 22vh;
    }
  }
</style>