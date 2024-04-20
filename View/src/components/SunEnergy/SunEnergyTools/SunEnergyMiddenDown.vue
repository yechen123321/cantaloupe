<script setup>
import SunEnergyMiddenDownThing from "@/components/SunEnergy/SunEnergyTools/SunEnergyMiddenDownThing.vue";
import {ref, reactive, onBeforeUnmount, onUnmounted, nextTick} from 'vue'
import {initKlist} from "@/api";

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

initKlist().then(data => {
    listData.splice(0, listData.length, ...data.data);
    nextTick(() => {
        start();
    });
}).catch(error => {
    console.error('Failed to fetch data:', error);
});


</script>

<template>
    <div class="SunEnergyMiddenDown">
        <div class="title">发电装置信息概览</div>
        <div class="SunEnergyMiddenDown-echarts" ref="echartsRef"></div>
        <div class="roll">
            <div class="top">
                <div class="name">名称</div>
                <div class="do">类型</div>
                <div class="number">状态</div>
                <div class="up">实时信息</div>
                <div class="when">检查时间</div>
            </div>
            <div class="roll-in" ref="roll">
                <div class="roll-main" v-for="item in listData" :key="item.id">
                    <div @mousemove="testMove" @mouseleave="testMend" class="name">
                        <div class="name">{{ item.name }}</div>
                        <div class="do">{{ item.do }}</div>
                        <div class="number">{{ item.number }}</div>
                        <div class="up">{{ item.up }}</div>
                        <div class="when">{{ item.when }}</div>
                    </div>
                </div>
            </div>
        </div>
        <div class="right">
            <SunEnergyMiddenDownThing id="SunEnergyMiddenDownThing-out"></SunEnergyMiddenDownThing>
        </div>
        <img src="../../../assets/pic/border4.png" alt="" class="BackImg">
    </div>
</template>

<style scoped lang="scss">
.SunEnergyMiddenDown {
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
        margin-left: 3.3vw;
      }

      .number {
        float: left;
        margin-top: 0.3vh;
        margin-left: 2.5vw;
      }

      .up {
        float: left;
        margin-top: 0.3vh;
        margin-left: 2vw;
      }

      .when {
        float: left;
        margin-top: 0.3vh;
        margin-left: 2.7vw;
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
          margin-left: 1.2vw;
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
          width: 5vw;
          margin-top: 0.3vh;
          text-align: center;
          margin-left: -0.3vw;
        }

        .do {
          float: left;
          margin-top: 0.3vh;
          text-align: center;
          margin-left: 0.3vw;
          width: 4vw;
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

    #SunEnergyMiddenDownThing-out {
      width: 24vw;
      height: 24vh;
      margin-left: -1.5vw;
      position: absolute;
      z-index: 300;
    }
  }

  .SunEnergyMiddenDown-echarts {
    position: absolute;
    width: 29vw;
    height: 34vh;
    margin-left: 1vw;
    z-index: 300;
  }

  .title {
    color: white;
    position: absolute;
    font-weight: bolder;
    font-size: 1.3em;
    width: 20vw;
    text-align: center;
    margin-left: 3.6vw;
    margin-top: 0.5vh;
  }

  .BackImg {
    width: 43vw;
    height: 31vh;
  }
}
</style>