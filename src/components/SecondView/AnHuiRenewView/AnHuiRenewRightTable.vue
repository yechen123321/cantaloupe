<script setup>
import AnHuiRightDownFirst from "@/components/SecondView/AnHuiRenewViewTools/AnHuiRightDownFirst.vue";
import AnHuiRightDownSecond from "@/components/SecondView/AnHuiRenewViewTools/AnHuiRightDownSecond.vue";
</script>

<template>
    <div class="SecondRightTable">
        <img class="BackImg" src="../../../assets/pic/border3.png" alt="">
        <AnHuiRightDownFirst id="AnHuiRightDownFirst-out"></AnHuiRightDownFirst>
        <AnHuiRightDownSecond id="AnHuiRightDownFirst-out"></AnHuiRightDownSecond>
    </div>
</template>

<style scoped lang="scss">
.SecondRightTable {
  width: 23vw;
  height: 80vh;
  //background: red;
    #AnHuiRightDownFirst-out{
        position: absolute;
        width: 21vw;
        height: 26vh;
        border-bottom: 1px solid #0d87f6;
        //background: red;
        margin-top: -55vh;
        margin-left: 2.5vw;
    }

    #AnHuiRightDownSecond-out{
        position: absolute;
        width: 21vw;
        height: 26vh;
        margin-left: 2.5vw;
    }
  #AnHuiRightDown {
    width: 23vw;
    height: 23vh;
    position: absolute;
    margin-top: -30vh;
  }

  .BackImg {
    width: 26vw;
    height: 58vh;
  }
}
</style>