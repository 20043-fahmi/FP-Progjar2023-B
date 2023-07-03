import smtplib
from email.message import EmailMessage


def send_highscore_email(highscore, username, email):
    # Compose email message
    message = EmailMessage()
    message["Subject"] = "High Score Notification"
    # Replace with your email address
    message["From"] = "fahmi.muhazir.12@gmail.com"
    message["To"] = email
    print(email)

    body = f"Hello {username},\n\nCongratulations on achieving a new high score of {highscore} in the game!\n\nKeep up the good work!\n\nBest regards,\nYour Game Team"
    message.set_content(body)

    # Send the email
    with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
        smtp.starttls()
        # Replace with your email credentials
        smtp.login("fahmi.muhazir.12@gmail.com", "supbrpyzvddbpmxj")
        smtp.send_message(message)
