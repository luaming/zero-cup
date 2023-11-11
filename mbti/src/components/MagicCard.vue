<template>
    <div>
        <div
            class="magic-card animate__animated animate__backInRight"
            @click="showDetail"
        >
            <div class="frame">
                <img :src="img" class="inner-image"  v-if="!isDetailVisible"/>
            <Detail v-if="isDetailVisible" :text="detailText" />
            </div>
        </div>
    </div>
</template>

<script>
import Detail from "./Detail.vue";
export default {
    name: "MagicCard",
    components: {
        Detail,
    },
    props: {
        img: {
            type: String,
            required: true,
        },
        detailText: {
            type: String,
            detailText: "Here is detail text",
        },
    },
    data() {
        return {
            isDetailVisible: false,
        };
    },
    methods: {
        showDetail() {
            this.isDetailVisible = !this.isDetailVisible;
        },
    },
};
</script>

<style lang="scss" scoped>
.magic-card {
    position: relative;
    width: 35vw;
    height: 35vw;
    overflow: hidden;
    .frame {
        position: absolute;
        width: 100%;
        height: 100%;
        background-image: url("../assets/image/frame.png");
        background-size: cover;
        border-radius: 50%;
        display: flex;
        justify-content: center;
        align-items: center;

        .inner-image {
            transform: scale(1.3);
            height: auto;
        }
    }
}
.card {
    transition: all 0.2s;
    position: relative;
    cursor: pointer;
    width: 80%;
    height: 85%;
    display: flex;
    justify-content: center;
    align-items: center;
    &:hover {
        transform: scale(1.04) rotate(1deg);
    }

    .card-inner {
        width: inherit;
        height: inherit;
        background: rgba(255, 255, 255, 0.05);
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.25);
        backdrop-filter: blur(10px);
        border-radius: 8px;
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
