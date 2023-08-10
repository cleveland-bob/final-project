#This is the app page

import gspread
from oauth2client.service_account import ServiceAccountCredentials
from flask import Flask, render_template, request, redirect

# Initialize Flask app
app = Flask(__name__)

# Google Sheets API setup
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/spreadsheets",
         "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
client = gspread.authorize(creds)
sheet = client.open("GolfScores").sheet1

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        hole = request.form["hole"]
        score = int(request.form["score"])
        putts = int(request.form["putts"])
        fairway = request.form["fairway"]

        # Log data in Google Sheet
        sheet.append_row([hole, score, putts, fairway])

        if int(hole) == 18:
            return redirect("/summary")
    
    return render_template("index.html")

@app.route("/summary")
def summary():
    data = sheet.get_all_values()
    return render_template("summary.html", data=data)

if __name__ == "__main__":
    app.run(debug=True)
