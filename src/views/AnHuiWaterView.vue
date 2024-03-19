<script setup>
import BigTitle from "@/components/BigTitle.vue";
import FootLoop from "@/components/FootLoop.vue";
</script>

<template>
  <div class="AnHuiWaterView">
      <BigTitle id="title"></BigTitle>

<!--      <FootLoop id="FootLoop"></FootLoop>-->
  </div>
</template>

<style scoped lang="scss">
  .AnHuiWaterView{
    width: 100%;
    height: 100%;

    #title {
      width: 100vw;
    }

    //#FootLoop {
    //  position: absolute;
    //  margin-top: -14vh;
    //}
  }
</style>