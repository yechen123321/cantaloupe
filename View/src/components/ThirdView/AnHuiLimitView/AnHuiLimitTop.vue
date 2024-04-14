<script setup>
import {onMounted, ref} from 'vue';
import router from "@/router";

const handleRouteChange = () => {
    // 在这里添加您的路由切换逻辑，下面是一个示例，实际根据您的路由配置进行修改
    router.push('/anhuilimit'); // 替换'/new-route'为您要跳转的路由路径
};
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



onMounted(() => {

});

</script>

<template>
    <div class="AnHuiLimitTop">
        <div class="title">安徽省有限资源储能图</div>
        <img src="../../../assets/pic/border4.png" alt="" class="BackImg">
        <div class="MySelect">
            <select class="SelectBox">
                <option class="options" v-for="(option, index) in options" :key="index">
                    {{ option.where }}
                </option>
            </select>
            <button class="SelectGo" @click="handleRouteChange">切换</button>
        </div>
    </div>
</template>

<style scoped lang="scss">
.AnHuiLimitTop {
  width: 100%;
  height: 100%;

  .MySelect {
    width: 12vw;
    height: 18vh;
    margin-left: 30vw;
    margin-top: -22vh;
    position: absolute;
    z-index: 222;
    border-left: 2px solid #0d87f6;

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

    .SelectGo {
      width: 7vw;
      height: 4vh;
      right: 0;
      margin-top: 9vh;
      margin-right: 2.5vw;
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

    .SelectGo:hover {
      width: 7.5vw;
      height: 5vh;
      margin-top: 8.5vh;
      margin-right: 2.15vw;
      font-size: 1.4vw;
    }

    .SelectGo:active {
      width: 7vw;
      height: 4vh;
      margin-top: 9vh;
      margin-right: 2.5vw;
      font-size: 1vw;
    }
  }

  .title {
    position: absolute;
    color: white;
    width: 40vw;
    text-align: center;
    font-size: 1.3em;
    margin-left: 1.2vw;
    margin-top: 1vh;
    font-weight: bolder;
  }

  .BackImg {
    width: 42.5vw;
    height: 28vh;
  }
}
</style>