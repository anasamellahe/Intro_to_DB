import mysql.connector

scriptFileName = "alx_book_store.sql"
host = "your host"
user = "your user"
password = "your Password"



# "CREATE DATABASE IF NOT EXISTS alx_book_store"
def connectToDB(user, host, password):
    try:
        myConnector = mysql.connector.connect(user=user, host=host, password=password)
    except mysql.connector.Error as e:
        print("exception here", e)
        return None
    else:
        print("connection success \n")
    return myConnector


def openScript(scriptFileName):
    try:
        with open(scriptFileName, 'r') as myScript:
            scriptContent = myScript.read()
    except Exception as e:
        print("exception here", e)
        return None
    else:
        return scriptContent

def splitSQLScript(mySQLScript):
    myList = mySQLScript.split(sep=";")
    for index in range(len(myList)):
        myList[index] = myList[index].replace("\n", "").strip()
        if len(myList[index]) == 0:
            myList.pop(index)
    return myList;
        
def executeCommands(command, connecterOBJ ,cursorOBJ):
    try:
        cursorOBJ.execute(command)
    except mysql.connector.Error as e:
        print(f"Failed to execute:\n{command}\nError: {e}\n")
        return False
    else:
        print(f"Executed: {command[:50]}...")
        return True

def startConnection():
    connectorOBJ  = connectToDB(user=user, host=host, password=password)
    if (connectorOBJ == None):
        exit(1)
    mySQLScript = openScript(scriptFileName=scriptFileName)
    if mySQLScript == None:
        connectorOBJ.close()
        exit(1)
    commands = splitSQLScript(mySQLScript)
    cursorOBJ = connectorOBJ.cursor()
    for command in commands:
        executeCommands(command=command, connecterOBJ=connectorOBJ, cursorOBJ=cursorOBJ)
    connectorOBJ.commit()
    connectorOBJ.close()
    print("Database 'alx_book_store' created successfully!.")

if __name__ == "__main__":
    startConnection()