<script setup>
import BigTitle from "@/components/BigTitle.vue";
import FootLoop from "@/components/FootLoop.vue";
import ThermalPowerLeft from "@/components/ThermalPower/ThermalPowerView/ThermalPowerLeft.vue";
import ThermalPowerMidden from "@/components/ThermalPower/ThermalPowerView/ThermalPowerMidden.vue";
import ThermalPowerRight from "@/components/ThermalPower/ThermalPowerView/ThermalPowerRight.vue";
</script>

<template>
    <div class="ThermalPowerView">
        <BigTitle id="title"></BigTitle>
        <ThermalPowerLeft id="ThermalPowerLeft-out"></ThermalPowerLeft>
        <ThermalPowerMidden id="ThermalPowerMidden-out"></ThermalPowerMidden>
        <ThermalPowerRight id="ThermalPowerRight-out"></ThermalPowerRight>
        <FootLoop id="FootLoop"></FootLoop>
    </div>
</template>

<style scoped lang="scss">
.ThermalPowerView {
  width: 100%;
  height: 100%;

  #ThermalPowerLeft-out {
    width: 25vw;
    height: 80vh;
    margin-top: 4vh;
    margin-left: -0.3vw;
    position: absolute;
  }

  #ThermalPowerMidden-out {
    width: 40vw;
    height: 80vh;
    margin-top: 4vh;
    margin-left: 28.5vw;
  }

  #ThermalPowerRight-out {
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