<script setup>
import BigTitle from "@/components/BigTitle.vue";
import FootLoop from "@/components/FootLoop.vue";
import DataAnalysisLeft from "@/components/FourthView/DataAnalysisView/DataAnalysisLeft.vue";
import DataAnalysisMidden from "@/components/FourthView/DataAnalysisView/DataAnalysisMidden.vue";
import DataAnalysisRight from "@/components/FourthView/DataAnalysisView/DataAnalysisRight.vue";
</script>

<template>
    <div class="DataAnalysisView">
        <BigTitle id="title"></BigTitle>
        <FootLoop id="FootLoop"></FootLoop>
        <DataAnalysisLeft id="DataAnalysisLeft-out"></DataAnalysisLeft>
        <DataAnalysisMidden id="DataAnalysisMidden-out"></DataAnalysisMidden>
        <DataAnalysisRight id="DataAnalysisRight-out"></DataAnalysisRight>
    </div>
</template>

<style scoped lang="scss">
.DataAnalysisView {
  width: 100%;
  height: 100%;

  #DataAnalysisRight-out {
    width: 23vw;
    height: 80vh;
    margin-top: 0vh;
    right: 0;
    margin-right: 3vw;
    //background: red;
    position: absolute;
  }

  #DataAnalysisMidden-out {
    width: 45vw;
    height: 84vh;
    margin-top: 2vh;
    margin-left: 30vw;
    //background: red;
    position: absolute;
  }

  #DataAnalysisLeft-out {
    width: 25vw;
    height: 80vh;
    margin-top: 2vh;
    margin-left: 0.5vw;
    //background: red;
    position: absolute;
  }

  #title {
    width: 100vw;
  }

  #FootLoop {
    position: absolute;
    margin-top: 70vh;
  }
}
</style>