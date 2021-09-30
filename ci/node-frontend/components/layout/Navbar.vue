<template>
  <div class="navbar-wrapper full-width">
    <div class="container">
      <div class="nav1">
        <NuxtLink to="/">
          <img src="/logos/winecharts.svg" alt="winecharts logo" class="logo" />
        </NuxtLink>
        <SearchBar class="search-bar" />
      </div>
      <div class="nav2"></div>
    </div>
  </div>
</template>

<script>
import SearchBar from '../common/SearchBar.vue'
export default {
  components: { SearchBar },
}
</script>

<style lang="scss" scoped>
.navbar-wrapper {
  box-shadow: 0 1px 4px #a8a5a3;
}
.nav1 {
  height: 64px;
  display: flex;
  align-items: center;
}
.logo {
  width: 200px;
}
.search-bar {
  margin-left: 24px;
}
</style>
