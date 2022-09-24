# import dependancies
from asyncio.format_helpers import extract_stack
import datetime as dt
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

# import the dependencies that we need for Flask
from flask import Flask, jsonify

# access and query our SQLite database file
engine = create_engine("sqlite:///hawaii.sqlite")

# reflect the database into our classes
Base = automap_base()

# reflect the tables into SQLAlchemy
Base.prepare(engine, reflect=True)

# create a variable for each of the classes so that we can reference them later
Measurement = Base.classes.measurement
Station = Base.classes.station

# create a session link from Python to our database
session = Session(engine)

# create a Flask application called "app."
app = Flask(__name__)

# define the welcome route
@app.route('/')

def welcome():
    return(
    '''
    Welcome to the Climate Analysis API!\n
    Available Routes:\n
    /api/v1.0/precipitation\n
    /api/v1.0/stations\n
    /api/v1.0/tobs\n
    /api/v1.0/temp/start/end\n
    ''')

# create precipitation analysis route
@app.route("/api/v1.0/precipitation")

# create the precipitation() function.
def precipitation():
    
    #  calculate the date one year ago from the most recent date in the database
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    
    # write a query to get the date and precipitation for the previous year
    precipitation = session.query(Measurement.date, Measurement.prcp).\
    filter(Measurement.date >= prev_year).all()

    # create a dictionary with the date as the key and the precipitation as the value
    precip = {date: prcp for date, prcp in precipitation}

    # "jsonify" our dictionary  
    return jsonify(precip)

# create stations route
@app.route("/api/v1.0/stations")

# create the stations function
def stations():

    # create a query that will allow us to get all of the stations in our database
    results = session.query(Station.station).all()

    # unravel our results into a one-dimensional array
    # convert our unraveled results into a list
    stations = list(np.ravel(results))

    # jsonify the list and return it
    return jsonify(stations=stations)

 # create temperature observations route
@app.route("/api/v1.0/tobs")

# create the temperatures function
def temp_monthly():
    
    # calculate the date one year ago from the last date in the database
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)

    # query the primary station for all the temperature observations from the previous year
    results = session.query(Measurement.tobs).\
        filter(Measurement.station == 'USC00519281').\
        filter(Measurement.date >= prev_year).all()    
    
    # unravel our results into a one-dimensional array
    # convert our unraveled results into a list
    temps = list(np.ravel(results))

    # jsonify the list and return it
    return jsonify(temps=temps)

@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")

# create a function called stats()

# add parameters to our stats()function: a start parameter and an end parameter. 
# set them both to None
def stats(start=None, end=None):

    # create a query to select the minimum, average, and maximum temperatures from our SQLite database
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

    # add an if-not statement to our code to determine the starting and ending date
    if not end:

        # query our database from the previous year
        results = session.query(*sel).\
            filter(Measurement.date >= start).all()
        
        # unravel our results into a one-dimensional array
        # convert our unraveled results into a list
        temps = list(np.ravel(results))
        
        # jsonify the list and return it   
        return jsonify(temps=temps)

    # create our next query, which will get our statistics data
    results = session.query(*sel).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()
    temps = list(np.ravel(results))
    return jsonify(temps)