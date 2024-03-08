<script setup>
import MainDownLeft from "@/components/FirstView/FirstViewTools/MainDownLeft.vue";
import MainDownSea from "@/components/FirstView/FirstViewTools/MainDownSea.vue";
import MainDownRight from "@/components/FirstView/FirstViewTools/MainDownRight.vue";
</script>

<template>
    <div class="MainDown">
        <MainDownLeft id="MainDownLeft-out"></MainDownLeft>
        <MainDownSea id="MainDownSea-out"></MainDownSea>
        <MainDownRight id="MainDownRight-out"></MainDownRight>
        <img class="BackImg" src="../../assets/pic/right.png" alt="">
    </div>

</template>

<style scoped lang="scss">
.MainDown {
  width: 100vw;
  height: 100vh;

  #MainDownLeft-out {
    width: 25vw;
    height: 26vh;
    position: absolute;
    margin-top: 32vh;
    margin-left: 4vw;
  }

  #MainDownSea-out {
    width: 25vw;
    height: 28vh;
    position: absolute;
    margin-top: 34vh;
    margin-left: 27vw;
  }

  #MainDownRight-out {
    width: 25vw;
    height: 28vh;
    position: absolute;
    margin-top: 30vh;
    margin-left: 47vw;

  }

  .BackImg {
    width: 74vw;
    height: 46vh;
  }
}
</style>