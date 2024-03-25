<script setup>
import WindEnergyLeftTop from "@/components/WindEnergy/WindEnergyTools/WindEnergyLeftTop.vue";
import WindEnergyLeftCenter from "@/components/WindEnergy/WindEnergyTools/WindEnergyLeftCenter.vue";
import WindEnergyLeftDown from "@/components/WindEnergy/WindEnergyTools/WindEnergyLeftDown.vue";
</script>

<template>
    <div class="WindEnergyLeft">
        <WindEnergyLeftTop id="WindEnergyLeftTop-out"></WindEnergyLeftTop>
        <WindEnergyLeftCenter id="WindEnergyLeftCenter-out"></WindEnergyLeftCenter>
        <WindEnergyLeftDown id="WindEnergyLeftDown-out"></WindEnergyLeftDown>
    </div>
</template>

<style scoped lang="scss">
.WindEnergyLeft {
  width: 100%;
  height: 100%;

  #WindEnergyLeftTop-out {
    width: 28vw;
    height: 25vh;
    position: absolute;
    margin-top: -5vh;
  }

  #WindEnergyLeftCenter-out {
    width: 28vw;
    height: 25vh;
    position: absolute;
    margin-top: 23.4vh;
  }

  #WindEnergyLeftDown-out {
    width: 28vw;
    height: 25vh;
    position: absolute;
    margin-top: 52vh;
  }
}
</style>