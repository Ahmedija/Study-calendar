from datetime import date
import db
import record
import datetime



def restart():


    def welcome():

        print("Wellcome to my program Study calendar \n")
        print("Please select the following: ")
        print("1. Make new entry for today")
        print("2. Make entry for some date")
        print("3. Print my entries")
        print("4. Print sorted entries")
        print("5. --------EXIT--------\n \n")


        #1 Make new entry
    def new_entry():
        datee = str(date.today())
        category = input("Enter category: ")
        description = input("Description: ")

        newEntryData = record.Record(datee, category, description)
        db.Insert(newEntryData)

        restart()

        #2 Edit entry
    def edit_entry():

        #validation of date
        inputDate = input("Enter the date in format 'YYYY-MM-DD': ")
        year,month,day = inputDate.split('-')

        isValidDate = True

        try :

            datetime.datetime(int(year),int(month),int(day))

        except ValueError :

            isValidDate = False

        if(isValidDate) :

            print ("\nInput date is VALID ...\n")
            inputCategoty = input("Enter new category: ")
            inputDescription = input("Enter new description: ")

            objectEdited = record.Record(inputDate, inputCategoty, inputDescription)
            db.Insert(objectEdited)

        else:
            print ("\nInput date is NOT VALID... \n")
            edit_entry()

        welcome()


        #3 Print entrys from database
    def list_entry():
        db.Fetch()
        restart()

        #4 Sort by date
    def sort_by_date():
        db.sort_by_date()
        restart()


    #first selection
    welcome()

    #validation of user input
    while True:
        try:
            num = int(input("Your selection 1 to 5: "))

            if num == 1:
                new_entry()
            elif num ==2:
                edit_entry()
            elif num==3:
                list_entry()
            elif num==4:
               sort_by_date()
            elif num == 5:
                exit()
        except ValueError :


            print("\nPlease enter number from 1 to 5: \n")
            restart()
            break


restart()

