import mysql.connector

#this file is to gathering the data from Github into a database

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "password"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE myGithubDatabase")
