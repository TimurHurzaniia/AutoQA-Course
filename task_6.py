import imaplib
'''Типа читает последнее письмо, но что за вид я не понял'''

def read_my_mail():
    from_mail = 'gurzaniya@gmail.com'
    pasword = '2786ZubastyGibon'
    server = 'imap.gmail.com'
    port = 993

    mail = imaplib.IMAP4_SSL(server)
    mail.login(from_mail, pasword)
    mail.select('inbox')
    result, data = mail.search(None, 'ALL')
    mail_ids = data[0]
    id_list = mail_ids.split()
    latest_email_id = id_list[-1]
    result, data = mail.fetch(latest_email_id, "(RFC822)")
    return result, data
print(read_my_mail())