from flask import Flask, render_template, Response
import requests
from icalendar import Calendar, Event
from datetime import datetime

app = Flask(__name__)

# ------------------------------
# PAGE D'ACCUEIL
# ------------------------------
@app.route("/")
def home():
    return render_template("index.html")


# ------------------------------
# EXPORT ICAL (ANCIEN - OPTIONNEL)
# ------------------------------
@app.route("/export-ical")
def export_ical():
    ical = """BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//Location Calendrier//FR
BEGIN:VEVENT
UID:1
DTSTAMP:20240503T120000Z
DTSTART:20240510T120000Z
DTEND:20240515T120000Z
SUMMARY:Réservation test
END:VEVENT
END:VCALENDAR"""
    return Response(ical, mimetype="text/calendar")


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
            start = component.get('dtstart').dt
            end = component.get('dtend').dt

            reservations.append({
                "start": start.isoformat(),
                "end": end.isoformat(),
                "summary": "Reserved"
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
            start = component.get('dtstart').dt
            end = component.get('dtend').dt

            reservations.append({
                "start": start.isoformat(),
                "end": end.isoformat(),
                "summary": "Reserved"
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


# ------------------------------
# EXPORT ICAL APPARTEMENT 133 (.ics)
# ------------------------------
@app.route('/export-ical-app1.ics')
def export_ical_app1_ics():
    data = requests.get("https://location-calendrier-1.onrender.com/import-airbnb-app1").json()
    reservations = data.get("reservations", [])

    cal = Calendar()
    cal.add('prodid', '-//Jardin dEden 133//mxm.dk//')
    cal.add('version', '2.0')

    for r in reservations:
        event = Event()
        event.add('summary', 'Reserved')
        event.add('dtstart', datetime.fromisoformat(r["start"]))
        event.add('dtend', datetime.fromisoformat(r["end"]))
        cal.add_component(event)

    return cal.to_ical(), 200, {
        'Content-Type': 'text/calendar',
        'Content-Disposition': 'attachment; filename="appartement133.ics"'
    }


# ------------------------------
# EXPORT ICAL APPARTEMENT 206 (.ics)
# ------------------------------
@app.route('/export-ical-app2.ics')
def export_ical_app2_ics():
    data = requests.get("https://location-calendrier-1.onrender.com/import-airbnb-app2").json()
    reservations = data.get("reservations", [])

    cal = Calendar()
    cal.add('prodid', '-//Jardin dEden 206//mxm.dk//')
    cal.add('version', '2.0')

    for r in reservations:
        event = Event()
        event.add('summary', 'Reserved')
        event.add('dtstart', datetime.fromisoformat(r["start"]))
        event.add('dtend', datetime.fromisoformat(r["end"]))
        cal.add_component(event)

    return cal.to_ical(), 200, {
        'Content-Type': 'text/calendar',
        'Content-Disposition': 'attachment; filename="appartement206.ics"'
    }
