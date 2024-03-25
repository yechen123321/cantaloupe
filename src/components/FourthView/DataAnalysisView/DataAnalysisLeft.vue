<script setup>
import DataAnalysisLeftTop from "@/components/FourthView/DataAnalysisTools/DataAnalysisLeftTop.vue";
import DataAnalysisLeftDown from "@/components/FourthView/DataAnalysisTools/DataAnalysisLeftDown.vue";
import DataAnalysisLeftMidden from "@/components/FourthView/DataAnalysisTools/DataAnalysisLeftMidden.vue";
</script>

<template>
    <div class="DataAnalysisLeft">
        <DataAnalysisLeftTop id="DataAnalysisLeftTop-out"></DataAnalysisLeftTop>
        <DataAnalysisLeftMidden id="DataAnalysisLeftMidden-out"></DataAnalysisLeftMidden>
        <DataAnalysisLeftDown id="DataAnalysisLeftDown-out"></DataAnalysisLeftDown>
    </div>
</template>

<style scoped lang="scss">
.DataAnalysisLeft {
  width: 100%;
  height: 100%;

  #DataAnalysisLeftMidden-out {
    width: 20vw;
    height: 30vh;
    margin-top: -3.2vh;
    position: absolute;
  }

  #DataAnalysisLeftDown-out {
    width: 20vw;
    height: 30vh;
    position: absolute;
    margin-top: 52vh;
  }

  #DataAnalysisLeftTop-out {
    width: 20vw;
    height: 30vh;
    position: absolute;
    margin-top: 21.5vh;

  }
}
</style>