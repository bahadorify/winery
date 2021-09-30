export default async ({ store }) => {
  await store.dispatch('wines/callApollo')
}
