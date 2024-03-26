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
    <div class="WindEnergyMiddenTop">
        <div class="VI">
            <Button @click="updateReport" class="First" v-show="!reportGenerated">模型操作</Button>
            <Button @click="showReport" class="Second" v-show="reportGenerated">视频展示</Button>
            <video v-show="!reportGenerated" class="VV" src="../../../assets/Wind.mp4" autoplay loop
                   muted></video>
        </div>
    </div>
</template>

<style scoped lang="scss">
.WindEnergyMiddenTop {
  width: 100%;
  height: 100%;

  .VI {
    Button {
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

    Button:hover {
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