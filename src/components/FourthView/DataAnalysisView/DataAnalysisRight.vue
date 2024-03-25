<script setup>
import DataAnalysisRightTop from "@/components/FourthView/DataAnalysisTools/DataAnalysisRightTop.vue";
import DataAnalysisRightDown from "@/components/FourthView/DataAnalysisTools/DataAnalysisRightDown.vue";
</script>

<template>
  <div class="DataAnalysisRight">
    <DataAnalysisRightTop id="DataAnalysisRightTop-out"></DataAnalysisRightTop>
      <DataAnalysisRightDown id="DataAnalysisRightDown-out"></DataAnalysisRightDown>
  </div>
</template>

<style scoped lang="scss">
.DataAnalysisRight{
  width: 100%;
  height: 100%;
  #DataAnalysisRightDown-out{
    width: 25vw;
    height: 50vh;
    position: absolute;
    margin-top: 27.3vh;
  }
  #DataAnalysisRightTop-out{
    width: 25vw;
    height: 27vh;
    position: absolute;
  }
}
</style>