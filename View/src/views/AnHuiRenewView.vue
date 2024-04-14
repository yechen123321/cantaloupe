<script setup>
import BigTitle from "@/components/BigTitle.vue";
import FootLoop from '@/components/FootLoop.vue';
import SecondLeftTable from "@/components/SecondView/AnHuiRenewView/AnHuiRenewLeftTable.vue";
import SecondRightTable from "@/components/SecondView/AnHuiRenewView/AnHuiRenewRightTable.vue";
import SecondMiddem from "@/components/SecondView/AnHuiRenewView/AnHuiRenewMidden.vue";
import AnHuiRightTop from "@/components/SecondView/AnHuiRenewViewTools/AnHuiRightTop.vue";

</script>

<template>
    <div class="CityMain">
        <BigTitle id="BigTitle"></BigTitle>
        <SecondLeftTable id="SecondLeftTable"></SecondLeftTable>
        <SecondMiddem id="SecondMiddem"></SecondMiddem>
        <AnHuiRightTop id="AnHuiRightTop-out"></AnHuiRightTop>
        <SecondRightTable id="SecondRightTable"></SecondRightTable>
        <FootLoop id="FootLoop"></FootLoop>
    </div>
</template>

<style scoped lang="scss">
.CityMain {
  #BigTitle {
    width: 100vw;
  }

  #AnHuiRightTop-out {
    position: absolute;
    width: 30vw;
    height: 23vh;
    right: 0;
    margin-right: 9vw;
    margin-top: 13vh;
  }

  #SecondLeftTable {
    width: 25vw;
    height: 80vh;
    margin-top: 2vh;
    margin-left: 2vw;
    position: absolute;
  }

  #SecondMiddem {
    width: 40vw;
    height: 80vh;
    margin-top: 3vh;
    margin-left: 30.2vw;
    position: absolute;
  }

  #SecondRightTable {
    width: 25vw;
    height: 60vh;
    right: 0;
    margin-top: 28vh;
    margin-right: 2.5vw;
    position: absolute;
  }

  #FootLoop {
    position: absolute;
    margin-top: 70vh;
  }
}
</style>