from rest_framework import status
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.serializers import ValidationError
from api.queue_datastructure import Queue
from api.mensajes import send_message 
import json


queueF = Queue('FIFO')
queueL = Queue('LIFO')
"""
The MembersView will contain the logic on how to:
 GET, POST, PUT or delete family members
"""


class QueueView(APIView):
    def get(self, request):

        next = queueF.dequeue()
        result = str(next) + " , eres el siguiente en la lista"
        mynumber= "+56968422617"
        send_message(mynumber, result)
        return Response(json.dumps(result), status=status.HTTP_200_OK)

    def post(self, request):
       
            espera = queueF.size() - 2
            queueF.enqueue(json.loads(request.body)['name'])
            msg = "Ha sido agregado exitosamente a la cola! Su espera es de " + str(espera) + " persona(s)."
            mynumber= "+56968422617"
            send_message(mynumber, msg)
            result = msg
            return Response(json.dumps(result), status=status.HTTP_200_OK)

class QueueAllView(APIView):
    def get(self, request):

        result = queueF.get_all()
        return Response(json.dumps(result), status=status.HTTP_200_OK)