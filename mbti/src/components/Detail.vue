<template>
    <div class="card">
        <div class="circle"></div>
        <div class="circle"></div>
        <div class="card-inner">
            <p>{{ text }}</p>
        </div>
    </div>
</template>

<script>
export default {
    props: {
        text: String,
    },
};
</script>

<style lang="scss">
.card {
    width: 190px;
    height: 254px;
    transition: all 0.2s;
    position: relative;
    cursor: pointer;

    &:hover {
        transform: scale(1.1) rotate(3deg);
    }

    .card-inner {
        width: inherit;
        height: inherit;
        background: rgba(255, 255, 255, 0.05);
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.25);
        backdrop-filter: blur(10px);
        border-radius: 8px;
        display: flex;
        padding: 2em;
        font-size: 1.6em;
        color: #fff;
    }

    .circle {
        width: 100px;
        height: 100px;
        background: radial-gradient(#b0e633, #53ef7d);
        border-radius: 50%;
        position: absolute;

        &:nth-child(1) {
            top: -25px;
            left: -25px;
            animation: move-up6 2s ease-in infinite alternate-reverse;
        }

        &:nth-child(2) {
            bottom: -25px;
            right: -25px;
            animation: move-down1 2s ease-in infinite alternate-reverse;
        }
    }

    @keyframes move-up6 {
        to {
            transform: translateY(-10px);
        }
    }

    @keyframes move-down1 {
        to {
            transform: translateY(10px);
        }
    }
}
</style>
