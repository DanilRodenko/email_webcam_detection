import smtplib
import imghdr
from email.message import EmailMessage

PASSWORD = "lgwuewjudetagnoh"
EMAIL = 'rodenko.d96@gmail.com'
RECIEVER = "rodenko.d96@gmail.com"
def send_email(image_path):
    email_message = EmailMessage()
    email_message["Subject"] = "New visitor"
    email_message.set_content("Hey, something was in your room")

    with open(image_path, 'rb') as file:
        content = file.read()
    email_message.add_attachment(content, maintype='image', subtype=imghdr.what(None, content))

    gmail = smtplib.SMTP("smtp.gmail.com", 587)
    gmail.starttls()
    gmail.ehlo()
    gmail.login(EMAIL, PASSWORD)
    gmail.sendmail(EMAIL, RECIEVER, email_message.as_string())
    gmail.quit()

if __name__ == "__main__":
    send_email(image_path="images/19.png")