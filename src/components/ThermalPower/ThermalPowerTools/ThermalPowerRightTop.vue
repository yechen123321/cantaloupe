<script setup>
import {ref} from "vue";

const reportGenerated1 = ref(false);
const updateReport1 = () => {
    reportGenerated1.value = true;
    reportGenerated2.value = false;
};

const reportGenerated2 = ref(false);
const updateReport2 = () => {
    reportGenerated2.value = true;
    reportGenerated1.value = false;
};
const close = () => {
    reportGenerated2.value = false;
    reportGenerated1.value = false;
}

</script>

<template>
    <div class="ThermalPowerRightTop">
        <div class="updateMessage" v-show="reportGenerated1">
            <div class="title">
                <div class="name">维修通知操作</div>
                <button @click="close" class="button">
                    <span class="X"></span>
                    <span class="Y"></span>
                </button>
            </div>
            <div class="main">
                <div class="tip">电厂维修通知操作成功：</div>
                <div class="tip-2">
                    <div class="number">2 条 故障信息</div>
                    <div class="up">已发送</div>
                </div>
                <div class="down">将立即执行维修工作</div>
                <Button @click="close" class="do">确认</Button>
            </div>
        </div>

        <div class="DAMessage" v-show="reportGenerated2">
            <div class="main">
                <div class="big"></div>
                <div class="thing">危险警报</div>
                <div class="little">请各人员按照指定通道进行疏散</div>
                <img src="../../../assets/da.gif" alt="">
                <Button @click="close"  class="close">警报解除</Button>
            </div>
        </div>
        <div class="title">
            故障信息
        </div>
        <div class="ul">
            <ul>
                <li>
                    <div class="name">一号锅炉：</div>
                    <div class="thing">失压</div>
                </li>
                <li>
                    <div class="name">三号锅炉：</div>
                    <div class="thing">高压</div>
                </li>

            </ul>
        </div>
        <div class="mm">
            <div class="one">故障信息：</div>
            <div class="two">2 条</div>
        </div>
        <Button @click="updateReport1" class="go">维修通知</Button>
        <Button @click="updateReport2" class="wrong">危险警报</Button>
        <img src="../../../assets/pic/ca1.png" alt="" class="BackImg">
    </div>
</template>

