from flask import Flask, jsonify, send_from_directory
import sqlite3

app = Flask(__name__)
DB_NAME = "pathfinder.db"

def query_db(query, args=(), one=False):
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute(query, args)
    rv = cursor.fetchall()
    conn.close()
    return (rv[0] if rv else None) if one else rv

@app.route("/")
def index():
    return send_from_directory('.', 'index.html')

@app.route("/api/k12")
def api_k12():
    rows = query_db("SELECT name, school_type, county, grades, total_students, website FROM k12_schools")
    return jsonify([dict(row) for row in rows])

@app.route("/api/private")
def api_private():
    rows = query_db("SELECT name, city, county, grades, total_students, website FROM private_schools")
    return jsonify([dict(row) for row in rows])

@app.route("/api/decal")
def api_decal():
    rows = query_db("SELECT title, city, county, phone, caps_subsidized, program_type, website FROM after_school_programs")
    return jsonify([dict(row) for row in rows])

@app.route("/api/usg")
def api_usg():
    rows = query_db("SELECT name, category, city, annual_tuition, annual_fees, website FROM usg_institutions")
    return jsonify([dict(row) for row in rows])

@app.route("/api/careers")
def api_careers():
    careers = [
        {
            "title": "Computer Science & Software Engineering",
            "category": "Technology",
            "avg_ga_salary": 115000,
            "key_credential": "AWS Certified Developer / Python & C Mastery",
            "links": [
                {"name": "Georgia Tech (College of Computing)", "url": "https://www.cc.gatech.edu/"},
                {"name": "University of Georgia (CS)", "url": "https://cs.uga.edu/"},
                {"name": "Georgia State University (Computer Science)", "url": "https://cs.gsu.edu/"},
                {"name": "Kennesaw State University (CCSE)", "url": "https://ccse.kennesaw.edu/"}
            ]
        },
        {
            "title": "Data Analytics & Business Intelligence",
            "category": "Technology & Analytics",
            "avg_ga_salary": 85000,
            "key_credential": "Google Data Analytics / SQL / Power BI",
            "links": [
                {"name": "GSU Robinson CIS Program", "url": "https://robinson.gsu.edu/information-systems/"},
                {"name": "Atlanta Metropolitan State College", "url": "https://www.atlm.edu"},
                {"name": "Kennesaw State University (Data Science)", "url": "https://www.kennesaw.edu/"}
            ]
        },
        {
            "title": "Game Design & Interactive Entertainment",
            "category": "Creative Media & Gaming",
            "avg_ga_salary": 79000,
            "key_credential": "Unity / Unreal Engine Certified Developer",
            "links": [
                {"name": "Georgia State University (CMII)", "url": "https://cmii.gsu.edu/"},
                {"name": "Kennesaw State University (Digital Animation)", "url": "https://www.kennesaw.edu/"},
                {"name": "SCAD (Interactive Design)", "url": "https://www.scad.edu/"}
            ]
        },
        {
            "title": "Commercial & Fine Art Photography",
            "category": "Creative Arts & Media",
            "avg_ga_salary": 61000,
            "key_credential": "Digital Imaging Specialist TCC / Adobe Certified",
            "links": [
                {"name": "Gwinnett Technical College", "url": "https://gwinnetttech.edu/"},
                {"name": "North Georgia Technical College", "url": "https://northgatech.edu/"},
                {"name": "SCAD (Photography)", "url": "https://www.scad.edu/academics/majors/photography"}
            ]
        },
        {
            "title": "Cybersecurity & Network Defense",
            "category": "Information Security",
            "avg_ga_salary": 96000,
            "key_credential": "CompTIA Security+ / CISSP / Network+",
            "links": [
                {"name": "Augusta University (Cyber Institute)", "url": "https://www.augusta.edu/ccs/"},
                {"name": "Kennesaw State University (InfoSec)", "url": "https://www.kennesaw.edu/"},
                {"name": "Georgia Southern University", "url": "https://www.georgiasouthern.edu/"}
            ]
        },
        {
            "title": "Registered Nursing (B.S.N. & ASN)",
            "category": "Healthcare",
            "avg_ga_salary": 84000,
            "key_credential": "Registered Nurse (RN) Licensure / BLS",
            "links": [
                {"name": "Augusta University (College of Nursing)", "url": "https://www.augusta.edu/nursing/"},
                {"name": "Georgia State University (School of Nursing)", "url": "https://snhp.gsu.edu/"},
                {"name": "Georgia Southern University (Nursing)", "url": "https://www.georgiasouthern.edu/nursing/"}
            ]
        }
    ]
    return jsonify(careers)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
