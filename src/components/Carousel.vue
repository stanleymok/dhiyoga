<template>
    <div class="carousel-container">
        <BIconChevronLeft class="icon left-nav end" v-on:click="decreasePage"/>
        <div class="card-container" :on="page">
            <div class="card" v-for="card in pageCollection[page]" :key="card.title">
                <div class="card-header">{{card.header}}</div>
                <div class="card-subheader">{{card.subheader}}</div>
                <img class="card-image" :src="card.image" />
                <div class="card-summary">{{card.summary}}</div>
                <a class="card-link" :src="card.link">Read more</a>
            </div>
        </div>
         <BIconChevronRight class="icon right-nav" v-on:click="increasePage"/>
    </div>
</template>

<style scoped lang="scss">
    @import '@/assets/stylesheets/variables.scss';

    .carousel-container {
        display: flex;
        justify-content: space-between;
        align-items: center;
        width: 100%;
        gap: 10px;
    }

    .icon {
        flex-shrink: 0;
        width: 24px;
        height: 24px;
        color: $grey-1;
        cursor: pointer;
        stroke: $grey-1;
        stroke-width: 2;
    }

    .end {
        color: $cream-3;
        cursor: auto;
        stroke: $cream-3;
    }

    .card-container {
        display: flex;
        justify-content: center;
    }

    .card {
        flex: 0 0 240px;
        height: 300px;
        box-shadow: 0px 0px 15px rgba(58, 59, 59, 0.26);
        border-radius: 10px;
        display: flex;
        flex-direction: column;
        gap: 10px;
        padding: 15px 0;
        margin: 0 10px;

        .card-header, .card-subheader, .card-summary, .card-link {
            margin: 0 15px;
        }

        .card-header {
            font-weight: 600;
            font-size: 18px;
            line-height: 20px;
            text-align: center;
        }

        .card-subheader {
            font-weight: 500;
            font-style: italic;
            font-size: 16px;
            line-height: 18px;
            color: $grey-1;
            text-align: center;
        }

        .card-summary {
            font-size: 14px;
            line-height: 16px;
        }

        .card-link {
            font-weight: 700;
            font-size: 14px;
            line-height: 16px;
            color: $green-3;
            margin-top: auto;
        }

        .card-image {
            width: 100%;
            height: 120px;
            object-fit: cover;
            background-color: $cream-2;
        }
    }
</style>

<script>
import $ from 'jquery';

export default ({
    name: "Carousel",
    props: {
        contentObject: Object,
    }, 
    data() {
        return {
            pageCollection: [],
            page: 0,
            setSize: 3,
        };
    },
    created() {
        this.groupObjects();
        window.addEventListener("resize", this.recalculateSetSize);
    },
    mounted() {
        this.recalculateSetSize();
    },
    unmounted() {
        window.removeEventListener("resize", this.recalculateSetSize);
    },
    methods: {
        groupObjects() {
            let cardSet = [];
            this.contentObject.cards.forEach((card, index) => {
                cardSet.push(card);
                if ((this.setSize == 1) || (index % this.setSize == this.setSize - 1)) {
                    this.pageCollection.push(cardSet);
                    cardSet = [];
                }
            });
        },
        decreasePage() {
            if (this.page > 0) {
                this.page--;
            }
        },
        increasePage() {
            if (this.page < this.pageCollection) {
                console.log("oy")
                this.page++;
            }
        },
        recalculateSetSize() {
            this.pageCollection = [];

            const cardWidth = parseInt($(".card").css("width")) || 240; // Not sure if hardcoding the width is the best choice
            const margin = parseInt($(".card").css("margin-right")) * 2 || 20;
            const containerWidth =  parseInt($(".component-container").css("width")) - parseInt($(".icon").css("width")) * 2;
            let newSetSize = Math.floor(containerWidth / (cardWidth + margin));

            if (newSetSize == this.contentObject.cards.length || newSetSize > 3) {
                newSetSize = 3;
            } else if (newSetSize == 0) {
                newSetSize = 1;
            }

            this.setSize = newSetSize;
            this.groupObjects();
        }
    }
});
</script>