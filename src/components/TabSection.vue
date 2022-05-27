<template>
    <div class="tab-section-container">
        <div class="title-container">
            {{title}}
        </div>
        <div class="tabs">
            <!-- TODO: the thingy to toggle difficulties -->
            <input type="radio" name="difficulty">
            </div>
        </div>
        <div class="tab-content-container">
            <BIconChevronLeft class="icon left-nav" :class="{end: prevDisabled}" v-on:click="decreasePage"/>
            <div class="tab-content">
                <component :on="page" :content-object="pageData" :is="ImageTextSummary"/>
            </div>
            <BIconChevronRight class="icon right-nav" :class="{end: nextDisabled}" v-on:click="increasePage"/>
        </div>
        <div class="carousel-pages">
            <div class="page-dot" v-for="(p, index) in pages" v-on:click="page = index" :key="index" :class="page === index ? 'active' : ''"></div>
        </div>
    </div>
</template>

<style scoped lang="scss">
    @import '@/assets/stylesheets/variables.scss';

    .title-container {
        border-bottom: 2px solid $cream-2;
        padding: 30px 350px;
        font-size: 24px;
        font-weight: 600;
        color: $grey-2;
    }

    .tab-section-container {
        background-color: $cream-1;
        border-bottom: 2px solid $cream-2;
    }

    .tab-content {
        padding: 35px 350px;
    }

    .tab-content-container {
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
</style>

<script>
import ImageTextSummary from '@/components/ImageTextSummary.vue';
import { shallowRef } from '@vue/reactivity';

export default {
    name: "TabSection",
    components: ImageTextSummary,
    props: {
        title: String,
        contentData: Object,
    },
    data() {
        return {
            pageData: this.contentData.tabContent[0].cards[0],
            ImageTextSummary: shallowRef(ImageTextSummary),
            page: 0,
            pages: this.contentData.tabContent[0].cards.length,
            prevDisabled: true,
            nextDisabled: this.page < this.contentData.tabContent[0].cards.length,
        }
    },
    methods: {
        decreasePage() {
            if (this.page > 0) {
                this.page--;
            }
            this.pageData = this.contentData.tabContent[0].cards[this.page];
            this.togglePageControls();
        },
        increasePage() {
            if (this.page < this.pages - 1) {
                this.page++;
            }
            this.pageData = this.contentData.tabContent[0].cards[this.page];
            this.togglePageControls();
        },
        togglePageControls() {
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
    }
};
</script>