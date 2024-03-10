<script setup>
import { ref, onMounted, onBeforeUnmount } from 'vue';
import * as echarts from 'echarts';

const echartsRef = ref(null);
let myChart31 = null;
let option31 = null;
let currentIndex = 0;
let intervalId = null;
let isHovering = false;

onMounted(() => {
    myChart31 = echarts.init(echartsRef.value);

    option31 = {
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
                        fontSize: 16,
                        color: 'white',
                        fontWeight: 'bold'
                    }
                },
                labelLine: {
                    show: false
                },
                data: [
                    { value: 1048, name: '煤炭' },
                    { value: 735, name: '铁矿' },
                    { value: 580, name: '基岩' },
                    { value: 484, name: '石灰石' },
                    { value: 300, name: '钻石' }
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
                dataIndex: prevIndex
            });
        }

        myChart31.dispatchAction({
            type: 'highlight',
            seriesIndex: 0,
            dataIndex: currentIndex
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
                dataIndex: prevIndex
            });

            myChart31.dispatchAction({
                type: 'highlight',
                seriesIndex: 0,
                dataIndex: currentIndex
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
        <div class="AnHuiMiddenDownThing-title">
            <div class="first">矿场数：</div>
            <div class="second">123123 座</div>
        </div>
        <div class="AnHuiMiddenDownThing-echarts" ref="echartsRef"></div>
    </div>
</template>

<style scoped lang="scss">
.AnHuiMiddenDownThing {
    width: 100%;
    height: 100%;
    .AnHuiMiddenDownThing-title{
        font-weight: bolder;
        margin-top: -1vh;
        width: 12vw;
        //background: red;
        margin-left: 1vw;
        .first{
            float: left;
        }
        .second{
            margin-top: 1vh;
        }
    }
    .AnHuiMiddenDownThing-echarts {
        width: 20vw;
        height: 20vh;
        margin-left: -3.5vw;
        margin-top: -1.5vh;
    }
}
</style>
