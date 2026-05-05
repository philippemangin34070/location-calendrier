from flask import Flask, render_template, Response
import requests
from icalendar import Calendar

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

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

@app.route("/import-airbnb")
def import_airbnb():
    url = "https://www.airbnb.fr/calendar/ical/1408690958278432453.ics?t=a818b992302442ebbba047191301735f"
    r = requests.get(url)
    cal = Calendar.from_ical(r.text)

    events = []
    for component in cal.walk():
        if component.name == "VEVENT":
            events.append({
                "start": component.get("DTSTART").dt,
                "end": component.get("DTEND").dt,
                "summary": str(component.get("SUMMARY"))
            })

    return {"reservations": events}

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
            summary = str(component.get('summary'))

            reservations.append({
                "start": start.isoformat(),
                "end": end.isoformat(),
                "summary": summary
            })

    return {"reservations": reservations}

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
            summary = str(component.get('summary'))

            reservations.append({
                "start": start.isoformat(),
                "end": end.isoformat(),
                "summary": summary
            })

    return {"reservations": reservations}

@app.route('/calendrier1')
def calendrier1():
    return render_template('calendrier1.html')

@app.route('/calendrier2')
def calendrier2():
    return render_template('calendrier2.html')



