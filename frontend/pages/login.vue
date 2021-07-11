<template>
  <div>
      <c-box
      mx="auto"
      w="300px"
      my="10"
      box-shadow="md"
      p="6"
      rounded="lg"
      justify-content="center">
        <c-box>
            <c-form-control>
            <c-form-label for="username">Username</c-form-label>
            <c-input v-model="user.username" type="text" id="username" aria-describedby="username-helper-text" />
            </c-form-control>

            <c-form-control mb="4">
            <c-form-label for="password">Password</c-form-label>
            <c-input @keyup.enter="login" v-model="user.password" type="password" id="password" aria-describedby="password-helper-text" />
            </c-form-control>

            <c-button @click="login">login</c-button>
        </c-box>
      </c-box>
  </div>
</template>

<script>
export default {
  data () {
    return {
      user: {}
    }
  },
  methods: {
    async login () {
      try {
        await this.$auth.loginWith('local', {
          data: this.user
        })
        console.log('sucsess login')
      } catch (err) {
        console.log('an error occured.')
      }
    }
  }
}
</script>

<style>

</style>
