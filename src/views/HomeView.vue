<template>
    <div class="main">
        <big-title id="title"></big-title>
        <MainRightTop id="MainRightTop"></MainRightTop>
        <MainRightButtom id="MainRightButtom"></MainRightButtom>
        <MainLeftTable id="MainLeftTable"></MainLeftTable>
        <china-map id="map"></china-map>
        <MainDown id="MainDown"></MainDown>
        <FootLoop id="FootLoop"></FootLoop>
    </div>
</template>

<script setup>
import ChinaMap from "@/components/ChinaMap.vue";
import BigTitle from "@/components/BigTitle.vue";
import MainRightTop from "@/components/FirstView/MainRightTop.vue";
import MainRightButtom from "@/components/FirstView/MainRightButtom.vue";
import MainLeftTable from "@/components/FirstView/MainLeftTable.vue";
import FootLoop from '@/components/FootLoop.vue'
import MainDown from "@/components/FirstView/MainDown.vue";
</script>

<style lang="scss">
.main, html {
  width: 100vw;
  height: 100vh;

  #map {
    width: 45vw;
    height: 45vh;
    margin-top: 1vw;
    margin-left: 39vw;
    position: absolute;
  }

  #title {
    width: 100vw;
  }

  #MainRightTop {
    width: 23vw;
    height: 10vh;
    margin-top: 5vh;
    margin-right: 2vw;
    right: 0;
    position: absolute;
      z-index: 126;
  }

  #MainRightButtom {
    width: 23vw;
    height: 20vh;
    margin-top: 22.5vh;
    margin-right: 2vw;
    right: 0;
    position: absolute;
  }

  #MainLeftTable {
    width: 23vw;
    height: 22vh;
    margin-top: 3vh;
    margin-left: 2vw;
    position: absolute;
    z-index: 124;
  }

  #MainDown {
    width: 68vw;
    height: 42vh;
    right: 0;
    margin-top: 44vh;
    margin-right: 5vw;
    position: absolute;
    z-index: 124;
  }

  #FootLoop {
    position: absolute;
    margin-top: 70vh;
  }
}

</style>