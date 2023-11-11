<template>
    <div class="container">
        <div class="part-2" :style="{ backgroundColor: bgColor }">
            <div class="left">
                <div class="left-top">
                    <canvas
                        id="dial"
                        width="420"
                        height="420"
                        @wheel="rotateWithWheel"
                    ></canvas>
                </div>
                <div class="left-bottom">
                    <h1
                        class="animate__animated animate__flip"
                        :key="highlightedIndex"
                    >
                        {{ highlightedType }}
                    </h1>
                    
                </div>
            </div>
            <div class="right">
                <MagicCard
                    :img="imgUrl"
                    :detailText="currentText"
                    :key="highlightedIndex"
                />
                <p>点击图片，查看你的灵魂伴侣简介</p>
            </div>
            
        </div>
    </div>
</template>

<script>
import MagicCard from "../components/MagicCard.vue";

export default {
    name: "Index",
    components: {
        MagicCard,
    },
    data() {
        return {
            lastAngle: 0,
            rotationAngle: 0,
            mbtiTypes: [
                "INFJ",
                "ENTP",
                "INTJ",
                "ENTJ",
                "ENFJ",
                "INFP",
                "ENFP",
                "INTP",
                "ESTP",
                "ISFP",
                "ESTJ",
                "ISTJ",
                "ESFP",
                "ISFJ",
                "ESFJ",
                "ISTP",
            ],
            colors: [
                "#0B3D91",
                "#FF6F00",
                "#333333",
                "#C0392B",
                "#F1C40F",
                "#9B59B6",
                "#1ABC9C",
                "#7F8C8D",
                "#E67E22",
                "#8E44AD",
                "#2C3E50",
                "#34495E",
                "#FFC0CB",
                "#16A085",
                "#F39C12",
                "#2980B9",
            ],
            texts: [
                "Infj：钱婆婆。钱婆婆是一个十分深沉的人，她是非分明，尊重个体，会严厉惩罚盗走契约印的白龙，也不会阻止千寻的离开。",
                "Entp：哈尔。哈尔总是可以以乐观幽默的态度快速解决问题，同时他也热爱探索，喜欢自由，也能对周围的环境作出即时的反应。",//另，作者认为光海组是天下第一cp
                "Intj：白龙；白龙是一个有组织和决断力的人。他在故事中担任了一个重要的角色，引导千寻在神灵世界中前进。他的决策和行动都表现出一种深思熟虑和计划性。",
                "Entj：千寻，千寻愿意和各种神灵交朋友，同时对眼前的事物具有自己的判断能力，成为家中唯一一个没有因为贪吃眼前食物落入陷阱的人。",
                "Enfj：娜乌西卡。娜乌西卡是一个十分善良的角色，她即便面对克罗托瓦的质疑与谩骂也要救核辐射环境中的孩子，即使这些孩子无法被带走，十分具有同情心。",
                "Infp：千寻。千寻内心十分细腻，能够在父母之前发现环境的不对，同时又充满了爱心，她对神灵世界中的不同角色展现出温暖和善良的态度，愿意帮助他们并与他们建立联系。",
                "Enfp：黑猫奇奇。黑猫展现出机智和幽默的一面，经常用幽默的语言和态度给琪琪带来欢乐和轻松氛围。他的反应和表情往往令人发笑。同时对未来和生活都充满了热忱。",
                "Intp：哈尔 哈尔对于魔法有着很大的热情，善于研究各种魔法，喜欢追求关于魔法的真理。哈尔是一个充满创造力和发明才能的人。他制造了许多令人惊叹的机械和装置，包括移动城堡本身。",
                "Estp：琪琪。琪琪在很小的年纪就离开了家乡，独自去寻求自己的命运，这使她面对新的挑战和未知环境。当她想到飞行速递时，立马展开行动，是一个行动派。",
                "Isfp：无脸男 。无脸男性格十分的平和善良，会陪着千寻坐车，也会通过各种礼物和行为来表达对周围人的友好，他的性格十分单纯直接。",
                "Estj：汤婆婆。汤婆婆是一个十分注重自身利益的人，她十分利益分明，给了契约者们庇护的同时也要求被庇护者们必须按照她的规章制度生存。",
                "Istj：珊。珊是一个野性、独立和保护本能强烈的角色。她的坚强和关心使她成为森林的守护者。她的认真可靠也使她能够更好的守护森林。",
                "Esfp：波妞。波妃和其他角色之间建立了深厚的情感联系。她对周围的生物和环境都表现出了关怀和体贴。她愿意帮助别人，并付出努力保护重要的人和事物。她对周围事物表现出极大的热情。",
                "Isfj：苏菲（哈尔的移动城堡）。苏菲总是对周围充满了关心与友善，同时也在以自己的方式一直默默守护着周围的人，为了救哈尔，她甚至愿意放弃自己的年轻美丽，具有奉献精神。",
                "Esfj：Moro。 Moro是一个坚定果断的角色，她具有强大的领导力和决心。作为森林之神，她保护着森林和动物，并为自己的族群提供指导和支持。",
                "Istp：锅炉爷爷。锅炉爷爷总会在千寻陷入困难时用行动帮助千寻，比如用自己的蜥蜴干为千寻谋得工作，送给千寻自己珍藏的车票。",
                
            ],

            bgColor: "#6a1b9a",
            highlightedType: "INFJ",
            highlightedIndex: 0,
        };
    },
    computed: {
        imgUrl() {
            const imageIndex = this.highlightedIndex + 1;
            return require(`../assets/image/people/${imageIndex}.jpg`);
        },
        currentText() {
            return this.texts[this.highlightedIndex];
        },
    },
    methods: {
        drawDial() {
            const canvas = this.$el.querySelector("#dial");
            if (!canvas.getContext) return;

            const ctx = canvas.getContext("2d");
            const centerX = canvas.width / 2;
            const centerY = canvas.height / 2;
            const radius = Math.min(centerX, centerY) * 0.8;
            const slice = (Math.PI * 2) / this.mbtiTypes.length;

            ctx.clearRect(0, 0, canvas.width, canvas.height);

            this.mbtiTypes.forEach((type, i) => {
                const angleStart = slice * i + this.rotationAngle;
                const angleEnd = slice * (i + 1) + this.rotationAngle;

                ctx.beginPath();
                ctx.moveTo(centerX, centerY);
                ctx.arc(centerX, centerY, radius, angleStart, angleEnd);
                ctx.closePath();
                ctx.fillStyle = this.colors[i];
                ctx.fill();

                const textAngle = angleStart + slice / 2;
                ctx.fillStyle = "#fff";
                ctx.font = "24px Consolas";

                ctx.translate(centerX, centerY);
                ctx.rotate(textAngle);
                ctx.fillText(type, radius - 10, 0);
                ctx.rotate(-textAngle);
                ctx.translate(-centerX, -centerY);
            });
        },
        updateHighlightedType() {
            const slice = (Math.PI * 2) / this.mbtiTypes.length;
            const adjustedRotation =
                (Math.PI * 2 - this.rotationAngle) % (Math.PI * 2);
            let highlightedIndex =
                Math.floor(adjustedRotation / slice) % this.mbtiTypes.length;
            if (highlightedIndex < 0) highlightedIndex = 1;
            if (this.highlightedIndex !== highlightedIndex) {
                this.highlightedIndex = highlightedIndex;
                this.bgColor = this.colors[highlightedIndex];
                this.highlightedType = this.mbtiTypes[highlightedIndex];
            }
        },
        rotateWithWheel(e) {
            e.preventDefault();

            const wheelRotationStep = 0.1; //22.5;

            if (e.deltaY < 0) {
                this.rotationAngle -= wheelRotationStep;
            } else {
                this.rotationAngle += wheelRotationStep;
            }

            this.rotationAngle =
                (this.rotationAngle + Math.PI * 2) % (Math.PI * 2);

            this.drawDial();

            this.updateHighlightedType();
        },
    },
    created() {
        this.highlightedType = this.$route.query.type || "INFJ";
        this.highlightedIndex = parseInt(this.$route.query.index, 10) || 0;
        this.bgColor = this.$route.query.color || "#0B3D91";
    },
    mounted() {
        this.highlightedIndex = this.mbtiTypes.indexOf(this.highlightedType);
        this.rotationAngle = 0;
        this.drawDial();
    },
};
</script>

<style lang="scss" scoped>
.container {
    width: 100vw;
    min-height: 100vh;
    .part-2 {
        display: flex;
        height: 100vh;
        .left {
            display: flex;
            flex-direction: column;
            flex: 0.618;

            .left-top {
                flex: 1;
                display: flex;
                justify-content: center;
                align-items: center;
                transition: background-color 1s ease;

                #dial {
                    border-radius: 50%;
                }
            }

            .left-bottom {
                flex: 0.618;
                display: flex;
                justify-content: center;
                align-items: center;
                h1 {
                    color: white;
                    font-family: monospace;
                    font-size: 6em;
                    font-weight: bold;
                }
            }
        }

        .right {
            flex: 1;
            display: flex;
            justify-content: center;
            align-items: center;
            flex-direction: column;
            font-size: 1.5em;
        }
    }
}
p{
    color: white;
}
</style>
