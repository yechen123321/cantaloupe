<script setup>
import {onMounted} from "vue";

onMounted(() => {

});
</script>

<template>
    <div class="AnHuiLeftTop">
        <div class="AnHuiLeftTop-title">安徽省再生能源统计</div>

        <img src="../../../assets/pic/border4.png" alt="" class="BackImg">
    </div>
</template>

<style scoped lang="scss">
.AnHuiLeftTop {
  width: 100%;
  height: 100%;
  color: white;

  .BackImg {
    position: absolute;
    width: 26vw;
    height: 22.5vh;
    margin-left: 2.5vw;
    margin-top: -4vh;
  }

  .AnHuiLeftTop-title {
    position: absolute;
    color: white;
    margin-top: -3vh;
    text-align: center;
    width: 25.8vw;
    margin-left: 2.6vw;
    font-weight: bolder;
    font-size: 1.15em;
  }

  .AnHuiLeftTop-echarts {
    width: 23vw;
    height: 25vh;
    margin-top: -1.2vh;
    margin-left: 3.2vw;
  }
}
</style>