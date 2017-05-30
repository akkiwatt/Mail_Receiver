#---Author: Akshay Wattamwar
#---Date:   29/05/2017
#---Application Name: Mail Receiver 

#import field
import tempfile
import email
import os
import django
import time
from parse_mail.models import email_info
from watchdog.observers import Observer  
from watchdog.events import PatternMatchingEventHandler  

#Class Declaration and parsing logic for Email  
class MyHandler(PatternMatchingEventHandler):
    #accept only below mentioned format	
    patterns = ["*.txt", "*.csv","*.log"]
    def process(self, event):
	import email
	from parse_mail.models import email_info
        print event.src_path, event.event_type  
	if not event.is_directory:	
		path = event.src_path	
		input_file = open(path,'r')
  		content = input_file.read()
		msg = email.message_from_string(content)
		header_file=['Return-Path','Received','X-SES-Spam-Verdict','X-SES-Virus-Verdict','Received-SPF','Authentication-Results','X-SES-RECEIPT','X-SES-DKIM-SIGNATURE','DKIM-Signature','X-Google-DKIM-Signature','X-Gm-Message-State','X-Received','MIME-Version','In-Reply-To','References','From','Date','Message-ID','Subject','To','Content-Type']	
		for i in header_file:
			if i not in msg.keys():
				msg[i]=''
		flag =0;
		#check for values if any 
		for i in msg.values():
			if i!='':
				flag=1;
				break;
	    	if flag==1:
			q = email_info(return_path=msg['Return-Path'],received=msg['Received'],x_ses_spam_verdict=msg['X-SES-Spam-Verdict'],x_ses_virus_verdict=msg['X-SES-Virus-Verdict'],received_spf=msg['Received-SPF'],authentication_results=msg['Authentication-Results'],x_ses_receipt=msg['X-SES-RECEIPT']
		,x_ses_dkim_signature=msg['X-SES-DKIM-SIGNATURE'],dkim_signature=msg['DKIM-Signature'],x_google_dkim_signature=msg['X-Google-DKIM-Signature'],x_gm_message_state=msg['X-Gm-Message-State'],x_received=msg['X-Received'],mime_version=msg['MIME-Version'],in_reply_to=msg['In-Reply-To'],references=msg['References'],
		from_field=msg['From'],date=msg['Date'],message_id=msg['Message-ID'],subject=msg['Subject'],to=msg['To'],content_type=msg['Content-Type'])
			q.save()
		else:
			print "file does not have proper values"
	


    def on_created(self, event):
        self.process(event)

##---Create Object for observer---## 
observer = Observer()
observer.schedule(MyHandler(),tempfile.gettempdir())
observer.start()
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()

observer.join()















