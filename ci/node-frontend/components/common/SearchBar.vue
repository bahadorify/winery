<template>
  <div class="search">
    <input
      type="text"
      name="wine-search"
      id="wine-search"
      placeholder="search for wines..."
      v-model="searchTerm"
      @input="handleSearch"
    />
  </div>
</template>

<script>
import { debounce } from '~/helpers/index'

export default {
  data() {
    return {
      searchTerm: '',
    }
  },
  methods: {
    handleSearch: debounce(function () {
      this.$store.dispatch('wines/filterSearch', this.searchTerm)
    }, 500),
  },
}
</script>

<style lang="scss" scoped>
input {
  width: 300px;
  font-size: 16px;
  color: #333;
  background-image: url(/icons/magnifying-glass.svg);
  background-position: 16px;
  background-size: 16px;
  background-repeat: no-repeat;
  outline: none;
  padding: 4px 0 4px 48px;
  border: 1px solid #dedede;
  transition: width 0.6s ease-in-out;
  height: 40px;
  background-color: #fff;
  border-radius: 32px;
  width: 100%;
}
</style>
