<script setup>
import {ref} from "vue";
// // import axios from "axios";
// import {API_BASE_URL} from "../../../config";
const items = ref([
    {name: '全国煤炭产量同比增长', number: 466000, up: '万吨', num: 2.19},
]);

// let items = ref([]); // 初始化 items 为响应式空数组
//
// onMounted(async () => {
//     try {
//         const response = await fetch(API_BASE_URL+'/api/fbv/list'); // 使用你的 API 端点
//         if (!response.ok) {
//             throw new Error(`HTTP error! status: ${response.status}`);
//         }
//         items.value = await response.json();
//     } catch (error) {
//         console.log('Fetch error: ', error);
//     }
// });

// let scrollDown = true; // 初始化 scrollDown 变量为 true
// let index = 0; // 初始化 index 变量为 0
//
// setInterval(() => {
//     const ulElement = document.querySelector('.year-on-year');
//     const liHeight = 95; // 每个 li 元素的高度，单位为 vh
//     if (ulElement) {
//         if (scrollDown) {
//             ulElement.scrollTop += liHeight;
//             if (ulElement.scrollTop + ulElement.clientHeight >= ulElement.scrollHeight) {
//                 ulElement.scrollTop = 0; // 滚动到最后一个时回到第一个
//             }
//         } else {
//             ulElement.scrollTop -= liHeight;
//         }
//
//         index++;
//         if (index >= items.value.length) {
//             index = 0;
//         }
//         const activeElement = document.querySelector('.li-active');
//         activeElement?.classList.remove('li-active');
//         const newActiveElement = document.querySelectorAll('.year-on-year li')[index];
//         newActiveElement?.classList.add('li-active');
//     }
// }, 2000);
</script>

<template>
    <div class="FirstMainTable">
        <img class="BackImg" src="../../assets/pic/ca1.png" alt="">
        <ul class="year-on-year">
            <li v-for="(item,index) in items" :class="{ 'li-active': index === 0 }" :key="index">
                <div class="li-title">{{ item.name }}</div>
                <div class="li-number">{{ item.number }}</div>
                <div class="li-up">{{ item.up }}</div>
                <div class="li-midden">同比增长</div>
                <div class="li-num">{{ item.num }}%</div>
            </li>
        </ul>
    </div>
</template>

<style scoped lang="scss">
.FirstMainTable {
  width: 100vw;
  height: 100vh;

  .year-on-year::-webkit-scrollbar {
    display: none;
  }

  .year-on-year {
    //background: red;
    height: 18vh;
    //margin: 0.5vw;
    //margin-top: 2vw;
    position: absolute;
    z-index: 10;
    //overflow: hidden;
    overflow-y: auto;
    //box-sizing: border-box;
    width: 100%;

    li {
      list-style-type: none;
      width: 100%;
      margin-top: 2%;
      line-height: 4.5vh;
      color: white;
      height: 100%;

      .li-title {
        float: left;
        width: 18vw;
          margin-bottom: 2%;
      }

      .li-number {
        float: left;
        color: #1cd7cd;
        text-align: center;
        width: 25%;
        font-weight: bolder;
        text-shadow: 0 0 1px #1cd7cd, 0 0 2px #1cd7cd, 0 0 3px #1cd7cd;
        font-size: 2em;
      }

      .li-up {
        float: left;
        margin-left: 4.5%;
        margin-top: 1.3%;
        color: #01bae4;
        text-shadow: 0 0 1px #1cd7cd, 0 0 1px #1cd7cd, 0 0 1.5px #1cd7cd;
      }

      .li-midden {
        float: left;
        margin-left: 4%;
        margin-top: 1.3%;
        color: #01bae4;
        text-shadow: 0 0 1px #1cd7cd, 0 0 1px #1cd7cd, 0 0 1.5px #1cd7cd;
      }

      .li-num {
        float: left;
        margin-left: 5%;
        font-size: 2em;
        color: yellow;
        font-weight: bolder;
      }
    }
  }

  .BackImg {
    position: absolute;
    width: 25vw;
    height: 10vw;
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
