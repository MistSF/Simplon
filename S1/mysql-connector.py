import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="mist",
    password="Plumette59!"
)

db_name = "you_are_in_army_now"
TABLES = {}
TABLES['Soldat'] = (
    """CREATE TABLE IF NOT EXISTS Soldat (
        id_soldat INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
        matricule VARCHAR(40),
        nom VARCHAR(40),
        email VARCHAR(40),
        grade VARCHAR(40)
    )"""
)

TABLES['Difficulte'] = (
    """CREATE TABLE IF NOT EXISTS Difficulte (
        difficulte VARCHAR(40) NOT NULL PRIMARY KEY,
        bonus INT UNSIGNED
    )"""
)


TABLES['Obstacle'] = (
    """CREATE TABLE IF NOT EXISTS Obstacle (
        id_obstacle INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
        nom VARCHAR(40),
        difficulte VARCHAR(40),
        note_minimal INT,
        FOREIGN KEY (difficulte) REFERENCES Difficulte(difficulte)
    )"""
)

TABLES['Passage'] = (
    """CREATE TABLE IF NOT EXISTS Passage (
        id_passage INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
        id_soldat INT UNSIGNED NOT NULL,
        id_obstacle INT UNSIGNED NOT NULL,
        date DATETIME,
        id_instructeur INT UNSIGNED,
        note_final INT,
        temps_passage FLOAT UNSIGNED,
        FOREIGN KEY (id_soldat) REFERENCES Soldat(id_soldat),
        FOREIGN KEY (id_obstacle) REFERENCES Obstacle(id_obstacle)
    )"""
)


cursor = mydb.cursor()

def create_database(cursor) :
    try :
        cursor.execute("CREATE DATABASE {}".format(db_name))
    except mysql.connector.Error as err :
        print("failed to create database {}".format(err))
        exit(1)
    
    try :
        cursor.execute("USE {}".format(db_name))
        print("Connected to {}".format(db_name))
    except mysql.connector.Error as err :
        print("Database {} doesn't exists".format(db_name))
        if err.errno == errorcode.ER_BAD_DB_ERROR:
            create_database(cursor)
            print("Database {} create successfully.".format(db_name))
            mydb.database = db_name
        else :
            print(err)
            exit(1)

create_database(cursor)
for x in TABLES :
   cursor.execute(TABLES[x])
mydb.close()