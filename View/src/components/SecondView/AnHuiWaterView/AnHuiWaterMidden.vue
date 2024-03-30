<script setup>
import ChooseTable from "@/components/SecondView/AnHuiWaterTools/ChooseTable.vue";
import AnHuiWaterMiddenCenter from "@/components/SecondView/AnHuiWaterTools/AnHuiWaterMiddenCenter.vue";
import AnHuiWaterMiddenDown from "@/components/SecondView/AnHuiWaterTools/AnHuiWaterMiddenDown.vue";
</script>

<template>
  <div class="AnHuiWaterMidden">
      <ChooseTable id="ChooseTable"></ChooseTable>
      <AnHuiWaterMiddenCenter id="AnHuiWaterMiddenCenter-out"></AnHuiWaterMiddenCenter>
      <AnHuiWaterMiddenDown id="AnHuiWaterMiddenDown-out"></AnHuiWaterMiddenDown>
  </div>
</template>

<style scoped lang="scss">
.AnHuiWaterMidden{
  width: 100%;
  height: 100%;
  #ChooseTable{
    width: 40vw;
    height: 20vh;
    position: absolute;
  }
  #AnHuiWaterMiddenCenter-out {
    position: absolute;
    margin-top: 22.5vh;
  }

  #AnHuiWaterMiddenDown-out {
    position: absolute;
    margin-top: 54vh;
  }
}
</style>