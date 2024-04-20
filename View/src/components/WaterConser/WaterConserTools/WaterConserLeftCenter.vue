<script setup>
import {onMounted, ref} from "vue";
import * as echarts from "echarts";

const echartsRef = ref(null);
let myChart92 = null;
let option92 = null;
var app = {};
onMounted(() => {
    myChart92 = echarts.init(echartsRef.value, "dark");
    // Your echarts option setup here...
    // (Your existing option setup code)
    var colorList = [

        new echarts.graphic.LinearGradient(0, 0, 0, 1, [
            {offset: 1, color: '#00C9FF'},
            {offset: 0, color: '#92FE9D'}
        ]),
        new echarts.graphic.LinearGradient(0, 0, 0, 1, [
            {offset: 0, color: '#56CCF2'},
            {offset: 1, color: '#2948ff'}
        ]),
    ];
    const categories = (function () {
        let now = new Date();
        let res = [];
        let len = 10;
        while (len--) {
            res.unshift(now.toLocaleTimeString().replace(/^\D*/, ""));
            now = new Date(+now - 2000);
        }
        return res;
    })();
    const categories2 = (function () {
        let res = [];
        let len = 10;
        while (len--) {
            res.push(10 - len - 1);
        }
        return res;
    })();
    const getRandomNumber = (min, max) => {
        return parseInt(Math.random() * (max - min + 1) + min);
    };

    const data = (function () {
        let res = [];
        let len = 10;
        while (len--) {
            res.push(Number(getRandomNumber(2, 10).toFixed(1)));
        }
        return res;
    })();

    const data2 = (function () {
        let res = [];
        let len = 0;
        while (len < 10) {
            res.push(Number(getRandomNumber(60, 90).toFixed(1)));
            len++;
        }
        return res;
    })();
    option92 = {
        color: colorList,
        backgroundColor: "rgba(128, 128, 128, 0)",
        tooltip: {
            trigger: "axis",
            axisPointer: {
                type: "cross",
                label: {
                    backgroundColor: "#283b56",
                },
            },
        },
        legend: {
            top: "12%",
            textStyle: {
                color: "white",
            },
        },
        dataZoom: {
            show: false,
            start: 0,
            end: 100,
        },
        xAxis: [
            {
                type: "category",
                boundaryGap: true,
                data: categories,
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
            },
            {
                type: "category",
                boundaryGap: true,
                data: categories,
                axisLabel: {
                    show: false,
                    textStyle: {
                        color: "white", // 设置Y轴上数据的颜色为白色
                    },
                },
                axisLine: {
                    lineStyle: {
                        color: "white",
                    },
                },
            },
        ],
        yAxis: [
            {
                type: "value",
                scale: true,
                name: "千瓦",
                nameTextStyle: {
                    padding: [0, 25, 0, 0],
                    color: "white",
                },
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
                max: 12.5,
                min: 0,
                interval: 2.5, // 设置Y轴刻度间隔为20
                splitNumber: 4, // 设置Y轴线条数量为4
                boundaryGap: [0.2, 0.2],
            },
            {
                type: "value",
                scale: true,
                name: "百分比",
                nameTextStyle: {
                    color: "white",
                    padding: [0, -40, 0, 0],
                },
                axisLabel: {
                    formatter: "{value}%", // 在每个数据后面添加%
                    textStyle: {
                        color: "white", // 设置Y轴上数据的颜色为白色
                    },
                },
                axisLine: {
                    lineStyle: {
                        color: "white",
                    },
                },
                max: 100,
                min: 0,
                interval: 25, // 设置Y轴刻度间隔为20
                splitNumber: 4, // 设置Y轴线条数量为4
                boundaryGap: [0.2, 0.2],
            },
        ],
        series: [
            {
                name: "发电量",
                type: "bar",
                itemStyle: {
                    barBorderRadius: [10, 10, 0, 0] // 设置柱子上方为圆角，数组中的四个值分别代表左上、右上、右下、左下的圆角半径
                },
                data: data,
            },
            {
                name: "转换率",
                type: "line",
                xAxisIndex: 1,
                yAxisIndex: 1,
                data: data2,
            },
        ],
    };
    app.count = 11;
    setInterval(function () {
        let axisData = new Date().toLocaleTimeString().replace(/^\D*/, "");
        data.shift();
        data.push(Number(getRandomNumber(2, 10).toFixed(1)));
        data2.shift();
        data2.push(+Number(getRandomNumber(60, 90).toFixed(1)));
        categories.shift();
        categories.push(axisData);
        categories2.shift();
        categories2.push(app.count++);
        myChart92.setOption({
            xAxis: [
                {
                    data: categories,
                },
                {
                    data: categories,
                },
            ],
            series: [
                {
                    data: data,
                },
                {
                    data: data2,
                },
            ],
        });
    }, 2100);
    option92 && myChart92.setOption(option92);

    const resizeObserver = new ResizeObserver(() => {
        myChart92.resize();
    });

    resizeObserver.observe(echartsRef.value);
});
</script>

<template>
    <div class="ThermalPowerLeftCenter">
        <div class="title">涡轮实时效率</div>
        <div class="ThermalPowerLeftCenter-echarts" ref="echartsRef"></div>
        <img src="../../../assets/pic/midden.png" alt="" class="BackImg"/>
    </div>
</template>

<style scoped lang="scss">
.ThermalPowerLeftCenter {
  width: 100%;
  height: 100%;

  .title {
    color: white;
    position: absolute;
    text-align: center;
    width: 10vw;
    font-weight: bolder;
    font-size: 1.2em;
    margin-top: 3.6vh;
    margin-left: 2.8vw;
  }

  .ThermalPowerLeftCenter-echarts {
    width: 26vw;
    height: 31vh;
    margin-left: 1.6vw;
    margin-top: 3.8vh;
    position: absolute;
  }

  .BackImg {
    width: 30vw;
    height: 32vh;
  }
}
</style>