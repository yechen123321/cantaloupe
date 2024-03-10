<script setup>
import BigTitle from "@/components/BigTitle.vue";
import FootLoop from '@/components/FootLoop.vue';
import SecondLeftTable from "@/components/SecondView/AnHuiLeftTable.vue";
import SecondRightTable from "@/components/SecondView/AnHuiRightTable.vue";
import SecondMiddem from "@/components/SecondView/AnHuiMidden.vue";
import AnHuiRightTop from "@/components/SecondView/AnHuiViewTools/AnHuiRightTop.vue";

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
    #AnHuiRightTop-out{
        position: absolute;
        width: 30vw;
        height: 23vh;
       right: 0;
        margin-right: 9vw;
        margin-top: 14vh;
    }
  #SecondLeftTable {
    width: 25vw;
    height: 80vh;
    margin-top: 3vh;
    margin-left: 2vw;
    position: absolute;
  }

  #SecondMiddem {
    width: 40vw;
    height: 80vh;
    margin-top: 4vh;
    margin-left: 30.2vw;
    position: absolute;
  }

  #SecondRightTable {
    width: 25vw;
    height: 80vh;
    right: 0;
    margin-top: 26.8vh;
    margin-right: 2.5vw;
    position: absolute;
  }

  #FootLoop {
    position: absolute;
    margin-top: 70vh;
  }
}
</style>