<script setup>

</script>

<template>
    <div className="AnHuiLeftTop">
        <div className="AnHuiLeftTop-title">北京市省再生能源统计</div>
        <div className="AnHuiLeftTop-main">
            <div className="MainOne">
                <img src="../../../assets/可再生能源.png" alt="" className="pic">
                <div className="number">
                    <div className="one">11.02</div>
                    <div className="up">亿千瓦时</div>
                </div>
                <div className="tow">再生能源总产量</div>
            </div>
            <div className="MainTow">
                <img src="../../../assets/装机容量.png" alt="" className="pic">
                <div className="number">
                    <div className="one" style="margin-left: 0.2vw">8.17</div>
                    <div className="up">%</div>
                </div>
                <div className="tow">装机容量提升率</div>
            </div>
            <div className="MainThree">
                <img src="../../../assets/投资.png" alt="" className="pic">
                <div className="number">
                    <div className="one">419</div>
                    <div className="up">亿元</div>
                </div>
                <div className="tow">能源建设投资</div>
            </div>
            <div className="MainFour">
                <img src="../../../assets/GenericChart.png" style="margin-top: 2vh" alt="" className="pic">
                <div className="number">
                    <div className="one" style="margin-left: 0.3vw">1.99</div>
                    <div className="up">%</div>
                </div>
                <div className="tow">发展指标增长</div>
            </div>
        </div>
        <img src="../../../assets/pic/border4.png" alt="" className="BackImg">
    </div>
</template>

<style scoped lang="scss">
.AnHuiLeftTop {
    width: 100%;
    height: 100%;
    color: white;

    .AnHuiLeftTop-main {
        position: absolute;
        width: 25vw;
        height: 18vh;
        margin-left: 3vw;

        .number {
            position: absolute;
            width: 8vw;
            height: 4vh;
            margin-top: 1.6vh;
            margin-left: 3.7vw;
            border-bottom: 2px solid #0a8cf8;

            .up {
                position: absolute;
                width: 5vw;
                margin-left: 4.2vw;
                text-align: center;
                font-size: 0.8em;
                margin-top: 1.3vh;
                font-weight: bolder;
            }

            .one {
                position: absolute;
                font-size: 1.6em;
                margin-left: -0.6vw;
                line-height: 3.7vh;
                margin-top: -0.3vh;
                font-weight: bolder;
                width: 6vw;
                text-align: center;
                height: 3.7vh;
                color: #2bfff1;
                text-shadow: 0 0 1px #1cd7cd, 0 0 2px #1cd7cd, 0 0 3px #1cd7cd;
            }
        }

        .tow {
            position: absolute;
            margin-left: 3.75vw;
            margin-top: 6vh;
            width: 8vw;
            font-size: 0.95em;
            font-weight: 400;
            height: 3vh;
            text-align: center;
        }

        .pic {
            position: absolute;
            width: 3.3vw;
            height: 6vh;
            margin-top: 1.6vh;
        }

        .MainOne {
            width: 11vw;
            height: 8vh;
            position: absolute;
        }

        .MainTow {
            width: 11vw;
            height: 8vh;
            position: absolute;
            margin-left: 13vw;
        }

        .MainThree {
            width: 11vw;
            height: 8vh;
            position: absolute;
            margin-top: 8vh;
        }

        .MainFour {
            width: 11vw;
            height: 8vh;
            position: absolute;
            margin-top: 8vh;
            margin-left: 13vw;
            z-index: 999;
        }
    }

    .BackImg {
        position: absolute;
        width: 27vw;
        height: 23vh;
        margin-left: 1.8vw;
        margin-top: -4vh;
    }

    .AnHuiLeftTop-title {
        position: absolute;
        color: white;
        margin-top: -3vh;
        text-align: center;
        width: 25.8vw;
        margin-left: 2.6vw;
        font-weight: bolder;
        font-size: 1.15em;
    }

}
</style>