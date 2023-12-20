# Creating all of the functions that will be used in the rest_server.py module 
# Creating the framesDAO class which contains the functions to carry out SQL commands 
# Code adapted from Topic 9 Lectures and Labs & Topic 10


# To allow to communicate with the sql database
import mysql.connector

#importing the database login details from config file 
from dbconfig import config as cfg


# Create the framesDAO class 
class framesDAO:
    host =""
    user = ""
    password =""
    database =""
    connection = ""
    cursor =""


    # login details are stored in the config.py file
    def __init__(self): 
        self.host=cfg["hostname"]
        self.user=cfg["username"]
        self.password=cfg["password"]
        self.database=cfg["databasename"]

        
    # Connects to the database
    def getCursor(self): 
        self.connection = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        self.cursor = self.connection.cursor()
        return self.cursor
    
    # Close the connection and cursor 
    def closeAll(self):
        self.connection.close()
        self.cursor.close()


    # Functions using SQL commands:
        
    # Function to create a new frame
    def createNewFrame(self, values):
        cursor = self.getCursor()
        sql="insert into frames (Occasion, Colour, Height, Width, Price) values (%s, %s, %s, %s,%s)"
        cursor.execute(sql, values)

        self.connection.commit()
        newid = cursor.lastrowid
        self.closeAll()
        return newid
    

    # Function to retrive all from the database table
    def getAllFrames(self):
        cursor = self.getCursor()
        sql="select * from frames"
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        print(results)
        for result in results:
            print(result)
            returnArray.append(self.convertToDictionary(result))
        
        self.closeAll()
        return returnArray
    

    # Function to retrieve a particular row of data by id from the database table
    def findFrameByID(self, id):
        cursor = self.getCursor()
        sql="select * from frames where id = %s"
        values = (id,)

        cursor.execute(sql, values)
        result = cursor.fetchone()
        returnvalue = self.convertToDictionary(result)
        self.closeAll()
        return returnvalue
    

    # Function to update an existing entry in the database table
    def updateFrame(self, values):
        cursor = self.getCursor()
        sql="update frames set Occasion= %s, Colour=%s, Height=%s, Width=%s, Price=%s  where id = %s"
        cursor.execute(sql, values)
        self.connection.commit()
        self.closeAll()


    # Function to delete an entry from the database table
    def deleteFrame(self, id):
        cursor = self.getCursor()
        sql="delete from frames where id = %s"
        values = (id,)

        cursor.execute(sql, values)

        self.connection.commit()
        self.closeAll
        print("delete done")


    # Function to covert results to dict to print in the Virtual Environment terminal 
    def convertToDictionary(self, result):
        colnames=['id','Occasion','Colour', "Height", 'Width', 'Price']
        item = {}
        
        if result:
            for i, colName in enumerate(colnames):
                value = result[i]
                item[colName] = value
        
        return item
    

# Store the framesDAO class inside framesDAO variable so it can be imported into rest_server.py
framesDAO = framesDAO()