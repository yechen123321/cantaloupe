<script setup>
// 定义处理点击事件的方法
const handleUpdate = () => {
    // 刷新页面
    window.location.reload();
}
</script>

<template>
    <div class="AnHuiSunRightTop">
        <div class="title">电场信息</div>
        <div class="ul">
            <ul>
                <li>
                    <div class="name">一号发电：</div>
                    <div class="thing">正常运行</div>
                </li>
                <li>
                    <div class="name" style="color: red; text-shadow: 0 0 0.5px red;">二号发电：</div>
                    <div class="thing" style="color: red; text-shadow: 0 0 0.5px red;">运行异常</div>
                </li>
                <li>
                    <div class="name" style="color: red; text-shadow: 0 0 0.5px red;">三号发电：</div>
                    <div class="thing" style="color: red; text-shadow: 0 0 0.5px red;">运行异常</div>
                </li>
                <li>
                    <div class="name">四号发电：</div>
                    <div class="thing">正常运行</div>
                </li>
                <li>
                    <div class="name">五号发电：</div>
                    <div class="thing">正常运行</div>
                </li>
            </ul>
        </div>
        <div class="mm">
            <div class="one">故障信息：</div>
            <div class="two">2 条</div>
        </div>
        <button @click="handleUpdate" class="update">更新信息</button>
        <img src="../../../assets/pic/border4.png" alt="" class="BackImg">
    </div>
</template>

<style scoped lang="scss">
.AnHuiSunRightTop {
  width: 100%;
  height: 100%;

  .mm {
    position: absolute;
    color: red;
    text-shadow: 0 0 0.5px red;
    font-weight: bolder;
    font-size: 1.2em;
    margin-top: 15.5vh;
    margin-left: 2vw;
    width: 20vw;

    .one {
      float: left;
    }

    .two {
      margin-top: 0.1vh;
    }
  }

  .ul {
    position: absolute;
    width: 22vw;
    height: 10vh;
    background: rgba(10, 67, 188, .3);
    border-radius: 5px;
    margin-top: 5vh;
    margin-left: 2vw;
    overflow-y: auto;
    -ms-overflow-style: none; /* IE 和 Edge */
    scrollbar-width: none; /* Firefox */
    ul {
      width: 21.4vw;
      margin-top: -0.5vh;
      height: 10vh;
      margin-left: -2vw;
      //background: red;

      li {
        list-style: none;
        width: 9vw;
        margin-top: 1.6vh;
        margin-left: 0.75vw;
        float: left;
        height: 3vh;
        //background: rgba(10, 67, 188, .4);
        .name {
          width: 6vw;
          height: 3vh;
          color: white;
          font-weight: bolder;
          margin-left: 0.3vw;
          margin-top: 0.2vh;
          //background: #0d87f6;
          position: absolute;
        }

        .thing {
          width: 10vw;
          height: 3vh;
          color: white;
          font-weight: bolder;
          margin-left: 5vw;
          margin-top: 0.2vh;
          //background: #ffffff;
          position: absolute;
        }
      }
    }

  }

  .update {
    font-size: 0.9em;
    width: 5vw;
    height: 3vh;
    line-height: 3vh;
    text-align: center;
    position: absolute;
    border-radius: 3px;
    margin-top: 16vh;
    margin-left: 14vw;
    color: white;
    background: rgb(25, 83, 206);
    border: none;
    font-weight: bolder;
  }

  .update:hover {
    cursor: pointer;
  }

  .title {
    position: absolute;
    color: white;
    font-size: 1.15em;
    margin-top: 1vh;
    margin-left: 1.5vw;
    font-weight: bolder;
  }

  .BackImg {
    width: 26vw;
    height: 20vh;
  }
}
</style>