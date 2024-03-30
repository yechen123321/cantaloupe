<script setup>
import AnHuiLimitLeftTop from "@/components/ThirdView/AnHuiLimitTools/AnHuiLimitLeftTop.vue";
import AnHuiLimitLeftMidden from "@/components/ThirdView/AnHuiLimitTools/AnHuiLimitLeftMidden.vue";
import AnHuiLimitLeftDown from "@/components/ThirdView/AnHuiLimitTools/AnHuiLimitLeftDown.vue";
</script>

<template>
    <div class="AnHuiLimitLeft">
        <AnHuiLimitLeftTop id="AnHuiLimitLeftTop-out"></AnHuiLimitLeftTop>
        <AnHuiLimitLeftMidden id="AnHuiLimitLeftMidden-out"></AnHuiLimitLeftMidden>
        <AnHuiLimitLeftDown id="AnHuiLimitLeftDown-out"></AnHuiLimitLeftDown>
        <img src="../../../assets/pic/border3.png" alt="" class="BackImg">
    </div>
</template>

<style scoped lang="scss">
.AnHuiLimitLeft {
  width: 100%;
  height: 100%;

  #AnHuiLimitLeftDown-out {
    width: 24vw;
    height: 20vh;
    margin-top: 54.5vh;
    position: absolute;
  }

  #AnHuiLimitLeftMidden-out {
    width: 24vw;
    height: 20vh;
    margin-top: 27.5vh;
    position: absolute;
  }

  #AnHuiLimitLeftTop-out {
    width: 24vw;
    height: 20vh;
    margin-top: 4.5vh;
    position: absolute;
  }

  .BackImg {
    width: 26vw;
    height: 84vh;
  }
}
</style>