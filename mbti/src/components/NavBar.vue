<template>
    <div class="menu-wrap">
        <input type="checkbox" class="toggler" v-model="isToggled" />
        <div class="hamburger"><div></div></div>
        <div
            class="menu animate__animated animate__rotateInUpLeft"
            v-show="isToggled"
        >
            <div class="overlay" @click="closeMenu">
                <div class="link-wrapper">
                    <ul>
                        <li><a href="/">Home</a></li>
                        <li>
                            <a href="/introduction"
                                >Introduction</a
                            >
                        </li>  
                        <li><a href="/test">Test</a></li>
                        <li>
                            <a href="/interaction">Interaction</a>
                        </li>
                      
                        <li>
                            <a href="/message">Message</a>
                        </li>
                        <li>
                            <a href="/contact">Contact</a>
                        </li>
                        
                    </ul>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: "NavBar",
    data() {
        return {
            isToggled: false,
        };
    },
    methods: {
        closeMenu() {
            this.isToggled = false;
        },
    },
};
</script>

<style lang="scss" scoped>
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

.menu-wrap {
    font-family: "monospace";
    line-height: 1.4;

    position: fixed;
    top: 0;
    left: 0;
    z-index: 999;

    .toggler {
        position: absolute;
        top: 0;
        left: 0;
        z-index: 999;
        cursor: pointer;
        width: 50px;
        height: 50px;
        opacity: 0;
    }

    .hamburger {
        position: absolute;
        top: 0;
        left: 0;
        z-index: 1;
        width: 4em;
        height: 5em;
        padding: 1rem;
        display: flex;
        align-items: center;
        justify-content: center;

        > div {
            position: relative;
            flex: none;
            width: 100%;
            height: 2px;
            background: #fff;
            display: flex;
            align-items: center;
            justify-content: center;
            transition: all 0.4s ease;

            &::before,
            &::after {
                content: "";
                position: absolute;
                z-index: 1;
                top: -10px;
                width: 100%;
                height: 2px;
                background: inherit;
            }

            &::after {
                top: 10px;
            }
        }
    }

    .toggler:checked + .hamburger > div {
        transform: rotate(135deg);
    }

    .toggler:checked + .hamburger > div:before,
    .toggler:checked + .hamburger > div:after {
        top: 0;
        transform: rotate(90deg);
    }

    .toggler:checked:hover + .hamburger > div {
        transform: rotate(225deg);
    }

    .toggler:checked ~ .menu {
        visibility: visible;

        > div {
            transform: scale(1);
            transition-duration: 1s;
            > div {
                opacity: 1;
            }
        }
    }

    .menu {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        visibility: hidden;
        overflow: hidden;
        display: flex;
        align-items: center;
        justify-content: center;

        .overlay {
            background: rgba(0, 0, 0, 0.7);
            border-radius: 50%;
            width: 200vw;
            height: 200vw;
            display: flex;
            flex: none;
            align-items: center;
            justify-content: center;
            transform: scale(0);
            transition: all 1s ease;

            .link-wrapper {
                text-align: center;
                max-width: 90vw;
                max-height: 100vh;
                opacity: 0;
                transition: opacity 1s ease;

                ul {
                    list-style: none;
                    color: #fff;
                    font-size: 1.5rem;

                    li {
                        padding: 1rem;

                        a {
                            color: inherit;
                            text-decoration: none;
                            transition: color 0.4s ease;
                            &:hover {
                                font-size: 1.8em;
                                letter-spacing: 0.2em;
                                transition: 0.2s;
                            }
                        }
                    }
                }
            }
        }
    }
}
</style>
