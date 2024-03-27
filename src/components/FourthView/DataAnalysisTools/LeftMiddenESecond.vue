<script setup>
import {ref, onMounted, onBeforeUnmount} from 'vue';
import * as echarts from 'echarts';

const echartsRef = ref(null);
let myChart82 = null;
let option82 = null;
let currentIndex = 0;
let intervalId = null;
let isHovering = false;

onMounted(() => {
    myChart82 = echarts.init(echartsRef.value);
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
    option82 = {
        color:colorList,
        series: [

            {
                roseType: 'area',
                name: 'Access From',
                type: 'pie',
                radius: ['25%', '50%'],
                center: ['32%', '48%'],
                avoidLabelOverlap: false,
                itemStyle: {
                    borderRadius: 5,
                },
                label: {
                    show: false,
                    position: 'center',
                    formatter: '{b}\n{d}%'
                },
                emphasis: {
                    label: {
                        show: true,
                        fontSize: 16,
                        color: 'white',
                        fontWeight: 'bold'
                    }
                },
                labelLine: {
                    show: false
                },
                data: [
                    {value: 1048, name: '新型'},
                    {value: 735, name: '火电'},
                ]
            },
        ]
    };

    option82 && myChart82.setOption(option82);
    const resizeObserver = new ResizeObserver(() => {
        myChart82.resize();
    });

    resizeObserver.observe(echartsRef.value);

    myChart82.on('mouseover', (params) => {
        isHovering = true;
        const prevIndex = currentIndex;
        currentIndex = params.dataIndex;
        clearInterval(intervalId);

        if (prevIndex !== currentIndex) {
            myChart82.dispatchAction({
                type: 'downplay',
                seriesIndex: 0,
                dataIndex: prevIndex,
            });
        }

        myChart82.dispatchAction({
            type: 'highlight',
            seriesIndex: 0,
            dataIndex: currentIndex,
        });
    });

    myChart82.on('mouseout', () => {
        isHovering = false;
        startInterval();
    });

    startInterval();
});

function startInterval() {
    intervalId = setInterval(() => {
        if (!isHovering) {
            const prevIndex = currentIndex;
            currentIndex = (currentIndex + 1) % option82.series[0].data.length;

            myChart82.dispatchAction({
                type: 'downplay',
                seriesIndex: 0,
                dataIndex: prevIndex,
            });

            myChart82.dispatchAction({
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
    <div class="LeftMiddenEFirst">
        <div class="LeftMiddenEFirst-echarts" ref="echartsRef"></div>
    </div>
</template>

<style scoped lang="scss">
.LeftMiddenEFirst {
  width: 100%;
  height: 100%;

  .LeftMiddenEFirst-echarts {
    width: 30vw;
    height: 30vh;
  }
}
</style>