import poplib, quopri
import random, md5
import sys, rfc822, StringIO
import email
from email.generator import Generator

user = "mygeneric.user19@gmail.com"
password = "pop34961064"
server = "pop.googlemail.com"

# connects
try:
    pop = poplib.POP3_SSL(server, '995')
except:
    print ("Erro ao se conectar com servidor")
    sys.exit(-1)

# user auth
try:
    print (pop.user(user))
    print (pop.pass_(password))
except:
    print ("Authentication error")
    sys.exit(-2)

# gets the mail list
mail_list = pop.list()[1]

for m in mail_list:
    mno, size = m.split()
    message = "\r\n".join(pop.retr(mno)[1])
    message = email.message_from_string(message)

    # uses the email flatten
    out_file = StringIO.StringIO()
    message_gen = Generator(out_file, mangle_from_=False, maxheaderlen=60)
    message_gen.flatten(message)
    message_text = out_file.getvalue()

    # fixes mime encoding issues (for display within html)
    clean_text = quopri.decodestring(message_text)

    msg = email.message_from_string(clean_text)

    # finds the last body (when in mime multipart, html is the last one)
    for part in msg.walk():
        if part.get_content_type():
            body = part.get_payload(decode=True)

    filename = "%s.email" % random.randint(1,100)

    email_file = open(filename, "w")

    email_file.write(msg["From"] + "\n")
    email_file.write(msg["Return-Path"] + "\n")
    email_file.write(msg["Subject"] + "\n")
    email_file.write(msg["Date"] + "\n")
    email_file.write(body)

    email_file.close()

pop.quit()
sys.exit()