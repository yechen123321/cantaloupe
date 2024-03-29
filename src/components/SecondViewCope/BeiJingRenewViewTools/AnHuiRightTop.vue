<script setup>
import {ref, onMounted, onBeforeUnmount} from 'vue';
import * as echarts from 'echarts';

const echartsRef = ref(null);
let myChart30 = null;
let option30 = null;
let currentIndex = 0;
let highlightTimer = null;

onMounted(() => {
    myChart30 = echarts.init(echartsRef.value);
    var colorList = [
        new echarts.graphic.LinearGradient(0, 0, 0, 1, [
            {offset: 0, color: '#396afc'},
            {offset: 1, color: '#2948ff'}
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
    let data = [
        {value: 800, name: '太阳能'},
        {value: 700, name: '风能'},
        {value: 600, name: '水利'},
        {value: 500, name: '生物质能'},
        {value: 450, name: '地热能'},
        {value: 400, name: '氢能'},
        {value: 300, name: '沼气'},
        {value: 200, name: '核能'},
    ];

    option30 = {

        series: [
            {

                backgroundColor: colorList,
                itemStyle: {
                    borderWidth: 0,
                    borderRadius: [10, 10, 0, 0],
                },
                name: 'Funnel',
                type: 'funnel',
                width: '40%',
                height: '45%',
                left: '30%',
                top: '5%',
                label: {
                    position: 'center',
                    textStyle: {
                        color: 'white',
                        fontSize: 14, // 初始字体大小
                        fontWeight: 'normal', // 初始字体粗细
                    },
                },
                data: data,
            },
        ],
    };

    option30 && myChart30.setOption(option30);

    // 循环触发数据项高亮效果
    highlightTimer = setInterval(() => {
        // 取消上一个数据项的高亮状态
        myChart30.dispatchAction({
            type: 'downplay',
            seriesIndex: 0,
            dataIndex: currentIndex === 0 ? data.length - 1 : currentIndex - 1,
        });

        myChart30.dispatchAction({
            type: 'highlight',
            seriesIndex: 0,
            dataIndex: currentIndex,
        });

        // 修改被选中数据项的字体大小和粗细
        myChart30.setOption({
            series: [{
                label: {
                    emphasis: {
                        fontSize: 18, // 被选中的字体变大
                        fontWeight: 'bold', // 被选中的字体变粗
                    },
                },
            }],
        });

        currentIndex = (currentIndex + 1) % data.length;
    }, 1000); // 每隔1秒切换高亮显示的数据项

    const resizeObserver = new ResizeObserver(() => {
        myChart30.resize();
    });

    resizeObserver.observe(echartsRef.value);
});

// 组件销毁时清除定时器
onBeforeUnmount(() => {
    clearInterval(highlightTimer);
});
</script>

<template>
    <div class="AnHuiRightTop">
        <div class="AnHuiRightTop-title">北京重要再生能源</div>
        <div class="AnHuiRightTop-echarts" ref="echartsRef"></div>
        <img class="BackImg" src="../../../assets/pic/border4.png" alt="">
    </div>
</template>

<style scoped lang="scss">
.AnHuiRightTop {
  width: 100%;
  height: 100%;

  .AnHuiRightTop-title {
    font-size: 1.2vw;
    width: 24vw;
    //background: red;
    color: white;
    text-align: center;
    position: absolute;
    font-weight: bolder;
    //background: none;
    margin-top: -9.5vh;
    margin-left: 13vw;
  }

  .AnHuiRightTop-echarts {
    position: absolute;
    width: 50vw;
    height: 33vh;
    margin-top: -7.5vh;
  }

  .BackImg {
    width: 25vw;
    height: 20vh;
    margin-left: 12vw;
    margin-top: -10vh;
  }
}
</style>