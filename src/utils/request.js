import axios from 'axios'
export function request(config) {
    // axios 实例
    const instance = axios.create({
        baseURL: '/api', // 接口地址
        timeout: 5000,
    })
    // 添加请求拦截器
    instance.interceptors.request.use(function (config) {
        // 在发送请求之前做些什么
        return config;
    }, function (error) {
        // 对请求错误做些什么
        return Promise.reject(error);
    });

// 添加响应拦截器
    instance.interceptors.response.use(function (response) {
        // 2xx 范围内的状态码都会触发该函数。
        // 对响应数据做点什么
        return response;
    }, function (error) {
        // 超出 2xx 范围的状态码都会触发该函数。
        // 对响应错误做点什么
        if (error.response) {
            if (error.status === 500) {
                alert('服务器内部发生错误');
            }
        }
        return Promise.reject(error);
    });

    // 发送一个真正的请求
    return instance(config)
}

// 对axios进行二次封装
// import axios from 'axios'

// // requests就是axios，只不过稍微配置一下
// const requests  = axios.create({
//     // 配置对象
//     //基础路径，发送请求时，路径当中会出现api
//     baseURL:'/api',
//     // 代表请求超时的时间
//     timeout:5000
// })
// // 请求拦截器：发送请求前做一些事情
// requests.interceptors.request.use((config)=>{
//     // config:配置对象，headers请求头很重要
//     return config;
// })

// requests.interceptors.response.use((res)=>{
//     // 成功的回调函数：服务器响应数据回来以后，响应拦截器可以检测到，可以做一些事情
//     return res.data;

// },(err)=>{
//     // 响应失败的回调函数
//     return Promise.reject(new Error('fail'))
// })


// export default requests;