import moment from 'moment'

export function filterWines(filter, wines) {
  let filteredList = [...wines]

  // Filter category
  if (filter.category !== 'all') {
    const filtered = filteredList.filter(
      (wine) => wine.category === filter.category
    )
    filteredList = filtered
  }

  // Search
  if (filter.search !== '') {
    const searchList = []
    const searchTerm = filter.search.toLowerCase()
    for (let i = 0; i < filteredList.length; i++) {
      if (
        // (filteredList[i].companyName !== null &&
        //   filteredList[i].companyName.toLowerCase().includes(searchTerm)) ||
        filteredList[i].name !== null &&
        filteredList[i].name.toLowerCase().includes(searchTerm)
      ) {
        searchList.push(filteredList[i])
      }
    }
    filteredList = searchList
  }

  return filteredList
}

export function orderWines(order, wines) {
  const orderedList = [...wines]

  if (order === 'createdAt') {
    orderedList.sort(function (a, b) {
      const unixA = moment(a.createdAt).unix()
      const unixB = moment(b.createdAt).unix()
      return unixA < unixB ? -1 : 1
    })
  } else if (order === 'bbs') {
    orderedList.sort(function (a, b) {
      return a.bbs > b.bbs ? -1 : 1
    })
  } else {
    orderedList.sort(function (a, b) {
      const nameA = a[order] ? a[order].toLowerCase() : 'zzz'
      const nameB = b[order] ? b[order].toLowerCase() : 'zzz'
      return nameA < nameB ? -1 : 1
    })
  }

  return orderedList
}
