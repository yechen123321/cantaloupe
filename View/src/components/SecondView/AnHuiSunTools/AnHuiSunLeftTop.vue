<script setup>

</script>

<template>
    <div class="AnHuiSunLeftTop">
        <div class="title">安徽省光电能源统计</div>
        <img src="../../../assets/pic/border4.png" alt="" class="BackImg">
        <div class="AnHuiSunLeftTop-main">
            <div class="MainOne">
                <img src="../../../assets/太阳发电.png" alt="" class="pic">
                <div class="number">
                    <div class="one">4232</div>
                    <div class="up">亿万千瓦</div>
                </div>
                <div class="tow">光电能源总产量</div>
            </div>
            <div class="MainTow">
                <img src="../../../assets/装机容量.png" alt="" class="pic">
                <div class="number">
                    <div class="one" style="margin-left: 0.2vw">13.44</div>
                    <div class="up">%</div>
                </div>
                <div class="tow">装机容量提升率</div>
            </div>
            <div class="MainThree">
                <img src="../../../assets/投资.png" alt="" class="pic">
                <div class="number">
                    <div class="one">3789</div>
                    <div class="up">亿元</div>
                </div>
                <div class="tow">能源建设投资</div>
            </div>
            <div class="MainFour">
                <img src="../../../assets/GenericChart.png" style="margin-top: 2vh" alt="" class="pic">
                <div class="number">
                    <div class="one" style="margin-left: 0.3vw">1.33</div>
                    <div class="up">%</div>
                </div>
                <div class="tow">发展指标增长</div>
            </div>
        </div>
    </div>
</template>

<style scoped lang="scss">
.AnHuiSunLeftTop {
  width: 100%;
  height: 100%;

  .title {
    position: absolute;
    color: white;
    font-weight: bolder;
    text-align: center;
    font-size: 1.15em;
    margin-top: 1vh;
    width: 24vw;
    margin-left: 1vw;
  }

  .AnHuiSunLeftTop-main {
    position: absolute;
    width: 25vw;
    height: 18vh;
    margin-left: 0.75vw;
    margin-top: -19vh;
    color: white;

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
    width: 26.5vw;
    height: 22vh;
  }
}
</style>