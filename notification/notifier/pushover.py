import httplib
import urllib
import re

__author__ = 'oker, alerticus'

class PushoverNotifier:

    PRIORITY_RE = re.compile('\[P:(-2|-1|0|1|2)\]')

    def notify(self, notification):
        params = {
          'token':    notification.user_to_notify.profile.pushover_app_key,
          'user':     notification.user_to_notify.profile.pushover_user_key,
          'message':  notification.message,
          'priority': self.priority(notification),
        }
        if params['priority'] == '2': # emergency
            params['retry']  = 42 # in seconds
            params['expire'] = 3600

        conn = httplib.HTTPSConnection("api.pushover.net:443")
        conn.request("POST", "/1/messages.json",
          urllib.urlencode(params), { "Content-type": "application/x-www-form-urlencoded" })
        status = conn.getresponse().status
        if status >= 200 and status < 300:
            print("Done")
        else:
            # todo: error handling
            print("Unable to connect.")

    # https://pushover.net/api#priority
    def priority(self, notification):
        match = PushoverNotifier.PRIORITY_RE.search(notification.message)
        if match is None:
            priority = '0'
        else:
            priority = match.groups()[0]
        return priority
