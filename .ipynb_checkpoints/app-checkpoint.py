# Import the dependencies.
import numpy as np
import datetime as dt

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(autoload_with = engine)
# Save references to each table
measurement = Base.classes.measurement
station = Base.classes.station

# Create our session (link) from Python to the DB
session=Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################
@app.route("/")
def index():
    return(
        f"Availabale Routes:<br/>"
        f"/api/v1.0/precipitation <br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end><br/>"        
    )
#Convert the query results from your precipitation analysis (i.e. retrieve only the last 12 months of data) to a dictionary using date as the key and prcp as the value.
#Return the JSON representation of your dictionary.


@app.route("/api/v1.0/precipitation")
def precipitation():
    #Create our session (link) from Python to the DB
    session = Session(engine)
    prev_year=dt.date(2017,8,23) - dt.timedelta(365)
    #Make query
    results= session.query(measurement.date, measurement.prcp) \
    .filter(measurement.date >= prev_year, measurement.prcp != None) \
    .order_by(measurement.date).all()
        
    return jsonify(dict(results))

@app.route("/api/v1.0/stations")
def stations():
    stations_m = session.query(measurement.station.distinct(), func.count(measurement.station)) \
    .group_by(measurement.station) \
    .order_by(func.count(measurement.station).desc()).all()

   
    return jsonify(dict(stations_m))

@app.route("/api/v1.0/tobs")
def tobs():
    prev_year=dt.date(2017,8,23) - dt.timedelta(365)
    
    tobs = session.query(measurement.date, measurement.tobs) \
    .filter(measurement.date >= prev_year) \
    .filter(measurement.station == 'USC00519281' ).all()
    
    return jsonify(dict(tobs))

def calc_start_temps(start_date):
    
    return session.query(func.min(measurement.tobs), func.avg(measurement.tobs), func.max(measurement.tobs)).\
        filter(measurement.date >= start_date).all()

@app.route("/api/v1.0/<start>")
    
def start_date(start):
    calc_start_temp = calc_start_temps(start)
    t_temp= list(np.ravel(calc_start_temp))

    t_min = t_temp[0]
    t_max = t_temp[2]
    t_avg = t_temp[1]
    t_dict = {'Minimum temperature': t_min, 'Maximum temperature': t_max, 'Avg temperature': t_avg}

    return jsonify(t_dict)

def calc_temps(start_date, end_date):
    
    return session.query(func.min(measurement.tobs), \
                         func.avg(measurement.tobs), \
                         func.max(measurement.tobs)).\
                         filter(measurement.date >= start_date).\
                         filter(measurement.date <= end_date).all()

@app.route("/api/v1.0/<start>/<end>")

def start_end_date(start, end):
    
    calc_temp = calc_temps(start, end)
    ta_temp= list(np.ravel(calc_temp))

    tmin = ta_temp[0]
    tmax = ta_temp[2]
    temp_avg = ta_temp[1]
    temp_dict = { 'Minimum temperature': tmin, 'Maximum temperature': tmax, 'Avg temperature': temp_avg}

    return jsonify(temp_dict)

if __name__ == '__main__':
    app.run(debug=True)

