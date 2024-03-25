<script setup>
import BigTitle from "@/components/BigTitle.vue";
import FootLoop from "@/components/FootLoop.vue";
import SunEnergyLeft from "@/components/SunEnergy/SunEnergyView/SunEnergyLeft.vue";
import SunEnergyMidden from "@/components/SunEnergy/SunEnergyView/SunEnergyMidden.vue";
import SunEnergyRight from "@/components/SunEnergy/SunEnergyView/SunEnergyRight.vue";
</script>

<template>
    <div class="SunEnergyView">
        <BigTitle id="title"></BigTitle>
        <SunEnergyLeft id="SunEnergyLeft-out"></SunEnergyLeft>
        <SunEnergyMidden id="SunEnergyMidden-out"></SunEnergyMidden>
        <SunEnergyRight id="SunEnergyRight-out"></SunEnergyRight>
        <FootLoop id="FootLoop"></FootLoop>
    </div>
</template>

<style scoped lang="scss">
.SunEnergyView {
  width: 100%;
  height: 100%;

  #SunEnergyLeft-out {
    width: 25vw;
    height: 80vh;
    margin-top: 4vh;
    margin-left: -0.3vw;
    position: absolute;
  }

  #SunEnergyMidden-out {
    width: 40vw;
    height: 80vh;
    margin-top: 4vh;
    margin-left: 28.5vw;
  }

  #SunEnergyRight-out {
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