<template>
  <table class="wine-table">
    <thead>
      <tr @click="handleSort">
        <th>Wine Name</th>
        <th>Producer</th>
        <th data-sortable="true" data-field="year" data-filter-control="select">
          Year
        </th>
        <th data-field="country" data-filter-control="select">Country</th>
        <th data-field="area" data-filter-control="select">Area</th>
        <th>Volume</th>
        <th data-sortable="true" data-field="price">Price</th>
        <th data-sortable="true" data-field="price_l">1L Price</th>
        <th data-sortable="true" data-field="ct">CT Score</th>
        <th data-sortable="true" data-field="price_075">0.75L Price</th>
        <th data-sortable="true" data-field="bbs_l">BBS Score/Liter</th>
        <th data-sortable="true" data-field="bbs_a">BBS Score/Adjusted</th>
        <th data-field="store" data-filter-control="select">Store?</th>
        <th data-field="home" data-filter-control="select">Home?</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="(wine, idx) in sortedWines" :key="idx">
        <td>
          <!-- <nuxt-link :to="`/wine/${wine['_id']['$oid']}`"> -->
          <img :src="wine.images[4].url" alt="" />
          {{ wine['name'] }}
          <!-- </nuxt-link> -->
        </td>
        <td>{{ wine['main_producer']['name'] }}</td>
        <td>{{ wine['year'] }}</td>
        <td>{{ wine['main_country']['name'] }}</td>
        <td>{{ wine['district']['name'] }}</td>
        <td>{{ wine['volume']['value'] }}</td>
        <td>{{ format_price(wine['price']['value']) }}</td>
        <td>{{ format_price(wine['litrePrice']['value']) }}</td>
        <td>{{ wine['ct']['score'] || 'N/A' }}</td>
        <td>{{ format_price(wine['price_adj']) }}</td>
        <td>{{ wine['bbs'] }}</td>
        <td>{{ wine['bbs_adj'] }}</td>
        <td>{{ wine['availability']['storeAvailability']['available'] }}</td>
        <td>{{ wine['availability']['deliveryAvailability']['available'] }}</td>
      </tr>
    </tbody>
  </table>
</template>

<script>
import _ from 'lodash'

export default {
  props: ['wines'],
  computed: {
    sortedWines() {
      return _.sortBy(this.wines, [(w) => w.ct.score]).reverse()
    },
  },
  mounted() {},
  methods: {
    format_price(amount) {
      return amount.toFixed(2)
    },
    handleSort(e) {
      console.log(e.target)
      console.log(e.currentTarget)
    },
  },
}
</script>

<style lang="scss" scoped>
.wine-table {
  font-family: Arial, Helvetica, sans-serif;
  border-collapse: collapse;
  width: 100%;
}

.wine-table td,
.wine-table th {
  border: 1px solid #ddd;
  padding: 8px;
}

.wine-table tr:nth-child(even) {
  background-color: #f2f2f2;
}

.wine-table tr:hover {
  background-color: #ddd;
}

.wine-table th {
  padding-top: 12px;
  padding-bottom: 12px;
  text-align: left;
  background-color: #4caf50;
  color: white;
}

td img {
  height: 50px;
  width: 50px;
  object-fit: contain;
}
</style>
