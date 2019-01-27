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

    print("\n+++++++Entry success++++++++ \n \n")

#Fetching data from Database
def Fetch():

    mySQLconnection = Connect()
    sqlSelectQuery = "select * from calendar"

    cursor = mySQLconnection .cursor()
    cursor.execute(sqlSelectQuery)

    calendar = cursor.fetchall()


    print ("\nPrinting each row's column values in format YYYY-MM-DD: \n \n")
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


#Sorting list by date buble sort
def sort_by_date():

    mySQLconnection = Connect()
    sqlSelectQuery = "select * from calendar"

    cursor = mySQLconnection .cursor()
    cursor.execute(sqlSelectQuery)

    #Tuple calendar
    calendar = cursor.fetchall()

    #List calendar
    calendarData = [list(row) for row in calendar]

    sub_li = calendarData


    #bubble sort
    def Sort(sub_li):
         l = len(sub_li)
         for i in range(0, l):
             for j in range(0, l-i-1):
                 if (sub_li[j][1] > sub_li[j + 1][1]):
                     tempo = sub_li[j]
                     sub_li[j]= sub_li[j + 1]
                     sub_li[j + 1]= tempo
         return sub_li

    sortedList = Sort(sub_li)

    #Printing sorted list
    print("Entries sorted by date: \n")
    for row in sortedList:
        print("Date         = ", row[1], )
        print("Category     = ", row[2])
        print("Description  = ", row[3], "\n \n")





