# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-28 15:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parse_mail', '0004_auto_20170527_1957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='email_info',
            name='authentication_results',
            field=models.CharField(default='', max_length=2000),
        ),
        migrations.AlterField(
            model_name='email_info',
            name='content_type',
            field=models.CharField(default='', max_length=2000),
        ),
        migrations.AlterField(
            model_name='email_info',
            name='date',
            field=models.CharField(default='', max_length=2000),
        ),
        migrations.AlterField(
            model_name='email_info',
            name='dkim_signature',
            field=models.CharField(default='', max_length=2000),
        ),
        migrations.AlterField(
            model_name='email_info',
            name='from_field',
            field=models.CharField(default='', max_length=2000),
        ),
        migrations.AlterField(
            model_name='email_info',
            name='in_reply_to',
            field=models.CharField(default='', max_length=2000),
        ),
        migrations.AlterField(
            model_name='email_info',
            name='message_id',
            field=models.CharField(default='', max_length=2000),
        ),
        migrations.AlterField(
            model_name='email_info',
            name='mime_version',
            field=models.CharField(default='', max_length=2000),
        ),
        migrations.AlterField(
            model_name='email_info',
            name='received',
            field=models.CharField(default='', max_length=2000),
        ),
        migrations.AlterField(
            model_name='email_info',
            name='received_spf',
            field=models.CharField(default='', max_length=2000),
        ),
        migrations.AlterField(
            model_name='email_info',
            name='references',
            field=models.CharField(default='', max_length=2000),
        ),
        migrations.AlterField(
            model_name='email_info',
            name='return_path',
            field=models.CharField(default='', max_length=2000),
        ),
        migrations.AlterField(
            model_name='email_info',
            name='subject',
            field=models.CharField(default='', max_length=2000),
        ),
        migrations.AlterField(
            model_name='email_info',
            name='to',
            field=models.CharField(default='', max_length=2000),
        ),
        migrations.AlterField(
            model_name='email_info',
            name='x_gm_message_state',
            field=models.CharField(default='', max_length=2000),
        ),
        migrations.AlterField(
            model_name='email_info',
            name='x_google_dkim_signature',
            field=models.CharField(default='', max_length=2000),
        ),
        migrations.AlterField(
            model_name='email_info',
            name='x_received',
            field=models.CharField(default='', max_length=2000),
        ),
        migrations.AlterField(
            model_name='email_info',
            name='x_ses_dkim_signature',
            field=models.CharField(default='', max_length=2000),
        ),
        migrations.AlterField(
            model_name='email_info',
            name='x_ses_receipt',
            field=models.CharField(default='', max_length=2000),
        ),
        migrations.AlterField(
            model_name='email_info',
            name='x_ses_spam_verdict',
            field=models.CharField(default='', max_length=2000),
        ),
        migrations.AlterField(
            model_name='email_info',
            name='x_ses_virus_verdict',
            field=models.CharField(default='', max_length=2000),
        ),
    ]