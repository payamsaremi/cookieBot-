<template>
  <div>
    <c-box
    bg="gray.50"
    p="10"
    pb="20"
    align="left"
    w="100%"
    h="100%">
    <c-box :width="['100%', '100%' , 1 / 2 , 1 / 3]" >
      <c-heading mb="2" fontSize="40px">Near you</c-heading>
      <c-button mb="3" variant-color="green" right-icon="arrow-forward" variant="outline" size="sm">See more</c-button>
    </c-box>
    <c-simple-grid min-child-width="250px" :columns="2" spacing-y="20px" spacing-x="20px">
    <c-box justify-content="center" v-for="card in 6" :key="card"><ProductCard /></c-box>
    </c-simple-grid>
    </c-box>
  </div>
</template>

<script>
export default {

}
</script>

<style>

</style>
