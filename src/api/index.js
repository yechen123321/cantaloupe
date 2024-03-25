import  {request}  from "@/utils/request";

// 设施
export const initKlist = () => request({
    url: '/rscefacilt/13',
    method: 'get'
})

// 全国能源产量及库存
export const initadd = () => request({
    url: '/energyproandinvnt/',
    method:'get',
})

// 进出口
export const initapp = () => request({
    url: '/energyiae/',
    method:'get',
})

// 全国装机容量
export const initkdd = () => request({
    url: '/energyproandinvnt/',
    method:'get',
})
