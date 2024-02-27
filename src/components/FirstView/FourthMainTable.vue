<script setup>
// import * as echarts from 'echarts';
import {onMounted} from "vue";

onMounted(() => {

})

</script>



<template>
    <div class="FourthMainTable">
        <img class="BackImg" src="../../assets/pic/k_3.png" alt="">
        <div id="echarts1"></div>
    </div>
</template>

<style scoped lang="scss">
.FourthMainTable {
  width: 100vw;
  height: 100vh;
  border-image: linear-gradient(to right, #00bfff, #0d0d0d, #00bfff) 30 30;
  border-radius: 0.5vw;
  box-shadow: 0px 0px 1vw 1vw #00bfff, 0px 0px 2vw 1vw #0d0d0d, 0px 0px 3vw 2vw #00bfff;
  animation: glow 1s ease-in-out infinite alternate;
  color: white;
  .BackImg {
    width: 23vw;
    height: 22vh;
  }
  #echarts1 {
    width: 23vw;
    height:20vh;
    margin-left: -0.5vw;
    //background: red;
    position: absolute;
    margin-top: -21.5vh;
  }
  @keyframes glow {

    from {
      box-shadow: 0px 0px 3px 3px #00bfff, 0px 0px 5px 3px #0d0d0d, 0px 0px 7px 5px #00bfff;
    }

    to {
      box-shadow: 0px 0px 5px 3px #00bfff, 0px 0px 7px 5px #0d0d0d, 0px 0px 9px 7px #00bfff;
    }
  }
}

</style>