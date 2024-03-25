<script setup>
import BigTitle from "@/components/BigTitle.vue";
import FootLoop from "@/components/FootLoop.vue";
import WaterConserLeft from "@/components/WaterConser/WaterConserView/WaterConserLeft.vue";
import WaterConserMidden from "@/components/WaterConser/WaterConserView/WaterConserMidden.vue";
import WaterConserRight from "@/components/WaterConser/WaterConserView/WaterConserRight.vue";
</script>

<template>
    <div class="WaterConserView">
        <BigTitle id="title"></BigTitle>
        <WaterConserLeft id="WaterConserLeft-out"></WaterConserLeft>
        <WaterConserMidden id="WaterConserMidden-out"></WaterConserMidden>
        <WaterConserRight id="WaterConserRight-out"></WaterConserRight>
        <FootLoop id="FootLoop"></FootLoop>
    </div>
</template>

<style scoped lang="scss">
.WaterConserView {
  width: 100%;
  height: 100%;

  #WaterConserLeft-out {
    width: 25vw;
    height: 80vh;
    margin-top: 4vh;
    margin-left: -0.3vw;
    position: absolute;
  }

  #WaterConserMidden-out {
    width: 40vw;
    height: 80vh;
    margin-top: 4vh;
    margin-left: 28.5vw;
  }

  #WaterConserRight-out {
    top: 0;
    right: 0;
    position: absolute;
    width: 25vw;
    height: 80vh;
    margin-right: 1.5vw;
    margin-top: 14vh;
  }

  #title {
    width: 100%;
  }

  #FootLoop {
    margin-top: -14vh;
    position: absolute;
  }
}
</style>