# -*- coding: utf-8 -*-
from flask import Flask, render_template, jsonify, redirect
# from flask_pymongo import PyMongo
import pymongo
import scrape_mars

app = Flask(__name__)

# mongo = PyMongo(app)

conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)
db = client.mars



@app.route("/")
def index():
    # mars_data = mongo.db.mars_data.find_one()
    data_outputs = db.mars_data.find_one()
    return render_template("index.html", data_outputs=data_outputs)

@app.route("/scrape")
def scrape():
    data_outputs = db.mars_data
    mars_data_output = scrape_mars.scrape()
    return redirect("http://localhost:5000/", code=302)


if __name__ == "__main__":
    app.run(debug=True)


