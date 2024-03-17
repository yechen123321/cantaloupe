<script setup>
import ChooseTable from "@/components/SecondView/AnHuiRenewViewTools/ChooseTable.vue";
import SecondMiddenCenter from "@/components/SecondView/AnHuiRenewViewTools/AnHuiMiddenCenter.vue";
import SecondMiddenDown from "@/components/SecondView/AnHuiRenewViewTools/AnHuiMiddenDown.vue";
</script>

<template>
    <div class="SecondMidden">
        <ChooseTable id="ChooseTable-out"></ChooseTable>
        <SecondMiddenCenter id="SecondMiddenCenter-out"></SecondMiddenCenter>
        <SecondMiddenDown id="SecondMiddenDown-out"></SecondMiddenDown>
    </div>
</template>

<style scoped lang="scss">
.SecondMidden {
  width: 100vw;
  height: 100vh;
  //background: white;
  #ChooseTable-out {
    width: 40vw;
    height: 20vh;
  }

  #SecondMiddenCenter-out {
    margin-top: 2vh;
    width: 40vw;
    height: 20vh;
  }

  #SecondMiddenDown-out {
    margin-top: 11vh;
    width: 40vw;
    height: 20vh;
  }
}
</style>