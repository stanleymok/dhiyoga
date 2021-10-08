<template>
    <div class="carousel-container">
        <div class="card" v-for="card in contentObject.cards" :key="card.title">
            <div class="card-header">{{card.header}}</div>
            <div class="card-subheader">{{card.subheader}}</div>
            <img class="card-image" :src="card.image" />
            <div class="card-summary">{{card.summary}}</div>
            <a :src="card.link">Read more</a>
        </div>
    </div>
</template>

<style scoped lang="scss">
    @import '@/assets/stylesheets/variables.scss';
    .carousel-container {
        display: flex;
        width: 100%;
        flex-wrap: wrap;
        justify-content: space-between;
    }

    .card {
        width: 260px;
        height: 380px;
        box-shadow: 0px 0px 15px rgba(58, 59, 59, 0.26);
        border-radius: 10px;

        .card-image {
            width: 100%;
        }
    }
</style>

<script>
export default ({
    name: "Carousel",
    props: {
        contentObject: Object
    }
});
</script>