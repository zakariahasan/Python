import smtplib
import os
EMAIL_ADDRESS = os.environ.get("mail_user")
EMAIL_PASSWORD = os.environ.get("mail_pass")
with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    subject = "Testing"
    body ="Hello there"

    msg = f"Subject:{subject}\n\n{body}"

    smtp.sendmail(EMAIL_ADDRESS, "zakaria.hasan199@gmail.com", msg)
