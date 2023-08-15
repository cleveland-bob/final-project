# Final-Project

## Introduction
```This app was built leveraging lessons learned in Professor Rossetti's Introduction to Python class. Accordingly, some of the files were not exclusively authored by Bob but were cribbed from class materials. 

The intent of this application is to allow you to enter golf scores and statistics for saving in a google sheet. While I'd also like to read from that sheet to see statistics over time, for simplicity and time-sake, this app reads from an included CSV to show what your stats might look like. 

This app is deployed with a number of tools which I will outline the processes for implementing below.... ```

## Setup

Create a virtual environment:

```sh
conda create -n final-project-env python=3.10
```

```sh
conda activate final-project-env
```

Install third-party packages:

```sh
pip install -r requirements.txt
```

## Notes
``This application requires the use of flask for deployment and csv to read files
This application uses twitter bootstrap to display the layout on a web page 
This application requires you to have a blank stats.csv file with headers that match the file in this repo. Please name the file accordingly and ensure its format is accurate before proceeding ``

## Usage

Run the App:

```sh
python app/final-project.py

python -m app.final
```

## 