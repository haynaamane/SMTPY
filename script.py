#smtp server
import sys
import smtplib

server=smtplib.SMTP("your_HOST",587)
server.ehlo()
server.starttls()

server.login('smtp_username','smtp_password')


try:
	subject='naamane.me'
	html = """\
this is HTML body
"""

	message= 'Subject: {}\n\n{}'.format(subject,html)

	server.sendmail("FROM_email",sys.argv[1],message)
	print('[SUCCESS] '+ sys.argv[1])
except Exception as e:
	print('[ERR] '+ sys.argv[1])

finally:
	server.quit()
