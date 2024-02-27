<script setup>
const items = [
    {name:'全国煤炭产量同比增长', number: 466000, up:'万吨', num: 2.19},
    {name:'全国铁矿产量同比增长', number: 466000, up:'万吨', num: 2.19},
    {name:'全国耕地产量同比增长', number: 466000, up:'万顷', num: 2.19},
    {name:'全国水产产量同比增长', number: 466000, up:'万吨', num: 2.19},
    {name:'全国太阳能发电同比增长', number: 466000, up:'万千瓦', num: 2.19},
    {name:'全国水力发电同比增长', number: 466000, up:'万千瓦', num: 2.19},
    {name:'全国铜矿产量同比增长', number: 466000, up:'万吨', num: 2.19},
    {name:'全国石油产量同比增长', number: 466000, up:'万吨', num: 2.19},
];

let scrollDown = true; // 初始化 scrollDown 变量为 true
let index = 0; // 初始化 index 变量为 0

setInterval(() => {
    const ulElement = document.querySelector('.year-on-year');

    if (ulElement) {
        if (scrollDown) {
            ulElement.scrollTop += 95;
            if (ulElement.scrollTop + ulElement.clientHeight >= ulElement.scrollHeight) {
                ulElement.scrollTop = 0; // 滚动到最后一个时回到第一个
            }
        } else {
            ulElement.scrollTop -= 95;
        }

        index++;
        if (index >= items.length) {
            index = 0;
        }
        const activeElement = document.querySelector('.li-active');
        activeElement?.classList.remove('li-active');
        const newActiveElement = document.querySelectorAll('.year-on-year li')[index];
        newActiveElement?.classList.add('li-active');
    }
}, 5000);
</script>

<template>
    <div class="FirstMainTable">
        <img class="BackImg" src="../../assets/pic/k_2.png" alt="">
        <ul class="year-on-year">
            <li v-for="(item,index) in items" :class="{ 'li-active': index === 0 }" :key="index">
                <div class="li-title">{{ item.name }}</div>
                <div class="li-number">{{ item.number }}</div>
                <div class="li-up">{{ item.up }}</div>
                <div class="li-num">{{ item.num }}%</div>
            </li>
        </ul>
    </div>
</template>

<style scoped lang="scss">
.FirstMainTable{
    width: 100vw;
    height: 100vh;
    border-image: linear-gradient(to right, #00bfff, #0d0d0d, #00bfff) 30 30;
    border-radius: 0.5vw;
    box-shadow: 0px 0px 1vw 1vw #00bfff, 0px 0px 2vw 1vw #0d0d0d, 0px 0px 3vw 2vw #00bfff;
    animation: glow 1s ease-in-out infinite alternate;
    .year-on-year::-webkit-scrollbar {
        display: none;
    }

    .year-on-year{
        //background: red;
        height: 8vh;
        margin: 0.5vw;
        position: absolute;
        z-index:10;
        //overflow: hidden;
        overflow-y: auto;
        //box-sizing: border-box;
        li{
            list-style-type: none;
            width: 100%;
            margin-top: -2%;
            line-height: 4.5vh;
            color: white;
            background: green;
            .li-title {
                float: left;
                width: 100%;
            }
            .li-number{
                float: left;
                color: #1cd7cd;
                font-weight: bolder;
                text-shadow: 0 0 1px #1cd7cd,0 0 2px #1cd7cd, 0 0 3px #1cd7cd;
                font-size: 2em;
            }
            .li-up{
                float: left;
                margin-left: 8%;
                margin-top: 1.3%;
            }
            .li-num{
                float: left;
                margin-left: 15%;
                font-size: 2em;
                color: yellow;
                font-weight: bolder;
            }
        }
    }
    .BackImg{
        position: absolute;
        width: 23vw;
        height: 5.3vw;
        //margin-top: -10%;
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
