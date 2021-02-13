# DROP TABLES

songplay_table_drop = """DROP TABLE IF EXISTS SONGPLAYS"""
user_table_drop = """DROP TABLE IF EXISTS USERS"""
song_table_drop = """DROP TABLE IF EXISTS SONGS"""
artist_table_drop = """DROP TABLE IF EXISTS ARTISTS"""
time_table_drop = """DROP TABLE IF EXISTS TIME"""

# CREATE TABLES

songplay_table_create = ("""CREATE TABLE IF NOT EXISTS SONGPLAYS\
                         (songplay_id SERIAL PRIMARY KEY NOT NULL,\
                         start_time timestamp,\
                         user_id int,\
                         level text,\
                         song_id varchar ,\
                         artist_id varchar,\
                         session_id int,\
                         location varchar,\
                         user_agent varchar);""")



user_table_create = ("""CREATE TABLE IF NOT EXISTS USERS (user_id int PRIMARY KEY, first_name text,\
                     last_name text,\
                     gender char(1),\
                     level text);""")

song_table_create = ("""CREATE TABLE IF NOT EXISTS SONGS (song_id varchar PRIMARY KEY, title varchar, artist_id varchar, year int, duration numeric);""")

artist_table_create = ("""CREATE TABLE IF NOT EXISTS ARTISTS(artist_id varchar PRIMARY KEY, name text,\
                       location varchar,\
                       latitude NUMERIC,\
                       longitude NUMERIC);""")

time_table_create = ("""CREATE TABLE IF NOT EXISTS TIME (start_time timestamp,\
                     hour int,\
                     day int,\
                     week int,\
                     month int,\
                     year int, weekday text);""")

# INSERT RECORDS

songplay_table_insert = ("""INSERT into SONGPLAYS(start_time,  user_id,  level, song_id, artist_id, session_id, location, user_agent) VALUES( %s, %s, %s, %s, %s, %s, %s, %s) ON CONFLICT (user_id) DO NOTHING;""")

user_table_insert = ("""INSERT into USERS(user_id, first_name, last_name, gender, level) VALUES(%s, %s, %s, %s, %s) ON CONFLICT (user_id) DO NOTHING;""")

song_table_insert = ("""INSERT into SONGS(song_id, title, artist_id, year, duration) VALUES(%s, %s, %s, %s, %s)""")

artist_table_insert = ("""INSERT INTO ARTISTS(artist_id, name, location, latitude, longitude) VALUES(%s, %s, %s, %s, %s)""")

time_table_insert = ("""insert into TIME(start_time, hour, day, week, month, year, weekday) VALUES(%s, %s, %s, %s, %s, %s, %s)""")
                     
        

# FIND SONGS
#timestamp, user ID, level, song ID, artist ID, session ID, location, and user agent and set to songplay_data



song_select = ("""SELECT songs.song_id, songs.artist_id FROM songs JOIN artists ON songs.artist_id = artists.artist_id WHERE songs.title =%s AND artists.name =%s AND songs.duration =%s;""")
# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]


#SELECT songs.song_id, artists.artist_id FROM  songs  JOIN artists ON songs.artist_id =artists.artist_id WHERE songs.title = %s AND artists.name = %s AND songs.duration = %s;