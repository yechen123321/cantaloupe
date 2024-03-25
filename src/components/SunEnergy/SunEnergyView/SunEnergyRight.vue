<script setup>
import SunEnergyRightTop from "@/components/SunEnergy/SunEnergyTools/SunEnergyRightTop.vue";
import SunEnergyRightDown from "@/components/SunEnergy/SunEnergyTools/SunEnergyRightDown.vue";
</script>

<template>
    <div class="SunEnergyRight">
        <SunEnergyRightTop id="SunEnergyRightTop-out"></SunEnergyRightTop>
        <SunEnergyRightDown id="SunEnergyRightDown-out"></SunEnergyRightDown>
    </div>
</template>

<style scoped lang="scss">
.SunEnergyRight {
  width: 100%;
  height: 100%;

  #SunEnergyRightTop-out {
    width: 30vw;
    height: 30vh;
    position: absolute;
    margin-left: -1.5vw;
    margin-top: -4.5vh;
  }

  #SunEnergyRightDown-out {
    width: 40vw;
    height: 20vh;
    position: absolute;
    margin-top: 28vh;
    margin-left: -0.5vw;
  }
}
</style>