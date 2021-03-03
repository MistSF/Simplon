def addSoldier(cursor, mydb) :
    print("New soldier information")
            print("Matricule : ")
            matricule = input()
            print("Name : ")
            nom = input()
            print("Mail : ")
            email = input()
            print("Grade : ")
            grade = input()
            try :
                cursor.execute("INSERT INTO Soldat (matricule, nom, email, grade) VALUES (%s, %s, %s, %s);", (matricule, nom, email, grade))
                mydb.commit()
                print("Soldier {} has been added".format(nom))
            except mysql.connector.Error as err :
                print("Soldier {} wasn't added, {}".format(nom, err))
            print()

def showSoldier(cursor) :
    try :
        cursor.execute("SELECT * FROM Soldat;")
        res = cursor.fetchall()
        for x in res :
            print(x)
        print()
    except mysql.connector.Error as err :
        print(err)

def addObstacle(cursor, mydb) :
    difficulte = ""
    print("add new obstacle")
    print("name : ")
    nom = input()
    while difficulte not in ["Easy", "Medium", "Hard"] :
        print("difficult level (Easy, Medium, Hard):")
        difficulte = input()
    print("minimal note : ")
    note_minimal = input()
    try :
        cursor.execute("INSERT INTO Obstacle (nom, difficulte, note_minimal) VALUES (%s, %s, %s)", (nom, difficulte, note_minimal))
        mydb.commit()
        print("Obstacle has been added")
    except mysql.connector.Error as err :
        print(err)

def showObstacle(cursor) :
    try :
        cursor.execute("SELECT * FROM Obstacle;")
        res = cursor.fetchall()
        for x in res :
            print(x)
        print()
    except mysql.connector.Error as err :
        print(err)