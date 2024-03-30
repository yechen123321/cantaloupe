<script setup>
import AnHuiWaterLeftTop from "@/components/SecondView/AnHuiWaterTools/AnHuiWaterLeftTop.vue";
import AnHuiWaterLeftCenter from "@/components/SecondView/AnHuiWaterTools/AnHuiWaterLeftCenter.vue";
import AnHuiWaterLeftDown from "@/components/SecondView/AnHuiWaterTools/AnHuiWaterLeftDown.vue";
</script>

<template>
  <div class="AnHuiWaterLeft">
      <AnHuiWaterLeftTop id="AnHuiWaterLeftTop-out"></AnHuiWaterLeftTop>
      <img src="../../../assets/pic/border3.png" alt="" class="BackImg">
      <AnHuiWaterLeftCenter id="AnHuiWaterLeftCenter-out"></AnHuiWaterLeftCenter>
      <AnHuiWaterLeftDown id="AnHuiWaterLeftDown-out"></AnHuiWaterLeftDown>
  </div>
</template>

<style scoped lang="scss">
.AnHuiWaterLeft{
  width: 100%;
  height: 100%;
  #AnHuiWaterLeftTop-out{
    width: 26vw;
    height: 24vh;
    position: absolute;
    //background: red;
    margin-top: 4vh;
    //margin-left: 2vw;
  }
  #AnHuiWaterLeftCenter-out{
    width: 26vw;
    height: 24vh;
    position: absolute;
    //background: #00ff24;
    margin-top: -51.7vh;
  }
  #AnHuiWaterLeftDown-out{
    width: 26vw;
    height: 24vh;
    position: absolute;
    //background: #ffe800;
    margin-left: -0.4vw;
    margin-top: -29vh;
  }
  .BackImg{
    width: 26vw;
    height: 82vh;
  }
}
</style>