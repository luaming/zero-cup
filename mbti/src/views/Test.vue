<template>
    <div class="bg">
        <h1>mbti性格测试</h1>
        <div class="progress-container">
            <svg class="progress-circle" viewBox="0 0 36 36">
                <path
                    class="circle-bg"
                    d="M18 2.0845
                a 15.9155 15.9155 0 0 1 0 31.831
                a 15.9155 15.9155 0 0 1 0 -31.831"
                />
                <path
                    class="circle"
                    :stroke-dasharray="progressPercentage + ', 100'"
                    d="M18 2.0845
                a 15.9155 15.9155 0 0 1 0 31.831
                a 15.9155 15.9155 0 0 1 0 -31.831"
                />
            </svg>
            <div
                class="progress-text"
                @click="answeredQuestionsCount === 12 && submitScores()"
            >
                {{
                    answeredQuestionsCount === 12
                        ? "查看结果"
                        : answeredQuestionsCount + "/12"
                }}
            </div>
        </div>
        <div class="test">
            <div class="a">
                <p>下列哪个描述更符合你</p>
                <button
                    :class="buttonState('a1')"
                    @click="changeScore('a', 1, 'a1', 'a2')"
                >
                    可以和任何人按需求进行适当的交谈
                </button>
                <button
                    :class="buttonState('a2')"
                    @click="changeScore('a', -1, 'a2', 'a1')"
                >
                    只对某些人在某些情况下才可以畅所欲言
                </button>
            </div>
            <div class="a">
                <p>你通常喜欢的科目是讲授概念和原则的，还是讲究事实和数据的</p>
                <button
                    :class="buttonState('b1')"
                    @click="changeScore('b', 1, 'b1', 'b2')"
                >
                    概念和原则
                </button>
                <button
                    :class="buttonState('b2')"
                    @click="changeScore('b', -1, 'b2', 'b1')"
                >
                    事实和数据
                </button>
            </div>
            <div class="a">
                <p>你更认为哪一个称赞更适合你</p>
                <button
                    :class="buttonState('c1')"
                    @click="changeScore('c', 1, 'c1', 'c2')"
                >
                    经常感性
                </button>
                <button
                    :class="buttonState('c2')"
                    @click="changeScore('c', -1, 'c2', 'c1')"
                >
                    经常理性
                </button>
            </div>
            <div class="a">
                <p>
                    你认为按照程序做事是有需要的，但是并不是很喜欢或者大多数情况下有帮助且你喜欢
                </p>
                <button
                    :class="buttonState('d1')"
                    @click="changeScore('d', 1, 'd1', 'd2')"
                >
                    前者
                </button>
                <button
                    :class="buttonState('d2')"
                    @click="changeScore('d', -1, 'd2', 'd1')"
                >
                    后者
                </button>
            </div>
            <div class="a">
                <p>你是否容易让人了解，或是难于让人了解</p>
                <button
                    :class="buttonState('a3')"
                    @click="changeScore('a', 1, 'a3', 'a4')"
                >
                    容易让人了解
                </button>
                <button
                    :class="buttonState('a4')"
                    @click="changeScore('a', -1, 'a4', 'a3')"
                >
                    难于让人了解
                </button>
            </div>
            <div class="a">
                <p>一般来说你和哪些人比较合得来</p>
                <button
                    :class="buttonState('b3')"
                    @click="changeScore('b', 1, 'b3', 'b4')"
                >
                    富于想象力的人
                </button>
                <button
                    :class="buttonState('b4')"
                    @click="changeScore('b', -1, 'b4', 'b3')"
                >
                    现实的人
                </button>
            </div>
            <div class="a">
                <p>你认为哪一个是较好的称赞</p>
                <button
                    :class="buttonState('c3')"
                    @click="changeScore('c', 1, 'c3', 'c4')"
                >
                    富有同情心的
                </button>
                <button
                    :class="buttonState('c4')"
                    @click="changeScore('c', -1, 'c4', 'c3')"
                >
                    能干的
                </button>
            </div>
            <div class="a">
                <p>
                    当你要外出一整天，你会计划你要做什么和在什么时候,还是说去就去？
                </p>
                <button
                    :class="buttonState('d3')"
                    @click="changeScore('d', 1, 'd3', 'd4')"
                >
                    说去就去
                </button>
                <button
                    :class="buttonState('d4')"
                    @click="changeScore('d', -1, 'd4', 'd3')"
                >
                    计划你要做什么和在什么时候
                </button>
            </div>
            <div class="a">
                <p>你通常与人容易混熟，还是比较沉静或矜持</p>
                <button
                    :class="buttonState('a5')"
                    @click="changeScore('a', 1, 'a5', 'a6')"
                >
                    前者
                </button>
                <button
                    :class="buttonState('a6')"
                    @click="changeScore('a', -1, 'a6', 'a5')"
                >
                    后者
                </button>
            </div>
            <div class="a">
                <p>如果你是一位老师，你会选教</p>
                <button
                    :class="buttonState('b5')"
                    @click="changeScore('b', 1, 'b5', 'b6')"
                >
                    设计理论的课程
                </button>
                <button
                    :class="buttonState('b6')"
                    @click="changeScore('b', -1, 'b6', 'b5')"
                >
                    以事实为主的课程
                </button>
            </div>
            <div class="a">
                <p>你宁愿替哪一类上司或者领导工作</p>
                <button
                    :class="buttonState('c5')"
                    @click="changeScore('c', 1, 'c5', 'c6')"
                >
                    天性纯良但常常前后不一的
                </button>
                <button
                    :class="buttonState('c6')"
                    @click="changeScore('c', -1, 'c6', 'c5')"
                >
                    言辞尖锐但永远合乎逻辑的
                </button>
            </div>
            <div class="a">
                <p>你认为自己是一个较为随性所至的人，还是较为有条理的人</p>
                <button
                    :class="buttonState('d5')"
                    @click="changeScore('d', 1, 'd5', 'd6')"
                >
                    较为随性所至的人
                </button>
                <button
                    :class="buttonState('d6')"
                    @click="changeScore('d', -1, 'd6', 'd5')"
                >
                    较为有条理的人
                </button>
            </div>
            <br />
        </div>
    </div>
