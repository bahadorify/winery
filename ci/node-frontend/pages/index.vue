<template>
  <div class="wrapper">
    <div class="container">
      <WineList />
      <Filters />
    </div>
  </div>
</template>

<script>
import Filters from '../components/common/Filters.vue'
import WineList from '../components/common/WineList.vue'
export default {
  components: { WineList, Filters },
}
</script>

<style lang="scss" scoped>
.container {
  padding-top: 30px;
  display: flex;
}
</style>
