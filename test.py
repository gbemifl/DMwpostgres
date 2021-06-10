import psycopg2


conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb user=student password=student")
cur = conn.cursor()

def artistdata():
    """
    sample data within the artist table
    """
    print("\n Sample data from Artists table\n SELECT * FROM ARTISTS:") 

    try:
        cur.execute("select * from artists LIMIT 2;")
    except psycopg2.Error as e: 
        print("Error: select *")
        print (e)

    row = cur.fetchone()
    while row:
       print(row)
       row = cur.fetchone()

# count data for artist table
        
    try:
        print("Count of artist data in data table: ")
        count_artist= """Select count (*) from artists;"""
        cur.execute(count_artist)
    except psycopg2.Error as e: 
        print("Error: select *")
        print (e)

    row = cur.fetchone()
    while row:
       print(row)
       row = cur.fetchone()
        
    try:
        print("Sample query with Join on song_id and artist_id Where Artist name is Gwen Stefani : ")
        cur.execute("select songs.song_id, songs.artist_id, artists.name, songs.title, artists.location FROM songs JOIN artists ON songs.artist_id= artists.artist_id WHERE artists.name = 'Gwen Stefani';")
    except psycopg2.Error as e: 
        print("Error: select *")
        print (e)

    row = cur.fetchone()
    while row:
       print(row)
       row = cur.fetchone()
        
        
        
        
def songdata():
    """sample data within the song table"""
    print("\n Sample data from Song \n")     
    print("SELECT * FROM songs: \n")
    
    try: 
        cur.execute("select * from songs LIMIT 2;")
    except psycopg2.Error as e: 
        print("Error: select *")
        print (e)

    row = cur.fetchone()
    while row:
       print(row)
       row = cur.fetchone()
        

def locationtest():
    """sample data to view data for where the users are located"""
    print("\n sample data where location is in CALIFORNIA-CA")
    
    try: 
        cur.execute("select * from songplays WHERE location like '%CA%';")
        cur.execute("select count(*) from songplays WHERE location like '%CA%';")
    except psycopg2.Error as e: 
        print("Error: select *")
        print (e)

    row = cur.fetchone()
    while row:
       print(row)
       row = cur.fetchone()
   