<script setup>
import {onMounted, ref} from "vue";
import * as echarts from "echarts";

const echartsRef = ref(null);
let myChart36 = null;
let option36 = null;

onMounted(() => {
    myChart36 = echarts.init(echartsRef.value, 'dark');

    // Your echarts option setup here...
    // (Your existing option setup code)
    option36 = {
        backgroundColor: 'rgba(128,128,128,0)',
        tooltip: {
            trigger: 'axis',
            axisPointer: {
                // Use axis to trigger tooltip
                type: 'shadow' // 'shadow' as default; can also be 'line' or 'shadow'
            }
        },
        legend: {
            top:"16%",
            itemWidth: 10, // 标签宽度为20px
            itemHeight: 10, // 标签高度为10px
        },
        grid: {
            left: '3%',
            right: '4%',
            bottom: '3%',
            containLabel: true
        },
        xAxis: {
            type: 'value'
        },
        yAxis: {
            type: 'category',
            data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
        },
        series: [
            {
                name: 'Direct',
                type: 'bar',
                stack: 'total',
                label: {
                    show: true
                },
                emphasis: {
                    focus: 'series'
                },
                data: [320, 302, 301, 334, 390, 330, 320]
            },
            {
                name: 'Mail Ad',
                type: 'bar',
                stack: 'total',
                label: {
                    show: true
                },
                emphasis: {
                    focus: 'series'
                },
                data: [120, 132, 101, 134, 90, 230, 210]
            },
            // {
            //     name: 'Affiliate Ad',
            //     type: 'bar',
            //     stack: 'total',
            //     label: {
            //         show: true
            //     },
            //     emphasis: {
            //         focus: 'series'
            //     },
            //     data: [220, 182, 191, 234, 290, 330, 310]
            // },
            {
                name: 'Video Ad',
                type: 'bar',
                stack: 'total',
                label: {
                    show: true
                },
                emphasis: {
                    focus: 'series'
                },
                data: [150, 212, 201, 154, 190, 330, 410]
            },
            {
                name: 'Search Engine',
                type: 'bar',
                stack: 'total',
                label: {
                    show: true
                },
                emphasis: {
                    focus: 'series'
                },
                data: [820, 832, 901, 934, 1290, 1330, 1320]
            }
        ]
    }
    option36 && myChart36.setOption(option36);

    const resizeObserver = new ResizeObserver(() => {
        myChart36.resize();
    });

    resizeObserver.observe(echartsRef.value);
})
;
</script>

<template>
    <div class="AnHuiLeftDown">
        <div class="AnHuiLeftDown-title">安徽省XXXXXXX</div>
        <div class="AnHuiLeftDown-echarts" ref="echartsRef"></div>
    </div>
</template>

<style scoped lang="scss">
.AnHuiLeftDown {
  width: 100%;
  height: 100%;

  .AnHuiLeftDown-title {
    width: 23vw;
    color: white;
      //background: red;
      margin-left: 1.5vw;
    font-weight: bolder;
    font-size: 1.3vw;
      margin-top: 1.5vh;
    position: absolute;
    text-align: center;
  }

  .AnHuiLeftDown-echarts {
    width: 25vw;
    height: 27vh;
  }
}
</style>