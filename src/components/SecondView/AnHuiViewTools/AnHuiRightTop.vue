<script setup>
import {ref, onMounted,} from 'vue';
import * as echarts from 'echarts';
const echartsRef = ref(null);
let myChart30 = null;
let option30 = null;

onMounted(() => {
    myChart30 = echarts.init(echartsRef.value);

    option30 = {
        series: [
            {
                type: 'gauge',
                startAngle: 180,
                endAngle: 0,
                center: ['50%', '75%'],
                radius: '90%',
                min: 0,
                max: 1,
                splitNumber: 5,
                axisLine: {
                    lineStyle: {
                        width: 6,
                        color: [
                            [0.25, '#FF6E76'],
                            [0.5, '#FDDD60'],
                            [0.75, '#58D9F9'],
                            [1, '#7CFFB2']
                        ]
                    }
                },
                pointer: {
                    icon: 'path://M12.8,0.7l12,40.1H0.7L12.8,0.7z',
                    length: '12%',
                    width: 20,
                    offsetCenter: [0, '-60%'],
                    itemStyle: {
                        color: 'auto'
                    }
                },
                axisTick: {
                    length: 12,
                    lineStyle: {
                        color: 'auto',
                        width: 2
                    }
                },
                splitLine: {
                    length: 20,
                    lineStyle: {
                        color: 'auto',
                        width: 5
                    }
                },
                axisLabel: {
                    color: '#fff',
                    fontSize: 20,
                    distance: -60,
                    rotate: 'tangential',
                    formatter: function (value) {
                        if (value === 0.875) {
                            return 'Grade A';
                        } else if (value === 0.625) {
                            return 'Grade B';
                        } else if (value === 0.375) {
                            return 'Grade C';
                        } else if (value === 0.125) {
                            return 'Grade D';
                        }
                        return '';
                    }
                },
                title: {
                    offsetCenter: [0, '-10%'],
                    fontSize: 20
                },
                detail: {
                    fontSize: 30,
                    offsetCenter: [0, '-35%'],
                    valueAnimation: true,
                    formatter: function (value) {
                        if (value <= 0.25 && value >= 0) {
                            return '低程度';
                        }
                        if (value > 0.25 && value <= 0.5) {
                            return '中低程度';
                        }
                        if (value > 0.5 && value <= 0.75) {
                            return '中高程度';
                        }
                        if (value > 0.75 && value <= 1) {
                            return '高程度';
                        }
                        return '';
                    },
                    color: 'inherit'
                },
                data: [
                    {
                        value: 0.7,
                        color:'white',
                        name:'发展程度'
                    }
                ]
            }
        ]
    };

    option30 && myChart30.setOption(option30);

    const resizeObserver = new ResizeObserver(() => {
        myChart30.resize();
    });

    resizeObserver.observe(echartsRef.value);
});

</script>

<template>
  <div class="AnHuiRightTop">
      <div class="AnHuiRightTop-echarts" ref="echartsRef"></div>
  </div>
</template>

<style scoped lang="scss">
  .AnHuiRightTop{
    width: 100%;
    height: 100%;
    .AnHuiRightTop-echarts{
      width: 30vw;
      height: 30vh;
    }
  }
</style>