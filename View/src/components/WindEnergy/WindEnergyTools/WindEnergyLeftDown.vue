<script setup>
import {onMounted, ref} from "vue";
import * as echarts from "echarts";

const echartsRef = ref(null);
let myChart93 = null;
let option93 = null;


onMounted(() => {
    myChart93 = echarts.init(echartsRef.value, "dark");
    // Your echarts option setup here...
    // (Your existing option setup code)
    const data = [];
    for (let i = 0; i < 6; ++i) {
        data.push(Math.round(Math.random() * 200));
    }
    var colorList = [
        new echarts.graphic.LinearGradient(0, 0,1,0, [
            {offset: 1, color: '#56CCF2'},
            {offset: 0, color: '#2948ff'}
        ]),
        // 其他渐变色定义...
    ];

    option93 = {
        color: colorList,
        backgroundColor: "rgba(128, 128, 128, 0)",
        tooltip: {
            trigger: 'axis',

            // textStyle: {
            //     fontWeight: 'bold'
            // },
        },
        xAxis: {
            max: 'dataMax',
            axisLabel: {
                textStyle: {
                    color: "white", // 设置Y轴上数据的颜色为白色
                },
            },
        },
        grid: {
            right: '12%'
        },
        yAxis: {
            type: 'category',
            data: ['电场1', '电场2', '电场3', '电场4', '电场5', '电场6',],
            inverse: true,
            name: 'KWh',
            nameTextStyle: {
                color: 'white',
                padding: [-180, -680, 0, 0],
            },
            animationDuration: 300,
            animationDurationUpdate: 300,
            axisLabel: {
                textStyle: {
                    color: "white", // 设置Y轴上数据的颜色为白色
                },
            },
            axisLine: {
                lineStyle: {
                    color: "white",
                },
            },
            max: 3 // only the largest 3 bars will be displayed
        },
        series: [
            {
                realtimeSort: true,
                name: '累计发电',
                type: 'bar',
                data: data,
                itemStyle: {
                    barBorderRadius: [0, 10, 10, 0] // 设置柱子上方为圆角，数组中的四个值分别代表左上、右上、右下、左下的圆角半径
                },
                label: {
                    show: true,
                    position: 'right',
                    valueAnimation: true
                }
            }
        ],
        legend: {
            show: false
        },
        animationDuration: 0,
        animationDurationUpdate: 3000,
        animationEasing: 'linear',
        animationEasingUpdate: 'linear'
    };

    function run() {
        for (var i = 0; i < data.length; ++i) {
            if (Math.random() > 0.9) {
                data[i] += Math.round(Math.random() * 2000);
            } else {
                data[i] += Math.round(Math.random() * 200);
            }
        }
        myChart93.setOption({
            series: [
                {
                    type: 'bar',
                    data
                }
            ]
        });
    }

    setTimeout(function () {
        run();
    }, 0);
    setInterval(function () {
        run();
    }, 3000);

    option93 && myChart93.setOption(option93);

    const resizeObserver = new ResizeObserver(() => {
        myChart93.resize();
    });

    resizeObserver.observe(echartsRef.value);
});
</script>


<template>
    <div class="ThermalPowerLeftDown">
        <div class="title">风场累计发电</div>
        <div class="ThermalPowerLeftDown-echarts" ref="echartsRef"></div>
        <img src="../../../assets/pic/midden.png" alt="" class="BackImg">
    </div>
</template>

<style scoped lang="scss">
.ThermalPowerLeftDown {
  width: 100%;
  height: 100%;

  .title {
    color: white;
    position: absolute;
    //background: red;
    text-align: center;
    width: 10vw;
    font-weight: bolder;
    font-size: 1.3em;
    margin-top: 3.6vh;
    margin-left: 2.8vw;
  }

  .ThermalPowerLeftDown-echarts {
    width: 26vw;
    height: 33vh;
    margin-left: 2vw;
    margin-top: 1vh;
    position: absolute;
    z-index: 300;
  }

  .BackImg {
    width: 30vw;
    height: 32vh;
  }
}
</style>