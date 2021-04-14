from django.shortcuts import render
from django.http import HttpResponse
# API Function Based Imports
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
# Local imports
from .models import MailFields
from .serializers import MailFieldsSerializer
from django.core.mail import send_mail

#================================================
# Api Function Based-Views
#================================================
@api_view(['GET', 'POST'])
def index(request):

	if request.method == "GET":
		mail = MailFields.objects.all().order_by('-id')
		serializer = MailFieldsSerializer(mail, many=True)
		return Response(serializer.data)

	elif request.method =="POST":
		serializer = MailFieldsSerializer(data=request.data)

		if serializer.is_valid():
			serializer.save()
			# SENDING MAIL
			# Getting the newly created message
			new_message = serializer.data[0]
			# Getting all the fields
			form_name 		= new_message['form_name']
			form_subject	= new_message['form_subject']
			form_message 	= new_message['form_message']
			form_email 		= new_message['form_email']
			sender_email 	= new_message['sender_email']
			recipient_email = new_message['recipient_email']
			attachment 		= new_message['attachment']
			date_sent 		= date_sent['date_sent']

			# Equating Form fields to the send_mail
			subject 		= form_subject
			message 		= form_message
			email_from 		= send_mail
			recipient_list 	= [recipient_email]
			
			send_mail(subject, message, email_from, recipient_list, fail_silently=True)
			return Response(serializer.data, status=status.HTTP_201_CREATED)

		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

