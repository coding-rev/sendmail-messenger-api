from django.contrib import admin
from .models import MailFields

# Customizing parts of the Admin page
admin.site.site_title 	= "Simply Send Mail"
admin.site.site_header	= "Simply Send Mail"

# Customizing Models display in admin
class MailFieldAdmin(admin.ModelAdmin):
	list_display = ['sender_email', 'recipient_email', 'form_subject']

# Registering models
admin.site.register(MailFields, MailFieldAdmin)




