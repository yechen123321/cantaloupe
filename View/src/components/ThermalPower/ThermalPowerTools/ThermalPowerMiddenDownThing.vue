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
            {offset: 0, color: '#f69ae3'},
            {offset: 1, color: '#de6acb'},
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
                        fontSize: 18,
                        color: 'white',
                        fontWeight: 'bold'
                    }
                },
                labelLine: {
                    show: false
                },
                data: [
                    {value: 1048, name: '煤炭'},
                    {value: 335, name: '天然气'},
                    {value: 235, name: '燃油'},
                    {value: 180, name: '焦炭'},
                    {value: 130, name: '石油焦'},
                    {value: 30, name: '其他'}
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
        <div class="title">各类燃料使用占比</div>
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
    margin-left: 2vw;
  }

  .ThermalPowerMiddenDownThing-echarts {
    width: 15vw;
    height: 24vh;
    margin-left: 0.5vw;
    margin-top: -1.5vh;
  }
}
</style>
