import {request} from "@/utils/request";

/////// 首页 ///////

// 全国能源开发需求占比 1
export const initcdd = () => request({
    url: '/get_energy_develop_demand/',
    method: 'get',
})

// 全国能源产量及库存 2
export const initadd = () => request({
    url: '/get_energy_production_and_inventory/',
    method: 'get',
})

// 全国数据 3
export const inita = () => request({
    url: '/get_market_investment/',
    method: 'get',
})

// 全国能耗水平 4
export const initqdd = () => request({
    url: '/get_energy_consumption/',
    method: 'get',
})

// 进出口 5
export const initapp = () => request({
    url: '/get_energy_import_and_export/',
    method: 'get',
})

// 全国装机容量 6
export const initkdd = () => request({
    url: '/get_power_generation_installed_capacity/',
    method: 'get',
})

// 全国储量统计 7
export const initsdd = () => request({
    url: '/get_energy_reserve/',
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
export const choose1 = () => request({
    url: '/renew/get_region_energy_production/1/',
    method: 'get'
})
// 设施
export const initKlist10 = () => request({
    url: '/renew/get_regional_resource_facilities/12/0',
    method: 'get'
})

export const initKlist11 = () => request({
    url: '/renew/get_regional_resource_facilities/12/1',
    method: 'get'
})
// 结构
export const initKlist2 = () => request({
    url: '/renew/get_energy_structure/12/',
    method: 'get'
})

export const initKlist21 = () => request({
    url: '/renew/get_energy_reserve/12/',
    method: 'get'
})
export const initKlist22 = () => request({
    url: '/renew/get_energy_structure/12/',
    method: 'get'
})
export const initKlist23 = () => request({
    url: '/renew/get_energy_capacity/12/',
    method: 'get'
})
export const initKlist24 = () => request({
    url: '/renew/get_energy_ranking/12/',
    method: 'get'
})
export const initKlist25 = () => request({
    url: '/renew/get_energy_reserve_general/12/',
    method: 'get'
})
export const initKlist26 = () => request({
    url: '/renew/get_energy_installation/12/',
    method: 'get'
})
export const initKlist27 = () => request({
    url: '/renew/get_energy_construction_investment/12/',
    method: 'get'
})
export const initKlist28 = () => request({
    url: '/renew/get_classification_capacity/12/',
    method: 'get'
})
export const initKlist29 = () => request({
    url: '/renew/get_classification_structure/12/',
    method: 'get'
})
export const initKlist30 = () => request({
    url: '/renew/get_classification_installation/12/',
    method: 'get'
})
export const initKlist31 = () => request({
    url: '/renew/get_classification_reserve_general/12/',
    method: 'get'
})

///////     ///////


/////// 有限 ///////

// limit数据
export const initK1 = () => request({
    url: '/limited/get_market_investment/12/',
    method: 'get'
})
export const initK11 = () => request({
    url: '/limited/get_energy_structure/12/',
    method: 'get'
})
export const initK12 = () => request({
    url: '/limited/get_energy_capacity/12/',
    method: 'get'
})
export const initK13 = () => request({
    url: '/limited/get_energy_reserve_general/12/',
    method: 'get'
})
export const initK14 = () => request({
    url: '/limited/get_energy_reserve/12/',
    method: 'get'
})
export const initK15 = () => request({
    url: '/limited/get_extraction_efficiency/12/',
    method: 'get'
})
///////     ///////


/////// 分析 ///////
export const initK = () => request({
    url: '/analyse/get_heat_map/12/',
    method: 'get'
})

export const initq = () => request({
    url: '/analyse/get_capacity_structure/12/',
    method: 'get'
})

export const initp = () => request({
    url: '/analyse/get_consumption/12/',
    method: 'get'
})

///////     ///////


/////// 电场 ///////
export const initp1 = () => request({
    url: '/power//get_electric_field_fault/12/',
    method: 'get'
})
export const initp2 = () => request({
    url: '/power//put_electric_field_fault/12/',
    method: 'put'
})
export const initp31 = () => request({
    url: '/power//get_base_distribution/12/0/',
    method: 'get'
})
export const initp32 = () => request({
    url: '/power//get_base_distribution/12/1/',
    method: 'get'
})
export const initp33 = () => request({
    url: '/power//get_base_distribution/12/2/',
    method: 'get'
})
export const initp34 = () => request({
    url: '/power//get_base_distribution/12/3/',
    method: 'get'
})

////// problem
export const initp41 = () => request({
    url: 'power/get_base_equipment_working_information/12/0/',
    method: 'get'
})
export const initp42 = () => request({
    url: 'power/get_base_equipment_working_information/12/1/',
    method: 'get'
})
export const initp43 = () => request({
    url: 'power/get_base_equipment_working_information/12/2/',
    method: 'get'
})
export const initp44 = () => request({
    url: 'power/get_base_equipment_working_information/12/3/',
    method: 'get'
})
///////     ///////