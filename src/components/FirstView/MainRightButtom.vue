<script setup>
import {ref} from "vue";
// // import axios from "axios";
// import {API_BASE_URL} from "../../../config";
const datas = ref([
    {name: '全国地质勘查投入', number: 1105.0, up: '亿', num: 2.19},
    {name: '全国地质勘查投入', number: 1105.0, up: '亿', num: 2.19},
]);


</script>

<template>
    <div class="MainRightButtom">
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
.MainRightButtom {
    width: 100vw;
    height: 100vh;

    .year-on-year::-webkit-scrollbar {
        display: none;
    }

    .year-on-year {
        //background: red;
        height: 22vh;
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
            height: 40%;

            .li-title {
                float: left;
                width: 18vw;
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
                margin-left: 4%;
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
        height: 14vw;
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
