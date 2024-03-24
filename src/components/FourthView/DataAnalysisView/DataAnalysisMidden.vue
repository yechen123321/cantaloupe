<script setup>
import DataAnalysisMiddenDown from "@/components/FourthView/DataAnalysisTools/DataAnalysisMiddenDown.vue";
import DataAnalysisMiddenTop from "@/components/FourthView/DataAnalysisTools/DataAnalysisMiddenTop.vue";
</script>

<template>
  <div class="DataAnalysisMidden">
    <DataAnalysisMiddenDown id="DataAnalysisMiddenDown-out"></DataAnalysisMiddenDown>
      <DataAnalysisMiddenTop id="DataAnalysisMiddenTop-out"></DataAnalysisMiddenTop>
  </div>
</template>

<style scoped lang="scss">
.DataAnalysisMidden{
  width: 100%;
  height: 100%;
  #DataAnalysisMiddenTop-out{
    width: 40vw;
    height: 40vh;
    position: absolute;
    margin-left: -2vw;
    margin-top: -5vh;
  }
  #DataAnalysisMiddenDown-out{
    position: absolute;
    width: 42.5vw;
    height: 30vh;
    margin-left: 0.5vw;
    margin-top: 56vh;
  }
}
</style>