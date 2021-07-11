<template>
    <div>
    <c-box p="5" my="20" mb="20" rounded="md" >
        <c-flex direction="column" align="center">
            <c-heading as="h1" size="2xl" mb="4" align="center" fontSize="50px">
            {{heading}}
            </c-heading>
            <c-text align="center" mx="5" mt="5" mb="10" font-size="xl">
            {{content}}
            </c-text>
            <c-button
            bg="green.400"
            color="white"
            size="lg"
            as="nuxt-link"
            to="order"
            >Start
            </c-button>
        </c-flex>
    </c-box>
    </div>
</template>

<script>
import { CBox } from '@chakra-ui/vue'
export default {
  props: ['heading', 'content'],
  components: {
    CBox
  }
}
</script>

<style>

</style>
