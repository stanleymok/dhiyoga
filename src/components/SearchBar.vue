<template>
    <div>
        <form>
            <input type="text" placeholder="Search something">
            <button class="search-button" type="submit"><BIconSearch></BIconSearch></button>
        </form>
    </div>
</template>

<style scoped lang="scss">
    @import '@/assets/stylesheets/variables.scss';
    input[type=text] {
        height: 25px;
        border-radius: 5px;
        border: 2px solid $cream-2;
        padding: 3px 10px;
        font-size: 12px;
        font-family: Montserrat;
    }
    .search-button {
        background-color: $green-2;
        border-radius: 5px;
        border: none;
        height: 35px;
        width: 40px;
        margin-left: 5px;
    }
</style>

<script>
export default ({
    name: "SearchBar"
})
</script>