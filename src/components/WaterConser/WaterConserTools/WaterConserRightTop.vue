<script setup>

</script>

<template>
    <div class="WaterConserRightTop">
        <div class="title">故障信息</div>
        <div class="ul">
            <ul>
                <li>
                    <div class="name">一号涡轮：</div>
                    <div class="thing">损坏</div>
                </li>
                <li>
                    <div class="name">三号涡轮：</div>
                    <div class="thing">离线</div>
                </li>

            </ul>
        </div>
        <Button class="go">维修通知</Button>
        <Button class="update">更新数据</Button>
        <Button class="wrong">危险警报</Button>
        <img src="../../../assets/pic/ca1.png" alt="" class="BackImg">
    </div>
</template>

<style scoped lang="scss">
.WaterConserRightTop {
  width: 100%;
  height: 100%;

  Button {
    position: absolute;
    margin-top: 22vh;
    margin-left: 4vw;
    border: none;
    font-weight: bolder;
    color: white;
    background: #0d87f6;
    border-radius: 3px;
    width: 6vw;
    font-size: 1em;
    height: 3vh;
  }

  Button:hover {
    cursor: pointer;
  }

  .update {
    margin-left: 11vw;
  }

  .wrong {
    margin-left: 18vw;
    background: #ff0202;
  }

  .ul {
    position: absolute;
    width: 23vw;
    height: 11vh;
    margin-left: 2.5vw;
    margin-top: 10vh;
    overflow-y: auto;
    -ms-overflow-style: none; /* IE 和 Edge */
    scrollbar-width: none; /* Firefox */
    background: rgba(10, 67, 188, .3);

    ul {
      width: 24vw;
      height: 12vh;
      margin-top: -1vh;
      margin-left: 5vw;

      li {
        list-style: none;
        color: white;
        font-weight: bolder;
        font-size: 1.3em;
        margin-top: 2vh;
        margin-left: -7vw;
        float: left;
        width: 18vw;

        .name {
          float: left;
          width: 7vw;
          text-align: center;
          color: #48b4ec;
        }

        .thing {
          width: 3vw;
          float: left;
          text-align: center;
        }
      }
    }
  }

  .title {
    color: white;
    position: absolute;
    font-size: 1.3em;
    font-weight: bolder;
    margin-top: 5vh;
    margin-left: 3vw;
  }

  .BackImg {
    width: 28vw;
    height: 30vh;
  }
}
</style>