<script setup>
import * as echarts from 'echarts';
import {onMounted} from "vue";

onMounted(() => {
    var chartDom2 = document.getElementById('echarts1');
    var myChart2 = echarts.init(chartDom2);
    var option2;
    var colorList = [
        '#5470c6', '#91cc75', '#fac858', '#ee6666', '#73c0de', '#3ba272', '#fc8452', '#9a60b4', '#546570', '#ea7ccc'
    ];
    option2 = {
        color: colorList,
        title: {
            text: '全国资源开发与消耗占比',
            // subtext: 'Fake Data',
            left: 'center',
            textStyle: {
                color: 'white',
            },
        },
        tooltip: {
            trigger: 'item',
            formatter: '{a} <br/>{b} : {c} ({d}%)'
        },
        legend: {
            left: 'center',
            top: 'bottom',
            data: [
                '东部',
                '西部',
                '北部',
                '南部',
                '中部',
            ],
            textStyle:{
                color:'white',
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
                name: 'Radius Mode',
                type: 'pie',
                radius: [20, 40],
                center: ['30%', '48%'],
                roseType: 'radius',
                itemStyle: {
                    borderRadius: 5
                },
                emphasis: {
                    label: {
                        show: true,
                    }
                },
                data: [
                    { value: 40, name: '北部' },
                    { value: 33, name: '东部' },
                    { value: 28, name: '西部' },
                    { value: 22, name: '南部' },
                    { value: 20, name: '中部' },
                ]
            },

            {
                name: '地区占比',
                type: 'pie',
                radius: [20, 40],
                center: ['75%', '48%'],
                roseType: 'area',
                itemStyle: {
                    borderRadius: 5
                },
                data: [
                    { value: 30, name: '北部' },
                    { value: 28, name: '南部' },
                    { value: 26, name: '中部' },
                    { value: 24, name: '东部' },
                    { value: 22, name: '西部' },
                ]
            }
        ]
    };

    option2 && myChart2.setOption(option2);
},)

</script>



<template>
    <div class="ThirdMainTable">
        <img class="BackImg" src="../../assets/pic/k_3.png" alt="">
        <div id="echarts1"></div>
    </div>
</template>

<style scoped lang="scss">
.ThirdMainTable {
    width: 100vw;
    height: 100vh;
    border-image: linear-gradient(to right, #00bfff, #0d0d0d, #00bfff) 30 30;
    border-radius: 0.5vw;
    box-shadow: 0px 0px 1vw 1vw #00bfff, 0px 0px 2vw 1vw #0d0d0d, 0px 0px 3vw 2vw #00bfff;
    animation: glow 1s ease-in-out infinite alternate;
    color: white;
    .BackImg {
        width: 23vw;
        height: 22vh;
    }
    #echarts1 {
        width: 23vw;
        height:20vh;
        margin-left: -0.5vw;
        //background: red;
        position: absolute;
        margin-top: -21.5vh;
    }
    @keyframes glow {

        from {
            box-shadow: 0px 0px 3px 3px #00bfff, 0px 0px 5px 3px #0d0d0d, 0px 0px 7px 5px #00bfff;
        }

        to {
            box-shadow: 0px 0px 5px 3px #00bfff, 0px 0px 7px 5px #0d0d0d, 0px 0px 9px 7px #00bfff;
        }
    }
}

</style>