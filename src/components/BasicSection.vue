<template>
    <div class="basic-section-container">
        <div class="title-container">
            {{title}}
        </div>
        <div class="component-container">
            <component :content-object="contentData" :is="shownComponent" />
        </div>
    </div>
</template>

<style scoped lang="scss">
    @import '@/assets/stylesheets/variables.scss';

    .title-container {
        border-bottom: 2px solid $cream-2;
        padding: 35px 350px;
        font-size: 24px;
        font-weight: 600;
        color: $grey-2;
    }

    .basic-section-container {
        background-color: $cream-1;
        border-bottom: 2px solid $cream-2;
    }

    .component-container {
        padding: 35px 350px;
    }
</style>

<script>
import { shallowRef } from 'vue';
import ImageTextSummary from '@/components/ImageTextSummary.vue';
import Carousel from '@/components/Carousel.vue';
import EmptySection from '@/components/EmptySection.vue';

export default {
    name: 'BasicSection',
    props: {
        title: String,
        contentData: Object // Data to be passed to the content component
    },
    methods: {
        selectComponent(contentData) {
            if (!contentData) {
                return EmptySection;
            }

            let contentType = contentData.contentType;

            switch (contentType) {
                case "ImageTextSummary":
                    return shallowRef(ImageTextSummary);
                case "Carousel":
                    return shallowRef(Carousel);
                default:
                    return EmptySection;
            }
        }
    },
    data() {
        return {
            shownComponent: this.selectComponent(this.contentData),
        }
    }
};
</script>
