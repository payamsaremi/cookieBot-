<template>
    <div>
    <c-box
    m="5"
    p="5"
    rounded="md"
    bg="green.400"
    w="400px"
    color="white">
        <c-flex direction="column" align="left">
            <c-heading as="h1" size="lg" mb="4" align="left" fontSize="30px">
            {{heading}}
            </c-heading>
            <c-text font-size="xl">
            {{content}}
            </c-text>
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
