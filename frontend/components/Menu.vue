<template>
  <div>
      <c-menu>
  <c-menu-button right-icon="chevron-down" variant-color="green">
    Menu
  </c-menu-button>
  <c-menu-list>
    <c-menu-group title="Profile">
      <c-menu-item>My Orders</c-menu-item>
      <c-menu-item>My Items </c-menu-item>
      <c-menu-item as="nuxt-link" :to="{ name:'admin-question' }">Questions</c-menu-item>
    </c-menu-group>
    <c-menu-divider />
    <c-menu-group title="Account">
      <c-menu-item>Settings</c-menu-item>
      <c-menu-item as="nuxt-link" to="/logout">Logout</c-menu-item>
    </c-menu-group>
  </c-menu-list>
</c-menu>
  </div>
</template>

<script>
export default {

}
</script>

<style>

</style>
