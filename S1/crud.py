import mysql.connector

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

def showSoldier(cursor, nom = False) :
    try :
        if nom :
            cursor.execute("SELECT nom FROM Soldat")
        else :
            cursor.execute("SELECT * FROM Soldat")
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

def showObstacle(cursor, nom=False) :
    try :
        if not nom :
            cursor.execute("SELECT * FROM Obstacle;")
        else :
            cursor.execute("SELECT nom FROM Obstacle")
        res = cursor.fetchall()
        for x in res :
            print(x)
        print()
    except mysql.connector.Error as err :
        print(err)
    
def editSoldier(cursor, mydb) :
    showSoldier(cursor, True)
    print("what Soldier : ")
    name = input()
    print("Edit :\n1) Matricule\n2) Name\n3) Grade")
    edit = int(input())
    if edit == 1 :
        request = "UPDATE Soldat SET matricule=%s WHERE nom = %s"
    elif edit == 2 :
        request = "UPDATE Soldat SET nom=%s WHERE nom = %s"
    elif edit == 3 :
        request = "UPDATE Soldat SET grade=%s WHERE nom = %s"
    else :
        exit(1)
    print("new Value : ")
    newValue = input()
    try :
        print(newValue, name)
        cursor.execute(request, (newValue, name))
        mydb.commit()
    except mysql.connector.Error as err :
        print("Edit failed {}".format(err))

def editObstacle(cursor, mydb) :
    showObstacle(cursor, True)
    print("what Obstacle : ")
    name = input()
    print("Edit :\n1) nom\n2) difficult\n3) minimum")
    edit = int(input())
    if edit == 1 :
        request = "UPDATE Obstacle SET nom=%s WHERE nom = %s"
    elif edit == 2 :
        request = "UPDATE Obstacle SET difficulte=%s WHERE nom = %s"
    elif edit == 3 :
        request = "UPDATE Obstacle SET minimum=%s WHERE nom = %s"
    else :
        exit(1)
    if edit != 2 :
        print("new Value : ")
        newValue = input()
    else :
        newValue = -1
        while newValue not in ["Easy","Medium","Hard"] :
            print("Easy,Medium, Hard")
            newValue = input()
    try :
        print(newValue, name)
        cursor.execute(request, (newValue, name))
        mydb.commit()
        cursor.execute("SELECT * FROM Obstacle WHERE nom = %s", (name))
        print()
    except mysql.connector.Error as err :
        print("Edit failed {}".format(err))

def removeSoldier(cursor, mydb) :
    showSoldier(cursor, True)
    print("what soldier :")
    target = input()
    try :
        request = "DELETE FROM Soldat WHERE nom = '{}'".format(target)
        mydb.commit()
        cursor.execute(request)
    except mysql.connector.Error as err :
        print(err)

def removeObstacle(cursor, mydb) :
    showObstacle(cursor, True)
    print("what obstacle :")
    target = input()
    try :
        request = "DELETE FROM Obstacle WHERE nom = '{}'".format(target)
        mydb.commit()
        cursor.execute(request)
    except mysql.connector.Error as err :
        print(err)