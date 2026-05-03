from flask import Flask, render_template, Response
from datetime import datetime

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
