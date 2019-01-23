from mysql.connector import MySQLConnection, Error, cursor

import mysql.connector

#connection to database
def Connect():
    cnx = mysql.connector.connect(
      host='localhost',
      user='root',
      password='Ahmed123.',
      database='studycalendar')

    return cnx


#insertion into database logic
def Insert(row):

    query = "INSERT INTO calendar (date, category, description) VALUES (%s, %s, %s)"
    val = (row.date, row.category, row.description)

    connection = Connect()

    cursor = connection.cursor()
    cursor.execute(query, val)


    connection.commit()
    cursor.close()

    print("Entry success.")

#Fetching data from Database
def Fetch():

    mySQLconnection = Connect()
    sqlSelectQuery = "select * from calendar"

    cursor = mySQLconnection .cursor()
    cursor.execute(sqlSelectQuery)

    calendar = cursor.fetchall()

    print ("\nPrinting each row's column values \n \n")
    for row in calendar:
       print("Date         = ", row[1], )
       print("Category     = ", row[2])
       print("Description  = ", row[3], "\n")
    cursor.close()

#Editing old date
def Edit(row):


    connection = Connect()

    mycursor = connection.cursor()

    connection.commit()



