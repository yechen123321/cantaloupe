<script setup>
import ThermalPowerLeftTop from "@/components/ThermalPower/ThermalPowerTools/ThermalPowerLeftTop.vue";
import ThermalPowerLeftCenter from "@/components/ThermalPower/ThermalPowerTools/ThermalPowerLeftCenter.vue";
import ThermalPowerLeftDown from "@/components/ThermalPower/ThermalPowerTools/ThermalPowerLeftDown.vue";
</script>

<template>
    <div class="ThermalPowerLeft">
        <ThermalPowerLeftTop id="ThermalPowerLeftTop-out"></ThermalPowerLeftTop>
        <ThermalPowerLeftCenter id="ThermalPowerLeftCenter-out"></ThermalPowerLeftCenter>
        <ThermalPowerLeftDown id="ThermalPowerLeftDown-out"></ThermalPowerLeftDown>
    </div>
</template>

<style scoped lang="scss">
.ThermalPowerLeft {
  width: 100%;
  height: 100%;

  #ThermalPowerLeftTop-out {
    width: 28vw;
    height: 25vh;
    position: absolute;
    margin-top: -5vh;
  }

  #ThermalPowerLeftCenter-out {
    width: 28vw;
    height: 25vh;
    position: absolute;
    margin-top: 23.4vh;
  }

  #ThermalPowerLeftDown-out {
    width: 28vw;
    height: 25vh;
    position: absolute;
    margin-top: 52vh;
  }
}
</style>