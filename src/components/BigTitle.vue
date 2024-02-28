<script setup>

</script>

<template>
  <div class="title_main">
      <img src="../assets/pic/11-r.png" class="top-title-first-gif" alt="">
      <img src="../assets/pic/top.png" class="top-title" alt="">
      <img src="../assets/pic/header.gif" class="top-title-head" alt="">
      <img src="../assets/pic/11-l.png" class="top-title-second-gif" alt="">
      <div class="TitleName">致态</div>
      <img class="Screen-left" src="../assets/pic/p.png" alt="">
      <img class="Screen-right" src="../assets/pic/pp.png" alt="">
  </div>
</template>

<style scoped lang="scss">
  .title_main{
    width: 100%;
    height: 10%;
    color: rgb(127,235,240);
    font-size: 3.5em;
    text-align: center;
    line-height: 100px;
    position: relative;
    .Screen-left{
      height: 80vh;
      position: absolute;
      margin-left: -99vw;
      margin-top: 10vh;
    }
    .Screen-right{
      height: 80vh;
      position: absolute;
      margin-left: -3.7vw;
      margin-top: 10vh;
    }
    .top-title{
      width: 100%;
      height: 100%;

    }
    .top-title-head{
      width: 20%;
      height: 200%;
      position: absolute;
      margin-left: -60%;
      margin-top: -1%;
    }
    .top-title-first-gif{
      width: 25vw;
      height: 3vh;
      margin-left: 4.65%;
      margin-top: 2vh;
      position: absolute;
    }
    .top-title-second-gif{
      width: 25vw;
      height: 3vh;
      margin-left: -29.7vw;
      margin-top: 2vh;
      position: absolute;
    }
    .TitleName{
      width: 100%;
      position: absolute;
      margin-top: -7.5%;
      font-size: 1em;
      font-family: 微软雅黑,serif;
      color: #1cd7cd;
      font-weight: bolder;
      text-shadow: 0 0 1px #1cd7cd;
    }
  }
</style>