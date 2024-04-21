<script setup>
import AnHuiLeftTop from "@/components/SecondView/AnHuiRenewViewTools/AnHuiLeftTop.vue";
import AnHuiLeftMidden from "@/components/SecondView/AnHuiRenewViewTools/AnHuiLeftMidden.vue";
import AnHuiLeftDown from "@/components/SecondView/AnHuiRenewViewTools/AnHuiLeftDown.vue";
</script>

<template>
    <div class="SecondLeftTable">
        <AnHuiLeftTop id="AnHuiLeftTop-out"></AnHuiLeftTop>
        <AnHuiLeftMidden id="AnHuiLeftMidden-out"></AnHuiLeftMidden>
        <img class="BackImg" src="../../../assets/pic/border3.png" alt="">
        <AnHuiLeftDown id="AnHuiLeftDown-out"></AnHuiLeftDown>
    </div>
</template>

<style scoped lang="scss">
.SecondLeftTable {
  width: 25vw;
  //background: green;
  height: 80vh;

  #AnHuiLeftTop-out {
    width: 23vw;
    height: 23vh;
    margin-left: -2.15vw;
    position: absolute;
    margin-top: 5vh;
  }

  #AnHuiLeftMidden-out {
    width: 23vw;
    height: 23vh;
    margin-left: 1.3vw;
    margin-top: 29vh;
    position: absolute;
  }

  #AnHuiLeftDown-out {
    width: 23vw;
    height: 23vh;
    //margin-left: 0vw;
    position: absolute;
    margin-top: -32vh;
  }

  .BackImg {
    width: 26vw;
    height: 58vh;
    margin-top: 25vh;
  }
}
</style>