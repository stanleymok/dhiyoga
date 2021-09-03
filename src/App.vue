<template>
    <NavHeader/>
    <router-view/>
</template>

<script>
import '@/assets/stylesheets/main.scss';
import NavHeader from "@/components/NavHeader.vue";

export default {
  name: "App",
  components: {
    NavHeader,
  },
};
</script>
