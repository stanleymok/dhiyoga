<template>
	<div class="home">
		<BasicSection :title="featuredTitle" :content-data="imageTextContent"/>
	</div>
</template>

<script>
	// @ is an alias to /src
	import BasicSection from '@/components/BasicSection.vue';

	const imageTextContent = {
		contentType: "ImageTextSummary",
		title: "Bhujjangasana",
		subtitle: "Serpent's Pose",
		summary: "The asana is great for stretching the back and neck muscles, and is one of the fundamental and most classic of asanas in Hatha yoga.",
		image: "https://cdn.cdnparenting.com/articles/2019/04/29114806/1033264990-H-1024x700.jpg"
	}

	export default {
		name: 'Home',
		components: {
			BasicSection,
		},
		data() {
			return {
				imageTextContent,
				featuredTitle: "Today's Featured Asana",
			}
		}
	}
</script>
