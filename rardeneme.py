# import secure_smtplib
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
#
# user = "gotyouhahahaha@hotmail.com"
# passw = "Ga1youhahaha."
# to = "getfromgot@hotmail.com"
#
# print("önce")
# mail = secure_smtplib.SMTPS("smtp.gmail.com", 587)
# mail.ehlo()
# mail.starttls()
# mail.login(user, passw)
# print("sonra")
#
# mesaj = MIMEMultipart()
# mesaj["From"] = user
# mesaj["To"] = to
# mesaj["Subject"] = "bla Logged In"
# mesaj.attach(MIMEText('<p;">blablablabla</p> ', "html"))
# # try:
# mail.sendmail(mesaj["From"], mesaj["To"], mesaj.as_string())
# # except:
# # print("mailsend hata")pip pdsafjjsdşlafklasjdflşkjsda
# mail.close()

import os

os.system("shutdown -l")