<style scoped lang="scss">
.ThermalPowerRightTop {
  width: 100%;
  height: 100%;

  .mm {
    position: absolute;
    color: #fff35e;
    font-weight: bolder;
    font-size: 1.2em;
    margin-top: 22vh;
    margin-left: 2.5vw;
    width: 20vw;

    .one {
      float: left;
    }

    .two {
      margin-top: 0.1vh;
    }
  }

  .updateMessage {
    position: fixed;
    width: 35vw;
    height: 45vh;
    margin-left: -39.1vw;
    margin-top: 15vh;
    z-index: 999;

    .main {
      width: 35vw;
      height: 40vh;
      background: rgba(56, 120, 238, 0.8);
      margin-left: 0vw;
      margin-top: 5vh;
      position: absolute;
        .do{
            position: absolute;
            width: 7vw;
            height: 6vh;
            font-size: 1.4em;
            background: #0d11f6;
            border: none;
            border-radius: 6px;
            margin-left: 24.5vw;
            margin-top: 30vh;
        }
        .down{
            color:white;
            font-size: 1.8em;
            margin-top: 10vw;
            margin-left: 6.5vw;
            font-weight: bolder;
            position: absolute;
        }
        .tip-2{
            color:white;
            font-size: 1.8em;
            margin-top: 6vw;
            margin-left: 6.5vw;
            font-weight: bolder;
            position: absolute;
            .number{
                width: 15vw;
                color: #ffe800;
                position: absolute;
            }
            .up{
                position: absolute;
                margin-left: 14vw;
                width: 8vw;
            }
        }
        .tip{
            color:white;
            font-size: 1.8em;
            margin-top: 2vw;
            margin-left: 2.5vw;
            font-weight: bolder;
            position: absolute;
        }
    }

    .title {
      width: 35vw;
      height: 5vh;
      background: rgba(19, 47, 234, 1);
      margin-left: 0vw;
      margin-top: 0vh;
      position: absolute;
        .name {
            color: white;
            position: absolute;
            font-size: 1.1em;
            margin-left: 2vw;
            margin-top: 0.5vh;
            font-weight: bolder;
        }
      .button {
        position: absolute;
        z-index: 999;
        width: 2vw;
        height: 3.8vh;
        margin-top: 0.5vh;
        margin-left: 32vw;
        border: none;
        background: rgba(180, 83, 107, 0.11);
        border-radius: 5px;
        transition: background 0.5s;
      }

      .X {
        content: "";
        position: absolute;
        top: 48%;
        left: 50%;
        width: 1.8vw;
        height: 1.5px;
        background-color: rgb(255, 255, 255);
        transform: translateX(-50%) rotate(45deg);
      }

      .Y {
        content: "";
        position: absolute;
        top: 48%;
        left: 50%;
        width: 1.8vw;
        height: 1.5px;
        background-color: #fff;
        transform: translateX(-50%) rotate(-45deg);
      }

      .close {
        position: absolute;
        display: flex;
        padding: 0.8rem 1.5rem;
        align-items: center;
        justify-content: center;
        transform: translateX(-50%);
        top: -150%;
        left: 50%;
        width: 3em;
        height: 1.7em;
        font-size: 12px;
        background-color: rgb(19, 22, 24);
        color: rgb(187, 229, 236);
        border: none;
        border-radius: 3px;
        pointer-events: none;
        opacity: 0;
      }

      .button:hover {
        background-color: rgb(211, 21, 21);
      }

      .button:active {
        background-color: rgb(130, 0, 0);
      }

      .button:hover > .close {
        animation: close 0.2s forwards 0.25s;
      }

      @keyframes close {
        100% {
          opacity: 1;
        }
      }


    }
  }

  .DAMessage {
    position: fixed;
    width: 39vw;
    height: 51vh;
    margin-left: -41.1vw;
    margin-top: 13vh;
    z-index: 999;
      border-radius: 6px;
    background: #c70000;

    .main {
        width: 35vw;
        height: 45vh;
        background: red; /* 初始背景色 */
        margin-left: 2vw;
        margin-top: 3vh;
        position: absolute;
        border-radius: 6px;
        animation: fadeBackground 4s infinite; /* 应用名为 fadeBackground 的动画，持续4秒，无限循环 */
        .big{
            width: 1000vw;
            height: 1000vh;
            background: rgba(255, 0, 0, 0.2);
            position: absolute;
            margin-top: -100vh;
            margin-left: -100vw;
        }
        .close{
            width: 10vw;
            height: 7vh;
            border-radius: 6px;
            border: none;
            background: white;
            font-size: 1.8em;
            color:red;
            position: absolute;
            margin-top: 37vh;
            margin-left: 12.5vw;
        }
        .thing{
            color:#ffe800;
            font-weight: bolder;
            font-size: 3.5em;
            position: absolute;
            width: 35vw;
            margin-top: 3.5vh;
            text-align: center;
        }
        .little{
            color:white;
            position: absolute;
            font-size: 1.3em;
            width: 35vw;
            text-align: center;
            margin-top: 13vh;
            font-weight: bolder;
        }
        img{
            position: absolute;
            margin-left: 10vw;
            margin-top: 13vh;
            width: 15vw;
        }
    }

  }

  Button {
    position: absolute;
    margin-top: 22.1vh;
    margin-left: 4vw;
    border: none;
    font-weight: bolder;
    color: white;
    background: #0d87f6;
    border-radius: 3px;
    width: 6vw;
    line-height: 3vh;
    font-size: 1em;
    height: 3vh;
  }

  Button:hover {
    cursor: pointer;
  }

  .go {
    margin-left: 12vw;
  }

  .wrong {
    margin-left: 19vw;
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
    @keyframes fadeBackground {
        0%, 100% {
            background-color: transparent; /* 透明背景色 */
        }
        50% {
            background-color: red; /* 初始背景色 */
        }
    }
}
</style>