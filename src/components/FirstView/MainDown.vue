<script setup>
import MainDownLeft from "@/components/FirstView/MainDownLeft.vue";
import MainDownSea from "@/components/FirstView/MainDownSea.vue";
import MainDownRight from "@/components/FirstView/MainDownRight.vue";
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
    margin-top: 30vh;
    margin-left: 4vw;
  }

  #MainDownMidden-out {
    width: 25vw;
    height: 26vh;
    position: absolute;
    margin-top: 30vh;
    margin-left: 30vw;
  }

  #MainDownSea-out {
    width: 25vw;
    height: 26vh;
    position: absolute;
    margin-top: 30vh;
    margin-left: 26.5vw;
  }

  #MainDownRight-out {
    width: 25vw;
    height: 26vh;
    position: absolute;
    margin-top: 30vh;
    margin-left: 48vw;
  }

  .BackImg {
    width: 74vw;
    height: 42vh;
  }
}
</style>