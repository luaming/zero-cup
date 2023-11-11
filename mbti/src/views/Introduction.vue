<template>
	<div
		class="shell"
		id="shell"
		:style="{ 'background-image': `url(${timeList[activeItem].img})` }"
	>
		<div class="header">
			<h2 class="title">{{ title }}</h2>
			<h3 class="subtitle">{{ subTitle }}</h3>
		</div>
		<div class="timeline">
			<div
				v-for="(item, key) in timeList"
				:key="key"
				:data-text="item.dataText"
				class="item"
				:class="{ 'item--active': activeItem === key }"
			>
				<div class="content">
					<img :src="item.img" alt="" class="img" />
					<h2 class="content-title">{{ item.title }}</h2>
					<p class="content-desc">{{ item.content }}</p>
				</div>
			</div>
		</div>
	</div>
</template>

<script setup>
import { onMounted, ref, defineProps } from "vue";
import bimg from "../assets/image/b.jpg";
import rimg from "../assets/image/r.jpg";
import textimg from "../assets/image/text.jpg";
import orgimg from "../assets/image/OIP.jpg";
import img0 from "../assets/image/0.jpg";
import img9 from "../assets/image/9.jpg";
import img6 from "../assets/image/6.jpg";
import img20 from "../assets/image/20.jpg";
const prop = defineProps({
	title: {
		type: String,
		default: "关于mbti",
	},
	subTitle: {
		type: String,
		default: "你需要了解的那些",
	},
	// 时间轴上的内容列表，包括图片、标题和内容
	timeList: {
		type: Array,
		default: () => [
			{
				dataText: "背景和创始人",
				img: bimg,
				title: "布里格斯母女",
				content:
					"MBTI是由伊莎贝尔·布里格斯（Isabel Briggs）和凯瑟琳·库克·布里格斯（Katharine Cook Briggs）母女共同创立的。\n" +
					"她们基于瑞士心理学家卡尔·荣格（Carl Jung）的理论开发了MBTI",
			},
			{
				dataText: "荣格的心理类型理论",
				img: rimg,
				title: "MBTI的基础",
				content:
					"荣格提出了人类心理中普遍存在的心理特质和倾向，并将其分为四个维度：外向（E）- 内向（I）、感觉（S）- 直觉（N）、思考（T）- 感觉（F）和判断（J）- 知觉（P）。",
			},
			{
				dataText: "MBTI的构建",
				img: textimg,
				title: "利用问卷调查工具",
				content:
					"布里格斯母女根据荣格的理论，开发了一套问卷调查工具，以帮助人们确定在四个维度上的偏好。" +
					"通过回答一系列选择题，个体可以被归类为16种不同的MBTI类型。",
			},
			{
				dataText: "MBTI类型",
				img: orgimg,
				title: "四个维度",
				content:
					"每个MBTI类型由四个字母表示，分别代表了四个维度的偏好。" +
					"例如，INTJ代表内向（I）、直觉（N）、思考（T）和判断（J）。共有16种不同的MBTI类型。",
			},
			{
				dataText: "应用和研究",
				img: img0,
				title: "应用广泛",
				content:
					"MBTI被广泛应用于人力资源管理、职业咨询、团队建设和个人发展等领域。" +
					"它可以帮助个体更好地了解自己的行为模式和偏好，以及与他人之间的交流和互动方式。",
			},
			{
				dataText: "争议和批评",
				img: img9,
				title: "存在一定争议",
				content:
					"尽管MBTI在应用中得到了广泛的认可和使用，但也受到了一些批评。一些人认为MBTI过于简化复杂的人格特征，并缺乏科学性和可靠性。",
			},
			{
				dataText: "认识自我",
				img: img6,
				title: "对自我的认知",
				content:
					"MBTI可以指导人们更好地认识自己，但是前提是没有误测。" +
					"我们不应该框于mbti的框架里，而是应该靠自己的生活经历更好的认识自己",
			},
			{
				dataText: "送给你的话",
				img: img20,
				title: "你生来就独特",
				content:
					"MBTI只是个小角度，充其量只能诠释你的一部分，而要更清晰地认识自己，只有自己才能做到。" +
					"所有的所谓测试结果，都是残缺的碎块，都不能代表你的全部。你就是你，你生而独特，你天生完美。",
			},
		],
	},
});

