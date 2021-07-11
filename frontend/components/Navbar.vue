<template>
  <div>
    <c-box box-shadow="lg" p="3">
    <c-flex align="center" justify-content="flex-end">
      <c-heading size="md" mr="auto"><nuxt-link to="/">Logo</nuxt-link></c-heading>
        <c-icon-button
        variant-color="vue"
        aria-label="Call Jonathan"
        size="md"
        icon="phone"
        />
        <c-box ml="2" v-if="loggedIn"><Menu/></c-box>
      <c-box v-if="!loggedIn">
        <c-button
        ml="2"
        right-icon="arrow-forward"
        variant-color="green"
        variant="outline"
        rounded="lg"
        >Start
        </c-button>
      </c-box>
    </c-flex>
  </c-box>
  </div>
</template>

<script>
import { mapState } from 'vuex'
export default {
  computed: {
    ...mapState('auth', ['loggedIn'])
  }
}
</script>

<style>

</style>
