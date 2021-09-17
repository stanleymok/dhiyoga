<template>
    <div class="nav-header">
        <img alt="Vue logo" src="../assets/dhiyoga_logo.png" class="nav-logo">
        <div class="nav-item" v-for="link in links" v-bind:key="link.id" >
            <a v-bind:href="link.URL">{{ link.label }}</a>
        </div>
        <div class="nav-search">
            <SearchBar/>
        </div>
    </div>
</template>

<style scoped lang="scss">
    @import '@/assets/stylesheets/variables.scss';
    .nav-header {
        background-color: $cream-1;
        display: flex;
        padding: 20px 30px;
        font-size: 14px;
        align-items: center;
        border-bottom: 2px $cream-2 solid;
    }

    .nav-item {
        padding: 5px;
        margin-right: 20px;
        font-weight: 600;
    }

    .nav-logo {
        width: 50px;
        margin-right: 15px;
    }

    .nav-search {
        margin-left: auto;
    }
</style>

<script>
import SearchBar from "@/components/SearchBar.vue";

export default ({
    name: "NavHeader",
    data: function() {
        return {
            links: [
                {id: 1, 'label': 'Home', 'URL': '/'},
                {id: 2, 'label': 'About', 'URL': '/about'},
                {id: 3, 'label': 'Contact', 'URL': '/contact'}
            ]
        }
    },
    components: {
        SearchBar
    }
})
</script>
