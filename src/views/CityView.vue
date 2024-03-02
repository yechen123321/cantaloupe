<script setup>
import BigTitle from "@/components/BigTitle.vue";
import FootLoop from '@/components/FootLoop.vue';
import ChooseTable from "@/components/SecondView/ChooseTable.vue";
</script>

<template>
    <div class="CityMain">
        <BigTitle id="BigTitle"></BigTitle>
        <FootLoop id="FootLoop"></FootLoop>
        <ChooseTable id="ChooseTable"></ChooseTable>
    </div>
</template>

<style scoped lang="scss">
.CityMain{
    #BigTitle{
        width: 100vw;
    }

    #ChooseTable{
        width: 2vw;
        height: 1vh;
    }

    #FootLoop {
        position: absolute;
        margin-top: 70vh;
    }
}
</style>