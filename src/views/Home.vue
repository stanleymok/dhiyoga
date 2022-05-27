<template>
	<div class="home">
		<BasicSection :title="featuredTitle" :content-data="imageTextContent"/>
		<BasicSection :title="carouselTitle" :content-data="carouselContent"/>
		<TabSection :title="carouselStepTitle" :content-data="carouselStepContent"/>
	</div>
</template>

<script>
	// @ is an alias to /src
	import BasicSection from '@/components/BasicSection.vue';
	import TabSection from '@/components/TabSection.vue';

	const imageTextContent = {
		contentType: "ImageTextSummary",
		title: "Bhujjangasana",
		subtitle: "Serpent's Pose",
		summary: "The asana is great for stretching the back and neck muscles, and is one of the fundamental and most classic of asanas in Hatha yoga.",
		image: "https://cdn.cdnparenting.com/articles/2019/04/29114806/1033264990-H-1024x700.jpg"
	};

	const carouselContent = {
		contentType: "Carousel",
		cards: [
			{
				header: "Asana 1",
				subheader: "Asana 1 Subheader",
				summary: "Asana 1 Summary - Maybe some background info",
				image: "https://i.natgeofe.com/n/3faa2b6a-f351-4995-8fff-36d145116882/domestic-dog_16x9.jpg",
				link: "/"
			}, {
				header: "Asana 2",
				subheader: "Asana 2 Subheader",
				summary: "Asana 2 Summary - Maybe some background info",
				image: "https://cdn.cnn.com/cnnnext/dam/assets/201030094143-stock-rhodesian-ridgeback-super-tease.jpg",
				link: "/"
			}, {
				header: "Asana 3",
				subheader: "Asana 3 Subheader",
				summary: "Asana 3 Summary - Maybe some background info",
				image: "https://static.theprint.in/wp-content/uploads/2020/10/dog-1809044_1280-e1575195192134-768x432-1.jpg",
				link: "/"
			}, {
				header: "Asana 4",
				subheader: "Asana 4 Subheader",
				summary: "Asana 4 Summary - Maybe some background info",
				image: "https://www.helpguide.org/wp-content/uploads/king-charles-spaniel-resting-head-768.jpg",
				link: "/"
			}, {
				header: "Asana 5",
				subheader: "Asana 5 Subheader",
				summary: "Asana 5 Summary - Maybe some background info",
				image: "https://image.cnbcfm.com/api/v1/image/105992231-1561667465295gettyimages-521697453.jpeg?v=1561667497&w=1600&h=900",
				link: "/"
			},
		]
	};

	const carouselStepContent = {
		contentType: "CarouselStep",
		tabs: [
			{
				id: 1,
				tab_label: "Beginner"
			}, {
				id: 2,
				tab_label: "Intermediate"
			}, {
				id: 3,
				tab_label: "Advanced"
			}
		],
		tabContent: [
			{
				tab_id: 1,
				cards: [
					{
						title: "Step 1",
						subtitle: "Asana 1 Subheader",
						summary: "Asana 1 Summary - Maybe some background info",
						image: "https://i.natgeofe.com/n/3faa2b6a-f351-4995-8fff-36d145116882/domestic-dog_16x9.jpg",
						link: "/"
					}, {
						title: "Step 2",
						subtitle: "Asana 2 Subheader",
						summary: "Asana 2 Summary - Maybe some background info",
						image: "https://cdn.cnn.com/cnnnext/dam/assets/201030094143-stock-rhodesian-ridgeback-super-tease.jpg",
						link: "/"
					}
				]
			}, {
				tab_id: 2,
				cards: [
					{
						title: "Step 1",
						subtitle: "Asana 3 Subheader",
						summary: "Asana 3 Summary - Maybe some background info",
						image: "https://static.theprint.in/wp-content/uploads/2020/10/dog-1809044_1280-e1575195192134-768x432-1.jpg",
						link: "/"
					}, {
						title: "Step 2",
						subtitle: "Asana 4 Subheader",
						summary: "Asana 4 Summary - Maybe some background info",
						image: "https://www.helpguide.org/wp-content/uploads/king-charles-spaniel-resting-head-768.jpg",
						link: "/"
					}, {
						title: "Step 3",
						subtitle: "Asana 4 Subheader",
						summary: "Asana 4 Summary - Maybe some background info",
						image: "https://www.helpguide.org/wp-content/uploads/king-charles-spaniel-resting-head-768.jpg",
						link: "/"
					}
				]
			}, {
				tab_id: 3,
				cards: [
					{
						title: "Step 1",
						subtitle: "Asana 5 Subheader",
						summary: "Asana 5 Summary - Maybe some background info",
						image: "https://image.cnbcfm.com/api/v1/image/105992231-1561667465295gettyimages-521697453.jpeg?v=1561667497&w=1600&h=900",
						link: "/"
					}
				]
			}
		]
	}

	export default {
		name: "Home",
		components: {
			BasicSection,
			TabSection
		},
		data() {
			return {
				imageTextContent,
				carouselContent,
				carouselStepContent,
				featuredTitle: "Today's Featured Asana",
				carouselTitle: "Beginner's Asanas",
				carouselStepTitle: "Basic Set-up"
			}
		}
	}
</script>
