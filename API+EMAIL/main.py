import sys
import requests
import json
import smtplib
from email.mime.text import MIMEText

def check_email(email):
    if '@' in email and '.' in email:
        return True
    else:
        return False

def get_weather():
    city = 'Helsink'
    api_key = 'YOUR_API_KEY_HERE'
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=imperial'.format(city, api_key)
    response = requests.get(url)
    data = json.loads(response.text)
    return data['main']['temp'], data['weather'][0]['description']

def send_email(email, message):
    gmail_user = 'YOUR_GMAIL_ADDRESS_HERE'
    gmail_password = 'YOUR_GMAIL_PASSWORD_HERE'
    recipient = email

    msg = MIMEText(message)
    msg['Subject'] = 'Weather update for New York'
    msg['From'] = gmail_user
    msg['To'] = recipient

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(gmail_user, gmail_password)
        server.sendmail(gmail_user, recipient, msg.as_string())
        server.close()
        print('Email sent successfully!')
    except:
        print('Something went wrong while sending the email.')

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: python program_name.py email_address api_choice')
        sys.exit()

    email = sys.argv[1]
    api_choice = sys.argv[2]

    if not check_email(email):
        print('Invalid email format.')
        sys.exit()

    if api_choice not in ['weather', 'another_api_choice']:
        print('Invalid API choice.')
        sys.exit()

    if api_choice == 'weather':
        temperature, description = get_weather()
        message = 'The temperature in New York is {}F with {}.'.format(temperature, description)
    else:
        # call the other API

        try:
         send_email(email, message)
        except:
            print('Something went wrong while sending the email.')

