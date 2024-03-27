import {request} from "@/utils/request";

/////// 首页 ///////

// 全国能源产量及库存
export const initadd = () => request({
    url: '/get_energy_production_and_inventory/',
    method: 'get',
})

// 全国能耗水平
export const initqdd = () => request({
    url: '/get_energy_consumption/',
    method: 'get',
})

// 进出口
export const initapp = () => request({
    url: '/get_energy_import_and_export/',
    method: 'get',
})

// 全国装机容量
export const initkdd = () => request({
    url: '/get_power_generation_installed_capacity/',
    method: 'get',
})

///////     ///////


/////// 再生 ///////

// 设施
export const initKlist = () => request({
    url: 'get_regional_resource_facilities/1/',
    method: 'get'
})


///////     ///////


/////// 有限 ///////


///////     ///////


/////// 分析 ///////


///////     ///////