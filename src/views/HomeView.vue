<template>
    <div class="main">
        <big-title id="title"></big-title>
        <first-table id="FirstMainTable"></first-table>
        <china-map id="map"></china-map>
    </div>
</template>

<script setup>
import ChinaMap from "@/components/ChinaMap.vue";
import BigTitle from "@/components/BigTitle.vue";
import FirstTable from "@/components/FirstView/FirstMainTable.vue";
</script>

<style lang="scss">
.main, html{
    width: 100%;
    height: 100%;
    #map{
        width: 75%;
        height: 75%;
        margin-top: 6%;
        margin-left: 12%;
        position: absolute;
    }
    #title{
        width: 100%;
    }
    #FirstMainTable{
        width: 23%;
        height: 20%;
        margin-top: 2%;
        margin-left: 3%;
        position: absolute;
    }

}

</style>