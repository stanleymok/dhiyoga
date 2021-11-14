<template>
    <div class="carousel-container">
        <BIconChevronLeft class="icon left-nav end" v-on:click="decreasePage"/>
        <div class="card-container" :on="pageCollection">
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
        pointer-events: none;
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
        //this.groupObjects();
        this.togglePageNav();
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
            const cards = this.contentObject.cards;
            let cardSet = [];

            for (var i = 0; i < cards.length; i++) {
                cardSet.push(cards[i]);
                if (cardSet.length === this.setSize) {
                    this.pageCollection.push(cardSet);
                    cardSet = [];
                } else if (cards.length - i < this.setSize) {
                    this.pageCollection.push(cards.slice(i));
                    break;
                }
            }
            console.log(this.pageCollection.length);
        },
        decreasePage() {
            if (this.page > 0) {
                this.page--;
            }
            this.togglePageNav();
        },
        increasePage() {
            if (this.page < this.pageCollection.length) {
                this.page++;
            }
            this.togglePageNav();
        },
        togglePageNav() {
            if (this.page === 0 && this.page === this.pageCollection.length - 1) {
                $(".left-nav").addClass("end");
                $(".right-nav").addClass("end");
            } else if (this.page === 0 || this.page === this.pageCollection.length - 1) {
                $(".left-nav").toggleClass("end");
                $(".right-nav").toggleClass("end");
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