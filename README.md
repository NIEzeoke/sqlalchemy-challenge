# sqlalchemy-challenge

This project involved conducting climate analysis in preparation for a vacation in Honolulu, Hawaii. 

Firstly, I made use of SQLAlchemy and Python to analyze and explore the climate database contained in a jupyter notebook and sqlite file by creating an connection to to the sqlite database, reflecting the tables into classes and saving the reference names. Once Python had been linked to the database I was able to perform an analysis on precipitation

 The precipitation analysis revolved around the previous 12 months of data and as such they needed to be queried. The values for date and precipitation were then selected and loaded to a Pandas DataFrame, which was sorted by date. The results were plotted and can be seen below. Finally, Pandas was used to generate summary statistics.
![image](https://github.com/NIEzeoke/sqlalchemy-challenge/assets/127510090/9cd915a5-a910-4451-b523-3d5fae93fdf2)


Similarly station data was queried, collected (in descending order of activity). Additionally, the high, low and average temperatures were. queried
The stations were queried again for the last 12 months and plotted as shown below.

![image](https://github.com/NIEzeoke/sqlalchemy-challenge/assets/127510090/c28ebc93-58c7-4982-941e-31df032143d5)

The final portion of the project involved designing a climate app by making use of Flask. The app contained pages for precipitation (dictionary formatted query results), weather stations and observed temperatures from the most active station, and an interactive page that returns a JSON list of the minimum temperature, the average temperature, and the maximum temperature for a specified start or start-end range.
