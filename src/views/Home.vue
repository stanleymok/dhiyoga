<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/dhiyoga_logo.png">
    <HelloWorld msg="DHIYOGA" subtext="Who am i?"/>
  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue'

export default {
  name: 'Home',
  components: {
    HelloWorld
  }
}
</script>
