<template>
  <div id="app">
    <nav>
      <div class="nav-wrapper navbar-dark bg-primary">
        <h1 class="brand-logo center mt-3">Teste ProMáxima</h1>
      </div>
    </nav>
    <div class="container">
      <form class="mt-4" @submit.prevent="buscar()">
        <h5 >Digite o nome do medicamento abaixo:</h5>
        <input type="text" class="" placeholder="Nome do medicamento" v-model="medicamento.nome">
        <div v-if="errors">
          <p class="text-danger"> Nenhum medicamento encontrado!</p>
        </div>
        <button class="blue lighten-1 btn-small">Salvar<i class="material-icons left">save</i></button>
      </form>
      <div class="mt-4" v-if="medicamentos_null">
        <p class="row d-flex justify-content-center">Acesse o link abaixo para conferir as ofertas!</p>
        <table class="table table-bordered mt-4">
          <thead>
            <tr>
              <th>NOME DO REMÉDIO</th>
              <th>LINK</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="medicamento of lista_medicamentos">
              <td>{{ medicamento.Nome }}</td>
              <td><a>{{ medicamento.link }}</a></td>
              <td>
                <hr>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script>
import repositories from './services/repositories';

export default {
  name: 'app',
  data() {
    return {
      medicamento: {
        nome: '',
        link: ''
      },
      messages: [],
      lista_medicamentos: [],
      medicamentos_null: false,
      errors: false
    }
  },
  mounted() {
  },
  methods: {
    async buscar() {
      await repositories.listar(this.medicamento.nome).then(resposta => {
        this.lista_medicamentos = resposta.data
        this.medicamentos_null = true
        this.errors = false
      }).catch(e => {
        this.medicamentos_null = false
        this.errors = true
      })
    },
  }
}
</script>

<style scoped>
table {
  background-color: rgb(224, 255, 255);
}

header {
  background-color: rgb(247, 195, 195);
}
</style>
