#This is the core app functionality code


#Import CSV and Import Flask Functions
import csv
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

#Write the entered statsitics into the stats.csv file

def write_to_csv(data):
    with open('stats.csv', 'a', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(data)

#Get and post the entered stats from the "hello" page
@app.route("/", methods=["GET", "POST"])
def index():
    message = None  # Initialize a message variable

    if request.method == "POST":
        hole = request.form["hole"]
        score = int(request.form["score"])
        putts = int(request.form["putts"])
        fairway = request.form["fairway"]

        data = [hole, score, putts, fairway]
        write_to_csv(data)

        if int(hole) == 18:
            return redirect("/")
        else:
            message = "Success! Data submitted for hole {}".format(hole)

    return render_template("golfstats.html", message=message)

if __name__ == '__main__':
    app.run(debug=True)


#Read from the stats.csv file 

@app.route("/golfstats")
def summary():
    round_data = {}  # Dictionary to store aggregate statistics for each round

    with open('stats.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)  # Skip the header row
        for row in csv_reader:
            round_id = int(row[0])
            strokes = int(row[1])
            putts = int(row[2])
            fairway = int(row[3])

            if round_id not in round_data:
                round_data[round_id] = {'strokes': [], 'putts': [], 'fairway': []}
            
            round_data[round_id]['strokes'].append(strokes)
            round_data[round_id]['putts'].append(putts)
            round_data[round_id]['fairway'].append(fairway)
 
 # Calculate aggregate statistics for each round
    aggregated_stats = []
    for round_id, stats in round_data.items():
        avg_strokes = sum(stats['strokes']) / len(stats['strokes'])
        avg_putts = sum(stats['putts']) / len(stats['putts'])
        fairways_hit_percentage = (sum(stats['fairway']) / len(stats['fairway'])) * 100
        aggregated_stats.append({
            'round_id': round_id,
            'average_strokes_per_hole': avg_strokes,
            'average_putts_per_hole': avg_putts,
            'fairways_hit_percentage': fairways_hit_percentage
        })

    return render_template("golfstats.html", data=aggregated_stats)

if __name__ == "__main__":
    app.run(debug=True)
