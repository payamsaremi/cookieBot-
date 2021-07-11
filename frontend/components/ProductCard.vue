<template>
  <div>
    <c-box
    maxW="sm"
    border-width="1px"
    shadow="md"
    rounded="sm"
    overflow="hidden"
    >
    <c-image size="sm" h="250px" objectFit="cover" :src="property.imageUrl" :alt="property.imageAlt" />
    <c-box p="6">
      <c-box d="flex" align-items="baseline">
        <c-badge rounded="full" px="2" variant-color="green">
          New
        </c-badge>
        <c-box
          color="gray.500"
          font-weight="semibold"
          letter-spacing="wide"
          font-size="xs"
          text-transform="uppercase"
          ml="2"
        >
           Low Carb &bull; {{ property.cookiesAmount }} cookies in a box
        </c-box>
      </c-box>
      <c-box
        mt="1"
        font-weight="semibold"
        as="h4"
        line-height="tight"
        is-truncated
      >
        {{ property.title }}
      </c-box>
      <c-box>
        {{ property.formattedPrice }}
        <c-box as="span" color="gray.600" fontSize="sm">
          / Box
        </c-box>
      </c-box>
      <c-box d="flex" mt="2" align-items="center">
        <c-icon
          v-for="(_, i) in Array(5).fill('')"
          name="star"
          :key="i"
          :color="i < property.rating ? 'green.500' : 'gray.300'"
        />
        <c-box as="span" ml="2" color="gray.600" font-size="sm">
          {{ property.reviewCount }} reviews
        </c-box>
      </c-box>
      <c-button w="100%" mt="4" >Order</c-button>
    </c-box>
  </c-box>
  </div>
</template>

<script>
export default {
  data () {
    return {
      property: {
        imageUrl: 'https://handletheheat.com/wp-content/uploads/2013/10/Soft-Chocolate-Chip-Cookies-SQUARE.jpg',
        imageAlt: 'My robotMade cookies',
        beds: 3,
        cookiesAmount: 6,
        title: 'Chocolate Chip Cookies With Chocolate Chunks',
        formattedPrice: '$1,900.00',
        reviewCount: 34,
        rating: 4
      }
    }
  }
}
</script>

<style>

</style>
