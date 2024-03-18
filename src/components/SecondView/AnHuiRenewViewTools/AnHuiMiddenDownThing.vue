<script setup>
import {ref, onMounted, onBeforeUnmount} from 'vue';
import * as echarts from 'echarts';

const echartsRef = ref(null);
let myChart35 = null;
let option35 = null;
let currentIndex = 0;
let intervalId = null;
let isHovering = false;

onMounted(() => {
    myChart35 = echarts.init(echartsRef.value);

    option35 = {
        series: [

            {

                name: 'Access From',
                type: 'pie',
                radius: ['45%', '80%'],
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
                    {value: 1048, name: '光伏'},
                    {value: 735, name: '风能'},
                    {value: 580, name: '水利'},
                    {value: 484, name: '新型储能'},
                    {value: 300, name: '其他'}
                ]
            }
        ]
    };

    option35 && myChart35.setOption(option35);
    const resizeObserver = new ResizeObserver(() => {
        myChart35.resize();
    });

    resizeObserver.observe(echartsRef.value);

    myChart35.on('mouseover', (params) => {
        isHovering = true;
        const prevIndex = currentIndex;
        currentIndex = params.dataIndex;
        clearInterval(intervalId);

        if (prevIndex !== currentIndex) {
            myChart35.dispatchAction({
                type: 'downplay',
                seriesIndex: 0,
                dataIndex: prevIndex,
            });
        }

        myChart35.dispatchAction({
            type: 'highlight',
            seriesIndex: 0,
            dataIndex: currentIndex,
        });
    });

    myChart35.on('mouseout', () => {
        isHovering = false;
        startInterval();
    });

    startInterval();
});

function startInterval() {
    intervalId = setInterval(() => {
        if (!isHovering) {
            const prevIndex = currentIndex;
            currentIndex = (currentIndex + 1) % option35.series[0].data.length;

            myChart35.dispatchAction({
                type: 'downplay',
                seriesIndex: 0,
                dataIndex: prevIndex,
            });

            myChart35.dispatchAction({
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
    <div class="AnHuiMiddenDownThing">
        <div class="AnHuiMiddenDownThing-name">
            <div class="name-title">总容量：</div>
            <div class="name-number">1.08</div>
            <div class="name-up">亿千瓦</div>
        </div>
        <div class="AnHuiMiddenDownThing-echarts" ref="echartsRef"></div>
    </div>
</template>

<style scoped lang="scss">
.AnHuiMiddenDownThing {
  width: 100%;
  height: 100%;

  .AnHuiMiddenDownThing-name {
    position: absolute;
    color: white;
    margin-left: 0.3vw;

    .name-title {
      margin-left: 0.5vw;
      width: 10vw;
      position: absolute;
    }

    .name-number {
      color: #4ed8fa;
      text-shadow: 0 0 1px #1cd7cd, 0 0 1px #1cd7cd, 0 0 1.5px #1cd7cd;
      margin-left: 4.5vw;
      font-size: 1.25em;
      width: 10vw;
      margin-top: -0.3vh;
      font-weight: bolder;
      position: absolute;
    }

    .name-up {
      margin-left: 8vw;
      width: 10vw;
      position: absolute;
    }
  }

  .AnHuiMiddenDownThing-echarts {
    width: 10vw;
    height: 20vh;
    //background: red;
    margin-top: 1.8vh;
    margin-left: 2vw;
    position: absolute;
    z-index: 999;
  }
}
</style>