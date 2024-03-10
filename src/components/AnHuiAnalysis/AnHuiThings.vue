<script setup>
import {ref,reactive,onBeforeUnmount,onUnmounted,nextTick} from 'vue'
//定时器初始化
let timer = ref(null)
//ref绑定初始化
let roll = ref(null)
//列表数据初始化
const listData = reactive([
    {name:'我是dom第一个'},
    {name:'我是dom第二个'},
    {name:'我是dom第三个'},
    {name:'我是dom第四个'},
    {name:'我是dom第五个'},
    {name:'我是dom第六个'},
    {name:'我是dom第七个'},
    {name:'我是dom第八个'},
    {name:'我是dom第二个'},
    {name:'我是dom第三个'},
    {name:'我是dom第四个'},
    {name:'我是dom第五个'},
    {name:'我是dom第六个'},
    {name:'我是dom第七个'},
    {name:'我是dom第八个'},
    {name:'我是dom第九个'},
    {name:'我是dom第十个'},

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
    <div class="AnHuiRightDown">
        <div @mousemove="testMove" @mouseleave="testMend" class="roll">
            <div class="roll-in"  ref="roll" >
                <div class="roll-main" v-for="item in listData" :key="item.id">
                    <span>{{item.name}}</span>
                </div>
            </div>
        </div>
    </div>
</template>

<style scoped lang="scss">
.AnHuiRightDown{
    width: 100%;
    height: 100%;
    .roll{
        color: white;

        width: 23vw;
        margin-top: -28vh;
        height: 52vh;
        margin-left: 1.5vw;
        .roll-in{
            width: 23vw;
            height: 51vh;
            margin-top: 3vh;
            overflow: hidden;
            margin-right: 2vw;
            //background: red;
            .roll-main{
                //background: red;
                margin-top: 2vh;
            }
        }
    }
}
</style>