import email
import imaplib
from email.header import decode_header


def mread(username, password, login):
    bod, sub, frm = "null", "null", "null"
    imap_server = "outlook.office365.com"

    imap = imaplib.IMAP4_SSL(imap_server)
    imap.login(username, password)

    status, messages = imap.select("INBOX")
    c = False
    messages = int(messages[0])
    for i in range(messages, 0, -1):
        res, msg = imap.fetch(str(i), "(RFC822)")
        for response in msg:
            if isinstance(response, tuple):
                msg = email.message_from_bytes(response[1])
                subject, encoding = decode_header(msg["Subject"])[0]
                if isinstance(subject, bytes):
                    try:
                        subject = str(subject.decode(encoding))
                    except:
                        None
                if login != str(subject).split(",")[0].lower():
                    continue
                From, encoding = decode_header(msg.get("From"))[0]
                if isinstance(From, bytes):
                    From = From.decode(encoding)
                frm = From
                sub = subject
                if msg.is_multipart():
                    for part in msg.walk():
                        content_type = part.get_content_type()
                        content_disposition = str(part.get("Content-Disposition"))
                        body = part.get_payload()
                        if content_type == "text/plain" and "attachment" not in content_disposition:
                            bod = body
                            c = True
        if c:
            imap.close()
            imap.logout()
            return frm, sub.lower(), bod.lower()
