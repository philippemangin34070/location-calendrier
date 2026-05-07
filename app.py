from flask import Flask, render_template
import requests
from icalendar import Calendar

app = Flask(__name__)

# ------------------------------
# PAGE D'ACCUEIL
# ------------------------------
@app.route("/")
def home():
    return render_template("index.html")


# ------------------------------
# IMPORT AIRBNB APPARTEMENT 133
# ------------------------------
@app.route('/import-airbnb-app1')
def import_airbnb_app1():
    url = "https://www.airbnb.fr/calendar/ical/1408690958278432453.ics?t=a818b992302442ebbba047191301735f"
    r = requests.get(url)
    cal = Calendar.from_ical(r.text)

    reservations = []
    for component in cal.walk():
        if component.name == "VEVENT":
            reservations.append({
                "start": component.get('dtstart').dt.isoformat(),
                "end": component.get('dtend').dt.isoformat(),
                "title": "Reserved"
            })

    return {"reservations": reservations}


# ------------------------------
# IMPORT AIRBNB APPARTEMENT 206
# ------------------------------
@app.route('/import-airbnb-app2')
def import_airbnb_app2():
    url = "https://www.airbnb.fr/calendar/ical/1421524208515391594.ics?t=dd3c5e79416d4e0392881fcf9b0bde58"
    r = requests.get(url)
    cal = Calendar.from_ical(r.text)

    reservations = []
    for component in cal.walk():
        if component.name == "VEVENT":
            reservations.append({
                "start": component.get('dtstart').dt.isoformat(),
                "end": component.get('dtend').dt.isoformat(),
                "title": "Reserved"
            })

    return {"reservations": reservations}


# ------------------------------
# PAGES DES CALENDRIERS
# ------------------------------
@app.route('/calendrier1')
def calendrier1():
    return render_template('calendrier1.html')

@app.route('/calendrier2')
def calendrier2():
    return render_template('calendrier2.html')
