import gql from 'graphql-tag'
import * as Filters from '~/helpers/filters'

export const state = () => ({
  wines: [],
  filteredWines: [],
  wine: {},
  filter: {
    search: '',
    category: 'all',
    order: 'bbs',
  },
})

export const getters = {
  getWines(state) {
    return state.wines
  },
  getFilteredWines(state) {
    return state.filteredWines
  },
  getWine(state) {
    return state.wine
  },
}

export const actions = {
  async callApollo({ commit }) {
    let response = await this.app.apolloProvider.defaultClient.query({
      query: gql`
        query GetWines {
          wines {
            name
            year
            ct {
              score
              reviews
            }
            bbs
            price_adj
            bbs_adj
            main_producer {
              name
            }
            main_country {
              name
            }
            district {
              name
            }
            volume {
              value
            }
            price {
              value
            }
            litrePrice {
              value
            }
            availability {
              storeAvailability {
                available
              }
              deliveryAvailability {
                available
              }
            }
            images {
              url
            }
          }
        }
      `,
    })

    await commit('setDbWines', response.data.wines)
    await commit('setFilteredWines', response.data.wines)
    await commit('orderWines')
  },
  // ...
  async filterOrder({ commit }, order) {
    await commit('setOrder', order)
    await commit('orderWines')
  },
  async filterCategory({ commit, dispatch }, category) {
    await commit('setFilterCategory', category)
    dispatch('filterWines')
  },
  async filterSearch({ commit, dispatch }, search) {
    await commit('setFilterSearch', search)
    dispatch('filterWines')
  },
  async filterWines({ commit }) {
    await commit('filterWines')
    await commit('orderWines')
  },
  // ...
}

export const mutations = {
  setDbWines: (state, data) => {
    state.wines = data
  },
  // ...
  setFilteredWines(state, wines) {
    state.filteredWines = wines
  },

  setFilterCategory(state, category) {
    state.filter.category = category
  },
  setFilterSearch(state, search) {
    state.filter.search = search
  },
  setOrder(state, order) {
    state.filter.order = order
  },

  filterWines(state) {
    const wines = [...state.wines]
    state.filteredWines = wines
    state.filteredWines = Filters.filterWines(state.filter, wines)
  },
  orderWines(state) {
    const wines = [...state.filteredWines]
    state.filteredWines = Filters.orderWines(state.filter.order, wines)
  },
  // ...
}
