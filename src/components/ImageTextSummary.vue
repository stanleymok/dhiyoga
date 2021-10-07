<template>
    <div class="image-text-container">
        <img class="image-text-image" :src="contentObject.image">
        <div class="text-container">
            <div class="image-text-title">{{contentObject.title}}</div>
            <div class="image-text-subtitle">{{contentObject.subtitle}}</div>
            <div class="image-text-summary">{{contentObject.summary}}</div>
            <a class="image-text-link">Read more</a>    <!-- TODO: Implement link to full asana page -->
            <a class="share-link"><span class="link-text">Share</span><BIconShareFill class="icon"></BIconShareFill></a> <!-- TODO: Implement social media linking -->
        </div>
    </div>
</template>

<style scoped lang="scss">
    @import '@/assets/stylesheets/variables.scss';
    .image-text-container {
        padding: 50px 350px;
        display: flex;
    }

    .image-text-image {
        width: 370px;
        height: 512px;
        object-fit: scale-down;
        border-radius: 10px;
        background-color: $cream-3;
    }

    .text-container {
        margin-left: 30px;
        display: flex;
        flex-direction: column;
        gap: 15px;
        flex-basis: 100%;

        .image-text-title {
            font-weight: 600;
            font-size: 20px;
            line-height: 29px;
        }

        .image-text-subtitle {
            font-weight: 500;
            font-size: 18px;
            font-style: italic;
            line-height: 20px;
            color: $grey-1;
        }

        .image-text-summary {
            font-weight: 500;
            font-size: 16px;
            line-height: 18px;
            text-align: justify;
        }

        .image-text-link {
            font-weight: 700;
            font-size: 16px;
            color: $green-3;
            margin-top: 24px;

            &:hover {
                color: $green-4;
            }
        }

        .share-link {
            align-self: end;
            justify-self: end;
            font-weight: 500;
            font-size: 14px;
            margin-top: 40px;

            .link-text, .icon {
                vertical-align: middle;
            }

            .icon {
                padding-left: 10px;
            }
        }
    }
</style>

<script>
export default ({
    name: "ImageTextSummary",
    props: {
        contentObject: Object
    }
});
</script>
