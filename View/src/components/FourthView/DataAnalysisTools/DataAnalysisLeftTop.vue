<script setup>

</script>
<template>
    <div class="DataAnalysisLeftTop">
        <div class="title">安徽能源总产能</div>
        <div class="top">
            <div class="topOne">
                <div class="topHead">当前统计基地数</div>
                <div class="topMain">1276</div>
                <div class="up">座</div>
            </div>
            <div class="topTow">
                <div class="topHead">发电装机总容量</div>
                <div class="topMain" style="margin-left: -2.4vw">3245</div>
                <div class="up">万千瓦</div>
            </div>
        </div>
        <div class="right">
            <div class="right-one">
                <div class="oneTop">月平均发电量</div>
                <div class="oneCenter">
                    <div class="centerLeft">234</div>
                    <div class="centerRight">万千瓦</div>
                </div>
                <div class="oneDown">
                    <div class="num">2.34%</div>
                    <img src="../../../assets/上升.png" alt="" class="Out">
                </div>
            </div>
            <div class="right-tow">
                <div class="oneTop">月平均损耗标准煤</div>
                <div class="oneCenter">
                    <div class="centerLeft">34</div>
                    <div class="centerRight">万吨</div>
                </div>
                <div class="oneDown">
                    <div class="num">4.5%</div>
                    <img src="../../../assets/下降.png" alt="" class="Out">
                </div>
            </div>
        </div>
        <img src="../../../assets/pic/midden.png" alt="" class="BackImg">
    </div>

</template>

<style scoped lang="scss">
.DataAnalysisLeftTop {
  width: 100%;
  height: 100%;

  .top {
    position: absolute;
    width: 42vw;
    height: 10vh;
    margin-top: 21vh;
    margin-left: 2.6vw;

    div {
      float: left;
    }

    .up {
      width: 5vw;
      height: 5vh;
      position: absolute;
      color: #00bfff;
      text-shadow: 0 0 0.5px #00bfff, 0 0 1px #00bfff, 0 0 1px #00bfff;
      margin-left: 5vw;
      margin-top: 3.6vh;
      font-size: 1.3em;
    }

    .topHead {
      width: 10vw;
      height: 4vh;
      color: #d851f3;
      text-shadow: 0 0 0.5px #d851f3, 0 0 0.5px #d851f3, 0 0 0.5px #d851f3;
      font-size: 1.2em;
    }

    .topMain {
      width: 10vw;
      height: 6vh;
        margin-top: -1vh;
      color: #00bfff;
      text-shadow: 0 0 0.5px #00bfff, 0 0 1px #00bfff, 0 0 1px #00bfff;
      margin-left: -1vw;
      font-size: 1.8em;
    }

    .topOne {
      width: 10vw;
      height: 10vh;
      margin-left: 1vw;
      margin-top: 1vh;
      text-align: center;
      color: #fff;
      font-weight: bolder;
    }

    .topTow {
      width: 10vw;
      height: 10vh;
      margin-top: 1vh;
      margin-left: 2.5vw;

      text-align: center;
      color: #fff;
      font-weight: bolder;
    }
  }

  .right {
    width: 30vw;
    height: 34vh;
    position: absolute;
    color: white;
    margin-left: 3.7vw;
    margin-top: 7vh;
    font-weight: bolder;

    .num {
      width: 5.5vw;
      text-align: center;
      margin-left: 1vw;
      margin-top: -0.5vh;
    }

    .Out {
      width: 2vw;
      position: absolute;
      margin-left: 6.5vw;
      margin-top: -4vh;
    }

    .oneTop {
      width: 10vw;
      height: 4.5vh;
      position: absolute;
      margin-top: 0.2vh;
      line-height: 5.5vh;
      border-bottom: 2px solid #0a8cf8;
      color: #00bfff;
      text-shadow: 0 0 0.5px #00bfff, 0 0 1px #00bfff, 0 0 1px #00bfff;
    }

    .oneCenter {
      width: 10vw;
      height: 6vh;
      position: absolute;
      margin-top: 4.5vh;
      line-height: 6vh;
      text-align: center;

      .centerLeft {
        width: 6vw;
        position: absolute;
        height: 7vh;
        color: #fac800;
        text-shadow: 0 0 1px #fac800, 0 0 1px #fac800, 0 0 2px #fac800;
        font-size: 1.8em;
      }

      .centerRight {
        position: absolute;
        width: 4vw;
        height: 7vh;
        right: 0;
        margin-top: 0.6vh;
      }
    }

    .oneDown {
      border-top: 2px solid #0a8cf8;
      width: 10vw;
      height: 4.5vh;
      line-height: 4.5vh;
      position: absolute;
      margin-top: 10.2vh;
      font-size: 1.3em;

    }

    .right-one {
      width: 10vw;
      height: 16vh;
      position: absolute;
    }

    .right-tow {
      width: 10vw;
      height: 16vh;
      position: absolute;
      margin-left: 12.5vw;
    }
  }

  .title {
    position: absolute;
    color: white;
    font-size: 1.25em;
    font-weight: bolder;
    margin-top: 4vh;
    margin-left: 3vw;
  }

  .BackImg {
    width: 30vw;
    height: 34vh;
  }
}
</style>