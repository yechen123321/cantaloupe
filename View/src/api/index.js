import {request} from "@/utils/request";

/////// 首页 ///////

// 全国能源产量及库存
export const initadd = () => request({
    url: '/get_energy_production_and_inventory/',
    method: 'get',
})
// 全国数据
export const inita = () => request({
    url: '/get_market_investment/',
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
// 选择框
export const choose = () => request({
    url: '/renew/get_region_energy_production/12/',
    method: 'get'
})
// 设施
export const initKlist = () => request({
    url: '/renew/get_regional_resource_facilities/12/',
    method: 'get'
})

export const choose1 = () => request({
    url: '/renew/get_region_energy_production/1/',
    method: 'get'
})
// 设施
export const initKlist1 = () => request({
    url: '/renew/get_regional_resource_facilities/1/',
    method: 'get'
})

///////     ///////


/////// 有限 ///////

// limit数据
export const initK1 = () => request({
    url: '/limited/get_market_investment/12/',
    method: 'get'
})
///////     ///////


/////// 分析 ///////
export const initK = () => request({
    url: '/analyse/get_heat_map/12/',
    method: 'get'
})

///////     ///////