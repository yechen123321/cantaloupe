<script setup>
import {ref, onMounted, onBeforeUnmount} from 'vue';
import * as echarts from 'echarts';

const echartsRef = ref(null);
let myChart31 = null;
let option31 = null;
let currentIndex = 0;
let intervalId = null;
let isHovering = false;

onMounted(() => {
    myChart31 = echarts.init(echartsRef.value);
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
    option31 = {
        color: colorList,
        series: [

            {

                name: 'Access From',
                type: 'pie',
                radius: ['40%', '70%'],
                avoidLabelOverlap: false,
                itemStyle: {
                    borderRadius: 5,
                },
                label: {
                    show: false,
                    position: 'center',
                    formatter: '{b}:\n{d}%'
                },
                emphasis: {
                    label: {
                        show: true,
                        fontSize: 20,
                        color: 'white',
                        fontWeight: 'bold'
                    }
                },
                labelLine: {
                    show: false
                },
                data: [
                    {value: 85, name: '多晶硅'},
                    {value: 15, name: '单晶硅'},
                    {value: 11, name: '薄膜'},
                    {value: 7, name: 'PERC'},
                    {value: 6, name: '集热式'},
                    {value: 5, name: '其他'}
                ]
            }
        ]
    };

    option31 && myChart31.setOption(option31);

    myChart31.on('mouseover', (params) => {
        isHovering = true;
        const prevIndex = currentIndex;
        currentIndex = params.dataIndex;
        clearInterval(intervalId);

        if (prevIndex !== currentIndex) {
            myChart31.dispatchAction({
                type: 'downplay',
                seriesIndex: 0,
                dataIndex: prevIndex,
            });
        }

        myChart31.dispatchAction({
            type: 'highlight',
            seriesIndex: 0,
            dataIndex: currentIndex,
        });
    });

    myChart31.on('mouseout', () => {
        isHovering = false;
        startInterval();
    });

    startInterval();
});

function startInterval() {
    intervalId = setInterval(() => {
        if (!isHovering) {
            const prevIndex = currentIndex;
            currentIndex = (currentIndex + 1) % option31.series[0].data.length;

            myChart31.dispatchAction({
                type: 'downplay',
                seriesIndex: 0,
                dataIndex: prevIndex,
            });

            myChart31.dispatchAction({
                type: 'highlight',
                seriesIndex: 0,
                dataIndex: currentIndex,
            });
        }
    }, 2000);
}

onBeforeUnmount(() => {
    clearInterval(intervalId);
});
</script>

<template>
    <div class="ThermalPowerMiddenDownThing">
        <div class="title">光伏电板使用占比</div>
        <div class="ThermalPowerMiddenDownThing-echarts" ref="echartsRef"></div>
    </div>
</template>

<style scoped lang="scss">
.ThermalPowerMiddenDownThing {
  width: 100%;
  height: 100%;

  .title {
    color: white;
    position: absolute;
    font-weight: bolder;
    font-size: 1.3em;
    margin-top: -4vh;
    margin-left: 3vw;
  }

  .ThermalPowerMiddenDownThing-echarts {
      width: 27vw;
      height: 27vh;
      margin-left: -4.5vw;
      margin-top: -2vh;
      z-index: 300;

  }
}
</style>
