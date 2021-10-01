<template>
	<div class="home">
		<BasicSection title-text=""/>
	</div>
</template>

<script>
	// @ is an alias to /src
	import BasicSection from '@/components/BasicSection.vue'
	export default {
		name: 'Home',
		components: {
			BasicSection
		},
		data() {
			return {
				passedComponent: {
					name: "ImageTextSummary"
				}
			}
		}
	}
</script>
