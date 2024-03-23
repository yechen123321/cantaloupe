<script setup>
import {ref, onMounted, onBeforeUnmount} from 'vue';
import * as echarts from 'echarts';
import LeftMiddenEFirst from "@/components/FourthView/DataAnalysisTools/LeftMiddenEFirst.vue";
import LeftMiddenESecond from "@/components/FourthView/DataAnalysisTools/LeftMiddenESecond.vue";
const echartsRef = ref(null);
let myChart80 = null;
let option80 = null;
let currentIndex = 0;
let intervalId = null;
let isHovering = false;

onMounted(() => {
    myChart80 = echarts.init(echartsRef.value);

    option80 = {
        series: [

            {
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
                    {value: 1048, name: '合肥'},
                    {value: 735, name: '马鞍山'},
                    {value: 580, name: '芜湖'},
                    {value: 484, name: '淮南'},
                    {value: 300, name: '其他'}
                ]
            },
        ]
    };

    option80 && myChart80.setOption(option80);
    const resizeObserver = new ResizeObserver(() => {
        myChart80.resize();
    });

    resizeObserver.observe(echartsRef.value);

    myChart80.on('mouseover', (params) => {
        isHovering = true;
        const prevIndex = currentIndex;
        currentIndex = params.dataIndex;
        clearInterval(intervalId);

        if (prevIndex !== currentIndex) {
            myChart80.dispatchAction({
                type: 'downplay',
                seriesIndex: 0,
                dataIndex: prevIndex,
            });
        }

        myChart80.dispatchAction({
            type: 'highlight',
            seriesIndex: 0,
            dataIndex: currentIndex,
        });
    });

    myChart80.on('mouseout', () => {
        isHovering = false;
        startInterval();
    });

    startInterval();
});

function startInterval() {
    intervalId = setInterval(() => {
        if (!isHovering) {
            const prevIndex = currentIndex;
            currentIndex = (currentIndex + 1) % option80.series[0].data.length;

            myChart80.dispatchAction({
                type: 'downplay',
                seriesIndex: 0,
                dataIndex: prevIndex,
            });

            myChart80.dispatchAction({
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
  <div class="DataAnalysisLeftMidden">
      <div class="title">安徽能源结构</div>
      <div class="DataAnalysisLeftMidden-echarts" ref="echartsRef"></div>
      <LeftMiddenEFirst id="LeftMiddenEFirst-out"></LeftMiddenEFirst>
      <LeftMiddenESecond id="LeftMiddenESecond-out"></LeftMiddenESecond>
      <img src="../../../assets/pic/midden.png" alt="" class="BackImg">
  </div>
</template>

<style scoped lang="scss">
.DataAnalysisLeftMidden{
  width: 100%;
  height: 100%;
  #LeftMiddenESecond-out{
    width: 20vw;
    height: 20vh;
    position: absolute;
    margin-top: 1.5vh;
    margin-left: 14vw;
  }
  #LeftMiddenEFirst-out{
    width: 20vw;
    height: 20vh;
    position: absolute;
    margin-top: 1.5vh;
    margin-left: 5.5vw;
  }
  .DataAnalysisLeftMidden-echarts{
    width: 30vw;
    height: 30vh;
    position: absolute;
    margin-left: -3vw;
    margin-top: 1.6vh;
  }
  .title{
    position: absolute;
    color:white;
    margin-top: 3.5vh;
    margin-left: 3vw;
    font-weight: bolder;
    font-size: 1.4em;
  }
  .BackImg{
    width: 30vw;
    height: 28vh;
  }
}
</style>