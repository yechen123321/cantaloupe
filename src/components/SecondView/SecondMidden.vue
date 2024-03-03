<script setup>
import ChooseTable from "@/components/SecondView/SecondViewTools/ChooseTable.vue";
import SecondMiddenCenter from "@/components/SecondView/SecondViewTools/SecondMiddenCenter.vue";
</script>

<template>
<div class="SecondMidden">
    <ChooseTable id="ChooseTable"></ChooseTable>
    <SecondMiddenCenter id="SecondMiddenCenter"></SecondMiddenCenter>
</div>
</template>

<style scoped lang="scss">
  .SecondMidden{
      width: 100vw;
      height: 100vh;
      //background: white;
    #ChooseTable{
        width: 40vw;
        height: 20vh;
    }
      #SecondMiddenCenter{
          margin-top:4vh;
          width: 40vw;
          height: 20vh;
      }
  }
</style>