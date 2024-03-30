<script setup>
import WindEnergyRightTop from "@/components/WindEnergy/WindEnergyTools/WindEnergyRightTop.vue";
import WindEnergyRightDown from "@/components/WindEnergy/WindEnergyTools/WindEnergyRightDown.vue";
</script>

<template>
    <div class="WindEnergyRight">
        <WindEnergyRightTop id="WindEnergyRightTop-out"></WindEnergyRightTop>
        <WindEnergyRightDown id="WindEnergyRightDown-out"></WindEnergyRightDown>
    </div>
</template>

<style scoped lang="scss">
.WindEnergyRight {
  width: 100%;
  height: 100%;

  #WindEnergyRightTop-out {
    width: 30vw;
    height: 30vh;
    position: absolute;
    margin-left: -1.5vw;
    margin-top: -4.5vh;
  }

  #WindEnergyRightDown-out {
      width: 40vw;
      height: 20vh;
      position: absolute;
      margin-top: 24.5vh;
      margin-left: -0.5vw;
  }
}
</style>