<template>
    <div class="main">
        <big-title id="title"></big-title>
        <FirstMainTable id="FirstMainTable"></FirstMainTable>
        <SecondMainTable id="SecondMainTable"></SecondMainTable>
        <ThirdMainTable id="ThirdMainTable"></ThirdMainTable>
        <FourthMainTable id="FourthMainTable"></FourthMainTable>
        <china-map id="map"></china-map>
    </div>
</template>

<script setup>
import ChinaMap from "@/components/ChinaMap.vue";
import BigTitle from "@/components/BigTitle.vue";
import FirstMainTable from "@/components/FirstView/FirstMainTable.vue";
import SecondMainTable from "@/components/FirstView/SecondMainTable.vue";
import ThirdMainTable from "@/components/FirstView/ThirdMainTable.vue";
import FourthMainTable from "@/components/FirstView/FourthMainTable.vue";
</script>

<style lang="scss">
.main, html{
    width: 100vw;
    height: 100vh;
    #map{
        width: 70vw;
        height: 70vh;
        margin-top: 6.5vw;
        margin-left: 15vw;
        position: absolute;
    }
    #title{
        width: 100vw;
    }
    #FirstMainTable{
        width: 23vw;
        height: 10vh;
        margin-top: 1.5vh;
        margin-left: 3vw;
        position: absolute;
    }
    #SecondMainTable{
        width: 23vw;
        height: 22vh;
        margin-top: 15vh;
        margin-left: 3vw;
        position: absolute;
        z-index: 123;
    }
    #ThirdMainTable{
        width: 23vw;
        height: 22vh;
        margin-top: 40.7vh;
        margin-left: 3vw;
        position: absolute;
        z-index: 123;
    }
    #FourthMainTable{
        width: 23vw;
        height: 22vh;
        margin-top: 66.5vh;
        margin-left: 3vw;
        position: absolute;
        z-index: 123;
    }
}

</style>