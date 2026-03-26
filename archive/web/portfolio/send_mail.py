import smtplib, ssl, os

def send_mail(message):
    host = "smtp.gmail.com"
    port = 465

    google_app_username = os.getenv("GOOGLE_APP_USERNAME")
    google_app_password = os.getenv("GOOGLE_APP_PASSWORD")

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(google_app_username, google_app_password)
        server.sendmail(google_app_username, google_app_username, message)