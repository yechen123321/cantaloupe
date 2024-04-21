<script setup>
import {onMounted, onUnmounted, ref} from 'vue';
import * as echarts from 'echarts';
import '../../assets/china';
import {getCityPositionByName} from '@/assets/cityPostion';

let mockData = [
    {name: '新疆', ww: 2503.36, meta: 123},
    {name: '西藏', ww: 118.33, meta: 345},
    {name: '青海', ww: 24.03, meta: 456},
    {name: '甘肃', ww: 444, meta: 121},
    {name: '四川', ww: 555, meta: 234},
    {name: '云南', ww: 556, meta: 543},
    {name: '贵州', ww: 58.8, meta: 654},
    {name: '重庆', ww: 776, meta: 786},
    {name: '广西', ww: 12.26, meta: 123},
    {name: '海南', ww: 992, meta: 432},
    {name: '澳门', ww: 121, meta: 432},
    {name: '香港', ww: 212, meta: 213},
    {name: '广东', ww: 313, meta: 212},
    {name: '宁夏', ww: 414, meta: 212},
    {name: '内蒙古', ww: 515, meta: 323},
    {name: '山西', ww: 616, meta: 434},
    {name: '陕西', ww: 717, meta: 545},
    {name: '湖南', ww: 43.74, meta: 676},
    {name: '湖北', ww: 201.59, meta: 675},
    {name: '河南', ww: 332, meta: 333},
    {name: '河北', ww: 212, meta: 222},
    {name: '江西', ww: 274.74, meta: 111},
    {name: '福建', ww: 545, meta: 323},
    {name: '台湾', ww: 212, meta: 122},
    {name: '山东', ww: 434, meta: 322},
    {name: '北京', ww: 875, meta: 444},
    {name: '天津', ww: 231, meta: 555},
    {name: '安徽', ww: 233, meta: 666},
    {name: '浙江', ww: 534, meta: 777},
    {name: '江苏', ww: 77.25, meta: 876},
    {name: '上海', ww: 768, meta: 767},
    {name: '辽宁', ww: 975, meta: 656},
    {name: '吉林', ww: 345, meta: 555},
    {name: '黑龙江', ww: 316.42, meta: 666},
];
// 在 data 之后添加以下代码
let currentIndex = 0; // 当前显示的省份索引

// 设置定时器，每隔一定时间切换 tooltip 显示内容
setInterval(() => {
    currentIndex = (currentIndex + 1) % data.length; // 循环切换到下一个省份
    showTooltip(currentIndex); // 显示对应省份的 tooltip
}, 2000); // 设置轮播间隔时间，单位为毫秒

// 显示指定索引的省份 tooltip
const showTooltip = (index) => {
    if (initMap.value) {
        initMap.value.dispatchAction({
            type: 'showTip',
            seriesIndex: 0,
            dataIndex: index,
        });
    }
};
const initMap = ref(null);

onMounted(() => {
    const mapDom = document.querySelector('#mapDom');
    if (!mapDom) {
        console.error('Map container not found.');
        return;
    }

    initMap.value = echarts.init(mapDom);

    window.addEventListener('resize', updateMapSize);

    updateMapSize();
});

onUnmounted(() => {
    window.removeEventListener('resize', updateMapSize);
    if (initMap.value) {
        initMap.value.dispose();
    }
});

const updateMapSize = () => {
    if (initMap.value) {
        initMap.value.resize();
    }
};

let data = mockData.map((i) => {
    let cityPosition = getCityPositionByName(i.name).value;
    return {
        name: i.name,
        value: cityPosition.concat(i.value),
        ww: i.ww,
        meta: i.meta,
    };
});

onMounted(() => {
    if (initMap.value) {
        // initMap.value.on('click', function (params) {
        //     if (params.componentType === 'series') {
        //         // 获取点击的数据信息
        //         let routePath = '/thermalpower';
        //         // 如果有路由路径，则进行页面跳转
        //         if (routePath) {
        //             router.push(routePath);
        //         }
        //     }
        // });
        initMap.value.setOption({
            backgroundColor: "transparent",
            tooltip: {
                show: true,
            },
            geo: {
                map: "china",
                top: '10.2%',
                zoom: 1.03,
                silent: true,
                show: true,
                roam: true,
                aspectScale: 0.75,
                itemStyle: {
                    borderColor: "#0FA3F0",
                    borderWidth: 1,
                    areaColor: "rgba(7,15,113,0.4)",
                    shadowColor: "rgba(1,34,73,0.48)",
                    shadowBlur: 10,
                    shadowOffsetX: -10,
                    shadowOffsetY: 10,
                },
                select: {
                    disabled: true,
                },
                emphasis: {
                    disabled: true,
                    areaColor: "#00F1FF",
                },
                left: "center",
                regions: [
                    {
                        name: "南海诸岛",
                        selected: false,
                        emphasis: {
                            disabled: true,
                        },
                        itemStyle: {
                            areaColor: "#000000",
                            borderColor: "#000000",
                        },
                    },
                ],
                z: 1,
            },
            series: [

                {
                    type: "map",
                    map: "china",
                    zoom: 1,
                    data: data,
                    tooltip: {
                        show: true,
                        trigger: "item",
                        formatter: function (params) {
                            if (params.data && typeof params.data.ww !== 'undefined' && typeof params.data.meta !== 'undefined') {
                                return (
                                    params.name +
                                    "<br/>" +
                                    "煤炭产量：" +
                                    params.data.ww + " 万吨" +
                                    "<br/>" +
                                    "电力产量：" +
                                    params.data.meta + " 万千瓦"
                                );
                            } else {
                                return 'Data not available'; // 或者返回其他默认信息
                            }
                        },

                        backgroundColor: "rgba(23,52,139,0.7)",
                        textStyle: {
                            color: "#fff",
                            fontSize: 14,
                        },
                        extraCssText: `
                      animation: glow 1s ease-in-out infinite alternate;
                      box-shadow: 0 0 10px #00bfff, 0 0 10px #00bfff, 0 0 15px #00bfff, 0 0 20px #00bfff;
                      border: 1px solid #fff;
                      border-radius: 5px;
                      background-color: linear-gradient(to right, #00bfff, #0d0d0d, #00bfff);
                      color: white;
                      font-size: 16px;
                    `,
                        padding: 10,
                        borderColor: "#fff",
                        borderWidth: 1,
                    },
                    label: {
                        show: false,
                        color: "#ffffff",
                        align: "center",
                    },
                    top: "10%",
                    left: "center",
                    aspectScale: 0.75,
                    roam: false,
                    itemStyle: {
                        borderColor: "#3ad6ff",
                        borderWidth: 1,
                        areaColor: "rgba(23,52,139,0.4)",
                        opacity: 1,
                    },
                    select: {
                        disabled: true,
                    },
                    emphasis: {
                        disabled: true,
                        label: {
                            align: "center",
                            color: "#ffffff",
                        },
                        itemStyle: {
                            color: "#ffffff",
                            areaColor: "rgba(0,117,244,0.4)",
                        },
                    },
                    z: 2,
                },
            ],
        })
    }

})

</script>

<template>
    <div className="h-full flex justify-center items-center">
        <!--        <img src="../assets/pic/k_3.png" alt="">-->
        <div id="mapDom" className="h-full w-full"></div>
    </div>
</template>

<style scoped lang="scss">
canvas {
  width: 100% !important;
  height: 100% !important;
}

.h-full {
  height: 100%;
}

.w-full {
  width: 100%;
}


#mapDom {
  position: absolute;
  //margin-top: 45.5vh;
  //margin-left: -18vw;
  z-index: 123;

}
</style>