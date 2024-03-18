<script setup>
import ChooseTable from "@/components/SecondView/AnHuiSunTools/ChooseTable.vue";
import AnHuiSunMiddenCenter from "@/components/SecondView/AnHuiSunTools/AnHuiSunMiddenCenter.vue";
import AnHuiSunMiddenDown from "@/components/SecondView/AnHuiSunTools/AnHuiSunMiddenDown.vue";
</script>

<template>
  <div class="AnHuiSunMidden">
      <ChooseTable id="ChooseTable-out"></ChooseTable>
      <AnHuiSunMiddenCenter id="AnHuiSunMiddenCenter-out"></AnHuiSunMiddenCenter>
      <AnHuiSunMiddenDown id="AnHuiSunMiddenDown-out"></AnHuiSunMiddenDown>
  </div>
</template>

<style scoped lang="scss">
.AnHuiSunMidden{
  width: 100%;
  height: 100%;
  #ChooseTable-out{
    width: 40vw;
    height: 20vh;
    position: absolute;
    //background: red;
  }
  #AnHuiSunMiddenCenter-out{
    position: absolute;
    margin-top: 22.5vh;
  }
  #AnHuiSunMiddenDown-out{
    position: absolute;
    margin-top: 54vh;
  }
}
</style>