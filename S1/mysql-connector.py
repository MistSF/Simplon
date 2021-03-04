import mysql.connector
import databaseconfig as cfg
import crud as cr

mydb = mysql.connector.connect(
    host="localhost",
    user=cfg.mysql["user"],
    password=cfg.mysql["passwd"]
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

cursor = mydb.cursor(buffered=True)
def create_database(cursor) :
    try :
        cursor.execute("CREATE DATABASE {}".format(db_name))
    except mysql.connector.Error as err :
        print("failed to create database {}".format(err))
    
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

create_database(cursor)

for x in TABLES :
   cursor.execute(TABLES[x])

try : 
    cursor.execute("INSERT INTO Difficulte VALUES ('Easy', 0)")
    cursor.execute("INSERT INTO Difficulte VALUES ('Medium', 2)")
    cursor.execute("INSERT INTO Difficulte VALUES ('Hard', 5)")
    mydb.commit()
except mysql.connector.Error as err : 
    print(err)

run = True
while run :
    print("You're in army now !")
    print("use help to see commands avaible\n")
    entry = input().lower()
    if entry == "quit" :
        run = False
    elif entry == "help" :
        print("add soldier, add obstacle, show soldier, show obstacle, edit soldier, edit obstacle")
    elif entry == "add soldier" :
        cr.addSoldier(cursor, mydb)
    elif entry == "show soldier" :
        cr.showSoldier(cursor)
    elif entry == "edit soldier" :
        cr.editSoldier(cursor, mydb)
    elif entry == "remove soldier" :
        cr.removeSoldier(cursor, mydb)
    elif entry == "add obstacle" :
        cr.addObstacle(cursor, mydb)
    elif entry == "show obstacle" :
        cr.showObstacle(cursor)
    elif entry == "edit obstacle" :
        cr.editObstacle(cursor, mydb)
    elif entry == "remove obstacle" :
        cr.removeObstacle(cursor, mydb)
    
mydb.close()