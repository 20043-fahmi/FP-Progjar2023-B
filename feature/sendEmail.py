import smtplib
import pyscreenshot
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.message import EmailMessage
import os.path


def send_highscore_email(highscore, username, email):
    image = pyscreenshot.grab()
    image.save('ss.jpg', 'jpeg')
    # Compose email message (multipart of text + image screenshot)
    message = MIMEMultipart()
    message["Subject"] = "High Score Notification"
    # Replace with your email address
    message["From"] = "kodokpu@gmail.com"
    message["To"] = email
    print("send to }"+email)
    
    file_ss = 'ss.jpg'
    with open(file_ss, 'rb') as f:
        img_data = f.read()
    text = MIMEText("Hello {username},\n\nCongratulations on achieving a new high score of {highscore} in the game!\n\nKeep up the good work!\n\nBest regards,\nYour Game Team")
    message.attach(text)
    image = MIMEImage(img_data, name=os.path.basename(file_ss))
    message.attach(image)

    # Send the email
    with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
        smtp.starttls()
        # Replace with your email credentials
        smtp.login("kodokpu@gmail.com", "qghrbsoftvsbfleq")
        smtp.send_message(message)
