<template>
    <div class="root">
        <div class="begin">
            <div class="one">留言板</div>
            <!--留言区开始-->
            <div class="two">
                <textarea
                    v-model="name"
                    cols="80"
                    rows="2"
                    placeholder="输入您的昵称。。。"
                ></textarea>
            </div>
            <div class="three">
                <span
                    >欢迎参与讨论！✧*｡ (ˊᗜˋ*) ✧*｡<br />快来和大家分享一下你对于mbti测试的一些经验和看法吧〃•ω‹〃</span
                >
            </div>
            <div>
                <textarea
                    v-model="comment"
                    cols="80"
                    rows="10"
                    placeholder="在这里留言(⑅˃◡˂⑅)"
                ></textarea>
            </div>
            <div class="button">
                <button class="green" @click="addComment">留言</button>
                <button class="purple" @click="delComment">删除</button>
            </div>
            <!--留言区结束-->
            <div>
                <hr />
                <h4 class="header">大家的话</h4>
                <h3 class="header">—— ฅ՞•ﻌ•՞ฅ♥︎ ——</h3>
                <div v-for="item in comments" :key="item.time">
                    <hr />
                    <h4>
                        <span>{{ item.name }}</span>
                        <span class="date">{{ item.time }}</span>
                    </h4>
                    <p>{{ item.comment }}</p>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    data() {
        return {
            comments: [
                {
                    name: "SunnySmiles",
                    comment:
                        "ISTP代表报道！MBTI帮助我扩大了对自己和周围世界的认知。我喜欢通过实践和经验来学习，好奇心驱使着我探索各种可能性。而MBTI则给了我一种框架，解释了为什么我喜欢挑战和解决问题，同时也让我更好地了解到需要平衡和尊重他人的需求。通过分享和比较不同的个性类型，我发现每个人都有自己的独特之处，这让我更加开放和包容。MBTI真是一种令人着迷的工具!",
                    time: "The Jan 12 2023",
                },
                {
                    name: "ExplorerHeart",
                    comment:
                        "作为一个ENFP，我一直对MBTI深感着迷。它为我提供了一个框架，解释了为什么我总是充满活力和创造力，喜欢结交新朋友，并追求新的冒险。我也意识到自己的某些挑战，比如集中注意力和做决策时的犹豫。通过了解这些方面，我能更加全面地管理自己，并找到适合我的成长和发展的方式。MBTI给予了我更多理解自己和他人的机会，让我更好地与世界互动。",
                    time: "The Jan 3 2023",
                },
            ],
            name: "",
            comment: "",
        };
    },
    methods: {
        addComment() {
            const commentData = {
                name: this.name.replace(/<(\/?\w+)>/g, "&lt;$1&gt;"),
                comment: this.comment.replace(/<(\/?\w+)>/g, "&lt;$1&gt;"),
                time: new Date().toLocaleDateString("en-US", {
                    year: "numeric",
                    month: "long",
                    day: "numeric",
                }),
            };
            this.comments.unshift(commentData);
            this.name = "";
            this.comment = "";
        },
        delComment() {
            this.name = "";
            this.comment = "";
        },
    },
};
</script>

<style scoped>
.top {
    background-color: #0083af;
}
#frozen-btn {
    display: flex;
    align-items: center;
    justify-content: center;
    height: 100vh;
}
.begin {
    font-family: maiyuan;
    width: 85%;
    margin-bottom: 100px;
    margin-top: 50px;
    background-color: rgba(255, 255, 255, 0.4);
    padding: 5px;
    display: flex;
    justify-content: center;
    flex-direction: column;
    border-radius: 5px;
}
.root {
    display: flex;
    justify-content: center;
    background-image: url("../assets/image/GQJ-214.jpg");
}
.one {
    font-size: 30px;
    font-weight: 600;
    margin: 50px 20px 35px 40px;
}

textarea {
    margin: 20px;
    outline: none;
    background-color: #efefef;
    border: 0;
    padding: 10px;
    padding-left: 30px;
    border-radius: 5px;
    resize: none;
    width: 94%;
}

.three {
    margin: 15px 20px 15px 40px;
}

.header {
    margin: 30px 20px 15px 40px;
    font-size: 27px;
    font-weight: 600;
}
button {
    margin: 12px 0 12px 30px;
    border: 0;
    color: black;
    padding: 12px 20px 12px 20px;
    transition: all 0.2s ease;
    border-radius: 5px;
    text-transform: uppercase;
    border-radius: 50px;
    position: relative;
}
button:before {
    content: "";
    display: block;
    background: linear-gradient(
        to left,
        rgba(255, 255, 255, 0) 50%,
        rgba(255, 255, 255, 0.4) 50%
    );
    background-size: 210% 100%;
    background-position: right bottom;
    height: 100%;
    width: 100%;
    position: absolute;
    top: 0;
    bottom: 0;
    right: 0;
    left: 0;
    outline: black;
    border-radius: 50px;
    transition: all 1s;
    -webkit-transition: all 1s;
}
.green {
    background-image: linear-gradient(to right, #25aea1, #40e495);
    box-shadow: 0 4px 15px 0 rgba(49, 196, 190, 0.75);
}

.purple {
    color: white;
    background-image: linear-gradient(to right, #6253e1, #852d91);
    box-shadow: 0 4px 15px 0 rgba(236, 116, 149, 0.75);
}

.purple:hover:before {
    background-position: left bottom;
}

.green:hover:before {
    background-position: left bottom;
}
h4 {
    margin: 10px 30px;
    text-transform: capitalize;
}
span.date {
    font-size: 12px;
    font-weight: 300;
    float: right;
    margin-right: 10px;
}
hr {
    border: 0;
    height: 0;
    border-top: 1px solid rgba(0, 0, 0, 0.2);
    border-bottom: 1px solid rgba(255, 255, 255, 0.3);
}
.begin p {
    margin: 0 30px 15px;
    font-weight: 300;
    color: #333;
    background-color: #eee;
    padding: 2rem 1rem;
    font-size: 18px;
}
</style>
