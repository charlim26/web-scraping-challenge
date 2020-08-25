# Import Dependencies 
from flask import Flask, render_template, redirect 
from flask_pymongo import PyMongo
import scrape_mars

# Create an instance of Flask app
app = Flask(__name__)

# Use PyMongo to establish Mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")

@app.route("/")
def home(): 

    # Find data
    mars_mongo = mongo.db.collection.find_one()

    # Return template and data
    return render_template("index.html", mars=mars_mongo)

# Route that will trigger scrape function
@app.route("/scrape")
def scrape(): 

    # Run scrapped functions
    mars_scrape = scrape_mars.scrape()
    
    mongo.db.collection.update({}, mars_scrape, upsert=True)

    return redirect("/")

if __name__ == "__main__": 
    app.run(debug= True)

























































