<script setup>
import BigTitle from "@/components/BigTitle.vue";
import FootLoop from "@/components/FootLoop.vue";
import DataAnalysisLeft from "@/components/FourthView/DataAnalysisView/DataAnalysisLeft.vue";
</script>

<template>
  <div class="DataAnalysisView">
      <BigTitle id="title"></BigTitle>
      <FootLoop id="FootLoop"></FootLoop>
      <DataAnalysisLeft id="DataAnalysisLeft-out"></DataAnalysisLeft>
  </div>
</template>

<style scoped lang="scss">
  .DataAnalysisView{
    width: 100%;
    height: 100%;
    #DataAnalysisLeft-out{
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