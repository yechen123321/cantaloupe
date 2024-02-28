<template>
    <div class="main">
        <big-title id="title"></big-title>
        <MainRightTop id="MainRightTop"></MainRightTop>
        <MainLeftTable id="MainLeftTable"></MainLeftTable>
<!--        <ThirdMainTable id="ThirdMainTable"></ThirdMainTable>-->
<!--        <FourthMainTable id="FourthMainTable"></FourthMainTable>-->
<!--        <FifthMainTable id="FifthMainTable"></FifthMainTable>-->
        <china-map id="map"></china-map>
        <FootLoop id="FootLoop"></FootLoop>
    </div>
</template>

<script setup>
import ChinaMap from "@/components/ChinaMap.vue";
import BigTitle from "@/components/BigTitle.vue";
import MainRightTop from "@/components/FirstView/MainRightTop.vue";
import MainLeftTable from "@/components/FirstView/MainLeftTable.vue";
import FootLoop from '@/components/FootLoop.vue'

</script>

<style lang="scss">
.main, html{
    width: 100vw;
    height: 100vh;
    #map{
        width: 45vw;
        height: 45vh;
        margin-top: 1vw;
        margin-left: 27vw;
        position: absolute;
    }
    #title{
        width: 100vw;
    }
    #MainRightTop{
        width: 23vw;
        height: 10vh;
        margin-top: 5vh;
        margin-right: 5vw;
        right: 0;
        position: absolute;
    }
    #MainLeftTable{
        width: 23vw;
        height: 22vh;
        margin-top: 3vh;
        margin-left: 5vw;
        position: absolute;
        z-index: 124;
    }

    #FootLoop{
        position: absolute;
        margin-top: 70vh;
    }
}

</style>