from rest_framework import serializers
from .models import MailFields


class MailFieldsSerializer(serializers.ModelSerializer):
 	class Meta:
 		model 	= MailFields
 		fields 	= '__all__'




 	

