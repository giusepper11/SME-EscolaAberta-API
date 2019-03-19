from django.shortcuts import render
from escolas.models import Escolas
from turmas.models import Turmas
from rest_framework.views import APIView
from django.db import connection
from rest_framework.response import Response


# Create your views here.


class ModalidadesPraticadas(APIView):

    def get(self, request, codesc, format=None):
        """

        :param request:
        :param codesc:
        :param format:
        :return:
        """
        query = """
        select turma.modal
        from turmas_turmas as turma
        group by turma.modal, turma.codesc
        having turma.codesc='{}'""".format(codesc)

        cursor = connection.cursor()
        cursor.execute(query)
        row = cursor.fetchall()
        modalidades = {'modalidade': [mod[0] for mod in row]}

        return Response(modalidades)

