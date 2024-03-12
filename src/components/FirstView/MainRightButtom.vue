<script setup>
import {onMounted, ref} from "vue";
import {useRouter} from "vue-router";
import * as echarts from "echarts";
// // import axios from "axios";
// import {API_BASE_URL} from "../../../config";

const router = useRouter();

const handleRouteChange = () => {
    // 在这里添加您的路由切换逻辑，下面是一个示例，实际根据您的路由配置进行修改
    router.push('/anhui'); // 替换'/new-route'为您要跳转的路由路径
};
const echartsRef = ref(null);
let myChart25 = null;
let option25 = null;

onMounted(() => {
    myChart25 = echarts.init(echartsRef.value, 'dark');

    // Your echarts option setup here...
    // (Your existing option setup code)
    option25 = {
        color: ['#73C0DE', '#FAC858'],
        backgroundColor: 'rgba(128, 128, 128, 0)',
        legend: {
            itemWidth: 15, // 标签宽度为10px
            itemHeight: 10, // 标签高度为10px
            width: '10vw',
            left: 'right',
            data: ['计划', '预估'],
            textStyle: {
                color: 'white',
            }
        },
        radar: {
            // shape: 'circle',
            center: ['50%', '50%'], // 调整雷达图的位置，这里设置为图表中心
            radius: '55%', // 调整雷达图的大小
            indicator: [
                {name: '矿产', max: 6500},
                {name: '能源', max: 16000},
                {name: '水产', max: 30000},
                {name: '林业', max: 38000},
                {name: '地质', max: 52000},
                {name: '海洋', max: 25000}
            ],

            splitNumber: 4, // 分割的圈数
            axisLine: {
                show: false, // 隐藏雷达图的轴线
                lineStyle: {
                    color: 'white'
                }
            },
            splitLine: {
                lineStyle: {
                    color: ['#B8B8B8'], // 设置分隔线的颜色
                    width: 1 // 设置分隔线的宽度
                }
            },
            name: {
                textStyle: {
                    fontWeight:'bold',
                    color: '#fff' // 设置雷达图每一个角的文字颜色为白色
                }
            },
        },
        series: [
            {
                name: 'Budget vs spending',
                type: 'radar',
                symbol: 'none', // 去掉每个角的小点
                data: [
                    {
                        value: [5000, 14000, 28000, 26000, 42000, 21000],
                        name: '计划',
                        areaStyle: {
                            color: '#73C0DE' // 粉红色，与深蓝色相呼应
                        },
                    },
                    {
                        value: [4200, 3000, 20000, 35000, 50000, 18000],
                        name: '预估',
                        areaStyle: {
                            color: '#FAC858' // 橙色，与深蓝色相呼应
                        },

                    },

                ]
            }
        ]
    };
    option25 && myChart25.setOption(option25);

    const resizeObserver = new ResizeObserver(() => {
        myChart25.resize();
    });

    resizeObserver.observe(echartsRef.value);
});
</script>

<template>
    <div class="MainRightButtom">
        <img class="BackImg" src="../../assets/pic/pic-3.png" alt="">
        <div class="MainRightButtom-title">全国自然资源发展概况图</div>
        <div class="MySelect">
            <select name="" id="" class="SelectBox">
                <option>全国</option>
                <option>安徽</option>
                <option>北京</option>
                <option>浙江</option>
                <option>重庆</option>
                <option>西藏</option>
                <option>四川</option>
                <option>山东</option>
                <option>上海</option>
                <option>广东</option>
                <option>广西</option>
            </select>
            <Button class="GotoAn" @click="handleRouteChange">切换</Button>
        </div>
        <div class="MainRightButtom-echarts" ref="echartsRef"></div>
    </div>
</template>

<style scoped lang="scss">
.MainRightButtom {
  width: 100vw;
  height: 100vh;

  .MainRightButtom-title {
    color: white;
    position: absolute;
    font-size: 1vw;
    font-weight: bolder;
    margin-top: 5vh;
    margin-left: 2vw;
  }

  .MainRightButtom-echarts {
    width: 16vw;
    height: 25vh;
    position: absolute;
    z-index: 166;
    margin-top: -1.5vh;
    margin-left: 1vw;
  }

  .MySelect {
    margin-top: 8vh;

    .SelectBox {
      position: absolute;
      width: 6vw;
      height: 3.5vh;
      cursor: pointer;
      overflow: hidden;
      font-size: 1vw;
      right: 0;
      margin-top: 5vh;
      margin-right: 0.5vw;
      background: #4d70cd;
      color: white;
      border: none;
      text-align: center;
      border-radius: 6px;
    }

    .GotoAn {
      width: 6vw;
      height: 3.5vh;
      right: 0;
      margin-top: 10.5vh;
      margin-right: 0.5vw;
      position: absolute;
      cursor: pointer;
      font-size: 1vw;
      font-weight: bolder;
      color: white;
      border: none;
      border-radius: 6px;
      background: #0d87f6;
      z-index: 222;
    }

    .GotoAn:hover {
      width: 6.5vw;
      height: 4vh;
      font-size: 1.2vw;
      margin-top: 10.4vh;
      margin-right: 0.2vw;
    }

    .GotoAn:active {
      width: 6vw;
      height: 3.5vh;
      font-size: 1vw;
      margin-top: 10.5vh;
      margin-right: 0.5vw;
    }
  }

  .BackImg {
    position: absolute;
    width: 27vw;
    height: 18vw;
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
