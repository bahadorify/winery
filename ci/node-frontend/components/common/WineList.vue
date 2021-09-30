<template>
  <div class="wine-list-wrapper">
    <div v-if="wines.length">
      <WineCard
        v-for="(wine, idx) in filteredWines"
        :key="idx"
        :wine="wine"
        class="wine-card"
      />
    </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
import _ from 'lodash'
import WineCard from '~/components/common/WineCard.vue'
export default {
  components: { WineCard },
  data() {
    return {}
  },
  computed: {
    ...mapGetters({
      wines: 'wines/getWines',
      filteredWines: 'wines/getFilteredWines',
    }),
  },
}
</script>

<style lang="scss" scoped>
.wine-card {
  margin-bottom: 10px;
}
</style>
