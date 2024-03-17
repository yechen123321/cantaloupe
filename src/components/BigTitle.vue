<script setup>

</script>

<template>
    <div class="title_main">
<!--        <img src="../assets/pic/12-r.png" class="top-title-first-gif" alt="">-->
        <img src="../assets/pic/top2.png" class="top-title" alt="">
        <img src="../assets/pic/header.gif" class="top-title-head" alt="">
<!--        <img src="../assets/pic/11-l.png" class="top-title-second-gif" alt="">-->
        <div class="TitleName">溯源</div>
<!--        &lt;!&ndash;      <img class="Screen-left" src="../assets/pic/p.png" alt="">&ndash;&gt;-->
<!--        &lt;!&ndash;      <img class="Screen-right" src="../assets/pic/pp.png" alt="">&ndash;&gt;-->
        <Router-Link class="Button" style="margin-left: 41.5vw;" to="/">
            全国数据概览
            <img style="" src="../assets/pic/anniu1.png" alt="">
        </Router-Link>
        <Router-Link class="Button" style="margin-left: 55vw;" to="/anhuirenew">
            地方再生能源
            <img src="../assets/pic/anniu1.png" alt="">
        </Router-Link>
        <a class="Button" style="margin-right: 6vw; right: 0" href="http://172.18.7.71:8080/admin/">
            数据站点分析
            <img src="../assets/pic/anniu1.png" alt="">
        </a>
        <Router-Link class="Button" style="margin-right: 19.5vw; right: 0" to="/">
            地方有限能源
            <img src="../assets/pic/anniu1.png" alt="">
        </Router-Link>
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

  .Button {
    display: block;
    width: 12vw;
    height: 6vh;
    margin-top: -8.5vh;
    font-size: 1.4vw;
    font-weight: bolder;
    line-height: 8vh;
    text-align: center;
    position: absolute;
    color: white;
    text-decoration: none;

    img {
      margin-left: -9.7vw;
      margin-top: 0.5vh;
      width: 11vw;
      height: 7vh;
      position: absolute;
    }
  }

  .Button:hover {
    text-shadow: 0 0 10px rgb(127, 235, 240), 0 0 20px rgb(127, 235, 240); //设置发光效果
    font-size: 1.7vw;

    img {
      width: 13vw;
      height: 8vh;
      margin-top: 0.3vh;
      margin-left: -11.5vw;
    }
  }

  .Button:active {
    font-size: 1.4vw;

    img {
      width: 11vw;
      height: 7vh;
      margin-left: -9.7vw;
      margin-top: 0.5vh;
    }
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
    margin-top: 0.5vh;

  }

  .top-title-head {
    width: 20vw;
    height: 20vh;
    left: 0;
    position: absolute;
    margin-left: 10vw;
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
    width: 20vw;
    position: absolute;
    margin-left: 10vw;
    margin-top: -8.5vh;
    font-size: 2.5vw;
    font-family: 微软雅黑, serif;
    color: #7debf0;
    font-weight: bolder;
    text-shadow: 0 0 1px #7debf0;
  }
}
</style>