<script setup>

</script>

<template>
    <div class="FirstMainTable">
        <img class="BackImg" src="../../assets/pic/k_3.png" alt="">
    </div>
</template>

<style scoped lang="scss">
.FirstMainTable{
      width: 100%;
      height: 100%;
      border-image: linear-gradient(to right, #00bfff, #0d0d0d, #00bfff) 30 30;
      border-radius: 10px;
      box-shadow: 0px 0px 2px 2px #00bfff, 0px 0px 4px 2px #0d0d0d, 0px 0px 6px 4px #00bfff;
      animation: glow 1s ease-in-out infinite alternate;
    .BackImg{
        position: absolute;
        width: 100%;
        height: 100%;
    }
    @keyframes glow {

        from {
          box-shadow: 0px 0px 3px 3px #00bfff, 0px 0px 5px 3px #0d0d0d, 0px 0px 7px 5px #00bfff;
        }

        to {
          box-shadow: 0px 0px 5px 3px #00bfff, 0px 0px 7px 5px #0d0d0d, 0px 0px 9px 7px #00bfff;
        }
    }
}
</style>