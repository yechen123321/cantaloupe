<script setup>
import ThermalPowerMiddenTop from "@/components/ThermalPower/ThermalPowerTools/ThermalPowerMiddenTop.vue";
import ThermalPowerMiddenDown from "@/components/ThermalPower/ThermalPowerTools/ThermalPowerMiddenDown.vue";
</script>

<template>
    <div class="ThermalPowerMidden">
        <ThermalPowerMiddenTop id="ThermalPowerMiddenTop-out"></ThermalPowerMiddenTop>
        <ThermalPowerMiddenDown id="ThermalPowerMiddenDown-out"></ThermalPowerMiddenDown>
    </div>
</template>

<style scoped lang="scss">
.ThermalPowerMidden {
  width: 100%;
  height: 100%;

  #ThermalPowerMiddenTop-out {
    width: 42vw;
    height: 48vh;
    margin-top: -1.8vh;
    position: absolute;
    margin-left: 1.1vw;
  }

  #ThermalPowerMiddenDown-out {
    width: 44.5vw;
    height: 20vh;
    margin-top: 51vh;
    position: absolute;
    margin-left: 0.7vw;
  }
}
</style>