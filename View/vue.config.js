const {defineConfig} = require('@vue/cli-service')
module.exports = defineConfig({
    transpileDependencies: true,
    lintOnSave: false,
    devServer: {
        port: 8089,
        proxy: {
            '/api': {
                target: 'http://172.18.7.71:8080/api', // 配置好的后端接口地址
                pathRewrite: {
                    '^/api': '' // 以'/api'开头的url会进行接口转发
                }
            }
        }
    },
})
