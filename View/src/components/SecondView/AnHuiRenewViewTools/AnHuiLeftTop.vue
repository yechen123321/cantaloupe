<script setup>
import {onMounted, ref} from "vue";
import * as echarts from "echarts";

const echartsRef = ref(null);
let myChart38 = null;
let option38 = null;

onMounted(() => {
    myChart38 = echarts.init(echartsRef.value, 'dark');



    option38 && myChart38.setOption(option38);

    const resizeObserver = new ResizeObserver(() => {
        myChart38.resize();
    });

    resizeObserver.observe(echartsRef.value);
});
</script>

<template>
    <div class="AnHuiLeftTop">
        <div class="AnHuiLeftTop-title">安徽省再生能源统计</div>
        <div class="AnHuiLeftTop-echarts" ref="echartsRef"></div>
    </div>
</template>

<style scoped lang="scss">
.AnHuiLeftTop {
  width: 100%;
  height: 100%;
  color: white;

  .AnHuiLeftTop-title {
    position: absolute;
    color: white;
    margin-top: -1.2vh;
    text-align: center;
    //background: red;
    width: 23vw;
    margin-left: 3.5vw;
    font-weight: bolder;
    font-size: 1.3vw;
  }

  .AnHuiLeftTop-echarts {
    width: 23vw;
    height: 25vh;
    margin-top: -1.2vh;
    margin-left: 3.2vw;
  }
}
</style>