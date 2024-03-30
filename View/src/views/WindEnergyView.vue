<script setup>
import BigTitle from "@/components/BigTitle.vue";
import FootLoop from "@/components/FootLoop.vue";
import WindEnergyLeft from "@/components/WindEnergy/WindEnergyView/WindEnergyLeft.vue";
import WindEnergyMidden from "@/components/WindEnergy/WindEnergyView/WindEnergyMidden.vue";
import WindEnergyRight from "@/components/WindEnergy/WindEnergyView/WindEnergyRight.vue";
</script>

<template>
    <div class="WindEnergyView">
        <BigTitle id="title"></BigTitle>
        <WindEnergyLeft id="WindEnergyLeft-out"></WindEnergyLeft>
        <WindEnergyMidden id="WindEnergyMidden-out"></WindEnergyMidden>
        <WindEnergyRight id="WindEnergyRight-out"></WindEnergyRight>
        <FootLoop id="FootLoop"></FootLoop>
    </div>
</template>

<style scoped lang="scss">
.WindEnergyView {
  width: 100%;
  height: 100%;

  #WindEnergyLeft-out {
    width: 25vw;
    height: 80vh;
    margin-top: 4vh;
    margin-left: -0.3vw;
    position: absolute;
  }

  #WindEnergyMidden-out {
    width: 40vw;
    height: 80vh;
    margin-top: 4vh;
    margin-left: 28.5vw;
  }

  #WindEnergyRight-out {
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