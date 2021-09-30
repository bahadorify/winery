<template>
  <div class="wine">
    <img :src="wine.images[2].url" :alt="wine.images[2].altText" />
    <div>
      <h1>{{ wine.name }}</h1>
      <span>{{ wine.main_producer.name }}</span> <b>{{ wine.year }}</b>
      <em>{{ wine.main_country.name }}</em>
      <div class="price">{{ wine.price.formattedValue }}</div>
    </div>
    <!-- <pre>{{ wine }}</pre> -->
  </div>
</template>

<script>
// const getWines = () =>
//   import('~/data/winery_dump.json').then((m) => m.default || m)

export default {
  async asyncData({ route, req }) {
    const wines = await getWines()
    const wine = wines.find((w) => w['_id']['$oid'] === route.params.id)

    return { wine }
  },
}
</script>

<style lang="scss" scoped>
.wine {
  margin-top: 30px;
  display: flex;
  img {
    height: 300px;
    width: 300px;
    object-fit: contain;
  }
  .price {
    margin-top: 30px;
    font-size: 30px;
  }
}
</style>
