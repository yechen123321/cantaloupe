<script setup>
import {ref, onMounted, onBeforeUnmount} from 'vue';
import * as echarts from 'echarts';

const echartsRef = ref(null);
let myChart46 = null;
let option46 = null;
let currentIndex = 0;
let intervalId = null;
let isHovering = false;

onMounted(() => {
    myChart46 = echarts.init(echartsRef.value);

    option46 = {
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
                        fontSize: 16,
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

    option46 && myChart46.setOption(option46);
    const resizeObserver = new ResizeObserver(() => {
        myChart46.resize();
    });

    resizeObserver.observe(echartsRef.value);

    myChart46.on('mouseover', (params) => {
        isHovering = true;
        const prevIndex = currentIndex;
        currentIndex = params.dataIndex;
        clearInterval(intervalId);

        if (prevIndex !== currentIndex) {
            myChart46.dispatchAction({
                type: 'downplay',
                seriesIndex: 0,
                dataIndex: prevIndex,
            });
        }

        myChart46.dispatchAction({
            type: 'highlight',
            seriesIndex: 0,
            dataIndex: currentIndex,
        });
    });

    myChart46.on('mouseout', () => {
        isHovering = false;
        startInterval();
    });

    startInterval();
});

function startInterval() {
    intervalId = setInterval(() => {
        if (!isHovering) {
            const prevIndex = currentIndex;
            currentIndex = (currentIndex + 1) % option46.series[0].data.length;

            myChart46.dispatchAction({
                type: 'downplay',
                seriesIndex: 0,
                dataIndex: prevIndex,
            });

            myChart46.dispatchAction({
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
  <div class="AnHuiSunMiddenCenterThing">
      <div class="title">
          <div class="name">总容量：</div>
          <div class="number">721.94</div>
          <div class="up">万千瓦</div>
      </div>
      <div class="AnHuiSunMiddenCenterThing-echarts" ref="echartsRef"></div>
  </div>
</template>

<style scoped lang="scss">
  .AnHuiSunMiddenCenterThing{
    width: 100%;
    height: 100%;
    .AnHuiSunMiddenCenterThing-echarts{
      width: 20vw;
      height: 20vh;
      position: absolute;
      margin-top: 2vh;
      margin-left: -1vw;
    }
    .title{
      color:white;
      width: 20vw;
      position: absolute;
      margin-left: 2.5vw;
      .name{
        float: left;
      }
      .number{
        float: left;
        margin-left: -0.2vw;
        margin-top: -0.3vh;
        font-weight: bolder;
        color: #4ed8fa;
        text-shadow: 0 0 1px #1cd7cd, 0 0 1px #1cd7cd, 0 0 1.5px #1cd7cd;
        font-size: 1.25em;
      }
      .up{
        float: left;
        margin-left: 0.6vw;
      }
    }
  }
</style>