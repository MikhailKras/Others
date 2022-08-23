import imaplib
mail_server = 'mail'
IMAP_server = {'yahoo': 'imap.mail.yahoo.com', 'mail': 'imap.mail.ru'}
mail_id = {'mail': 'kras2011@mail.ru', 'yahoo': 'kras2011@yahoo.com'}
password = {'yahoo': 'zhjdwtpgihacibfr', 'mail': '3C3q8qMVDaAsqGxtmug1'}
IMAP_server, mail_id, password = IMAP_server[mail_server], mail_id[mail_server], password[mail_server]
with imaplib.IMAP4_SSL(IMAP_server, port=993) as mail:
    try:
        status, summary = mail.login(mail_id, password)
        if status == 'OK':
            print(summary)
    except imaplib.IMAP4.error:
        print("Error logging into Mail")
    status, mailboxes = mail.list()
    if status == "OK":
        print("***List of mailboxes***")
        for index, mailbox in enumerate(mailboxes):
            print(index, mailbox)
    else:
        print("Error retreiving mailbox information - {}".format(status))
    status, data = mail.select('email_parsing')
    if status == "OK":
        print(data, status)
    else:
        print("This mailbox doesn't exist")
    msg = mail.search('utf-8', 'SUBJECT', '"LDJ"')
    print(msg)




