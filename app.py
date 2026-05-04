from flask import Flask, render_template, Response
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/export-ical")
def export_ical():
    import requests
from icalendar import Calendar

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


