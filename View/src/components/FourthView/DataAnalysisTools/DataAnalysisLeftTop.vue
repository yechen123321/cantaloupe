<script setup>
import {initp1, initp2, initp31, initp32, initp33, initp34 } from '@/api'
</script>
<template>
    <div class="DataAnalysisLeftTop">
        <div class="title">安徽天气数据概览</div>
        <div class="right">
            <div class="right-one">
                <div class="oneTop">月平均降雨量</div>
                <div class="oneCenter">
                    <div class="centerLeft">95.75</div>
                    <div class="centerRight">毫米</div>
                </div>
                <div class="oneDown">
                    <div class="num">2.34%</div>
                    <img src="../../../assets/up.png" alt="" class="Out">
                </div>
            </div>
            <div class="right-tow">
                <div class="oneTop">月平均空气质量</div>
                <div class="oneCenter">
                    <div class="centerLeft">79</div>
                    <div class="centerRight">AQI</div>
                </div>
                <div class="oneDown">
                    <div class="num">2.3%</div>
                    <img src="../../../assets/down.png" alt="" class="Out">
                </div>
            </div>
            <div class="right-three">
                <div class="oneTop">月平均日照时间</div>
                <div class="oneCenter">
                    <div class="centerLeft">166.5</div>
                    <div class="centerRight">小时</div>
                </div>
                <div class="oneDown">
                    <div class="num">4.3%</div>
                    <img src="../../../assets/down.png" alt="" class="Out">
                </div>
            </div>
            <div class="right-four">
                <div class="oneTop">月平均风速</div>
                <div class="oneCenter">
                    <div class="centerLeft">2.1</div>
                    <div class="centerRight">米/秒</div>
                </div>
                <div class="oneDown">
                    <div class="num">1.1%</div>
                    <img src="../../../assets/up.png" alt="" class="Out">
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
      margin-top: 4vh;
      line-height: 6vh;
      text-align: center;

      .centerLeft {
        width: 6vw;
        position: absolute;
        height: 7vh;
        color: #fac800;
        text-shadow: 0 0 1px #fac800, 0 0 1px #fac800, 0 0 2px #fac800;
        font-size: 1.5em;
      }

      .centerRight {
        position: absolute;
        width: 4vw;
        height: 7vh;
        font-size: 1.1em;
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
      margin-top: 9vh;
      font-size: 1.3em;

    }

    .right-one {
      width: 10vw;
      height: 16vh;
      margin-top: -1vh;
      position: absolute;
    }

    .right-tow {
      width: 10vw;
      height: 16vh;
      position: absolute;
      margin-top: -1vh;
      margin-left: 12.5vw;
    }

    .right-three {
      width: 10vw;
      height: 16vh;
      margin-top: 10.5vh;
      position: absolute;
    }

    .right-four {
      width: 10vw;
      height: 16vh;
      position: absolute;
      margin-top: 10.5vh;
      margin-left: 12.5vw;
    }
  }

  .title {
    position: absolute;
    color: white;
    font-size: 1.25em;
    font-weight: bolder;
    margin-top: 4vh;
    margin-left: 2.5vw;
  }

  .BackImg {
    width: 30vw;
    height: 34vh;
  }
}
</style>