#This is the app page

import gspread
from oauth2client.service_account import ServiceAccountCredentials
from flask import Flask, render_template, request, redirect

# Initialize Flask app
app = Flask(__name__)

@app.route("/final_routes", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        hole = request.form["hole"]
        score = int(request.form["score"])
        putts = int(request.form["putts"])
        fairway = request.form["fairway"]

        # Write data into CSV file
        with open('stats.csv', 'a', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow([round_id, strokes, putts, fairway])

        if int(hole) == 18:
            return redirect("/summary")
    
    return render_template("index.html")

@app.route("/summary")
def summary():
    # You can still read data from the CSV file if needed
    with open('stats.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        data = list(csv_reader)
    
    return render_template("summary.html", data=data)

if __name__ == "__main__":
    app.run(debug=True)

@app.route('/golfstats')
def golfstats():
    csv_file_path = "stats.csv"
    avg_strokes, avg_putts, fairways_percentage = process_csv(csv_file_path)
    return render_template('golfstats.html', average_strokes=avg_strokes, average_putts=avg_putts, fairways_percentage=fairways_percentage)



def process_csv(csv_file_path):
    total_strokes = 0
    total_putts = 0
    total_fairways_hit = 0
    total_holes = 0

    with open('stats.csv', 'r') as csvfile:
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

