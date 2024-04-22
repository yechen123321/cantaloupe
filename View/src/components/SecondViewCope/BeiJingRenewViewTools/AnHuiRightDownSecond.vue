<script setup>
import {ref, reactive, onBeforeUnmount, onUnmounted, nextTick} from 'vue'
const listData = reactive([
    {name:'北控新能', do:'发电', number:'234.1', up:'万千瓦', when:'2024-04-12'},
    {name:'新华能源', do:'发电', number:'312.2', up:'万千瓦', when:'2024-04-13'},
    {name:'晶澳电力', do:'发电', number:'139.3', up:'万千瓦', when:'2024-04-14'},
    {name:'天合光能', do:'发电', number:'36.5', up:'万千瓦', when:'2024-04-16'},
    {name:'明阳能源', do:'发电', number:'128.7', up:'万千瓦', when:'2024-04-13'},
    {name:'星辉能源', do:'发电', number:'333.5', up:'万千瓦', when:'2024-04-15'},
    {name:'鸿宇能源', do:'发电', number:'435.6', up:'万千瓦', when:'2024-04-16'},
    {name:'凌阳能源', do:'发电', number:'134.3', up:'万千瓦', when:'2024-04-17'},    
    {name:'瑞丰电力', do:'发电', number:'34.3', up:'万千瓦', when:'2024-04-18'},
    {name:'海阳能源', do:'发电', number:'84.8', up:'万千瓦', when:'2024-04-11'},
    {name:'汇智能源', do:'发电', number:'239.1', up:'万千瓦', when:'2024-04-12'},    
])


let timer = ref(null);
let roll = ref(null);

onBeforeUnmount(() => {
    clearTimeout(timer.value);
});

onUnmounted(() => {
    clearTimeout(timer.value);
});

function testMove() {
    clearTimeout(timer.value);
}

function testMend() {
    start();
}

function start() {
    clearTimeout(timer.value);
    let speed = ref(100);
    timer.value = setInterval(MarqueeTest, speed.value);
}

function MarqueeTest() {
    let test1 = roll.value;

    if (test1 && test1.offsetHeight == 0) {
        test1 = roll.value;
    } else {
        test1.scrollTop += 1;

        if (test1.scrollTop >= (test1.scrollHeight - test1.clientHeight)) {
            test1.scrollTop = 0;
        }
    }
}

</script>

<template>
    <div class="AnHuiRightDownSecond">
        <div class="roll">
            <div class="top">
                <div class="name">设施</div>
                <div class="do">工作</div>
                <div class="number">数目</div>
                <div class="up">单位</div>
                <div class="when">时间</div>
            </div>
            <div class="roll-in" ref="roll">
                <div class="roll-main" v-for="item in listData" :key="item.id">
                    <div @mousemove="testMove" @mouseleave="testMend" class="name">
                        <div class="name">{{ item.name }}</div>
                        <div class="do">{{ item.do }}</div>
                        <div class="number">{{ item.number }}</div>
                        <div class="up">{{ item.up }}</div>
                        <div class="when">{{ item.when }}</div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<style scoped lang="scss">
.AnHuiRightDownSecond {
    width: 100%;
    height: 100%;

    .roll {
        color: white;
        width: 23vw;
        margin-top: 28vh;
        height: 40vh;
        margin-left: -1vw;

        .top {
            width: 100%;
            height: 3.5vh;
            background: rgba(255, 255, 255, .2);
            margin-top: -1vh;

            .name {
                float: left;
                margin-left: 1.3vw;
                margin-top: 0.3vh;

            }

            .do {
                float: left;
                margin-top: 0.3vh;
                margin-left: 2.3vw;
            }

            .number {
                float: left;
                margin-top: 0.3vh;
                margin-left: 1.9vw;
            }

            .up {
                float: left;
                margin-top: 0.3vh;
                margin-left: 2vw;
            }

            .when {
                float: left;
                margin-top: 0.3vh;
                margin-left: 2.7vw;
            }
        }

        .roll-in {
            width: 23vw;
            height: 20.5vh;
            //background: red;
            overflow: hidden;
            margin-right: 2vw;
            margin-top: 1vh;

            .roll-main {
                //background: red;
                width: 100%;
                height: 5vh;
                background: rgba(13, 135, 246, 0.1);
                margin-top: 1vh;

                .name {
                    float: left;
                    //background: red;
                    margin-left: 0.1vw;
                    margin-top: 0.3vh;
                    text-align: center;
                }

                .number {
                    float: left;
                    //background: red;
                    margin-top: 0.3vh;
                    text-align: center;
                    margin-left: 1.2vw;
                    width: 4vw;
                }

                .when {
                    float: left;
                    //background: red;
                    margin-top: 0.3vh;
                    text-align: center;
                    margin-left: 1vw;
                }

                .up {
                    float: left;
                    width: 5vw;
                    //background: red;
                    margin-top: 0.3vh;
                    text-align: center;
                    margin-left: -0.3vw;
                    margin-right: -1.1vw;
                }

                .do {
                    float: left;
                    margin-top: 0.3vh;
                    text-align: center;
                    margin-left: 0.3vw;
                    margin-right: -1.3vw;
                    //background: red;
                    width: 4vw;
                }
            }
        }
    }
}
</style>