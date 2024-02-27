<script setup>

</script>

<template>
  <div class="title_main">
<!--      <img src="../assets/pic/progress.gif" class="top-title-first-gif" alt="">-->
      <img src="../assets/pic/top.png" class="top-title" alt="">
      <img src="../assets/pic/header.gif" class="top-title-head" alt="">
<!--      <img src="../assets/pic/progress.gif" class="top-title-second-gif" alt="">-->
      <div class="TitleName">致态</div>
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
      width: 20%;
      height: 50%;
      margin-left: 8.65%;
      margin-top: 1%;
      position: absolute;
    }
    .top-title-second-gif{
      width: 20%;
      height: 50%;
      margin-left: -29%;
      margin-top: 1%;
      transform: scaleX(-1);
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