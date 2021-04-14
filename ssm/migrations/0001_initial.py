# Generated by Django 3.1.3 on 2021-04-14 00:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MailFields',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('form_name', models.CharField(blank=True, max_length=100, null=True)),
                ('form_subject', models.CharField(blank=True, max_length=100, null=True)),
                ('form_message', models.TextField(blank=True, max_length=700, null=True)),
                ('form_email', models.EmailField(blank=True, max_length=254, null=True)),
                ('sender_email', models.EmailField(max_length=254)),
                ('recipient_email', models.EmailField(max_length=254)),
                ('attachment', models.FileField(blank=True, null=True, upload_to='')),
                ('date_sent', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Mail Fields',
            },
        ),
    ]