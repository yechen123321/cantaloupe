<script setup>
import ChooseTable from "@/components/SecondView/AnHuiWindTools/ChooseTable.vue";
import AnHuiWindMiddenCenter from "@/components/SecondView/AnHuiWindTools/AnHuiWindMiddenCenter.vue";
import AnHuiWindMiddenDown from "@/components/SecondView/AnHuiWindTools/AnHuiWindMiddenDown.vue";
</script>

<template>
    <div class="AnHuiWindMidden">
        <ChooseTable id="ChooseTable"></ChooseTable>
        <AnHuiWindMiddenCenter id="AnHuiWindMiddenCenter-out"></AnHuiWindMiddenCenter>
        <AnHuiWindMiddenDown id="AnHuiWindMiddenDown-out"></AnHuiWindMiddenDown>
    </div>
</template>

<style scoped lang="scss">
.AnHuiWindMidden {
  width: 100%;
  height: 100%;

  #ChooseTable {
    width: 40vw;
    height: 20vh;
    position: absolute;
  }

  #AnHuiWindMiddenCenter-out {
    position: absolute;
    margin-top: 22.5vh;
  }

  #AnHuiWindMiddenDown-out {
    position: absolute;
    margin-top: 54vh;
  }
}
</style>