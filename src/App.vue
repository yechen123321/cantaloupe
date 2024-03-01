<template>
        <div id="app">
                <div id="stars"></div>
                <router-view/>
        </div>
</template>

<style lang="scss">
html, body {
        width: 100%;
        height: 100%;
        margin: 0;
        padding: 0;
        overflow: hidden;
}

* {
        user-drag: none;
        -webkit-touch-callout: none; /* iOS Safari */
        -webkit-user-select: none; /* Safari */
        -khtml-user-select: none; /* Konqueror HTML */
        -moz-user-select: none; /* Firefox */
        -ms-user-select: none; /* Internet Explorer/Edge */
        user-select: none; /* Non-prefixed version, currently supported by Chrome and Opera */
}

html {
        background-color: #040e1a;
        background-size: cover;
}

#app {
        width: 100%;
        height: 100%;
        position: relative;
}

#stars {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
}

.star {
        position: absolute;
        width: 2px;
        height: 2px;
        border-radius: 50%;
        background: #fff;
        animation: twinkle 1s infinite;
}

@keyframes twinkle {
        0% {
                opacity: 0;
        }
        10% {
                opacity: 0.2;
        }
        20% {
                opacity: 0.4;
        }
        30% {
                opacity: 0.6;
        }
        40% {
                opacity: 0.8;
        }
        50% {
                opacity: 1;
        }
        60% {
                opacity: 0.8;
        }
        70% {
                opacity: 0.6;
        }
        80% {
                opacity: 0.4;
        }
        90% {
                opacity: 0.2;
        }
        100% {
                opacity: 0;
        }
}
</style>

<script setup>
import { onMounted } from 'vue';

onMounted(() => {
        createStars();
        disableZoom();
});

function createStars() {
        const stars = document.getElementById('stars');
        const starCount = 300;

        for (let i = 0; i < starCount; i++) {
                const star = document.createElement('div');
                star.classList.add('star');
                star.style.left = Math.random() * 100 + 'vw';
                star.style.top = Math.random() * 100 + 'vh';
                star.style.animationDelay = Math.random(400,600) * 5 + 's'; // 设置随机的闪烁延迟时间
                stars.appendChild(star);
        }
}

function disableZoom() {
        document.addEventListener('wheel', function(e) {
                if (e.ctrlKey) {
                        e.preventDefault();
                }
        }, { passive: false });

        document.addEventListener('keydown', function(e) {
                if (e.ctrlKey && (e.key === '+' || e.key === '-' || e.key === '0')) {
                        e.preventDefault();
                }
        });
}
</script>
