<script setup>
import BigTitle from "@/components/BigTitle.vue";
import FootLoop from "@/components/FootLoop.vue";
import AnHuiSunLeft from "@/components/SecondView/AnHuiSunView/AnHuiSunLeft.vue";
import AnHuiSunRightTop from "@/components/SecondView/AnHuiSunTools/AnHuiSunRightTop.vue";
import AnHuiSunRight from "@/components/SecondView/AnHuiSunView/AnHuiSunRight.vue";
import AnHuiSunMidden from "@/components/SecondView/AnHuiSunView/AnHuiSunMidden.vue";
</script>

<template>
    <div class="AnHuiSunView">
        <BigTitle id="title"></BigTitle>
        <AnHuiSunLeft id="AnHuiSunLeft-out"></AnHuiSunLeft>
        <AnHuiSunMidden id="AnHuiSunMidden-out"></AnHuiSunMidden>
        <AnHuiSunRightTop id="AnHuiSunRightTop-out"></AnHuiSunRightTop>
        <AnHuiSunRight id="AnHuiSunRight-out"></AnHuiSunRight>
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

  #AnHuiSunLeft-out {
    width: 25vw;
    height: 80vh;
    margin-top: 3vh;
    margin-left: 2vw;
    position: absolute;
  }

  #AnHuiSunMidden-out {
    width: 40vw;
    height: 80vh;
    margin-top: 4vh;
    margin-left: 30.2vw;
  }

  #AnHuiSunRightTop-out {
    top: 0;
    right: 0;
    position: absolute;
    width: 20vw;
    height: 20vh;
    margin-right: 7.5vw;
    margin-top: 14vh;
  }

  #AnHuiSunRight-out {
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