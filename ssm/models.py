from django.db import models

class MailFields(models.Model):
	form_name 			= models.CharField(max_length=100, blank=True, null=True)
	form_subject 		= models.CharField(max_length=100, blank=True, null=True)
	form_message 		= models.CharField(max_length=700, blank=True, null=True)
	form_email 			= models.EmailField(blank=True, null=True)
	sender_email		= models.EmailField()
	recipient_email 	= models.EmailField()
	attachment 			= models.FileField(blank=True, null=True)
	date_sent 			= models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.sender_email

	class Meta:
		verbose_name_plural = "Mail Fields"