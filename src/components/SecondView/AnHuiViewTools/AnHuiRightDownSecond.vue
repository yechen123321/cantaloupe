<script setup>
import {ref,reactive,onBeforeUnmount,onUnmounted,nextTick} from 'vue'
//定时器初始化
let timer = ref(null)
//ref绑定初始化
let roll = ref(null)
//列表数据初始化
const listData = reactive([
    {name:'矿地1',do:'采集煤矿',number:12301,up:'吨',when:'2024-02-23'},
    {name:'矿地1',do:'采集煤矿',number:12301,up:'吨',when:'2024-02-23'},
    {name:'矿地1',do:'采集煤矿',number:12301,up:'吨',when:'2024-02-23'},
    {name:'矿地1',do:'采集煤矿',number:12301,up:'吨',when:'2024-02-23'},
    {name:'矿地1',do:'采集煤矿',number:12301,up:'吨',when:'2024-02-23'},
    {name:'矿地1',do:'采集煤矿',number:12301,up:'吨',when:'2024-02-23'},
    {name:'矿地1',do:'采集煤矿',number:12301,up:'吨',when:'2024-02-23'},
    {name:'矿地1',do:'采集煤矿',number:12301,up:'吨',when:'2024-02-23'},
    {name:'矿地1',do:'采集煤矿',number:12301,up:'吨',when:'2024-02-23'},
    {name:'矿地1',do:'采集煤矿',number:12301,up:'吨',when:'2024-02-23'},
])

//等同于vue2中的beforeDestroy
onBeforeUnmount(()=>{
    //清除定时器
    clearTimeout(timer.value)
})
//等同于vue2中的destroyed
onUnmounted(()=>{
    //清除定时器
    clearTimeout(timer.value)
})

/**
 * @Description: 鼠标移动事件
 * @Author: admin
 */
function testMove(){
    clearTimeout(timer.value)
}
/**
 * @Description: 鼠标离开事件
 * @Author: admin
 */
function testMend(){
    start()
}
//开启定时器方法
function start(){
    //清除定时器
    clearTimeout(timer.value)
    //定时器触发周期
    let speed = ref(75)
    timer.value = setInterval(MarqueeTest, speed.value)
}
function MarqueeTest() {
    let test1 = roll.value;

    if (test1.offsetHeight == 0) {
        test1 = roll.value;
    } else {
        test1.scrollTop += 1;

        if (test1.scrollTop >= (test1.scrollHeight - test1.clientHeight)) {
            test1.scrollTop = 0;
        }
    }
}
//vue2中在created中调用
//vue3中 setup 包含beforeCreate和created
//启动定时器
start()

//注
//示例中 listData 写的静态数据 可以直接调用start()
//如果是接口获取 listData 列表时 需在 nextTick 中调用 start()；否则，
//进入页面不会滚动 必须鼠标移入移出才会滚动
//用nextTick 的原因是 需要等dom元素加载完毕后 再执行方法

nextTick(()=>{
    start()
})
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
            <div  class="roll-in"  ref="roll" >
                <div  class="roll-main" v-for="item in listData" :key="item.id">
                    <div @mousemove="testMove" @mouseleave="testMend" class="name">
                        <div class="name">{{ item.name }}</div>
                        <div class="do">{{ item.do }}</div>
                        <div class="number">{{ item.number }}</div>
                        <div class="up">{{ item.up }}</div>
                        <div class="when">{{ item.when}}</div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<style scoped lang="scss">
.AnHuiRightDownSecond{
    width: 100%;
    height: 100%;
    .roll{
        color: white;
        width: 23vw;
        margin-top: 28vh;
        height: 40vh;
        margin-left: -1vw;
        .top{
            width: 100%;
            height: 3.5vh;
            background: rgba(255, 255, 255,.2);
            margin-top: -1vh;
            .name{
                float: left;
                margin-left: 1.3vw;
                margin-top: 0.3vh;
            }
            .do{
                float: left;
                margin-top: 0.3vh;
                margin-left: 2.4vw;
            }
            .number{
                float: left;
                margin-top: 0.3vh;
                margin-left: 2.9vw;
            }

            .up{
                float: left;
                margin-top: 0.3vh;
                margin-left: 1.15vw;
            }

            .when{
                float: left;
                margin-top: 0.3vh;
                margin-left: 2.25vw;
            }
        }
        .roll-in{
            width: 23vw;
            height: 20.5vh;
            //background: red;
            overflow: hidden;
            margin-right: 2vw;
            margin-top: 1vh;
            .roll-main{
                //background: red;
                width: 100%;
                height: 5vh;
                background: rgba(13, 135, 246, 0.1);
                margin-top: 1vh;
                .name{
                    float: left;
                    margin-left: 0.5vw;
                    margin-top: 0.3vh;
                    text-align: center;
                }
                .do, .when, .number, .up{
                    float: left;
                    margin-top: 0.3vh;
                    text-align: center;
                    margin-left: 1.2vw;
                }
            }
            .roll-main:hover{

            }
        }
    }
}
</style>