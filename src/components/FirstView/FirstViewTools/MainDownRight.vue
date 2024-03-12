<script setup>
import {ref, onMounted} from 'vue';
import * as echarts from 'echarts';
import 'echarts-gl';

const echartsRef = ref(null);
let myChart11 = null;
let option11 = null;

onMounted(() => {
    myChart11 = echarts.init(echartsRef.value);
    const rawData = [
        [100, 302, 301, 334, 390,],
        [320, 132, 101, 134, 90,],
        [220, 182, 191, 234, 290,],
        [150, 212, 201, 154, 190,],
    ];
    const totalData = [];
    for (let i = 0; i < rawData[0].length; ++i) {
        let sum = 0;
        for (let j = 0; j < rawData.length; ++j) {
            sum += rawData[j][i];
        }
        totalData.push(sum);
    }
    const grid = {
        left: 100,
        right: 100,
        top: 50,
        bottom: 50
    };
    const gridWidth = myChart11.getWidth() - grid.left - grid.right;
    const gridHeight = myChart11.getHeight() - grid.top - grid.bottom;
    const categoryWidth = gridWidth / rawData[0].length;
    const barWidth = categoryWidth * 0.6;
    const barPadding = (categoryWidth - barWidth) / 2;
    const series = [
        '乔木林地',
        '灌木林地',
        '竹木林地',
        '其他林地',
    ].map((name, sid) => {
        return {
            name,
            type: 'bar',
            stack: 'total',
            barWidth: '60%',
            // label: {
            //     show: true,
            //     formatter: (params) => Math.round(params.value) + '%'
            // },
            data: rawData[sid].map((d, did) =>
                totalData[did] <= 0 ? 0 : ((d / totalData[did]) * 100).toFixed(1) // 将数据转换为百分比
            )
        };
    });
    const color = ['#5470c6', '#91cc75', '#fac858', '#ee6666', '#73c0de'];
    const elements = [];
    for (let j = 1, jlen = rawData[0].length; j < jlen; ++j) {
        const leftX = grid.left + categoryWidth * j - barPadding;
        const rightX = leftX + barPadding * 2;
        let leftY = grid.top + gridHeight;
        let rightY = leftY;
        for (let i = 0, len = series.length; i < len; ++i) {
            const points = [];
            const leftBarHeight = (rawData[i][j - 1] / totalData[j - 1]) * gridHeight;
            points.push([leftX, leftY]);
            points.push([leftX, leftY - leftBarHeight]);
            const rightBarHeight = (rawData[i][j] / totalData[j]) * gridHeight;
            points.push([rightX, rightY - rightBarHeight]);
            points.push([rightX, rightY]);
            points.push([leftX, leftY]);
            leftY -= leftBarHeight;
            rightY -= rightBarHeight;
            elements.push({
                type: 'polygon',
                shape: {
                    points
                },
                style: {
                    fill: color[i],
                    opacity: 0.25,
                },
            });
        }
    }
    option11 = {
        tooltip: {
            trigger: 'axis',
            extraCssText: 'width: 10vw; height: 16vh;', // 设置tooltip框的宽度和高度，调整框的大小
            formatter: function (params) {
                let tooltipContent = '';
                let mineName = params[0].name; // 获取矿地的名字
                tooltipContent += '<span style="font-weight: bold; margin-top: -500px;">' + mineName + '年</span>' + '<br>' + '<br>'; // 设置矿地名字的样式为加粗并向上移动5px
                params.forEach(function (param) {
                    if (param.seriesName !== '趋势') {
                        tooltipContent += param.marker + param.seriesName + ': ' + '<span style="float: right; font-weight: bold;">' + param.value + '%</span>' + '<br>';
                    }
                });
                return tooltipContent;
            },

        },
        // title: {
        //     text: '全国林地结构图',
        //     top: '7%',
        //     left: 'center',
        //     textStyle: {
        //         color: 'white',
        //     },
        // },
        legend: {
            top: '7%',
            itemWidth: 10, // 标签宽度为10px
            itemHeight: 10, // 标签高度为10px
            textStyle: {
                color: 'white'
            },
            selectedMode: true
        },
        grid,
        yAxis: {
            type: 'value',
            max: 100,
            axisLine: {
                lineStyle: {
                    color: 'white',
                },
            },
            axisLabel: {
                formatter: '{value}%'
            },
        },
        xAxis: {
            type: 'category',
            axisLine: {
                lineStyle: {
                    color: 'white',
                },
            },
            data: ['2019', '2020', '2021', '2022', '2023',]
        },
        series,
        graphic: {
            elements
        },
    };

    option11 && myChart11.setOption(option11);

    const resizeObserver = new ResizeObserver(() => {
        myChart11.resize();
    });

    resizeObserver.observe(echartsRef.value);
});
</script>


<template>
    <div className="MainDownRight">
        <Button class="GotoForest">全国森林结构图</Button>
        <div id="MainDownRight-echarts" ref="echartsRef"></div>
    </div>
</template>

<style scoped lang="scss">
.MainDownRight {
  width: 100vw;
  height: 100vh;
  color: white;

  .GotoForest {
    position: absolute;
    font-size: 1.2vw;
    font-weight: bolder;
    margin-top: -22.5vh;
    border: none;
    background: none;
    color: white;
    margin-left: 7.7vw;
    z-index: 999;
    //cursor: pointer;
  }

  //.GotoForest:hover {
  //  font-size: 1.3vw;
  //  margin-left: 7.5vw;
  //  margin-top: -19.2vh;
  //}
  //
  //.GotoForest:active {
  //  font-size: 1.2vw;
  //  margin-top: -19vh;
  //  margin-left: 7.7vw;
  //}

  #MainDownRight-echarts {
    width: 26vw;
    height: 35vh;
    //margin-left: 0vw;
    position: absolute;
    margin-top: -21.5vh;

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
