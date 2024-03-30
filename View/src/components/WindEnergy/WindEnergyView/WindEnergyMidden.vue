<script setup>
import WindEnergyMiddenTop from "@/components/WindEnergy/WindEnergyTools/WindEnergyMiddenTop.vue";
import WindEnergyMiddenDown from "@/components/WindEnergy/WindEnergyTools/WindEnergyMiddenDown.vue";
</script>

<template>
    <div class="WindEnergyMidden">
        <WindEnergyMiddenTop id="WindEnergyMiddenTop-out"></WindEnergyMiddenTop>
        <WindEnergyMiddenDown id="WindEnergyMiddenDown-out"></WindEnergyMiddenDown>
    </div>
</template>

<style scoped lang="scss">
.WindEnergyMidden {
  width: 100%;
  height: 100%;

  #WindEnergyMiddenTop-out {
    width: 42vw;
    height: 48vh;
    margin-top: -1.8vh;
    position: absolute;
    margin-left: 1.1vw;
  }

  #WindEnergyMiddenDown-out {
    width: 44.5vw;
    height: 20vh;
    margin-top: 51vh;
    position: absolute;
    margin-left: 0.7vw;
  }
}
</style>