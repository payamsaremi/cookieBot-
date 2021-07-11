<template>
  <div>
    <c-box m="3">
      <c-heading>Questions</c-heading>
      <c-button>Add Question</c-button>
      <c-box bg="red.50" v-for="q in questions" :key="q.id">
          {{q.text}}
          <c-button @click="loadQuestion(q)">edit</c-button>
          <c-box bg="green.100" p="1" v-for="c in q.choices" :key="c.id">
            {{c.text}}
          </c-box>
      </c-box>
          <c-box v-if="editable">
            <c-form-control>
              <c-form-label for="question">question</c-form-label>
              <c-input v-model="question.text" type="text" id="question" />
            </c-form-control>
            <c-form-control>
              <c-form-label for="choices">choices</c-form-label>
              <div
              v-for="choice in question.choices"
              :key="choice.id"
              >
              {{choice}}
              <c-input
              v-model="choice.text"
              type="text"
              :id="choice.id"/>
              </div>
            </c-form-control>
            <c-button @click="save">save</c-button>
          </c-box>
    </c-box>
  </div>
</template>

<script>
export default {
  data () {
    return {
      questions: [],
      editable: false,
      choices: null,
      question: {
        creation_date: new Date().toISOString(),
        choices: []
      }
    }
  },
  async fetch () {
    this.questions = await this.$axios.$get('/api/pools')
  },
  methods: {
    async save () {
      const method = this.question.id ? 'put' : 'post'
      const id = this.question.id ? `${this.question.id}/` : ''
      const url = `/api/pools/${id}`
      try {
        await this.$axios[method](url, this.question)
        this.editable = false
        alert('saved succesfuly')
        this.$fetch()
      } catch (err) {
        console.log(err)
      }
    },
    loadQuestion (question) {
      this.editable = true
      this.question = {
        id: question.id,
        text: question.text,
        creation_date: question.creation_date,
        start_date: new Date(question.start_date),
        end_date: new Date(question.end_date),
        choices: question.choices
      }
    }
  }
}
</script>

<style>

</style>
