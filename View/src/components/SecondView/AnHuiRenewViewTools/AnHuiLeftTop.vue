<script setup>

</script>

<template>
    <div class="AnHuiLeftTop">
        <div class="AnHuiLeftTop-title">安徽省再生能源统计</div>
        <div class="AnHuiLeftTop-main">
            <div class="MainOne"></div>
            <div class="MainTow"></div>
            <div class="MainThree"></div>
            <div class="MainFour"></div>
        </div>
        <img src="../../../assets/pic/border4.png" alt="" class="BackImg">
    </div>
</template>

<style scoped lang="scss">
.AnHuiLeftTop {
  width: 100%;
  height: 100%;
  color: white;

  .AnHuiLeftTop-main {
    position: absolute;
    width: 25vw;
    height: 18vh;
    margin-left: 3vw;
      .MainOne{
          width: 11vw;
          height: 8vh;
          position: absolute;
          margin-left: 1vw;
      }
      .MainTow{
          width: 11vw;
          height: 8vh;
          position: absolute;
          margin-left: 13vw;
      }
      .MainThree{
          width: 11vw;
          height: 8vh;
          position: absolute;
          margin-top: 9vh;
          margin-left: 1vw;
      }
      .MainFour{
          width: 11vw;
          height: 8vh;
          position: absolute;
          margin-top: 9vh;
          margin-left: 13vw;
      }
  }

  .BackImg {
    position: absolute;
    width: 26vw;
    height: 22.5vh;
    margin-left: 2.5vw;
    margin-top: -4vh;
  }

  .AnHuiLeftTop-title {
    position: absolute;
    color: white;
    margin-top: -3vh;
    text-align: center;
    width: 25.8vw;
    margin-left: 2.6vw;
    font-weight: bolder;
    font-size: 1.15em;
  }

}
</style>