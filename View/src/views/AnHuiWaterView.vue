<script setup>
import BigTitle from "@/components/BigTitle.vue";
import FootLoop from "@/components/FootLoop.vue";
import AnHuiWaterLeft from "@/components/SecondView/AnHuiWaterView/AnHuiWaterLeft.vue";
import AnHuiWaterMidden from "@/components/SecondView/AnHuiWaterView/AnHuiWaterMidden.vue";
import AnHuiWaterRight from "@/components/SecondView/AnHuiWaterView/AnHuiWaterRight.vue";
import AnHuiWaterRightTop from "@/components/SecondView/AnHuiWaterTools/AnHuiWaterRightTop.vue";
</script>

<template>
    <div class="AnHuiSunView">
        <BigTitle id="title"></BigTitle>
        <AnHuiWaterLeft id="AnHuiWaterLeft-out"></AnHuiWaterLeft>
        <AnHuiWaterMidden id="AnHuiWaterMidden-out"></AnHuiWaterMidden>
        <AnHuiWaterRightTop id="AnHuiWaterRightTop-out"></AnHuiWaterRightTop>
        <AnHuiWaterRight id="AnHuiWaterRight-out"></AnHuiWaterRight>
        <FootLoop id="FootLoop"></FootLoop>
    </div>

</template>

<style scoped lang="scss">
.AnHuiSunView {
  width: 100%;
  height: 100%;

  #title {
    width: 100vw;
  }

  #AnHuiWaterLeft-out {
    width: 25vw;
    height: 80vh;
    margin-top: 29vh;
    margin-left: 2vw;
    position: absolute;
  }

  #AnHuiWaterMidden-out {
    width: 40vw;
    height: 80vh;
    margin-top: 4vh;
    margin-left: 30.2vw;
  }

  #AnHuiWaterRightTop-out {
    top: 0;
    right: 0;
    position: absolute;
    width: 20vw;
    height: 20vh;
    margin-right: 7.5vw;
    margin-top: 14vh;
  }

  #AnHuiWaterRight-out {
    width: 25vw;
    height: 58vh;
    right: 0;
    top: 0;
    margin-top: 37vh;
    margin-right: 2.5vw;
    position: absolute;
  }

  #FootLoop {
    position: absolute;
    margin-top: -14vh;
  }
}
</style>