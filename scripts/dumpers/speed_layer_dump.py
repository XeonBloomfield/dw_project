import sc2reader
import psycopg2

replays = sc2reader.load_replays('../../../3.16.1-Pack_1-fix/Replays')
connection = None
try:
    connection = psycopg2.connect(user = "postgres",
                                    password = "user",
                                    host = "127.0.0.1",
                                    port = "5432",
                                    database = "speed")
    cursor = connection.cursor()
    print ( connection.get_dsn_parameters(),"\n")

    # Print PostgreSQL version
    cursor.execute("SELECT version();")
    record = cursor.fetchone()
    print("You are connected to - ", record,"\n")
    
    # Create Tables
    create_table_query = '''
            CREATE TABLE REPLAY
                (ID INT PRIMARY KEY     NOT NULL,
                BUILD          TEXT    NOT NULL,
                DATE           DATE,
                SPEED          TEXT,
                WINNER         TEXT
                ); 
            '''
    
    cursor.execute(create_table_query)
    connection.commit()
    print("Table created successfully in PostgreSQL ")


    for i, replay in enumerate(replays):
        cursor.execute("INSERT INTO REPLAY (ID, BUILD, DATE, SPEED, WINNER) VALUES(%s, %s, %s, %s, %s)", (i, replay.build, replay.date, replay.speed, str(replay.winner)))
        connection.commit()
        # TODO DELET
        if i == 10:
            break
except (Exception, psycopg2.Error) as error :
    print ("Error while connecting to PostgreSQL", error)
finally:
    #closing database connection.
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")