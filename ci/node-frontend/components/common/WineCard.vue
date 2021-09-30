<template>
  <div class="wine-card">
    <div class="image">
      <img :src="wine.images[3].url" :alt="wine.name" ref="img" />
    </div>
    <div class="info">
      <div class="producer">{{ wine.main_producer.name }}</div>
      <div class="name">{{ getName }}</div>
      <div class="area">
        <span class="flag">{{ getFlag }}</span>
        <span class="country">{{ wine.main_country.name }}</span>
        <span class="dot">.</span>
        <span class="district">{{ wine.district.name }}</span>
      </div>
      <div class="score">
        <span class="bbs">{{ (wine.bbs * 10).toFixed(1) }}</span>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: ['wine'],
  computed: {
    getName() {
      const re = /\b(\w+)$/
      const lastWord = this.wine.main_producer.name.match(re)
      if (lastWord && lastWord[1]) {
        return this.wine.name.split(lastWord[1])[1]
      } else {
        return this.wine.name
      }
    },
    getFlag() {
      switch (this.wine.main_country.name) {
        case 'Italia':
          return '🇮🇹'
        case 'Spania':
          return '🇪🇸'
        case 'USA':
          return '🇺🇸'
        case 'Frankrike':
          return '🇫🇷'
        case 'Sør-Afrika':
          return '🇿🇦'
        case 'Australia':
          return '🇦🇺'
        case 'Portugal':
          return '🇵🇹'
        case 'Østerrike':
          return '🇦🇹'
        case 'Chile':
          return '🇨🇱'
        case 'Bulgaria':
          return '🇧🇬'
        case 'Tyskland':
          return '🇩🇪'
        case 'Argentina':
          return '🇦🇷'
        case 'Brasil':
          return '🇧🇷'
        case 'Uruguay':
          return '🇺🇾'
        case 'New Zealand':
          return '🇳🇿'
        case 'Libanon':
          return '🇱🇧'
        case 'England':
          return '🏴󠁧󠁢󠁥󠁮󠁧󠁿'
        case 'Makedonia':
          return '🇲🇰'

        default:
          return ''
      }
    },
  },
}
</script>

<style lang="scss" scoped>
.wine-card {
  height: 130px;
  width: 800px;
  box-shadow: 0 0 7px 0 rgb(0 0 0 / 6%);
  background: #fff;
  border-radius: 4px;
  padding: 8px;
  display: flex;
  align-items: center;
}

.image {
  height: 110px;
  width: 150px;
  display: flex;
  justify-content: center;
  align-items: center;
  box-shadow: 0 0 7px 0 rgb(0 0 0 / 6%);
  img {
    height: 100px;
  }
}

.info {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  padding: 8px 16px;
  .producer {
    font-size: 14px;
  }
  .name {
    font-size: 16px;
  }
  .area {
    font-size: 13px;
  }
  .score {
    font-size: 40px;
  }
}
</style>
