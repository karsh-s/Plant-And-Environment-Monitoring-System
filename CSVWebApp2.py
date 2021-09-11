# -*- coding: utf-8 -*-
#  Importing all modules needed for reading the csv and starting the website on the server
from flask import Flask
from flask import Flask, render_template
from flask import Markup
import os 
import csv
import time
from prettytable import PrettyTable


#  Creating Website Variable
app = Flask (__name__)


#  Creating the starting webpage route 
@app.route("/graphs")
def index():
    # Opening csv file to read
    f=open("./static/demofile3.csv", 'r')

    # Reading csv file (all lines)
    file = f.readlines()
    head = file [0]
    head = head.split(',')

    # Creating each column of table based on the data available
    table = PrettyTable(["Timestamp", "Temp", "Humidity", "Light", "Moisture"])

    # Adding all table rows
    for i in range(1, len(file)):
        table.add_row(file[i].split(','))

    # Preparing Table to be set to the webpage
    htmlCode = table.get_html_string()
    print(htmlCode)
        
    f.close()
    
#Using a HTML, CSS and JAVASCRIPT file and putting it on the website which is started on the internet's server using connected IP
    return render_template("line.html", variable = Markup(htmlCode))
    
#  Creating the second webpage route using /gaugegraph
@app.route("/gaugegraph")
def gauge():
    # Opening csv file to read
    f=open("./static/demofile3.csv", 'r')

    # Reading csv file (all lines)
    file = f.readlines()
    head = file [0]
    head = head.split(',')

    # Creating each column of table based on the data available
    table = PrettyTable(["Timestamp", "Temp", "Humidity", "Light", "Moisture"])

    # Adding all table rows
    for i in range(1, len(file)):
        table.add_row(file[i].split(','))

    # Preparing Table to be set to the webpage
    htmlCode = table.get_html_string()
    print(htmlCode)
        
    f.close()
    
#Using a HTML, CSS and JAVASCRIPT file and putting it on the website which is started on the internet's server using connected IP
    return render_template("result.html", variable = Markup(htmlCode))

#  Creating the third webpage route using /table
@app.route("/table")
def table():
    # Opening csv file to read
    f=open("./static/demofile3.csv", 'r')

    # Reading csv file (all lines)
    file = f.readlines()
    head = file [0]
    head = head.split(',')

    # Creating each column of table based on the data available
    table = PrettyTable(["Timestamp", "Temp", "Humidity", "Light", "Moisture"])

    # Adding all table rows
    for i in range(1, len(file)):
        table.add_row(file[i].split(','))

    # Preparing Table to be set to the webpage
    htmlCode = table.get_html_string()
    print(htmlCode)
        
    f.close()
    
#Using a HTML, CSS and JAVASCRIPT file and putting it on the website which is started on the internet's server using connected IP
    return render_template("page.html", variable = Markup(htmlCode))

@app.route("/plant_height")
def plant_height():
    # Opening csv file to read and creating table
    table ="<table><colgroup><col class= 'twenty' /><col class='thirty' / ><col /></colgroup>"
    table = table + "<tr><th>Week</th><th>Height</th><th>Image</th></tr>"
    with open("./static/heights.csv", "r") as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)
        
        if header != None:
            for row in reader:
                table = table + "<tr><td>" + row[0] + "</td><td>" + row[1]+ "</td><td><img src='static/result_images/"+row[2] +"'></td></tr>"
    table = table + "</table>"
    
#Using a HTML, CSS and JAVASCRIPT file and putting it on the website which is started on the internet's server using connected IP
    return render_template("height.html", height_table = Markup(table))

@app.route("/")
def virtual_twin():
    # Opening csv file to read and creating table
    table ="<table><colgroup><col class= 'twenty' /><col class='thirty' / ><col /></colgroup>"
    table = table + "<tr><th>Week</th><th>Height</th><th>Image</th></tr>"
    with open("./static/heights.csv", "r") as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)
        
        if header != None:
            for row in reader:
                table = table + "<tr><td>" + row[0] + "</td><td>" + row[1]+ "</td><td><img src='static/result_images/"+row[2] +"'></td></tr>"
    table = table + "</table>"
    
#Using a HTML, CSS and JAVASCRIPT file and putting it on the website which is started on the internet's server using connected IP
    return render_template("vt.html", height_table = Markup(table))

#Starting/ Creating the website on launch
if __name__ == "__main__":
    app.run()


