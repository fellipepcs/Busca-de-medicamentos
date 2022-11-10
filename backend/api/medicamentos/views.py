from rest_framework import viewsets, status
from rest_framework.response import Response
from medicamentos.service import get_medicamentos


class MedicamentoViewSets(viewsets.ModelViewSet):

    def list(self, request, *args, **kwargs):
        try:
            medicamento = request.GET['medicamento']

            dados_medicamento = get_medicamentos(medicamento=medicamento)
            return Response(dados_medicamento, status=status.HTTP_200_OK)
        except Exception as error:
            return Response(str(error), status=status.HTTP_400_BAD_REQUEST)