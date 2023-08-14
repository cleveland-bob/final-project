import csv
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

def write_to_csv(data):
    with open('stats.csv', 'a', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(data)

@app.route("/home_routes", methods=["POST"])
def index():
    if request.method == "POST":
        hole = request.form["hole"]
        score = int(request.form["score"])
        putts = int(request.form["putts"])
        fairway = request.form["fairway"]

        data = [hole, score, putts, fairway]
        write_to_csv(data)

        if int(hole) == 18:
            return redirect("/summary")
    
    return render_template("index.html")

@app.route("/summary")
def summary():
    data = []
    with open('stats.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            data.append(row)
    
    return render_template("summary.html", data=data)

if __name__ == "__main__":
    app.run(debug=True)
