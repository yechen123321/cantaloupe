<script setup>
import AnHuiWindLeftTop from "@/components/SecondView/AnHuiWindTools/AnHuiWindLeftTop.vue";
import AnHuiWindLeftCenter from "@/components/SecondView/AnHuiWindTools/AnHuiWindLeftCenter.vue";
import AnHuiWindLeftDown from "@/components/SecondView/AnHuiWindTools/AnHuiWindLeftDown.vue";
</script>

<template>
    <div class="AnHuiWindLeft">
        <AnHuiWindLeftTop id="AnHuiWindLeftTop-out"></AnHuiWindLeftTop>
        <img src="../../../assets/pic/border3.png" alt="" class="BackImg">
        <AnHuiWindLeftCenter id="AnHuiWindLeftCenter-out"></AnHuiWindLeftCenter>
        <AnHuiWindLeftDown id="AnHuiWindLeftDown-out"></AnHuiWindLeftDown>
    </div>
</template>

<style scoped lang="scss">
.AnHuiWindLeft {
  width: 100%;
  height: 100%;

  #AnHuiWindLeftTop-out {
    width: 26vw;
    height: 24vh;
    position: absolute;
    margin-top: 4vh;
  }

  #AnHuiWindLeftCenter-out {
    width: 26vw;
    height: 24vh;
    position: absolute;
    margin-top: -81.5vh;
  }

  #AnHuiWindLeftDown-out {
    width: 26vw;
    height: 24vh;
    position: absolute;
    margin-left: -0.4vw;
    margin-top: -27vh;
  }

  .BackImg {
    width: 26vw;
    height: 57vh;
  }
}
</style>