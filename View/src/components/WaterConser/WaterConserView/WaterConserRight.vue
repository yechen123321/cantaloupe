<script setup>
import WaterConserRightTop from "@/components/WaterConser/WaterConserTools/WaterConserRightTop.vue";
import WaterConserRightDown from "@/components/WaterConser/WaterConserTools/WaterConserRightDown.vue";
</script>

<template>
    <div class="WaterConserRight">
        <WaterConserRightTop id="WaterConserRightTop-out"></WaterConserRightTop>
        <WaterConserRightDown id="WaterConserRightDown-out"></WaterConserRightDown>
    </div>
</template>

<style scoped lang="scss">
.WaterConserRight {
  width: 100%;
  height: 100%;

  #WaterConserRightTop-out {
    width: 30vw;
    height: 30vh;
    position: absolute;
    margin-left: -1.5vw;
    margin-top: -4.5vh;
  }

  #WaterConserRightDown-out {
      width: 40vw;
      height: 20vh;
      position: absolute;
      margin-top: 24.5vh;
      margin-left: -0.5vw;
  }
}
</style>