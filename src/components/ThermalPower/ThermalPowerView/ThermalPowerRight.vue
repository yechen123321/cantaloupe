<script setup>
import ThermalPowerRightTop from "@/components/ThermalPower/ThermalPowerTools/ThermalPowerRightTop.vue";
import ThermalPowerRightDown from "@/components/ThermalPower/ThermalPowerTools/ThermalPowerRightDown.vue";
</script>

<template>
    <div class="ThermalPowerRight">
        <ThermalPowerRightTop id="ThermalPowerRightTop-out"></ThermalPowerRightTop>
        <ThermalPowerRightDown id="ThermalPowerRightDown-out"></ThermalPowerRightDown>
    </div>
</template>

<style scoped lang="scss">
.ThermalPowerRight {
  width: 100%;
  height: 100%;

  #ThermalPowerRightTop-out {
    width: 30vw;
    height: 30vh;
    position: absolute;
    margin-left: -1.5vw;
    margin-top: -4.5vh;
  }

  #ThermalPowerRightDown-out {
    width: 40vw;
    height: 20vh;
    position: absolute;
    margin-top: 24.5vh;
    margin-left: -0.5vw;
  }
}
</style>