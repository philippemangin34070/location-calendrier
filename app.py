from flask import Flask, request, jsonify, Response
from datetime import date, datetime
import uuid

app = Flask(__name__)

# Base de données en mémoire
bookings = []

def parse_date(d):
    return datetime.strptime(d, "%Y-%m-%d").date()

def is_available(start, end):
    for b in bookings:
        if not (end <= b["start_date"] or start >= b["end_date"]):
            return False
    return True

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")
    from flask import Response
from datetime import datetime

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


@app.route("/book", methods=["POST"])
def book():
    data = request.json
    start = parse_date(data["start_date"])
    end = parse_date(data["end_date"])

    if end <= start:
        return jsonify({"error": "Dates invalides"}), 400

    if not is_available(start, end):
        return jsonify({"error": "Déjà réservé sur cette période"}), 409

    booking = {
        "id": str(uuid.uuid4()),
        "start_date": start,
        "end_date": end,
        "source": data.get("source", "direct")
    }
    bookings.append(booking)
    return jsonify(booking), 201

def to_ical_date(d: date) -> str:
    return d.strftime("%Y%m%d")

@app.route("/calendar.ics", methods=["GET"])
def export_ical():
    lines = [
        "BEGIN:VCALENDAR",
        "VERSION:2.0",
        "PRODID:-//MonSite//LocationVacances//FR"
    ]

    for b in bookings:
        uid = b["id"]
        dtstart = to_ical_date(b["start_date"])
        dtend = to_ical_date(b["end_date"])
        lines.extend([
            "BEGIN:VEVENT",
            f"UID:{uid}",
            f"DTSTART;VALUE=DATE:{dtstart}",
            f"DTEND;VALUE=DATE:{dtend}",
            "SUMMARY:Réservation location",
            "END:VEVENT"
        ])

    lines.append("END:VCALENDAR")
    ical_content = "\r\n".join(lines)

    return Response(ical_content, mimetype="text/calendar")

if __name__ == "__main__":
    app.run()
