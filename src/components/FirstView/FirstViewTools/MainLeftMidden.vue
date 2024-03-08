<script setup>
import {ref, onMounted} from 'vue';
import * as echarts from 'echarts';

const echartsRef = ref(null);
let myChart2 = null;
let option2 = null;

onMounted(() => {
    myChart2 = echarts.init(echartsRef.value);

    // Your echarts option setup here...
    // (Your existing option setup code)
    var colorList = [
        '#5470c6', '#91cc75', '#fac858', '#ee6666', '#73c0de', '#3ba272', '#fc8452', '#9a60b4', '#546570', '#ea7ccc'
    ];
    option2 = {
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
                '东部',
                '西部',
                '北部',
                '南部',
                '中部',
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
                emphasis: {
                    label: {
                        show: true,
                    }
                },
                data: [
                    {value: 40, name: '北部'},
                    {value: 33, name: '东部'},
                    {value: 28, name: '西部'},
                    {value: 22, name: '南部'},
                    {value: 20, name: '中部'},
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
                data: [
                    {value: 30, name: '北部'},
                    {value: 28, name: '南部'},
                    {value: 26, name: '中部'},
                    {value: 24, name: '东部'},
                    {value: 22, name: '西部'},
                ]
            }
        ]
    };
    option2 && myChart2.setOption(option2);

    const resizeObserver = new ResizeObserver(() => {
        myChart2.resize();
    });

    resizeObserver.observe(echartsRef.value);
});
</script>

<template>
    <div className="MainLeftMidden">
        <div class="MainLeftMidden-title">全国资源开发与需求占比</div>
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
    height: 20vh;
    margin-left: -2vw;
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
