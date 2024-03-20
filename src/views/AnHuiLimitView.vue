<script setup>
import BigTitle from "@/components/BigTitle.vue";
import AnHuiLimitTop from "@/components/ThirdView/AnHuiLimitView/AnHuiLimitTop.vue";
import AnHuiLimitLeft from "@/components/ThirdView/AnHuiLimitView/AnHuiLimitLeft.vue";
import AnHuiLimitMidden from "@/components/ThirdView/AnHuiLimitView/AnHuiLimitMidden.vue";
import AnHuiLimitRightTop from "@/components/ThirdView/AnHuiLimitView/AnHuiLimitRightTop.vue";
import AnHuiLimitRight from "@/components/ThirdView/AnHuiLimitView/AnHuiLimitRight.vue";
import FootLoop from '@/components/FootLoop.vue';
</script>

<template>
    <div class="AnHuiLimitView">
        <BigTitle id="BigTitle"></BigTitle>
        <AnHuiLimitTop id="AnHuiLimitTop-out"></AnHuiLimitTop>
        <AnHuiLimitLeft id="AnHuiLimitLeft-out"></AnHuiLimitLeft>
        <AnHuiLimitMidden id="AnHuiLimitMidden-out"></AnHuiLimitMidden>
        <AnHuiLimitRight id="AnHuiLimitRight-out"></AnHuiLimitRight>
        <AnHuiLimitRightTop id="AnHuiLimitRightTop-out"></AnHuiLimitRightTop>
        <FootLoop id="FootLoop"></FootLoop>
    </div>
</template>

<style scoped lang="scss">
.AnHuiLimitView {
  width: 100%;
  height: 100%;
    #AnHuiLimitRightTop-out{
        position: absolute;
        width: 20vw;
        height: 20vh;
        right: 0;
        margin-top: 1vh;
        margin-right: 8vw;
    }
  #AnHuiLimitRight-out {
    width: 25vw;
    height: 60vh;
    margin-top: 34vh;
    //margin-left: 2vw;
    //right: 0;
    margin-left: 28.5vw;
    position: absolute;
  }

  #AnHuiLimitMidden-out {
    position: absolute;
    margin-left: 53.5vw;
    margin-top: 29vh;

  }

  #AnHuiLimitTop-out {
    width: 96vw;
    margin-left: 29vw;
    height: 28vh;
    margin-top: 4vh;
    position: absolute;
  }

  #AnHuiLimitLeft-out {
    width: 25vw;
    height: 60vh;
    margin-top: 2vh;
    margin-left: 1.5vw;
    position: absolute;
  }

  #BigTitle {
    width: 100vw;
  }

  #FootLoop {
    position: absolute;
    margin-top: 70vh;
  }
}
</style>