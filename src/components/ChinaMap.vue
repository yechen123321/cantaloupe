<template>
    <div className="h-full flex justify-center items-center">
        <div id="mapDom" className="h-full w-full"></div>
    </div>
</template>

<style scoped>
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
</style>

<script setup>
import {onMounted, onUnmounted, ref} from 'vue';
import * as echarts from 'echarts';
import '../assets/china';
import {getCityPositionByName} from '@/assets/cityPostion';

let mockData = [
    {name: '北京', value: 500, meta: 340},
    {name: '天津', value: 200, meta: 340},
    {name: '河南', value: 300, meta: 340},
    {name: '广西', value: 300, meta: 340},
    {name: '广东', value: 300, meta: 340},
    {name: '河北', value: 300, meta: 340},
    {name: '新疆', value: 230, meta: 340},
    {name: '江苏', value: 123, meta: 340},
    {name: '黑龙江', value: 230, meta: 340},
    {name: '新疆', value: 111, meta: 123},
    {name: '西藏', value: 222, meta: 345},
    {name: '青海', value: 333, meta: 456},
    {name: '甘肃', value: 444, meta: 121},
    {name: '四川', value: 555, meta: 234},
    {name: '云南', value: 556, meta: 543},
    {name: '贵州', value: 666, meta: 654},
    {name: '重庆', value: 776, meta: 786},
    {name: '广西', value: 887, meta: 123},
    {name: '海南', value: 992, meta: 432},
    {name: '澳门', value: 121, meta: 432},
    {name: '香港', value: 212, meta: 213},
    {name: '广东', value: 313, meta: 212},
    {name: '宁夏', value: 414, meta: 212},
    {name: '内蒙古', value: 515, meta: 323},
    {name: '山西', value: 616, meta: 434},
    {name: '陕西', value: 717, meta: 545},
    {name: '湖南', value: 828, meta: 676},
    {name: '湖北', value: 949, meta: 675},
    {name: '河南', value: 332, meta: 333},
    {name: '河北', value: 212, meta: 222},
    {name: '江西', value: 242, meta: 111},
    {name: '福建', value: 545, meta: 323},
    {name: '台湾', value: 212, meta: 122},
    {name: '山东', value: 434, meta: 322},
    {name: '北京', value: 875, meta: 444},
    {name: '天津', value: 231, meta: 555},
    {name: '安徽', value: 233, meta: 666},
    {name: '浙江', value: 534, meta: 777},
    {name: '江苏', value: 546, meta: 876},
    {name: '上海', value: 768, meta: 767},
    {name: '辽宁', value: 975, meta: 656},
    {name: '吉林', value: 345, meta: 555},
];

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
        meta: i.meta
    };
});

onMounted(() => {
    if (initMap.value) {

        initMap.value.setOption({
            backgroundColor: "transparent",
            tooltip: {
                show: false,
            },
            geo: {
                map: "china",
                tooltip: {
                    show: true,
                    trigger: "item",
                    formatter: function (params) {
                        if (params.componentType === "series") {
                            return (
                                params.name +
                                "<br/>" +
                                "煤炭产量：" +
                                params.value[2] +
                                "<br/>" +
                                "铁矿产量：" +
                                params.meta
                            );
                        }
                    },
                    backgroundColor: "rgba(0,0,0,0.7)",
                },
                label: {
                    show: false,
                },
                zoom: 1.03,
                silent: true,
                show: true,
                roam: false,
                aspectScale: 0.75,
                itemStyle: {
                    borderColor: "#0FA3F0",
                    borderWidth: 1,
                    areaColor: "#070f71",
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
                top: "10%",
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
                    tooltip: {
                        show: false,
                    },
                    label: {
                        show: true,
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
                        areaColor: "#17348b",
                        opacity: 1,
                    },
                    select: {
                        disabled: true,
                    },
                    emphasis: {
                        disabled: false,
                        label: {
                            align: "center",
                            color: "#ffffff",
                        },
                        itemStyle: {
                            color: "#ffffff",
                            areaColor: "#0075f4",
                        },
                    },
                    z: 2,
                    data: data,
                },
                {
                    type: "scatter",
                    coordinateSystem: "geo",
                    symbol: "pin",
                    symbolSize: [50, 50],
                    label: {
                        show: true,
                        color: "#fff",
                        formatter(value) {
                            return value.data.value[2];
                        },
                    },
                    itemStyle: {
                        color: "rgba(255,255,255,0.7)",
                    },
                    z: 2,
                    data: data,
                    tooltip: {
                        show: true,
                        trigger: "item",
                        formatter: function (params) {
                            return (
                                params.name +
                                "<br/>" +
                                "煤炭产量：" +
                                params.value[2] +
                                "<br/>" +
                                "铁矿产量：" +
                                params.data.meta
                            );
                        },
                        backgroundColor: "rgba(23,52,139,0.7)",
                        textStyle: {
                            color: "#fff",
                            fontSize: 14,
                        },
                        extraCssText: `
                      animation: glow 1s ease-in-out infinite alternate;
                      box-shadow: 0 0 10px #00bfff, 0 0 20px #00bfff, 0 0 30px #00bfff, 0 0 40px #00bfff;
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
                },
            ],
        })
    }
})
</script>
