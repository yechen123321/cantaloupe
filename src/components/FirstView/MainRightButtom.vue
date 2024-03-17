<script setup>
// import {onMounted, ref} from "vue";
// import * as echarts from "echarts";
// // // import axios from "axios";
// // import {API_BASE_URL} from "../../../config";
//
// const echartsRef = ref(null);
// let myChart25 = null;
// let option25 = null;
//
// onMounted(() => {
//     myChart25 = echarts.init(echartsRef.value, 'dark');
//
//     // Your echarts option setup here...
//     // (Your existing option setup code)
//     option25 = {}
//     option25 && myChart25.setOption(option25);
//
//     const resizeObserver = new ResizeObserver(() => {
//         myChart25.resize();
//     });
//
//     resizeObserver.observe(echartsRef.value);
// });
import {ref} from "vue";

const twice = ref([
    {name: '全国电力市场交易电量', number: 28000, up: '亿', num: 1.6},
    {name: '全国煤层气开发投资', number: 28000, up: '亿', num: 1.6},
]);
</script>

<template>
    <div class="MainRightButtom">
        <img class="BackImg" src="../../assets/pic/pic-3.png" alt="">
        <div class="MainRightButtom-main">
            <li v-for="(item,index) in twice" :class="{ 'li-active': index === 0 }" :key="index">
                <div class="MainRightButtom-title">{{ item.name }}</div>
                <div class="MainRightButtom-number">{{ item.number }}</div>
                <div class="MainRightButtom-up">{{ item.up }}</div>
                <div class="MainRightButtom-midden">同比增长</div>
                <div class="MainRightButtom-num">{{ item.num }}%</div>
            </li>
        </div>

        <!--        <div class="MySelect">-->
        <!--            <select name="" id="" class="SelectBox">-->
        <!--                <option>全国</option>-->
        <!--                <option>安徽</option>-->
        <!--                <option>北京</option>-->
        <!--                <option>浙江</option>-->
        <!--                <option>重庆</option>-->
        <!--                <option>西藏</option>-->
        <!--                <option>四川</option>-->
        <!--                <option>山东</option>-->
        <!--                <option>上海</option>-->
        <!--                <option>广东</option>-->
        <!--                <option>广西</option>-->
        <!--            </select>-->
        <!--            <Button class="GotoAn" @click="handleRouteChange">切换</Button>-->
        <!--        </div>-->

        <!--        <div class="MainRightButtom-echarts" ref="echartsRef"></div>-->
    </div>
</template>

<style scoped lang="scss">
.MainRightButtom {
  width: 100vw;
  height: 100vh;

  .MainRightButtom-main {
    width: 100%;
    //background-color: red;
    height: 25vh;
    margin-top: 6vh;
    //margin-left: 0.3vw;
    list-style: none;

    li {
      //background: red;
      width: 100%;
      height: 10vh;
      margin-top: 2vh;
    }

    .MainRightButtom-title {
      color: white;
      position: absolute;
      width: 18vw;
      font-size: 1.2vw;
      font-weight: bolder;
      //margin-top: 5vh;
      margin-left: 2vw;
    }

    .MainRightButtom-number {
      position: absolute;
      font-weight: bolder;
      margin-top: 4vh;
      margin-left: 2vw;
      color: #1cd7cd;
      text-align: center;
      width: 30%;
      text-shadow: 0 0 1px #1cd7cd, 0 0 2px #1cd7cd, 0 0 3px #1cd7cd;
      font-size: 2em;

    }

    .MainRightButtom-up {
      color: #01bae4;
      text-shadow: 0 0 0.1px #1cd7cd, 0 0 0.1px #1cd7cd;
      position: absolute;
      font-size: 1em;
      font-weight: bolder;
      margin-top: 6vh;
      margin-left: 10vw;
    }

    .MainRightButtom-midden {
      color: #01bae4;
      text-shadow: 0 0 0.1px #1cd7cd, 0 0 0.1px #1cd7cd;
      position: absolute;
      font-size: 1em;
      font-weight: bolder;
      margin-top: 6vh;
      width: 25%;
      margin-left: 12vw;
    }

    .MainRightButtom-num {
      color: yellow;
      position: absolute;
      font-size: 2em;
      font-weight: bolder;
      margin-top: 5vh;
      margin-left: 17.3vw;
    }
  }


  .MainRightButtom-echarts {
    width: 16vw;
    height: 25vh;
    position: absolute;
    z-index: 166;
    margin-top: -1.5vh;
    margin-left: 1vw;
  }

  .MySelect {
    margin-top: 8vh;

    .SelectBox {
      position: absolute;
      width: 6vw;
      height: 3.5vh;
      cursor: pointer;
      overflow: hidden;
      font-size: 1vw;
      right: 0;
      margin-top: 5vh;
      margin-right: 0.5vw;
      background: #4d70cd;
      color: white;
      border: none;
      text-align: center;
      border-radius: 6px;
    }

    .GotoAn {
      width: 6vw;
      height: 3.5vh;
      right: 0;
      margin-top: 10.5vh;
      margin-right: 0.5vw;
      position: absolute;
      cursor: pointer;
      font-size: 1vw;
      font-weight: bolder;
      color: white;
      border: none;
      border-radius: 6px;
      background: #0d87f6;
      z-index: 222;
    }

    .GotoAn:hover {
      width: 6.5vw;
      height: 4vh;
      font-size: 1.2vw;
      margin-top: 10.4vh;
      margin-right: 0.2vw;
    }

    .GotoAn:active {
      width: 6vw;
      height: 3.5vh;
      font-size: 1vw;
      margin-top: 10.5vh;
      margin-right: 0.5vw;
    }
  }

  .BackImg {
    position: absolute;
    width: 27vw;
    height: 18vw;
    margin-left: -1vw;
    margin-top: -0.5vw;
  }

  @keyframes glow {

    from {
      box-shadow: 0px 0px 3px 3px #00bfff, 0px 0px 5px 3px #0d0d0d, 0px 0px 7px 5px #00bfff;
    }

    to {
      box-shadow: 0px 0px 5px 3px #00bfff, 0px 0px 7px 5px #0d0d0d, 0px 0px 9px 7px #00bfff;
    }
  }

}
</style>
