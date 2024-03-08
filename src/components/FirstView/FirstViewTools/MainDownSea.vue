<script setup>
import {ref, onMounted} from 'vue';
import * as echarts from 'echarts';
import 'echarts-gl';

const echartsRef = ref(null);
let myChart7 = null;
let option7 = null;

onMounted(() => {
    myChart7 = echarts.init(echartsRef.value);
    option7 = {
        tooltip: {
            trigger: 'item',
            textStyle:{
                fontWeight:'bold',
            },
            formatter: '{a} <br/>{b}: {c} ({d}%)'
        },
        legend: {
            // type: 'scroll',
            itemWidth: 10, // 标签宽度为20px
            itemHeight: 10, // 标签高度为10px
            top: '-4',
            textStyle: {
                color: 'white'
            },
            data: [
                '渔业用海',
                '工业用海',
                '交通运输用海',
                '造地工程用海',
                '特殊用海',
                '其他用海',
                '滨海旅游业',
                '海洋交通运输业',
                '海洋渔业',
            ]
        },
        series: [
            {
                name: '主要海洋产业增加值',
                type: 'pie',
                selectedMode: 'single',
                radius: [0, '30%'],
                top: '27%',
                labelLine: {
                    length: 30
                },
                label: {
                    color: 'white',
                },
                data: [
                    {value: 1548, name: '滨海旅游业'},
                    {value: 775, name: '海洋交通运输业',},
                    {value: 679, name: '海洋渔业', selected: true}
                ]
            },
            {
                name: '全国批准用海结构',
                type: 'pie',
                top: '25%',
                radius: ['45%', '60%'],
                label: {
                    color: 'white',
                },
                labelLine: {
                    length: 30
                },
                data: [
                    {value: 1048, name: '渔业用海'},
                    {value: 335, name: '工业用海'},
                    {value: 310, name: '交通运输用海'},
                    {value: 251, name: '造地工程用海'},
                    {value: 234, name: '特殊用海'},
                    {value: 147, name: '其他用海'},
                ]
            }
        ]
    };

    option7 && myChart7.setOption(option7);

    const resizeObserver = new ResizeObserver(() => {
        myChart7.resize();
    });

    resizeObserver.observe(echartsRef.value);
});
</script>


<template>
    <div className="MainDownSea">
        <Button class="GotoSea">全国批准用海结构</Button>
        <div id="MainDownSea-echarts" ref="echartsRef"></div>
    </div>
</template>

<style scoped lang="scss">
.MainDownSea {
  width: 100vw;
  height: 100vh;
  color: white;

  .GotoSea {
    position: absolute;
    margin-top: -26vh;
    border: none;
    background: none;
    color: white;
    font-weight: bolder;
    font-size: 1.2vw;
    margin-left: 7vw;
    //cursor: pointer;
  }

  //.GotoSea:hover {
  //  font-size: 1.3vw;
  //  margin-left: 6.7vw;
  //  margin-top: -26.1vh;
  //}
  //
  //.GotoSea:active {
  //  margin-top: -26vh;
  //  font-size: 1.2vw;
  //  margin-left: 7vw;
  //}

  #MainDownSea-echarts {
    width: 23vw;
    height: 28vh;
    margin-left: 1vw;
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
