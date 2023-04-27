from email.message import EmailMessage
import ssl, smtplib

sender_email = 'pythonwik@gmail.com'
sender_email_password = 'wtyjsnymuoaepmhq' 

def send_email(receiver_email, username, subject, message):
    body = "Dear " + username + "," + "\n\n" + message + "\n\nThe Python Wiki Team"

    em = EmailMessage()
    em['From'] = sender_email
    em['To'] = receiver_email
    em['Subject'] = subject
    em.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp: # (email server, port, context)
        smtp.login(sender_email, sender_email_password)
        smtp.sendmail(sender_email, receiver_email, em.as_string())
    return


receiver_email = 'dansammci@gmail.com'


username = 'DanielleMc'
subject = 'The Python Wiki'
message = 'Welcome to the Python Wiki hub 😎!'


send_email(receiver_email, username, subject, message)