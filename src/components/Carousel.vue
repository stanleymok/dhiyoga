<template>
    <div class="carousel-container">
        <BIconChevronLeft class="icon left-nav" :class="{end: prevDisabled}" v-on:click="decreasePage"/>
        <div class="card-container" :on="page" name="slide" tag="p">
            <div class="card" v-for="card in pageCollection[page]" :key="card.title">
                <div class="card-header">{{card.header}}</div>
                <div class="card-subheader">{{card.subheader}}</div>
                <img class="card-image" :src="card.image" />
                <div class="card-summary">{{card.summary}}</div>
                <a class="card-link" :src="card.link">Read more</a>
            </div>
        </div>
        <BIconChevronRight class="icon right-nav" :class="{end: nextDisabled}" v-on:click="increasePage"/>
    </div>
    <div class="carousel-pages">
        <div class="page-dot" v-for="(p, index) in pages" v-on:click="page = index" :key="index" v-bind:class="page === index ? 'active' : ''"></div>
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
        margin: 10px 0;
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
        display: flex;
        flex-direction: column;
        flex: 0 0 240px;
        gap: 10px;
        height: 300px;
        box-shadow: 0px 0px 15px rgba(58, 59, 59, 0.26);
        border-radius: 10px;
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

    .carousel-pages {
        display: flex;
        justify-content: center;
        margin-top: 24px;
    }

    .page-dot {
        height: 10px;
        width: 10px;
        border-radius: 50%;
        background-color: $cream-3;
        margin: 0 5px;
        cursor: pointer;

        &.active {
            background-color: $grey-1;
        }
    }
</style>

<script>
export default ({
    name: "Carousel",
    props: {
        contentObject: Object,
    },
    data() {
        return {
            pageCollection: [],
            cards: this.contentObject.cards,
            page: 0,
            pages: Math.ceil(this.contentObject.cards.length / 3),
            setSize: 3,
            prevDisabled: true,
            nextDisabled: this.page < Math.ceil(this.contentObject.cards.length / 3),
        };
    },
    created() {
        this.calculatePages();
        this.groupObjects();
        this.togglePageNav();
    },
    methods: {
        groupObjects() {
            let cardSet = [];

            for (var i = 0; i < this.cards.length; i++) {
                cardSet.push(this.cards[i]);
                if (cardSet.length === this.setSize) {
                    this.pageCollection.push(cardSet);
                    cardSet = [];
                } else if (this.cards.length - i < this.setSize) {
                    this.pageCollection.push(this.cards.slice(i));
                    break;
                }
            }
        },
        decreasePage() {
            if (this.page > 0) {
                this.page--;
            }
            this.togglePageNav();
        },
        increasePage() {
            if (this.page < this.pages) {
                this.page++;
            }
            this.togglePageNav();
        },
        togglePageNav() {
            if (this.page > 0) {
                this.prevDisabled = false;
            } else {
                this.prevDisabled = true;
            }

            if (this.page < this.pages - 1) {
                this.nextDisabled = false;
            } else {
                this.nextDisabled = true;
            }
        },
        calculatePages() {
            this.pageCollection = [];
            this.pages = Math.ceil(this.cards.length / this.setSize);
        },
    }
});
</script>