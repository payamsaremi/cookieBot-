<template>
  <div>
      <c-box align="center" my="10">
          <c-heading mb="5" size="md">Are your sure, you want to logout?</c-heading>
           <c-button mr="2" as="nuxt-link" to="/">cancel</c-button>
          <c-button variant-color="red" @click="logout">confirm</c-button>
      </c-box>
  </div>
</template>

<script>
export default {
  methods: {
    async logout () {
      await this.$auth.logout()
    }
  }
}
</script>

<style>

</style>
