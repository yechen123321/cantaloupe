<script setup>
import AnHuiSunLeftTop from "@/components/SecondView/AnHuiSunTools/AnHuiSunLeftTop.vue";
import AnHuiSunLeftCenter from "@/components/SecondView/AnHuiSunTools/AnHuiSunLeftCenter.vue";
import AnHuiSunLeftDown from "@/components/SecondView/AnHuiSunTools/AnHuiSunLeftDown.vue";
</script>

<template>
    <div class="AnHuiSunLeft">
        <AnHuiSunLeftTop id="AnHuiSunLeftTop"></AnHuiSunLeftTop>
        <img src="../../../assets/pic/border3.png" alt="" class="BackImg">
        <AnHuiSunLeftCenter id="AnHuiSunLeftCenter"></AnHuiSunLeftCenter>
        <AnHuiSunLeftDown id="AnHuiSunLeftDown"></AnHuiSunLeftDown>
    </div>
</template>

<style scoped lang="scss">
.AnHuiSunLeft {
  width: 100%;
  height: 100%;
    #AnHuiSunLeftTop{
        width: 26vw;
        height: 24vh;
        position: absolute;
        //background: red;
        margin-top: 4vh;
        //margin-left: 2vw;
    }
    #AnHuiSunLeftCenter{
        width: 26vw;
        height: 24vh;
        position: absolute;
        //background: #00ff24;
        margin-top: -54.5vh;
    }
    #AnHuiSunLeftDown{
        width: 26vw;
        height: 24vh;
        position: absolute;
        //background: #ffe800;
        margin-left: -0.4vw;
        margin-top: -29vh;
    }
  .BackImg {
    width: 26vw;
    height: 82vh;
  }
}
</style>