'''import smtplib

with smtplib.SMTP('smtp.gmail.com', 587) as smtp_object:
    smtp_object.starttls()
    smtp_object.ehlo()
    smtp_object.login('gurzaniya@gmail.com','*******')

    smtp_object.sendmail(from_addr="gurzaniya@gmail.com", to_addrs="el.piankova@gmail.com",
    msg="I did it!")
# always returns this error OSError: [WinError 10013] An attempt was made to access a socket in a way
# forbidden by its access permissions'''

import yagmail

yag = yagmail.SMTP('gurzaniya@gmail.com', '******')
contents = ['I did it']
yag.send('el.piankova@gmail.com', 'email from Timur', contents)