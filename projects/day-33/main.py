import requests
import datetime
import smtplib

MYLAT = 19.075983
MYLONG = 72.877655


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_lat = float(data['iss_position']['latitude'])
    iss_lng = float(data['iss_position']['longitude'])
    if MYLAT - 5 <= iss_lat <= MYLAT + 5 and MYLONG - 5 <= iss_lng <= MYLONG + 5:
            return True

def is_night():
        parameters = {
            'lat': MYLAT,
            'lng': MYLONG,
        }

        response = requests.get(url ="https://api.sunrise-sunset.org/v2",params= parameters)
        response.raise_for_status()
        data = response.json()
        sunrise = data['sunrise'].split('T')[1].split(':')[0]
        sunset = data['sunset'].split('T')[1].split(':')[0]
        time_now = datetime.datetime.now().hour

        if time_now >= int(sunset) and time_now <= int(sunrise):
            return True

if is_iss_overhead() and is_night():
    connection = smtplib.SMTP('smtp.gmail.com')
    connection.starttls()
    connection.login('', '')
    connection.sendmail(
        from_addr='',
        to_addrs='',
        msg="subject: look up \n\n is iss is above you in the sky."
    )


