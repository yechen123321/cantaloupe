<script setup>
import {ref, onMounted, onBeforeUnmount} from 'vue';
import * as echarts from 'echarts';

const echartsRef = ref(null);
let myChart63 = null;
let option63 = null;
let currentIndex = 0;
let intervalId = null;
let isHovering = false;

onMounted(() => {
    myChart63 = echarts.init(echartsRef.value);
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
    option63 = {
        color:colorList,
        series: [

            {

                name: 'Access From',
                type: 'pie',
                radius: ['40%', '75%'],
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
                        fontSize: 20,
                        color: 'white',
                        fontWeight: 'bold'
                    }
                },
                labelLine: {
                    show: false
                },
                data: [
                    {value: 1048, name: '合肥'},
                    {value: 735, name: '马鞍山'},
                    {value: 580, name: '芜湖'},
                    {value: 484, name: '淮南'},
                    {value: 300, name: '其他'}
                ]
            }
        ]
    };

    option63 && myChart63.setOption(option63);
    const resizeObserver = new ResizeObserver(() => {
        myChart63.resize();
    });

    resizeObserver.observe(echartsRef.value);

    myChart63.on('mouseover', (params) => {
        isHovering = true;
        const prevIndex = currentIndex;
        currentIndex = params.dataIndex;
        clearInterval(intervalId);

        if (prevIndex !== currentIndex) {
            myChart63.dispatchAction({
                type: 'downplay',
                seriesIndex: 0,
                dataIndex: prevIndex,
            });
        }

        myChart63.dispatchAction({
            type: 'highlight',
            seriesIndex: 0,
            dataIndex: currentIndex,
        });
    });

    myChart63.on('mouseout', () => {
        isHovering = false;
        startInterval();
    });

    startInterval();
});

function startInterval() {
    intervalId = setInterval(() => {
        if (!isHovering) {
            const prevIndex = currentIndex;
            currentIndex = (currentIndex + 1) % option63.series[0].data.length;

            myChart63.dispatchAction({
                type: 'downplay',
                seriesIndex: 0,
                dataIndex: prevIndex,
            });

            myChart63.dispatchAction({
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
    <div class="AnHuiWindMiddenDownThing">
        <div class="title">
            <div class="name">当年增长率：</div>
            <div class="number">35.6</div>
            <div class="up">%</div>
        </div>
        <div class="AnHuiWindMiddenDownThing-echarts" ref="echartsRef"></div>
    </div>
</template>

<style scoped lang="scss">
.AnHuiWindMiddenDownThing {
  width: 100%;
  height: 100%;

  .AnHuiWindMiddenDownThing-echarts {
    width: 23vw;
    height: 23vh;
    position: absolute;
    margin-top: 0.3vh;
    margin-left: -5.3vw;
  }

  .title {
    color: white;
    width: 20vw;
    position: absolute;
    margin-left: 1vw;
    margin-top: -1vh;
    .name {
      float: left;
    }

    .number {
      float: left;
      margin-left: -0.2vw;
      margin-top: -0.3vh;
      font-weight: bolder;
      color: #4ed8fa;
      text-shadow: 0 0 1px #1cd7cd, 0 0 1px #1cd7cd, 0 0 1.5px #1cd7cd;
      font-size: 1.25em;
    }

    .up {
      float: left;
      margin-left: 0.6vw;
    }
  }
}
</style>