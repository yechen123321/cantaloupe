<script setup>
import ThermalPowerMiddenDownThing from "@/components/ThermalPower/ThermalPowerTools/ThermalPowerMiddenDownThing.vue";
import {ref, reactive, onBeforeUnmount, onUnmounted, nextTick} from 'vue'
import {initp41} from "@/api";

let timer = ref(null);
let roll = ref(null);
let listData = reactive([]);

onBeforeUnmount(() => {
    clearTimeout(timer.value);
});

onUnmounted(() => {
    clearTimeout(timer.value);
});

function testMove() {
    clearTimeout(timer.value);
}

function testMend() {
    start();
}

function start() {
    clearTimeout(timer.value);
    let speed = ref(100);
    timer.value = setInterval(MarqueeTest, speed.value);
}

function MarqueeTest() {
    let test1 = roll.value;

    if (test1 && test1.offsetHeight == 0) {
        test1 = roll.value;
    } else {
        test1.scrollTop += 1;

        if (test1.scrollTop >= (test1.scrollHeight - test1.clientHeight)) {
            test1.scrollTop = 0;
        }
    }

}

initp41().then(data => {
    listData.splice(0, listData.length, ...data.data);
    nextTick(() => {
        start();
    });
}).catch(error => {
    console.error('Failed to fetch data:', error);
});


</script>

<template>
    <div class="ThermalPowerMiddenDown">
        <div class="title">发电装置信息概览</div>
        <div class="roll">
            <div class="top">
                <div class="name">序号</div>
                <div class="do">类型</div>
                <div class="number">状态</div>
                <div class="up">实时信息</div>
                <div class="when">检查时间</div>
            </div>
            <div class="roll-in" ref="roll">
                <div class="roll-main" v-for="item in listData" :key="item.id">
                    <div @mousemove="testMove" @mouseleave="testMend" class="name">
                        <div class="name">{{ item.name }}</div>
                        <div class="do">{{ item.type }}</div>
                        <div class="number">{{ item.state }}</div>
                        <div class="up">{{ item.manage }}</div>
                        <div class="when">{{ item.when }}</div>
                    </div>
                </div>
            </div>
        </div>
        <div class="right">
            <ThermalPowerMiddenDownThing id="ThermalPowerMiddenDownThing-out"></ThermalPowerMiddenDownThing>
        </div>
        <img src="../../../assets/pic/border4.png" alt="" class="BackImg">
    </div>
</template>

<style scoped lang="scss">
.ThermalPowerMiddenDown {
  width: 100%;
  height: 100%;

  .roll {
    color: white;
    position: absolute;
    width: 27vw;
    margin-top: 6vh;
    height: 40vh;
    margin-left: 1vw;

    .top {
      width: 100%;
      height: 3.5vh;
      background: rgba(255, 255, 255, .2);
      margin-top: -1vh;

      .name {
        float: left;
        margin-left: 1.3vw;
        margin-top: 0.3vh;

      }

      .do {
        float: left;
        margin-top: 0.3vh;
        margin-left: 2.1vw;
      }

      .number {
        float: left;
        margin-top: 0.3vh;
        margin-left: 1.6vw;
      }

      .up {
        float: left;
        margin-top: 0.3vh;
        margin-left: 2vw;
      }

      .when {
        float: left;
        margin-top: 0.3vh;
        margin-left: 3.2vw;
      }
    }

    .roll-in {
      width: 27vw;
      height: 20.5vh;
      overflow: hidden;
      margin-right: 2vw;
      margin-top: 1vh;

      .roll-main {
        width: 100%;
        height: 5vh;
        background: rgba(13, 135, 246, 0.1);
        margin-top: 1vh;

        .name {
          float: left;
          margin-left: 0.1vw;
          margin-top: 0.3vh;
          text-align: center;
        }

        .number {
          float: left;
          margin-top: 0.3vh;
          text-align: center;
          margin-left: -0.9vw;
          width: 4vw;
        }

        .when {
          float: left;
          margin-top: 0.3vh;
          text-align: center;
          margin-left: 1vw;
        }

        .up {
          float: left;
          width: 7vw;
          margin-top: 0.3vh;
          text-align: center;
          margin-left: -0.3vw;
        }

        .do {
          float: left;
          margin-top: 0.3vh;
          text-align: center;
          margin-left: 0.2vw;
          width: 5vw;
        }
      }
    }
  }

  .right {
    width: 15vw;
    height: 23vh;
    margin-top: 6vh;
    border-left: #0d87f6 2px solid;
    margin-right: 1vw;
    position: absolute;
    right: 0;

    #ThermalPowerMiddenDownThing-out {
      width: 15vw;
      height: 24vh;
      margin-left: -0.5vw;
      position: absolute;

    }
  }

  .ThermalPowerMiddenDown-echarts {
    position: absolute;
    width: 28.5vw;
    height: 35vh;
    margin-left: -0.3vw;
    margin-top: 1vh;
    z-index: 300;
  }

  .title {
    color: white;
    position: absolute;
    font-weight: bolder;
    font-size: 1.25em;
    width: 20vw;
    text-align: center;
    margin-left: 3.6vw;
    margin-top: 1vh;
  }

  .BackImg {
    width: 43vw;
    height: 31vh;
  }
}
</style>