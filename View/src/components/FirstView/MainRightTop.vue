<script setup>
import {ref} from "vue";
import { inita } from "@/api"
const datas = ref([]);
const listData = ref({});

inita().then(response => {
    Object.assign(listData.value, response.data);
    // 将listData中的数据写入datas
    const newData = {
        name: listData.value["name"][0],
        number: listData.value["number"][0],
        up: listData.value["up"][0],
        num: listData.value["num"][0]
    };
    datas.value.push(newData);
}).catch(error => {
    console.error('Error fetching data:', error);
});
</script>

<template>
    <div class="FirstMainTable">
        <img class="BackImg" src="../../assets/pic/ca1.png" alt="">
        <ul class="year-on-year">
            <li v-for="(item,index) in datas" :class="{ 'li-active': index === 0 }" :key="index">
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
    height: 18vh;
    position: absolute;
    z-index: 10;
    overflow-y: auto;
    width: 100%;
    margin-top: 0.6vh;
    margin-left: -1.5vw;

    li {
      list-style-type: none;
      width: 90%;
      margin-top: 2%;
      line-height: 4.5vh;
      color: white;
      height: 100%;

      .li-title {
        float: left;
        width: 18vw;
        font-size: 1.2vw;
        font-weight: bolder;
        margin-bottom: 2%;
      }

      .li-number {
        float: left;
        color: #1cd7cd;
        text-align: center;
        width: 30%;
        font-weight: bolder;
        text-shadow: 0 0 1px #1cd7cd, 0 0 2px #1cd7cd, 0 0 3px #1cd7cd;
        font-size: 2em;
      }

      .li-up {
        float: left;
        margin-left: 4.5%;
        font-size: 1em;
        margin-top: 1.3%;
        color: #01bae4;
        text-shadow: 0 0 1px #1cd7cd, 0 0 1px #1cd7cd, 0 0 1.5px #1cd7cd;
      }

      .li-midden {
        float: left;
        margin-left: 4%;
        margin-top: 1.3%;
        font-size: 1em;
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
    height: 8vw;
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
