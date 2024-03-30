<script setup>
import SunEnergyLeftTop from "@/components/SunEnergy/SunEnergyTools/SunEnergyLeftTop.vue";
import SunEnergyLeftCenter from "@/components/SunEnergy/SunEnergyTools/SunEnergyLeftCenter.vue";
import SunEnergyLeftDown from "@/components/SunEnergy/SunEnergyTools/SunEnergyLeftDown.vue";
</script>

<template>
    <div class="SunEnergyLeft">
        <SunEnergyLeftTop id="SunEnergyLeftTop-out"></SunEnergyLeftTop>
        <SunEnergyLeftCenter id="SunEnergyLeftCenter-out"></SunEnergyLeftCenter>
        <SunEnergyLeftDown id="SunEnergyLeftDown-out"></SunEnergyLeftDown>
    </div>
</template>

<style scoped lang="scss">
.SunEnergyLeft {
  width: 100%;
  height: 100%;

  #SunEnergyLeftTop-out {
    width: 28vw;
    height: 25vh;
    position: absolute;
    margin-top: -5vh;
  }

  #SunEnergyLeftCenter-out {
    width: 28vw;
    height: 25vh;
    position: absolute;
    margin-top: 23.4vh;
  }

  #SunEnergyLeftDown-out {
    width: 28vw;
    height: 25vh;
    position: absolute;
    margin-top: 52vh;
  }
}
</style>