<script setup>

</script>

<template>
    <div class="title_main">
        <img src="../assets/pic/12-r.png" class="top-title-first-gif" alt="">
        <img src="../assets/pic/top1.png" class="top-title" alt="">
        <img src="../assets/pic/header.gif" class="top-title-head" alt="">
        <img src="../assets/pic/11-l.png" class="top-title-second-gif" alt="">
        <div class="TitleName">致态</div>
        <!--      <img class="Screen-left" src="../assets/pic/p.png" alt="">-->
        <!--      <img class="Screen-right" src="../assets/pic/pp.png" alt="">-->
        <Router-Link class="Button" style="margin-left: 6vw;" to="">
            你好姿态
        </Router-Link>
        <Router-Link class="Button" style="margin-left: 21vw;" to="">姿态你好</Router-Link>
        <Router-Link class="Button" style="margin-right: 6vw; right: 0" to="">我红温啦</Router-Link>
        <Router-Link class="Button" style="margin-right: 21vw; right: 0" to="">奇迹行者</Router-Link>
    </div>
</template>

<style scoped lang="scss">
.title_main {
  width: 100vw;
  height: 10vh;
  color: rgb(127, 235, 240);
  font-size: 3.5vw;
  text-align: center;
  line-height: 5vh;
  position: relative;

    .Button{
        display: block;
        width: 12vw;
        height: 8vh;
        margin-top: -3.8vh;
        font-size: 2vw;
        line-height: 8vh;
        text-align: center;
        position: absolute;
        color: white;
        text-decoration: none;

    }


  .Screen-left {
    height: 80vh;
    position: absolute;
    margin-left: -99vw;
    margin-top: 10vh;
  }

  .Screen-right {
    height: 80vh;
    position: absolute;
    margin-left: -3.7vw;
    margin-top: 10vh;
  }

  .top-title {
    width: 100%;
    height: 100%;

  }

  .top-title-head {
    width: 20vw;
    height: 20vh;
    position: absolute;
    margin-left: -60vw;
    margin-top: -1.5vh;
  }

  .top-title-first-gif {
    width: 25vw;
    height: 3vh;
    margin-left: 4.65vw;
    margin-top: 2vh;
    position: absolute;
  }

  .top-title-second-gif {
    width: 25vw;
    height: 3vh;
    margin-left: -29.7vw;
    margin-top: 2vh;
    position: absolute;
  }

  .TitleName {
    width: 100%;
    position: absolute;
    margin-top: -8vh;
    font-size: 2.5vw;
    font-family: 微软雅黑, serif;
    color: #7debf0;
    font-weight: bolder;
    text-shadow: 0 0 1px #7debf0;
  }
}
</style>