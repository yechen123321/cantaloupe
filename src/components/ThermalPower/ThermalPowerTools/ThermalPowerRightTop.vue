<script setup>
import {ref} from "vue";

const reportGenerated = ref(false);

const updateReport = () => {
    reportGenerated.value = true;
};

const showReport = () => {
    // 这里可以添加显示报告的逻辑
    reportGenerated.value = false;
};

</script>

<template>
    <div class="ThermalPowerRightTop">
        <div class="updateMessage" v-show="!reportGenerated">
            <div class="title">
                <button @click="showReport" class="button">
                    <span class="X"></span>
                    <span class="Y"></span>
<!--                    <div class="close">关闭</div>-->
                </button>
            </div>
            <div class="main"></div>
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
        <Button @click="updateReport" class="go">维修通知</Button>
        <Button class="update">更新数据</Button>
        <Button class="wrong">危险警报</Button>
        <img src="../../../assets/pic/ca1.png" alt="" class="BackImg">
    </div>
</template>

<style scoped lang="scss">
.ThermalPowerRightTop {
  width: 100%;
  height: 100%;
    .updateMessage{
        position: fixed;
        width: 35vw;
        height: 45vh;
        margin-left: -39.1vw;
        margin-top: 15vh;
        z-index:999;
        .main{
            width: 35vw;
            height: 40vh;
            background: rgba(56, 120, 238, 0.8);
            margin-left: 0vw;
            margin-top: 5vh;
            position: absolute;
        }
        .title{
            width: 35vw;
            height: 5vh;
            background: rgba(19, 47, 234, 0.8);
            margin-left: 0vw;
            margin-top: 0vh;
            position: absolute;
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

            .name{
                color:white;
                position: absolute;
                font-size: 1.3em;
                font-weight: bolder;

            }
        }
    }

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