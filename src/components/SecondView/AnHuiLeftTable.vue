<script setup>
import AnHuiLeftTop from "@/components/SecondView/AnHuiViewTools/AnHuiLeftTop.vue";
import AnHuiLeftMidden from "@/components/SecondView/AnHuiViewTools/AnHuiLeftMidden.vue";
</script>

<template>
    <div class="SecondLeftTable">
        <AnHuiLeftTop id="AnHuiLeftTop-out"></AnHuiLeftTop>
        <AnHuiLeftMidden id="AnHuiLeftMidden-out"></AnHuiLeftMidden>
        <img class="BackImg" src="../../assets/pic/border3.png" alt="">
    </div>
</template>

<style scoped lang="scss">
.SecondLeftTable {
  width: 25vw;
  //background: green;
  height: 80vh;
    #AnHuiLeftTop-out{
        width: 23vw;
        height: 23vh;
        margin-left: -2.15vw;
        position: absolute;
        margin-top: 5vh;
    }
    #AnHuiLeftMidden-out{
        width: 23vw;
        height: 23vh;
        margin-left: 1.5vw;
        margin-top: 28vh;
        position: absolute;
    }
  .BackImg {
    width: 26vw;
    height: 82vh;
  }
}
</style>