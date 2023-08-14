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

@app.route("/final_routes", methods=["GET", "POST"])
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

@app.route('/golfstats')
def golfstats():
    csv_file_path = "stats.csv"
    avg_strokes, avg_putts, fairways_percentage = process_csv(csv_file_path)
    return render_template('golfstats.html', average_strokes=avg_strokes, average_putts=avg_putts, fairways_percentage=fairways_percentage)



def process_csv(file_path):
    total_strokes = 0
    total_putts = 0
    total_fairways_hit = 0
    total_holes = 0

    with open(file_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            total_strokes += int(row['strokes'])
            total_putts += int(row['putts'])
            total_fairways_hit += int(row['fairway'])
            total_holes += 1

    average_strokes_per_hole = total_strokes / total_holes
    average_putts_per_hole = total_putts / total_holes
    fairways_hit_percentage = (total_fairways_hit / total_holes) * 100

    return average_strokes_per_hole, average_putts_per_hole, fairways_hit_percentage

