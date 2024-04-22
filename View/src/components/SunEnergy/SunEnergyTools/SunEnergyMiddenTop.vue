<script setup>
import {ref} from "vue";

const reportGenerated = ref(false);

const updateReport = () => {
    reportGenerated.value = true;
};

const showReport = () => {
    // 这里可以添加显示报告的逻辑
    reportGenerated.value = false;
};
</script>

<template>
    <div class="SunEnergyMiddenTop">
        <div class="VI">
            <button class="Second" v-show="!reportGenerated">模型操控</button>
            <button @click="showReport" class="Second" v-show="reportGenerated">视频展示</button>
            <video v-show="!reportGenerated" class="VV" src="../../../assets/Sun.mp4" autoplay loop
                   muted></video>
        </div>
    </div>
</template>

<style scoped lang="scss">
.SunEnergyMiddenTop {
  width: 100%;
  height: 100%;

  .VI {
    button {
      color: white;
      width: 6vw;
      font-size: 1em;
      height: 3.5vh;
      position: absolute;
      font-weight: bolder;
      background: #0d87f6;
      border: none;
      border-radius: 5px;
      margin-top: 2vh;
      margin-left: 2vw;
      z-index: 333;
    }

    button:hover {
      cursor: pointer;
    }

    .VV {
      width: 42.2vw;
      height: 50vh;
      object-fit: inherit;
      border-radius: 5px;
    }
  }
}
</style>