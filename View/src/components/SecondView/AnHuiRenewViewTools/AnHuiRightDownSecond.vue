<script setup>
import {ref, reactive, onBeforeUnmount, onUnmounted, nextTick} from 'vue'
import {initKlist10} from "@/api";

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

initKlist10().then(data => {
    listData.splice(0, listData.length, ...data.data);
    console.log(data)
    nextTick(() => {
        start();
    });
}).catch(error => {
    console.error('Failed to fetch data:', error);
});


</script>


<template>
    <div class="AnHuiRightDownSecond">
        <div class="roll">
            <div class="top">
                <div class="name">设施</div>
                <div class="do">工作</div>
                <div class="number">数目</div>
                <div class="up">单位</div>
                <div class="when">时间</div>
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
    </div>
</template>

<style scoped lang="scss">
.AnHuiRightDownSecond {
  width: 100%;
  height: 100%;

  .roll {
    color: white;
    width: 23vw;
    margin-top: 28vh;
    height: 40vh;
    margin-left: -1vw;

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
        margin-left: 2.3vw;
      }

      .number {
        float: left;
        margin-top: 0.3vh;
        margin-left: 1.9vw;
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
      width: 23vw;
      height: 20.5vh;
      //background: red;
      overflow: hidden;
      margin-right: 2vw;
      margin-top: 1vh;

      .roll-main {
        //background: red;
        width: 100%;
        height: 5vh;
        background: rgba(13, 135, 246, 0.1);
        margin-top: 1vh;

        .name {
          float: left;
          //background: red;
          margin-left: 0.1vw;
          margin-top: 0.3vh;
          text-align: center;
        }

        .number {
          float: left;
          //background: red;
          margin-top: 0.3vh;
          text-align: center;
          margin-left: 1.2vw;
          width: 4vw;
        }

        .when {
          float: left;
          //background: red;
          margin-top: 0.3vh;
          text-align: center;
          margin-left: 1vw;
        }

        .up {
          float: left;
          width: 5vw;
          //background: red;
          margin-top: 0.3vh;
          text-align: center;
          margin-left: -0.3vw;
          margin-right: -1.1vw;
        }

        .do {
          float: left;
          margin-top: 0.3vh;
          text-align: center;
          margin-left: 0.3vw;
          margin-right: -1.3vw;
          //background: red;
          width: 4vw;
        }
      }
    }
  }
}
</style>