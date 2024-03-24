<script setup>
import DataAnalysisMiddenTopLeft from "@/components/FourthView/DataAnalysisTools/DataAnalysisMiddenTopLeft.vue";
import DataAnalysisMiddenTopRight from "@/components/FourthView/DataAnalysisTools/DataAnalysisMiddenTopRight.vue";
</script>

<template>
  <div class="DataAnalysisMiddenTop">
      <div class="title">暗暗暗暗暗暗啊啊啊</div>
      <DataAnalysisMiddenTopLeft id="DataAnalysisMiddenTopLeft-out"></DataAnalysisMiddenTopLeft>
      <DataAnalysisMiddenTopRight id="DataAnalysisMiddenTopRight-out"></DataAnalysisMiddenTopRight>
      <img src="../../../assets/pic/midden.png" alt="" class="BackImg">
  </div>
</template>

<style scoped lang="scss">
  .DataAnalysisMiddenTop{
    width: 100%;
    height: 100%;
    #DataAnalysisMiddenTopRight-out{
      width: 15vw;
      height: 38vh;
      right: 0;
      margin-top: 16vh;
      margin-right: -4vw;
      border-left: 2px solid #0d87f6;
      position: absolute;
    }
    #DataAnalysisMiddenTopLeft-out{
      width: 27vw;
      height: 44vh;
      margin-left: 3vw;
      margin-top: 13vh;
      position: absolute;
    }
    .title{
      position: absolute;
      font-weight: bolder;
      font-size: 1.6em;
      color: white;
      margin-left: 4.5vw;
      margin-top: 7.5vh;
    }
    .BackImg{
      width: 48vw;
      height: 63vh;
      position: absolute;
    }
  }
</style>