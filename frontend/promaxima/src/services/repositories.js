import { http } from './config'

export default {

	listar: (medicamento) => {
		return http.get(`/medicamentos/?medicamento=${medicamento}`)
	},
}