</template>
<script>
import axios from "axios";
export default {
    data() {
        return {
            scores: {
                a: 0,
                a1: 0,
                a2: 0,
                a3: 0,
                a4: 0,
                a5: 0,
                a6: 0,
                b: 0,
                b1: 0,
                b2: 0,
                b3: 0,
                b4: 0,
                b5: 0,
                b6: 0,
                c: 0,
                c1: 0,
                c2: 0,
                c3: 0,
                c4: 0,
                c5: 0,
                c6: 0,
                d: 0,
                d1: 0,
                d2: 0,
                d3: 0,
                d4: 0,
                d5: 0,
                d6: 0,
            },
            buttonStates: {},
        };
    },
    computed: {
        answeredQuestionsCount() {
            return Object.values(this.buttonStates).filter(
                (state) => state === "color-change clicked"
            ).length;
        },
        progressPercentage() {
            const totalQuestions = 12;
            return (this.answeredQuestionsCount / totalQuestions) * 100;
        },
    },
    methods: {
        changeScore(key, value, btnId1, btnId2) {
            this.scores[btnId1] =
                this.buttonStates[btnId1] === "color-change clicked"
                    ? 0
                    : value;
            this.scores[btnId2] = 0;
            this.scores[key] = this.scores[btnId1] + this.scores[btnId2];

            this.buttonStates[btnId1] =
                this.scores[key] === value
                    ? "color-change clicked"
                    : "color-change";
            this.buttonStates[btnId2] = "color-change";
        },
        buttonState(btnId) {
            return this.buttonStates[btnId] || "color-change";
        },
        submitScores() {
            axios
                .post("http://localhost:5000/mbti-result", this.scores)
                .then((response) => {
                    const mbtiType = response.data.type;
                    const index = response.data.index;
                    const color = encodeURIComponent(response.data.color);
                    const path = `/interaction?type=${mbtiType}&index=${index}&color=${color}`;
                    this.$router.push(path);
                })
                .catch((error) => {
                    console.error("Error:", error);
                });
        },
    },
};
</script>

<style lang="scss" scoped>
* {
    padding: 0;
    margin: 0;
}

.bg {
    background-image: url(../assets/image/bgtest-2.jpg);
}

h1 {
    display: flex;
    justify-content: center;
    line-height: 10vh;
}

#shiny-shadow {
    display: flex;
    align-items: center;
    justify-content: center;
    height: 100vh;
    background: #1c2541;
}

.color-change {
    &.clicked {
        background-color: #daa6a9;
        transform: scale(1.2);
        border: 3.5px solid black;
        background: transparent;
        text-transform: uppercase;
        padding: 15px 50px;
        transition: transform 0.4s ease;
    }
}

.test {
    font-family: maiyuan;
    position: relative;
    margin: 20px;
    font-size: 27px;
    font-weight: 600;
    text-align: center;
}

.a {
    padding: 20px;
    margin: 40px;
    background: rgba(255, 255, 255, 0.25);
    box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
    backdrop-filter: blur(4px);
    border-radius: 10px;
    border: 1px solid rgba(255, 255, 255, 0.18);
    button {
        margin: 20px 70px 10px;
        border: 3.5px solid black;
        background: transparent;
        text-transform: uppercase;
        color: black;
        padding: 15px 50px;
        outline: none;
        overflow: hidden;
        position: relative;
        font-family: maiyuan;
        font-weight: 500;
        font-size: 20px;
        background: rgba(255, 255, 255, 0.25);
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
        backdrop-filter: blur(4px);
        -webkit-backdrop-filter: blur(4px);
        border-radius: 10px;
        border: 1px solid rgba(255, 255, 255, 0.18);
        &:hover:after {
            left: 120%;
            transition: all 600ms cubic-bezier(0.3, 1, 0.2, 1);
        }

        &:after {
            content: "";
            display: block;
            position: absolute;
            top: -36px;
            left: -100px;
            background: rgb(255, 255, 255);
            width: 50px;
            height: 125px;
            opacity: 20%;
            transform: rotate(-45deg);
        }
    }
}

.progress-container {
    position: fixed;
    width: 10em;
    height: 10em;
    margin: 20px auto;
    z-index: 99;
    left: 1em;
    .progress-circle {
        transform: rotate(-90deg);
        width: 100%;
        height: 100%;

        .circle-bg {
            fill: none;
            stroke: #eee;
            stroke-width: 3.8;
        }

        .circle {
            fill: none;
            stroke-width: 2.8;
            stroke-linecap: round;
            stroke: #03e9f4;
            transform: rotate(-90deg);
            transform-origin: 50% 50%;
        }
    }

    .progress-text {
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        font-size: 20px;
        font-weight: bold;
    }
}
</style>
