import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

fromaddr = 'youremail'
recipients = ["receiver@abc.com", "receiver@abc.com", "receiver@abc.com"]
toaddr = ', '.join(recipients)

msg = MIMEMultipart()

msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Python: Test email with attachment"

body = "Hello, " \
       "This is a simple mail. There is only text, no attachments are there The mail is sent using Python SMTP library"

msg.attach(MIMEText(body, 'plain'))

filename = "titanic.csv"
attachment = open("yourattachmenthere", "rb")

part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

msg.attach(part)

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, "yourpassword")
text = msg.as_string()
server.sendmail(fromaddr, recipients, text)
server.quit()
print('Mail Sent')