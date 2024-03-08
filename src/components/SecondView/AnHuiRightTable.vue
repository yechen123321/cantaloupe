<script setup>
import AnHuiRightTop from "@/components/SecondView/AnHuiViewTools/AnHuiRightTop.vue";
</script>

<template>
    <div class="SecondRightTable">
        <AnHuiRightTop id="AnHuiRightTop-out"></AnHuiRightTop>
        <img class="BackImg" src="../../assets/pic/border3.png" alt="">

    </div>
</template>

<style scoped lang="scss">
.SecondRightTable {
  width: 23vw;
  height: 80vh;
  //background: red;
    #AnHuiRightTop-out{
        position: absolute;
        width: 30vw;
        height: 23vh;

    }
  .BackImg {
    width: 26vw;
    height: 82vh;
  }
}
</style>