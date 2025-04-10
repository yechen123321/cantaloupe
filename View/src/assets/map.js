import BMap from "echarts/extension/bmap/bmap";
export function loadBMap(ak) {
    return new Promise(function (resolve, reject) {
        if (typeof BMap !== 'undefined') {
            resolve(BMap)
            return true
        }
        window.onBMapCallback = function () {
            resolve(BMap)
        }
        let script = document.createElement('script')
        script.type = 'text/javascript'
        script.src = 'http://api.map.baidu.com/api?v=3.0&ak=' + ak + '&__ec_v__=20190126&callback=onBMapCallback'
        script.onerror = reject
        document.head.appendChild(script)
    })
}