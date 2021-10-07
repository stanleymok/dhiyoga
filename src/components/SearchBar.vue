<template>
    <div>
        <form>
            <input type="text" placeholder="Search something">
            <button class="search-button ok-btn" type="submit"><BIconSearch></BIconSearch></button>
        </form>
    </div>
</template>

<style scoped lang="scss">
    @import '@/assets/stylesheets/variables.scss';
    .search-button {
        stroke-width: 3px;
        margin-left: 5px;
    }
</style>

<script>
export default ({
    name: "SearchBar"
})
</script>