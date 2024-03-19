<script setup>
import {ref} from 'vue';
import {useRouter} from 'vue-router';

const router = useRouter();

const handleRouteChange = () => {
    // 在这里添加您的路由切换逻辑，下面是一个示例，实际根据您的路由配置进行修改
    router.push('/anhuirenew'); // 替换'/new-route'为您要跳转的路由路径
};

const RouteToSun = () => {
    // 在这里添加您的路由切换逻辑，下面是一个示例，实际根据您的路由配置进行修改
    router.push('/anhuisun'); // 替换'/new-route'为您要跳转的路由路径
};

const RouteToWind = () => {
    // 在这里添加您的路由切换逻辑，下面是一个示例，实际根据您的路由配置进行修改
    router.push('/anhuiwind'); // 替换'/new-route'为您要跳转的路由路径
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


</script>

<template>
    <div class="ChooseTable">
        <div class="ChooseTitle">
            安徽地区基本信息
        </div>
        <div class="MySelect">
            <select class="SelectBox">
                <option class="options" v-for="(option, index) in options" :key="index">
                    {{ option.where }}
                </option>
            </select>
        </div>
        <button class="SelectGo" @click="handleRouteChange">切换</button>
        <div class="factory">
            <ul class="factoryUl">
                <li @click="handleRouteChange" style="margin-top: -2vh">
                    <img src="../../../assets/水库.png" alt="">
                    <img src="../../../assets/pic/pic-5.png" alt=""
                         style="width: 10vw;margin-top: -1vh; margin-left: -4.5vw; position: absolute;">
                    <div class="number">43.59</div>
                    <div class="up">
                        水生电能
                    </div>
                    <div class="down">
                        亿千瓦时
                    </div>
                </li>
                <li @click="RouteToSun" style="margin-top: 0.8vh">
                    <img src="../../../assets/太阳能发电.png" alt="">
                    <div class="number">3135</div>
                    <div class="up">
                        光生电能
                    </div>
                    <div class="down">
                        亿千瓦时
                    </div>
                </li>
                <li @click="RouteToWind">
                    <img src="../../../assets/风力发电.png" alt="">
                    <div class="number">8800</div>
                    <div class="up">
                        风生电能
                    </div>
                    <div class="down">
                        亿千瓦时
                    </div>
                </li>
            </ul>
        </div>
        <img src="../../../assets/pic/border4.png" alt="" class="BackImg">
    </div>
</template>

<style scoped lang="scss">
.ChooseTable {
  .factory {
    position: absolute;
    width: 26vw;
    height: 15vh;
    margin-top: 2.5vh;
    margin-left: 2vw;
    //background: white;
    .factoryUl {
      position: absolute;
      list-style: none;
      width: 40vw;
      height: 15vh;
      margin-left: -6.8vw;
      //background: red;
      li:hover {
        cursor: pointer;
      }

      li {
        width: 6vw;
        height: 15vh;
        float: left;
        margin-left: 4vw;
        margin-top: -1vh;
        //background: red;
        .number {
          color: white;
          margin-left: 4vw;
          margin-top: -5vh;
          font-size: 1.6vw;
          font-weight: bolder;
        }

        img {
          width: 3.5vw;
        }


        .up {
          width: 8vw;
          height: 6vh;
          margin-top: 1vh;
          padding-top: 0.5vh;
          border-top: 2px solid #0d87f6;
          color: rgb(127, 235, 240);
          text-shadow: 0 0 2px #b6d4df, 0 0 5px #b6d4df; //设置发光效果
          font-size: 1.5vw;
          text-align: center;
          //background: red;
        }

        .down {
          color: white;
          font-size: 1vw;
          margin-left: 2vw;
          font-weight: bolder;
          margin-top: -1.5vh;
          text-align: center;
        }
      }
    }
  }

  .ChooseTitle {
    font-size: 1.5vw;
    font-weight: bolder;
    color: white;
    right: 0;
    margin-right: 2vw;
    position: absolute;
    margin-left: 2vw;
    margin-top: 1vh;
  }

  .MySelect {
    width: 10vw;
    height: 10vh;
    right: 0;
    position: absolute;
    margin-top: 6vh;
    z-index: 222;
    margin-right: -1vw;

    .SelectBox {
      width: 7vw;
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

  .SelectGo {
    width: 7vw;
    height: 4vh;
    right: 0;
    margin-top: 12vh;
    margin-right: 2vw;
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
    margin-top: 11.5vh;
    margin-right: 1.7vw;
    font-size: 1.4vw;
  }

  .SelectGo:active {
    width: 7vw;
    height: 4vh;
    margin-top: 12vh;
    margin-right: 2vw;
    font-size: 1vw;
  }

  .BackImg {
    width: 40vw;
    height: 20vh;
  }
}
</style>
