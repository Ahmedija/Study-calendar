from datetime import date
import db
import record


def welcome():
    print("Wellcome to my program Study calendar \n")
    print("Please select the folowing below: ")
    print("1. Make new entry")
    print("2. Edit date")
    print("3. Print my entries")
    print("4. List by date\n \n")

    #1 ubaci u bazu
def new_entry():
    datum = str(date.today())
    category = input("Enter category: ")
    description = input("Description: ")
    objekat = record.Record(datum, category, description)
    db.Insert(objekat)

    #2 edit entry
def edit_entry():
    dateEdited = input("Enter date you want to edit in format YYYY-MM-DD: ")
    categotyEdited = input("Enter category you want to edit: ")
    descriptionEdited = input("Enter description you want to edit: ")
    objectEdited = record.Record(dateEdited, categotyEdited, descriptionEdited)
    db.Insert(objectEdited)

    #3 print entrys from database
def list_entry():
    db.Fetch()

    #4
def list_by_date(self):
    print("Enter date")
    date = 0




welcome()


num = int(input("Your selection: "))

if num == 1:
    new_entry()
elif num ==2:
    edit_entry()
elif num==3:
    list_entry()
elif num==4:
    list_by_date()
else:
    print("Please enter number from 1 to 4")
