<script setup>
import {ref} from 'vue';

const options = ref([
    {where: '安徽', value: 1},
    {where: '北京', value: 2},
    {where: '浙江', value: 3},
    {where: '重庆', value: 4},
    {where: '西藏', value: 5},
    {where: '四川', value: 6},
    {where: '山东', value: 7},
    {where: '上海', value: 8},
    {where: '广东', value: 9},
    {where: '广西', value: 10},
]);
</script>

<template>
  <div class="AnHuiLimitTop">
      <div class="title">安徽省有限资源产能图</div>
      <img src="../../../assets/pic/border4.png" alt="" class="BackImg">
      <div class="MySelect">
          <select class="SelectBox">
              <option class="options" v-for="(option, index) in options" :key="index">
                  {{ option.where }}
              </option>
          </select>
      </div>
  </div>
</template>

<style scoped lang="scss">
  .AnHuiLimitTop{
    width: 100%;
    height: 100%;
    .MySelect {
      width: 12vw;
      height: 18vh;
      //background: red;
      margin-left: 30vw;
      margin-top: -22vh;
      position: absolute;
      //margin-top: 6vh;
      z-index: 222;
      border-left: 2px solid #0d87f6;
      //margin-right: -1vw;

      .SelectBox {
        width: 7vw;
        margin-left: 2.5vw;
        margin-top: 2vh;
        height: 4vh;
        cursor: pointer;
        overflow: hidden;
        font-size: 1vw;
        background: #4d70cd;
        color: white;
        border: none;
        text-align: center;
        border-radius: 6px;

      }
    }
    .title{
      position: absolute;
      color:white;
      width: 40vw;
      //background: red;
      text-align: center;
      font-size: 1.4em;
      margin-left: 13vw;
      margin-top: 1.5vh;
      font-weight: bolder;
    }
    .BackImg{
      width: 42.5vw;
      height: 28vh;
      //position: absolute;
    }
  }
</style>