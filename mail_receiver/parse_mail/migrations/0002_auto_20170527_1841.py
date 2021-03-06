# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-27 18:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parse_mail', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='email_info',
            name='authentication_results',
            field=models.CharField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='email_info',
            name='dkim_signature',
            field=models.CharField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='email_info',
            name='received_spf',
            field=models.CharField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='email_info',
            name='x_google_dkim_signature',
            field=models.CharField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='email_info',
            name='x_ses_dkim_signature',
            field=models.CharField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='email_info',
            name='x_ses_receipt',
            field=models.CharField(max_length=2000),
        ),
    ]
