import  {request}  from "@/utils/request";

export const initlandlist = () => request({
    url: '/landuse/1',
    method: 'get'
})

