<script setup>
import {ref} from "vue";

const downloadLocalWordDoc = () => {
    // 本地 Word 文档的文件路径
    const localDocPath = 'https://student-portrait-1314223587.cos.ap-nanjing.myqcloud.com/Data.docx';
    // 创建一个链接元素并设置下载属性
    const a = document.createElement('a');
    a.href = localDocPath;
    a.download = 'local-doc.docx';
    document.body.appendChild(a);
    // 模拟点击链接进行下载
    a.click();
    // 清理链接元素
    document.body.removeChild(a);
};
const datas = ref([
    {name: '资源', thing: '生物质能源'},
    {name: '资源', thing: '水能资源'},
    {name: '资源', thing: '太阳能资源'},
    {name: '转换', thing: '生物质能转换'},
    {name: '转换', thing: '水能转换'},
    {name: '转换', thing: '太阳能转换'},
]);
const reportGenerated = ref(false);
const updateReport = () => {
    reportGenerated.value = true;
};
const showReport = () => {
    // 这里可以添加显示报告的逻辑
};


</script>

<template>
    <div class="DataAnalysisRightTop">
        <div class="title">能源转换示例</div>
        <div class="ul">
            <ul>
                <li v-for="(item,index) in datas" :class="{ 'li-active': index === 0 }" :key="index">
                    <div class="name">{{ item.name }}：</div>
                    <div class="thing">{{ item.thing }}</div>
                </li>
            </ul>
        </div>
        <button class="update" @click="updateReport" v-show="!reportGenerated">生成报告</button>
        <button class="done" @click="showReport" v-show="reportGenerated">已生成报告</button>
        <button @click="downloadLocalWordDoc" class="goto" :disabled="!reportGenerated">导出报告</button>
        <img src="../../../assets/pic/ca1.png" alt="" class="BackImg">
    </div>
</template>

<style scoped lang="scss">
.DataAnalysisRightTop {
  width: 100%;
  height: 100%;

  .ul {
    position: absolute;
    width: 22vw;
    height: 10vh;
    background: rgba(10, 67, 188, .3);
    border-radius: 5px;
    margin-top: 9vh;
    margin-left: 2vw;
    overflow-y: auto;
    -ms-overflow-style: none; /* IE 和 Edge */
    scrollbar-width: none; /* Firefox */
    ul {
      width: 21.4vw;
      margin-top: -0.5vh;
      height: 10vh;
      margin-left: -2vw;
      //background: red;

      li {
        list-style: none;
        width: 9vw;
        margin-top: 1.6vh;
        margin-left: 1vw;
        float: left;
        height: 3vh;
        //background: rgba(10, 67, 188, .4);
        .name {
          width: 8vw;
          height: 3vh;
          color: white;
          font-weight: bolder;
          //margin-left: -1vw;
          margin-top: 0.2vh;
          //background: #0d87f6;
          position: absolute;
        }

        .thing {
          width: 8vw;
          height: 3vh;
          color: white;
          font-weight: bolder;
          margin-left: 3.5vw;
          margin-top: 0.2vh;
          //background: #ffffff;
          position: absolute;
        }
      }
    }

  }

  .goto {
    width: 6vw;
    height: 3.5vh;
    line-height: 3vh;
    text-align: center;
    position: absolute;
    border-radius: 3px;
    margin-top: 19.8vh;
    margin-left: 14vw;
    font-size: 1em;
    color: white;
    background: rgb(25, 83, 206);
    border: none;
    font-weight: bolder;
  }

  .goto:hover {
    cursor: pointer;
  }

    .goto:disabled{
        background: #b6d4df;
        color:white;
        cursor: no-drop;
    }

  .done {
    width: 6vw;
    height: 3.5vh;
    line-height: 3vh;
    text-align: center;
    position: absolute;
    border-radius: 3px;
    margin-top: 19.8vh;
    margin-left: 6vw;
    font-size: 1em;
    color: white;
    background: rgb(25, 83, 206);
    border: none;
    font-weight: bolder;
  }

  .update {
    width: 6vw;
    height: 3.5vh;
    line-height: 3vh;
    text-align: center;
    position: absolute;
    border-radius: 3px;
    margin-top: 19.8vh;
    margin-left: 6vw;
    font-size: 1em;
    color: white;
    background: rgb(25, 83, 206);
    border: none;
    font-weight: bolder;
  }

  .done:hover {
    cursor: pointer;
  }

  .update:hover {
    cursor: pointer;
  }

  .title {
    position: absolute;
    color: white;
    font-size: 1.3em;
    font-weight: bolder;
    margin-top: 5vh;
    margin-left: 2.5vw;
  }

  .BackImg {
    width: 26vw;
    height: 28vh;
  }
}
</style>