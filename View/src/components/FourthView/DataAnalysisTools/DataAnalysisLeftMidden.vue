<script setup>
import {initq, initp} from "@/api";
</script>

<template>
    <div class="DataAnalysisLeftMidden">
        <div class="title">安徽能源总计</div>
        <div class="AnHuiLeftTop-main">
            <div class="MainOne">
                <img src="../../../assets/renew.png" alt="" class="pic">
                <div class="number">
                    <div class="one">3521</div>
                    <div class="up">亿千瓦时</div>
                </div>
                <div class="tow">全省能源总产量</div>
            </div>
            <div class="MainTow">
                <img src="../../../assets/zhuangji.png" alt="" class="pic">
                <div class="number">
                    <div class="one" style="margin-left: 0.2vw">27.7</div>
                    <div class="up">%</div>
                </div>
                <div class="tow">装机容量提升率</div>
            </div>
            <div class="MainThree">
                <img src="../../../assets/makemoney.png" alt="" class="pic">
                <div class="number">
                    <div class="one">1311</div>
                    <div class="up">亿元</div>
                </div>
                <div class="tow">能源建设投资</div>
            </div>
            <div class="MainFour">
                <img src="../../../assets/GenericChart.png" style="margin-top: 2vh" alt="" class="pic">
                <div class="number">
                    <div class="one" style="margin-left: 0.3vw">7.02</div>
                    <div class="up">%</div>
                </div>
                <div class="tow">发展指标增长</div>
            </div>
        </div>
        <img src="../../../assets/pic/midden.png" alt="" class="BackImg">
    </div>
</template>

<style scoped lang="scss">
.DataAnalysisLeftMidden {
  width: 100%;
  height: 100%;

  .AnHuiLeftTop-main {
    position: absolute;
    width: 25vw;
    height: 18vh;
    margin-left: 3vw;
    color: white;
    margin-top: 7vh;

    .number {
      position: absolute;
      width: 8vw;
      height: 4vh;
      margin-top: 1.6vh;
      margin-left: 3.7vw;
      border-bottom: 2px solid #0a8cf8;

      .up {
        position: absolute;
        width: 5vw;
        margin-left: 4.2vw;
        text-align: center;
        font-size: 0.8em;
        margin-top: 1.3vh;
        font-weight: bolder;
      }

      .one {
        position: absolute;
        font-size: 1.6em;
        margin-left: -0.6vw;
        line-height: 3.7vh;
        margin-top: -0.3vh;
        font-weight: bolder;
        width: 6vw;
        text-align: center;
        height: 3.7vh;
        color: #2bfff1;
        text-shadow: 0 0 1px #1cd7cd, 0 0 1.5px #1cd7cd, 0 0 2px #1cd7cd;
      }
    }

    .tow {
      position: absolute;
      margin-left: 3.75vw;
      margin-top: 6vh;
      width: 8vw;
      font-size: 0.95em;
      font-weight: 400;
      height: 3vh;
      text-align: center;
    }

    .pic {
      position: absolute;
      width: 3.3vw;
      height: 6vh;
      margin-top: 1.6vh;
    }

    .MainOne {
      width: 11vw;
      height: 8vh;
      position: absolute;
    }

    .MainTow {
      width: 11vw;
      height: 8vh;
      position: absolute;
      margin-left: 13vw;
    }

    .MainThree {
      width: 11vw;
      height: 8vh;
      position: absolute;
      margin-top: 8vh;
    }

    .MainFour {
      width: 11vw;
      height: 8vh;
      position: absolute;
      margin-top: 8vh;
      margin-left: 13vw;
      z-index: 999;
    }
  }

  .title {
    position: absolute;
    color: white;
    margin-top: 3.5vh;
    margin-left: 3vw;
    font-weight: bolder;
    font-size: 1.25em;
  }

  .BackImg {
    width: 30vw;
    height: 28vh;
  }
}
</style>