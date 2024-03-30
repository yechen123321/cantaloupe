<script setup>
import SunEnergyMiddenTop from "@/components/SunEnergy/SunEnergyTools/SunEnergyMiddenTop.vue";
import SunEnergyMiddenDown from "@/components/SunEnergy/SunEnergyTools/SunEnergyMiddenDown.vue";
</script>

<template>
    <div class="SunEnergyMidden">
        <SunEnergyMiddenTop id="SunEnergyMiddenTop-out"></SunEnergyMiddenTop>
        <SunEnergyMiddenDown id="SunEnergyMiddenDown-out"></SunEnergyMiddenDown>
    </div>
</template>

<style scoped lang="scss">
.SunEnergyMidden {
  width: 100%;
  height: 100%;

  #SunEnergyMiddenTop-out {
    width: 42vw;
    height: 48vh;
    margin-top: -1.8vh;
    position: absolute;
    margin-left: 1.1vw;
  }

  #SunEnergyMiddenDown-out {
    width: 44.5vw;
    height: 20vh;
    margin-top: 51vh;
    position: absolute;
    margin-left: 0.7vw;
  }
}
</style>