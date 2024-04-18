<script setup>
import BigTitle from "@/components/BigTitle.vue";
import FootLoop from "@/components/FootLoop.vue";
import AnHuiWindRightTop from "@/components/SecondView/AnHuiWindTools/AnHuiWindRightTop.vue";
import AnHuiWindLeft from "@/components/SecondView/AnHuiWindView/AnHuiWindLeft.vue";
import AnHuiWindMidden from "@/components/SecondView/AnHuiWindView/AnHuiWindMidden.vue";
import AnHuiWindRight from "@/components/SecondView/AnHuiWindView/AnHuiWindRight.vue";
</script>

<template>
    <div class="AnHuiSunView">
        <BigTitle id="title"></BigTitle>
        <AnHuiWindLeft id="AnHuiWindLeft-out"></AnHuiWindLeft>
        <AnHuiWindMidden id="AnHuiWindMidden-out"></AnHuiWindMidden>
        <AnHuiWindRightTop id="AnHuiWindRightTop-out"></AnHuiWindRightTop>
        <AnHuiWindRight id="AnHuiWindRight-out"></AnHuiWindRight>
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

  #AnHuiWindLeft-out {
    width: 25vw;
    height: 80vh;
    margin-top: 28vh;
    margin-left: 2vw;
    position: absolute;
  }

  #AnHuiWindMidden-out {
    width: 40vw;
    height: 80vh;
    margin-top: 4vh;
    margin-left: 30.2vw;
  }

  #AnHuiWindRightTop-out {
    top: 0;
    right: 0;
    position: absolute;
    width: 20vw;
    height: 20vh;
    margin-right: 7.5vw;
    margin-top: 14vh;
  }

  #AnHuiWindRight-out {
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