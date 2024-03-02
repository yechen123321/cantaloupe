<script setup>
import BigTitle from "@/components/BigTitle.vue";
import FootLoop from '@/components/FootLoop.vue';
</script>

<template>
    <div class="CityMain">
        <BigTitle id="BigTitle"></BigTitle>
        <FootLoop id="FootLoop"></FootLoop>
    </div>
</template>

<style scoped lang="scss">
.CityMain{
    #BigTitle{
        width: 100vw;
    }

    #FootLoop {
        position: absolute;
        margin-top: 70vh;
    }
}
</style>