<template>
  <div class="layout">
    <navbar />
    <Nuxt />
  </div>
</template>

<script>
import Navbar from '~/components/layout/Navbar.vue'
export default {
  components: { Navbar },
}
</script>

<style lang="scss" scoped>
.layout {
  background: #fafafa;
  min-height: 100vw;
}
</style>
