const {defineConfig} = require('@vue/cli-service')
module.exports = defineConfig({
    transpileDependencies: true,
    lintOnSave: false,
    outputDir: 'dist',
    assetsDir: 'static',
    devServer: {
        port: 80,
        proxy: {
            '/api': {
                 // target: 'http://172.18.7.26:8085/api', // 配置好的后端接口地址
               target: 'http://101.42.158.192:8085/api', // 配置好的后端接口地址
                pathRewrite: {
                    '^/api': '' // 以'/api'开头的url会进行接口转发
                }
            }
        }
    },
})
