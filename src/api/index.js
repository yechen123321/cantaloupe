import  {request}  from "@/utils/request";

export const initKlist = () => request({
    url: '/rscefacilt/13',
    method: 'get'
})

export const initadd = () => request({
    url: '/energyproandinvnt/',
    method:'get',
})