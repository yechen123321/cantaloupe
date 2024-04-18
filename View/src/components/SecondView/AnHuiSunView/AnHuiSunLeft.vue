<script setup>
import AnHuiSunLeftTop from "@/components/SecondView/AnHuiSunTools/AnHuiSunLeftTop.vue"
import AnHuiSunLeftCenter from "@/components/SecondView/AnHuiSunTools/AnHuiSunLeftCenter.vue";
import AnHuiSunLeftDown from "@/components/SecondView/AnHuiSunTools/AnHuiSunLeftDown.vue";
</script>

<template>
    <div class="AnHuiSunLeft">
        <AnHuiSunLeftTop id="AnHuiSunLeftTop"></AnHuiSunLeftTop>
        <AnHuiSunLeftCenter id="AnHuiSunLeftCenter"></AnHuiSunLeftCenter>
        <img src="../../../assets/pic/border3.png" alt="" class="BackImg">
        <AnHuiSunLeftDown id="AnHuiSunLeftDown"></AnHuiSunLeftDown>
    </div>
</template>

<style scoped lang="scss">
.AnHuiSunLeft {
  width: 100%;
  height: 100%;

  #AnHuiSunLeftTop {
    width: 26vw;
    height: 26vh;
    position: absolute;
    margin-top: -23vh;
  }

  #AnHuiSunLeftCenter {
    width: 26vw;
    height: 24vh;
    position: absolute;
    margin-top: 3vh;
  }

  #AnHuiSunLeftDown {
    width: 26vw;
    height: 24vh;
    position: absolute;
    margin-left: -0.4vw;
    margin-top: -30vh;
  }

  .BackImg {
    width: 26vw;
    height: 58vh;
  }
}
</style>