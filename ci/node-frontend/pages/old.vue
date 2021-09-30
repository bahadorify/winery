<template>
  <div class="container">
    <div class="filters">
      <search-bar @searchInputChange="doSearch($event)" />
      <div class="filter-year">
        <b>before year</b>
        <span>{{ minYear }}</span>
        <div class="slider-year">
          <span>{{ valueYear }}</span>
          <input
            type="range"
            :min="minYear"
            :max="maxYear"
            v-model="valueYear"
            step="1"
            @change="handleYearChange"
          />
        </div>
        <span>{{ maxYear }}</span>
      </div>
    </div>
    <wine-table :wines="resultWines"></wine-table>
  </div>
</template>

<script>
import _ from 'lodash'
import { mapState } from 'vuex'
import SearchBar from '~/components/common/SearchBar.vue'
import WineTable from '~/components/common/WineTable.vue'

export default {
  components: { WineTable, SearchBar },
  data() {
    return {
      resultWines: [],
      valueYear: 2020,
      searchTerm: '',
    }
  },
  mounted() {
    this.resultWines = this.wines
  },
  methods: {
    doSearch(searchTerm) {
      this.searchTerm = searchTerm
      if (searchTerm.length >= 3) {
        this.resultWines = this.filteredWines.filter((w) =>
          w.name.toLowerCase().includes(searchTerm.toLowerCase())
        )
      } else {
        this.resultWines = this.filteredWines
      }
    },
    handleYearChange() {
      this.doSearch(this.searchTerm)
    },
  },
  computed: {
    ...mapState({
      wines: 'wines',
      // winesAll: 'wines',
      // resultWines: 'wines',
    }),
    minYear() {
      return _.minBy(this.wines, (w) => w.year).year
    },
    maxYear() {
      return _.maxBy(this.wines, (w) => w.year).year
    },
    filteredWines() {
      return this.wines.filter((w) => w.year <= this.valueYear)
    },
  },
}
</script>

<style lang="scss" scoped>
.container {
  margin: 10px;
}
.filters {
  padding: 20px 10px;
}
.filter-year {
  margin-top: 10px;
  display: flex;
}
.slider-year {
  display: flex;
  flex-direction: column;
  align-items: center;
}
</style>
