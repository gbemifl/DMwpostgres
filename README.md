# Data-modeling-postgres #Data modelling with postgres
Sparkify has been collecting songs and user activity on their new music app for analysis. Sparkify would like to analyse data and derive insights for marketing and user experience purposes. They want to be able to serve their customers optimally by doing predictive analysis.


The Sparkifydb database was created and consists of five tables based on a star schema. The fact table, songplay table and the dimension tables- songs, artists, time, users

STAR SCHEMA
The basis for the star schema was to keep our model very simple and denormalized, the json data provided was very simple and can answer a lot of question about our customers, the songs played and location played.
Sparkify also wanted the data to provide query responses very quickly to make it very easy to make changes to data.
We want to be able to do simple queries and simplify our business reporting logic especially with our period reporting of user logins based on the timestamps provided. We have one fact table and the dimensional tables that feed into the fact table. With the schema this way we are able to answer questions like:

What location are users playing music in?
what songs are played the most?
How is the free and paid subscriptions serving customers?


The data files given were the Song file and Log file in json format:

The song file was used to derive the song table and artist table and the log file was used to derive the user table and time table with python as the driver.

In songplay table, songplay_id is a serial and primary key
In the user table, user_id is the primary key, we want to be able to identify each user as one entity
in the song table, song_id is the primary key 
In the artist table, artist_id was the primary key

songplay- the database is optimized for queries on the songplay table which collates the user data for analysis.

The Dimension tables which each of the attributes as depicted in the diagram:



There are 3 main code files to execute the database:

etl.py
This file reads and processes and extracts a single file from song_data and log_data and processes the data and transforms to a format suitable for each of the tables.

sql_queries.py
This file scripts how the data should be loaded into the database. Creates all the tables and its variables and specifies the data types. Scripts all create, insert and drop statements for all tables.

create_tables.py
This file provides functions to drop and create the sql queries

test.py
This file provides sample queries to test and validate data quality


HOW TO RUN THE FILES 
1. First, you need to run the create_tables.py
2. Second, you run the etl.py

Other python files run within the scripts above. 


