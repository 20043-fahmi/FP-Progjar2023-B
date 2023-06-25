import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_congratulations_email(email, username, score):
    # Konfigurasi SMTP server
    smtp_server = 'smtp.example.com'
    smtp_port = 587
    smtp_username = 'your_username'
    smtp_password = 'your_password'

    # Pembentukan email
    sender_email = 'your_email@example.com'
    receiver_email = email
    subject = 'Selamat! Anda mencapai hightscore baru di permainan 2048!'
    body = f'Halo {username},\n\nSelamat! Anda telah mencapai skor tertinggi di permainan 2048. Skor Anda adalah {score}.\n\nTerima kasih telah bermain!\n\nSalam,\nTim Permainan 2048'

    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = subject

    message.attach(MIMEText(body, 'plain'))

    # Mengirim email
    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.ehlo()
            server.starttls()
            server.login(smtp_username, smtp_password)
            server.sendmail(sender_email, receiver_email, message.as_string())
        print('Email berhasil dikirim!')
    except smtplib.SMTPException as e:
        print('Email gagal dikirim:', e)


# Contoh penggunaan
"""
email = 'user@example.com'
username = 'John Doe'
score = 2048

send_congratulations_email(email, username, score)
"""
