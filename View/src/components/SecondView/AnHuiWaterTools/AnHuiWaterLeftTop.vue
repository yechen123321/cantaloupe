<script setup>

</script>

<template>
    <div class="AnHuiWaterLeftTop">
        <div class="title">安徽省水电能源统计</div>
        <div class="AnHuiWaterLeftTop-main">
            <div class="MainOne">
                <img src="../../../assets/water2.png" alt="" class="pic">
                <div class="number">
                    <div class="one">86.6</div>
                    <div class="up">亿千瓦时</div>
                </div>
                <div class="tow">水电能源总产量</div>
            </div>
            <div class="MainTow">
                <img src="../../../assets/zhuangji.png" alt="" class="pic">
                <div class="number">
                    <div class="one">623.6</div>
                    <div class="up">万千瓦</div>
                </div>
                <div class="tow">水电装机总容量</div>
            </div>
            <div class="MainThree">
                <img src="../../../assets/makemoney.png" alt="" class="pic">
                <div class="number">
                    <div class="one">641.3</div>
                    <div class="up">亿元</div>
                </div>
                <div class="tow">能源建设投资</div>
            </div>
            <div class="MainFour">
                <img src="../../../assets/GenericChart.png" style="margin-top: 2vh" alt="" class="pic">
                <div class="number">
                    <div class="one" style="margin-left: 0.3vw">11.33</div>
                    <div class="up">%</div>
                </div>
                <div class="tow">发展指标增长</div>
            </div>
        </div>
        <img src="../../../assets/pic/border4.png" alt="" class="BackImg">
    </div>
</template>

<style scoped lang="scss">
.AnHuiWaterLeftTop {
  width: 100%;
  height: 100%;
  color: white;

  .AnHuiWaterLeftTop-main {
    position: absolute;
    width: 25vw;
    height: 18vh;
    margin-left: 0.75vw;
    margin-top: 5vh;

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
        text-shadow: 0 0 1px #1cd7cd, 0 0 2px #1cd7cd, 0 0 3px #1cd7cd;
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

  .BackImg {
    position: absolute;
    width: 26.5vw;
    height: 23vh;
    margin-top: 1vh;
  }

  .title {
    position: absolute;
    color: white;
    font-weight: bolder;
    text-align: center;
    font-size: 1.15em;
    margin-top: 2vh;
    width: 24vw;
    margin-left: 1vw;
  }


}
</style>