<template>
    <div class="basic-section-container">
        <div class="title-container">
            {{title}}
        </div>
        <component :content-object="contentData" :is="shownComponent" />
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
    }
</style>

<script>
import { shallowRef } from 'vue'
import ImageTextSummary from '@/components/ImageTextSummary.vue';
import EmptySection from '@/components/EmptySection.vue';

export default {
    name: 'BasicSection',
    props: {
        title: String,
        contentData: Object // Data to be passed to the content component
    },
    methods: {
        selectComponent(contentType) {
            switch (contentType) {
                case "ImageTextSummary":
                    return shallowRef(ImageTextSummary);
                default:
                    return EmptySection;
            }
        }
    },
    data() {
        return {
            shownComponent: this.selectComponent(this.contentData.contentType),
        }
    }
};
</script>
