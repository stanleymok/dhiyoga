<template>
    <div>
        <div class="title-container">
            Today's Featured Asana
        </div>
        <div class="content-container">
            <component :is="content-component"></component>
        </div>
    </div>
</template>

<style scoped lang="scss">
    @import '@/assets/stylesheets/variables.scss';
    .title-container {
        background-color: $cream-1;
        border-bottom: 1px solid $cream-2;
        padding: 40px 50px;
        font-size: 30px;
        font-weight: 600;
        color: $grey-2;
    }
    .content-container {
        background-color: $cream-1;
    }
</style>

<script>
    export default {
        name: 'BasicSection',
        data() {
            return { content_component: '' };
        }
    };
</script>
