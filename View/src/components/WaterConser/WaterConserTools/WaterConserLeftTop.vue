<script setup>
import { ref, onMounted, onUnmounted } from 'vue';

const totalPower = ref(5321); // 初始总发电量
let timer = null;

const startIncreasing = () => {
    const min = 20;
    const max = 70;
    const range = max - min + 1;
    const randomValue = Math.floor(Math.random() * range) + min;

    timer = setInterval(() => {
        // 每次增加的值将是20到70之间的随机整数
        totalPower.value += randomValue;
    }, 1000);
};
const stopIncreasing = () => {
    clearInterval(timer);
};

onMounted(() => {
    startIncreasing();
});

onUnmounted(() => {
    stopIncreasing();
});
</script>

<template>
    <div class="ThermalPowerLeftTop">
        <div class="title">电场信息总览</div>
        <ul>
            <li>
                <img src="../../../assets/fadian.png" alt="">
                <div class="number">{{ totalPower }}</div>
                <div class="up">KWh</div>
                <div class="what">总 发 电 量</div>
            </li>
            <li>
                <img src="../../../assets/jizu.png" alt="">
                <div class="number">21</div>
                <div class="up">个</div>
                <div class="what">机 组 数 量</div>
            </li>
            <li>
                <img src="../../../assets/water1.png" alt="">
                <div class="number">77</div>
                <div class="up">个</div>
                <div class="what">涡 轮 数 量</div>
            </li>
            <li>
                <img src="../../../assets/zhuanhuan.png" alt="">
                <div class="number">92</div>
                <div class="up">%</div>
                <div class="what">可 利 用 率</div>
            </li>
        </ul>
        <img src="../../../assets/pic/midden.png" alt="" class="BackImg">
    </div>
</template>

<style scoped lang="scss">
.ThermalPowerLeftTop {
    width: 100%;
    height: 100%;
    ul{
        position: absolute;
        width: 30vw;
        height: 20vh;
        margin-top: 7vh;
        margin-left: -2.5vw;
        //background: red;
        li{
            color:white;
            font-weight: bolder;
            font-size: 1em;
            width: 10vw;
            height: 8vh;
            float: left;
            margin-top: 2vh;
            margin-left: 3vw;
            list-style: none;
            img{
                width: 4vw;
                position: absolute;
            }
            .number{
                position: absolute;
                margin-left: 5vw;
                margin-top: 0.2vh;
                font-size: 1.6em;
                width: 4vw;
                text-align: center;
            }
            .up{
                margin-left: 9.5vw;
                margin-top: 1.3vh;
                position: absolute;
                color: #0ca6e0;
                text-shadow: 0 0 1px #0ca6e0, 0 0 1px #0ca6e0, 0 0 1px #0ca6e0;
            }
            .what{
                position: absolute;
                margin-left: 5vw;
                color: #3de9fa;
                text-shadow: 0 0 0.6px #3de9fa, 0 0 0.6px #3de9fa, 0 0 0.6px #3de9fa;
                margin-top: 4.5vh;
            }
        }
    }
    .title{
        color:white;
        position: absolute;
        font-weight: bolder;
        font-size: 1.2em;
        margin-left: 3.6vw;
        margin-top: 4vh;
    }
    .BackImg {
        width: 30vw;
        height: 32vh;
        position: absolute;
    }
}
</style>