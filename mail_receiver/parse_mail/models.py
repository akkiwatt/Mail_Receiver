##--Author: Akshay Wattamwar--#
##--Date : 29/05/2017
## Create class for Email-Data Table 

##column which has indexing for faster access.
#--return_path
#--x_ses_spam_verdict
#--x_ses_virus_verdict
#--from_field
#--date
from __future__ import unicode_literals
from django.db import models
import datetime

class email_info(models.Model):
	return_path = models.CharField(db_index=True, max_length=2000,default='')
	received = models.CharField(max_length=2000,default='')
	x_ses_spam_verdict = models.CharField(db_index=True ,max_length=2000,default='')
	x_ses_virus_verdict = models.CharField(db_index=True ,max_length=2000,default='')
	received_spf = models.CharField(max_length=2000,default='')
	authentication_results = models.CharField(max_length=2000,default='')
	x_ses_receipt = models.CharField(max_length=2000,default='')
	x_ses_dkim_signature = models.CharField(max_length=2000,default='')
	dkim_signature = models.CharField(max_length=2000,default='')
	x_google_dkim_signature = models.CharField(max_length=2000,default='')
	x_gm_message_state = models.CharField(max_length=2000,default='')
	x_received = models.CharField(max_length=2000,default='')
	mime_version = models.CharField(max_length=2000,default='')
	in_reply_to = models.CharField(max_length=2000,default='')
	references = models.CharField(max_length=2000,default='')
	from_field = models.CharField(db_index=True,max_length=2000,default='')
	date = models.CharField(db_index=True, max_length=2000,default='')
	message_id = models.CharField(max_length=2000,default='')
	subject = models.CharField(max_length=2000,default='')
	to = models.CharField(max_length=2000,default='')
	content_type = models.CharField(max_length=2000,default='')
	def __str__(self):
	    return self.question_text

