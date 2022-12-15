import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

user = "hmt430@hotmail.com"
passw = "12a08h2001m"
to = "uygunfbahmet@hotmail.com"
mail = smtplib.SMTP('smtp-mail.outlook.com', 587)
mail.ehlo()
mail.starttls()
mail.login(user, passw)
mesaj = MIMEMultipart()
mesaj["From"] = user
mesaj["To"] = to
mesaj["Subject"] = " Logged In"

mesaj.attach(MIMEText('<p;">blablablabla</p> ', "html"))
# try:
mail.sendmail(mesaj["From"], mesaj["To"], mesaj.as_string())
# except:
# print("mailsend hata")
mail.close()