from settings import *


BASE_URL = os.getenv('OPENDUTY_BASE_URL', "http://localhost")

XMPP_SETTINGS = {
    'user': os.getenv('OPENDUTY_XMPP_USER'),
    'password': os.getenv('OPENDUTY_XMPP_PASS'),
    'server': os.getenv('OPENDUTY_XMPP_SERVER', 'xmpp'),
    'port': os.getenv('OPENDUTY_XMPP_PORT', 5222),
}

EMAIL_SETTINGS = {
    'user': os.getenv('OPENDUTY_EMAIL_USER'),
    'password': os.getenv('OPENDUTY_EMAIL_PASS'),
}

'''
TWILIO_SETTINGS = {
    'SID': "TWILIO_ACCOUNT_SID",
    'token': "TWILIO_ACCOUNT_TOKEN",
    'phone_number': "your_twilio_phone_number",
    'sms_number': "your_twilio_sms_number",
    'twiml_url': "http://www.website.org/voice.xml"
}
'''

SLACK_SETTINGS = {
    'apikey': os.getenv('OPENDUTY_SLACK_APIKEY', "YOUR_SLACK_API_KEY")
}

'''
PROWL_SETTINGS = {
    'priority': 0
    'application': 'openduty'
}
'''

DATABASES = {
    'default': {
        'ENGINE': os.getenv('OPENDUTY_DATABASE_ENGINE', 'django.db.backends.mysql'),
        'NAME': os.getenv('OPENDUTY_DATABASE_NAME', 'openduty'),
        'USER': os.getenv('OPENDUTY_DATABASE_USER', 'openduty'),
        'PASSWORD': os.getenv('OPENDUTY_DATABASE_PASS', 'dutyfree'),
        'HOST': os.getenv('OPENDUTY_DATABASE_HOST', 'db'),
        'PORT': os.getenv('OPENDUTY_DATABASE_PORT', '3306')
    }
}

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('OPENDUTY_SECRET_KEY', 'yoursecretkey')

ALLOWED_HOSTS = ['your.dutyfree.host']

DEBUG = os.getenv('OPENDUTY_DEBUG', False)
TEMPLATE_DEBUG = os.getenv('OPENDUTY_TEMPLATE_DEBUG', False)
