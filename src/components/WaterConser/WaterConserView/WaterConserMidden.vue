<script setup>
import WaterConserMiddenTop from "@/components/WaterConser/WaterConserTools/WaterConserMiddenTop.vue";
import WaterConserMiddenDown from "@/components/WaterConser/WaterConserTools/WaterConserMiddenDown.vue";
</script>

<template>
    <div class="WaterConserMidden">
        <WaterConserMiddenTop id="WaterConserMiddenTop-out"></WaterConserMiddenTop>
        <WaterConserMiddenDown id="WaterConserMiddenDown-out"></WaterConserMiddenDown>
    </div>
</template>

<style scoped lang="scss">
.WaterConserMidden {
  width: 100%;
  height: 100%;

  #WaterConserMiddenTop-out {
    width: 42vw;
    height: 48vh;
    margin-top: -1.8vh;
    position: absolute;
    margin-left: 1.1vw;
  }

  #WaterConserMiddenDown-out {
    width: 44.5vw;
    height: 20vh;
    margin-top: 51vh;
    position: absolute;
    margin-left: 0.7vw;
  }
}
</style>