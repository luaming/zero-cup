<template>
    <NavBar></NavBar>
    <router-view />
</template>

<script>
import NavBar from "./components/NavBar.vue";

export default {
    components: {
        NavBar,
    },
};
</script>
<style lang="scss">
html,
body,
#app {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    height: 100%;
    font-family: maiyuan;
}
</style>