// 是否完成滚动的标志，默认为true
const isFinish = ref(true);
// 当前激活的文章项，默认为0
const activeItem = ref(0);
// 定义滚动容器的引用，默认为null
const el_shell = ref(null);
// 根据滚动的位置判断当前激活的文章项
const change = function (event) {
	isFinish.value = false;
	let el = event.target.scrollingElement;
	let pos = el.scrollTop;
	el_shell.value.querySelectorAll(".item").forEach((item, key) => {
		let flag = pos > item.offsetTop + 20;
		if (flag) {
			activeItem.value = key;
		}
	});
	// 设置滚动完成标志
	isFinish.value = true;
};

// 当容器滚动时的处理函数
const handleBoxScroll = function (event) {
	if (isFinish.value) {
		change(event);
	}
};

onMounted(() => {
	el_shell.value = document.getElementById("shell");
	// 给window对象添加滚动事件监听器
	window.addEventListener("scroll", handleBoxScroll);
});
</script>

<style scoped>
* {
	padding: 0;
	margin: 0;
	font-family: kaishu;
}
.top {
	background-color: #787878;
}
.shell {
	width: 100%;
	position: relative;
	padding: 80px 0;
	transition: 0.3s ease 0s;
	background-attachment: fixed;
	background-size: cover;
}

.shell:before {
	position: absolute;
	left: 0;
	top: 0;
	width: 100%;
	height: 100%;
	background: rgba(99, 99, 99, 0.8);
	content: "";
}

.header {
	width: 100%;
	text-align: center;
	margin-bottom: 80px;
	position: relative;
}

.title {
	color: #fff;
	font-size: 46px;
	font-weight: normal;
	margin: 0;
}

.timeline {
	display: flex;
	margin: 0 auto;
	flex-wrap: wrap;
	flex-direction: column;
	max-width: 700px;
	position: relative;
}

.content-title {
	font-weight: normal;
	font-size: 66px;
	margin: -10px 0 0 0;
	transition: 0.4s;
	padding: 0 10px;
	box-sizing: border-box;
	color: #fff;
}

.content-desc {
	margin: 0;
	font-size: 15px;
	box-sizing: border-box;
	color: rgba(255, 255, 255, 0.7);
	line-height: 25px;
}

.timeline:before {
	position: absolute;
	left: 50%;
	width: 2px;
	height: 100%;
	margin-left: -1px;
	content: "";
	background: rgba(255, 255, 255, 0.07);
}

.item {
	padding: 40px 0;
	opacity: 0.3;
	filter: blur(2px);
	transition: 0.5s;
	box-sizing: border-box;
	width: calc(50% - 40px);
	display: flex;
	position: relative;
	transform: translateY(-80px);
}

.item:before {
	content: attr(data-text);
	letter-spacing: 3px;
	width: 100%;
	position: absolute;
	color: rgba(255, 255, 255, 0.5);
	font-size: 13px;
	border-left: 2px solid rgba(255, 255, 255, 0.5);
	top: 70%;
	margin-top: -5px;
	padding-left: 15px;
	opacity: 0;
	right: calc(-100% - 56px);
	font: 900 20px "";
	letter-spacing: 5px;
}

.item:nth-child(even) {
	align-self: flex-end;
}

.item:nth-child(even):before {
	right: auto;
	text-align: right;
	left: calc(-100% - 56px);
	padding-left: 0;
	border-left: none;
	border-right: 2px solid rgba(255, 255, 255, 0.5);
	padding-right: 15px;
}

.item--active {
	opacity: 1;
	transform: translateY(0);
	filter: blur(0px);
}

.item--active:before {
	top: 50%;
	transition: 0.3s all 0.2s;
	opacity: 1;
}

.item--active .content-title {
	margin: -50px 0 20px 0;
}

.img {
	max-width: 100%;
	box-shadow: 0 10px 15px rgba(0, 0, 0, 0.4);
}

.subtitle {
	color: rgba(255, 255, 255, 0.5);
	font-size: 16px;
	letter-spacing: 5px;
	margin: 10px 0 0 0;
	font-weight: normal;
}

@media only screen and (max-width: 767px) {
	.item {
		align-self: baseline !important;
		width: 100%;
		padding: 0 30px 150px 80px;
	}

	.item:before {
		left: 10px !important;
		padding: 0 !important;
		top: 50px;
		text-align: center !important;
		width: 60px;
		border: none !important;
	}

	.item:last-child {
		padding-bottom: 40px;
	}
}
</style>
