<script setup>
import WaterConserLeftTop from "@/components/WaterConser/WaterConserTools/WaterConserLeftTop.vue";
import WaterConserLeftCenter from "@/components/WaterConser/WaterConserTools/WaterConserLeftCenter.vue";
import WaterConserLeftDown from "@/components/WaterConser/WaterConserTools/WaterConserLeftDown.vue";
</script>

<template>
    <div class="WaterConserLeft">
        <WaterConserLeftTop id="WaterConserLeftTop-out"></WaterConserLeftTop>
        <WaterConserLeftCenter id="WaterConserLeftCenter-out"></WaterConserLeftCenter>
        <WaterConserLeftDown id="WaterConserLeftDown-out"></WaterConserLeftDown>
    </div>
</template>

<style scoped lang="scss">
.WaterConserLeft {
  width: 100%;
  height: 100%;

  #WaterConserLeftTop-out {
    width: 28vw;
    height: 25vh;
    position: absolute;
    margin-top: -5vh;
  }

  #WaterConserLeftCenter-out {
    width: 28vw;
    height: 25vh;
    position: absolute;
    margin-top: 23.4vh;
  }

  #WaterConserLeftDown-out {
    width: 28vw;
    height: 25vh;
    position: absolute;
    margin-top: 52vh;
  }
}
</style>