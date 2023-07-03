#Project 03 Covid 19 Database Management

try:
    import mysql.connector
    mydb=mysql.connector.connect(
        host="localhost",
        user="karthi",password="password",
        database="std"
        )
    mycursor=mydb.cursor()
except mysql.connector.Error as error:
        print(f"Failed to connect from mysql :{error}")

# IMPORT DATE & TIME
import datetime
from datetime import date
from re import L
x=datetime.datetime.now()
date=x.strftime("%D")
current_time=int(x.strftime("%H"))
current_minutes=x.strftime("%M")

print("\n \t \t \t \t \t WELCOME")
print("\n THIS SITE IS CREATED FOR SHOWING THE COVID19 DATA'S RECIEVED FROM THE GOVERNMENT OF THE INDIA")
print("\n \t \t PLEASE CHECK BELOW FOR SOME OF THE DATA'S")
print("\n  ENTER THE NUMBER FOR WHICH THE DATA YOU ARE CAME TO KNOW, IN THE SPACE GIVEN BELOW")
# HIGHEST_CASES() definition
def HIGHEST_CASES():
    mycursor.execute("SELECT state,total_case FROM covid ORDER BY total_case DESC; ")
    cases=mycursor.fetchall()
    print("="*60)
    print("\nSTATE HAS THE HIGHEST NUMBER OF COVID19 CASES:")
    for row in cases:
        print(f"\n ->  {row[0]} : \t({row[1]}) CASES")
        break
    print("\n-> 1.BACK")
    print("\n-> 0.EXIT")
    while(1>0):
        option=int(input("\nEnter option : "))
        if(option==1):
            MENU()     # function call
            break
        elif(option==0):
            print("="*60)
            print("\nPlease wear mask -- Be vaccinated")
            print("\nThank you for Visiting")
            break
        else:
            print("\n-> You Entered Invalid option :")
            print("\n-> Try again or Enter '0' to Exit")
            MENU()
  # HIGHEST_DEATHS() definition
def HIGHEST_DEATHS():
    mycursor.execute("SELECT state,total_death FROM covid ORDER BY total_death DESC; ")
    cases=mycursor.fetchall()
    print("="*60)
    print("\nSTATE HAS THE HIGHEST DEATH'S FOR COVID19 CASES:")
    for row in cases:
        print(f"\n ->  {row[0]} : \t({row[1]}) persons were died")
        break
    print("\n-> 1.BACK")
    print("\n-> 0.EXIT")
    while(1>0):
        option=int(input("\nEnter option : "))
        if(option==1):
            MENU()     # function call
            break
        elif(option==0):
            print("="*60)
            print("\nPlease wear mask -- Be vaccinated")
            print("\nThank you for Visiting")
            break
        else:
            print("\n-> You Entered Invalid option :")
            print("\n-> Try again or Enter '0' to Exit")
            MENU()
  # TOP_6() definition
def TOP_6():
    mycursor.execute("SELECT state,total_case FROM covid ORDER BY total_case DESC; ")
    cases=mycursor.fetchall()
    print("="*60)
    print("\nTOP 6 STATES WHICH HAS HIGHEST CASES IN THE COUNTRY :")
    for row in cases:
        print(f"\n ->  {row[0]} : \t({row[1]}) CASES")
    print("\n-> 1.BACK")
    print("\n-> 0.EXIT")
    while(1>0):
        option=int(input("\nEnter option : "))
        if(option==1):
            MENU()     # function call
            break
        elif(option==0):
            print("="*60)
            print("\nPlease wear mask -- Be vaccinated")
            print("\nThank you for Visiting")
            break
        else:
            print("\n-> You Entered Invalid option :")
            print("\n-> Try again or Enter '0' to Exit")
            MENU()
# MAHARASHTRA() definition
def MAHARASHTRA():
    mycursor.execute("SELECT * FROM covid WHERE state='MAHARASHTRA'")
    cases=mycursor.fetchall()
    print("="*60)
    print("\nELOBRATE VIEWS ON STATE MAHARASHTRA :")
    for row in cases:
        print(f"\n -> TOTAL CASES: {row[0]}" f"\n -> TODAY CASES: {row[1]}" f"\n -> TOTAL DEATHS: {row[2]}" f"\n -> PERSONS IN TREATMENT: {row[3]}" f"\n -> DISCHARGES: {row[4]}")
    print("\n-> 1.BACK")
    print("\n-> 0.EXIT")
    while(1>0):
        option=int(input("\nEnter option : "))
        if(option==1):
            MENU()     # function call
            break
        elif(option==0):
            print("="*60)
            print("\nPlease wear mask -- Be vaccinated")
            print("\nThank you for Visiting")
            break
        else:
            print("\n-> You Entered Invalid option :")
            print("\n-> Try again or Enter '0' to Exit")
            MENU()
# KERALA() definition
def KERALA():
    mycursor.execute("SELECT * FROM covid WHERE state='KERALA'")
    cases=mycursor.fetchall()
    print("="*60)
    print("\nELOBRATE VIEWS ON STATE KERALA :")
    for row in cases:
        print(f"\n -> TOTAL CASES: {row[0]}" f"\n -> TODAY CASES: {row[1]}" f"\n -> TOTAL DEATHS: {row[2]}" f"\n -> PERSONS IN TREATMENT: {row[3]}" f"\n -> DISCHARGES: {row[4]}")
    print("\n-> 1.BACK")
    print("\n-> 0.EXIT")
    while(1>0):
        option=int(input("\nEnter option : "))
        if(option==1):
            MENU()     # function call
            break
        elif(option==0):
            print("="*60)
            print("\nPlease wear mask -- Be vaccinated")
            print("\nThank you for Visiting")
            break
        else:
            print("\n-> You Entered Invalid option :")
            print("\n-> Try again or Enter '0' to Exit")
            MENU()
# ANDHRA_PRADESH() definition
def ANDHRA_PRADESH():
    mycursor.execute("SELECT * FROM covid WHERE state='ANDHRA PRADESH'")
    cases=mycursor.fetchall()
    print("="*60)
    print("\nELOBRATE VIEWS ON STATE ANDHRA PRADESH :")
    for row in cases:
        print(f"\n -> TOTAL CASES: {row[0]}" f"\n -> TODAY CASES: {row[1]}" f"\n -> TOTAL DEATHS: {row[2]}" f"\n -> PERSONS IN TREATMENT: {row[3]}" f"\n -> DISCHARGES: {row[4]}")
    print("\n-> 1.BACK")
    print("\n-> 0.EXIT")
    while(1>0):
        option=int(input("\nEnter option : "))
        if(option==1):
            MENU()     # function call
            break
        elif(option==0):
            print("="*60)
            print("\nPlease wear mask -- Be vaccinated")
            print("\nThank you for Visiting")
            break
        else:
            print("\n-> You Entered Invalid option :")
            print("\n-> Try again or Enter '0' to Exit")
            MENU()
# UTTRA_PRADESH() definition
def UTTRA_PRADESH():
    mycursor.execute("SELECT * FROM covid WHERE state='UTTRA PRADESH'")
    cases=mycursor.fetchall()
    print("="*60)
    print("\nELOBRATE VIEWS ON STATE UTTRA PRADESH :")
    for row in cases:
        print(f"\n -> TOTAL CASES: {row[0]}" f"\n -> TODAY CASES: {row[1]}" f"\n -> TOTAL DEATHS: {row[2]}" f"\n -> PERSONS IN TREATMENT: {row[3]}" f"\n -> DISCHARGES: {row[4]}")
    print("\n-> 1.BACK")
    print("\n-> 0.EXIT")
    while(1>0):
        option=int(input("\nEnter option : "))
        if(option==1):
            MENU()     # function call
            break
        elif(option==0):
            print("="*60)
            print("\nPlease wear mask -- Be vaccinated")
            print("\nThank you for Visiting")
            break
        else:
            print("\n-> You Entered Invalid option :")
            print("\n-> Try again or Enter '0' to Exit")
            MENU()
# TAMIL_NADU() definition
def TAMIL_NADU():
    mycursor.execute("SELECT * FROM covid WHERE state='TAMIL NADU'")
    cases=mycursor.fetchall()
    print("="*60)
    print("\nELOBRATE VIEWS ON STATE TAMIL NADU :")
    for row in cases:
        print(f"\n -> TOTAL CASES: {row[0]}" f"\n -> TODAY CASES: {row[1]}" f"\n -> TOTAL DEATHS: {row[2]}" f"\n -> PERSONS IN TREATMENT: {row[3]}" f"\n -> DISCHARGES: {row[4]}")
    print("\n-> 1.BACK")
    print("\n-> 0.EXIT")
    while(1>0):
        option=int(input("\nEnter option : "))
        if(option==1):
            MENU()     # function call
            break
        elif(option==0):
            print("="*60)
            print("\nPlease wear mask -- Be vaccinated")
            print("\nThank you for Visiting")
            break
        else:
            print("\n-> You Entered Invalid option :")
            print("\n-> Try again or Enter '0' to Exit")
            MENU()
# KARNATAKA() definition
def KARNATAKA():
    mycursor.execute("SELECT * FROM covid WHERE state='KARNATAKA'")
    cases=mycursor.fetchall()
    print("="*60)
    print("\nELOBRATE VIEWS ON STATE KARNATAKA :")
    for row in cases:
        print(f"\n -> TOTAL CASES: {row[0]}" f"\n -> TODAY CASES: {row[1]}" f"\n -> TOTAL DEATHS: {row[2]}" f"\n -> PERSONS IN TREATMENT: {row[3]}" f"\n -> DISCHARGES: {row[4]}")
    print("\n-> 1.BACK")
    print("\n-> 0.EXIT")
    while(1>0):
        option=int(input("\nEnter option : "))
        if(option==1):
            MENU()     # function call
            break
        elif(option==0):
            print("="*60)
            print("\nPlease wear mask -- Be vaccinated")
            print("\nThank you for Visiting")
            break
        else:
            print("\n-> You Entered Invalid option :")
            print("\n-> Try again or Enter '0' to Exit")
            MENU()
#  TOTAL() definition
def TOTAL():
    mycursor.execute("SELECT SUM(total_case) 'TOTAL CASES'  FROM covid; ")
    cases=mycursor.fetchall()
    print("="*60)
    for row in cases:
        print("\n TOTAL NUMBER OF CASES OVER THE COUNTRY: ")
        print(f"- {row[0]}")
        break
    print("\n-> 1.BACK")
    print("\n-> 0.EXIT")
    while(1>0):
        option=int(input("\nEnter option : "))
        if(option==1):
            MENU()     # function call
            break
        elif(option==0):
            print("="*60)
            print("\nPlease wear mask -- Be vaccinated")
            print("\nThank you for Visiting")
            break
        else:
            print("\n-> You Entered Invalid option :")
            print("\n-> Try again or Enter '0' to Exit")
            MENU()
# DEATHS() definition
def TDEATHS():
    mycursor.execute("SELECT SUM(total_death) 'TOTAL DEATH'  FROM covid; ")
    cases=mycursor.fetchall()
    print("="*60)
    for row in cases:
        print("\n TOTAL NUMBER OF DEATH'S OVER THE COUNTRY:  ")
        print(f"-> {row[0]}")
        break
    print("\n-> 1.BACK")
    print("\n-> 0.EXIT")
    while(1>0):
        option=int(input("\nEnter option : "))
        if(option==1):
            MENU()     # function call
            break
        elif(option==0):
            print("="*60)
            print("\nPlease wear mask -- Be vaccinated")
            print("\nThank you for Visiting")
            break
        else:
            print("\n-> You Entered Invalid option :")
            print("\n-> Try again or Enter '0' to Exit")
            MENU()
# TODAY_CASES() definition
def TODAY_CASES():
    mycursor.execute("SELECT SUM(today_case) 'TODAY CASES'  FROM covid; ")
    cases=mycursor.fetchall()
    print("="*60)
    for row in cases:
        print("\n TODAY CASES IN THE COUNTRY: ")
        print(f"-> {row[0]}")
        break
    print("\n-> 1.BACK")
    print("\n-> 0.EXIT")
    while(1>0):
        option=int(input("\nEnter option : "))
        if(option==1):
            MENU()     # function call
            break
        elif(option==0):
            print("="*60)
            print("\nPlease wear mask -- Be vaccinated")
            print("\nThank you for Visiting")
            break
        else:
            print("\n-> You Entered Invalid option :")
            print("\n-> Try again or Enter '0' to Exit")
            MENU()
# TREATMENTS() definition
def TREATMENTS():
    mycursor.execute("SELECT SUM(in_treatment) 'in_treatment'  FROM covid; ")
    cases=mycursor.fetchall()
    print("="*60)
    for row in cases:
        print(f"\n PEOPLE IN TREATMENT ACROSS THE COUNTRY: ")
        print(f"->{row[0]}")
        break
    print("\n-> 1.BACK")
    print("\n-> 0.EXIT")
    while(1>0):
        option=int(input("\nEnter option : "))
        if(option==1):
            MENU()     # function call
            break
        elif(option==0):
            print("="*60)
            print("\nPlease wear mask -- Be vaccinated")
            print("\nThank you for Visiting")
            break
        else:
            print("\n-> You Entered Invalid option :")
            print("\n-> Try again or Enter '0' to Exit")
            MENU()
# MENU() definition
def MENU():
    print("\n-> 1. STATE HAS HIGHEST NUMBER OF TOTAL CASES")
    print("\n-> 2. STATE HAS HIGHEST NUMBER OF DEATHS")
    print("\n-> 3. TOP 6 STATES WHICH HAS HIGHEST CASES IN THE COUNTRY")
    print("\n-> 4. ELOBRATE VIEWS ON STATE MAHARASHTRA")
    print("\n-> 5. ELOBRATE VIEWS ON STATE KERALA")
    print("\n-> 6. ELOBRATE VIEWS ON STATE ANDHRA PRADESH")
    print("\n-> 7. ELOBRATE VIEWS ON STATE UTTRA PRADESH")
    print("\n-> 8. ELOBRATE VIEWS ON STATE TAMIL NADU")
    print("\n-> 9. ELOBRATE VIEWS ON STATE KARNATAKA")
    print("\n-> 10. COUNTRY'S TOTAL COVID19 CASES ")
    print("\n-> 11. TOTAL NUMBER OF DEATHS ACROSS THE COUNTRY")
    print("\n-> 12. COUNTRY'S TODAY CASES")
    print("\n-> 13. NUMBER OF PEOPLE ARE IN TREATMENT OVER THE COUNTRY")
    print("\n-> 0.EXIT")
    option=int(input("\nEnter option:"))
    if option==1:
        HIGHEST_CASES()
    elif option==2:
        HIGHEST_DEATHS()
    elif option==3:
        TOP_6()
    elif option==4:
        MAHARASHTRA()
    elif option==5:
        KERALA()
    elif option==6:
        ANDHRA_PRADESH()
    elif option==7:
        UTTRA_PRADESH()
    elif option==8:
        TAMIL_NADU()
    elif option==9:
        KARNATAKA()
    elif option==10:
        TOTAL()
    elif option==11:
        TDEATHS()
    elif option==12:
        TODAY_CASES()
    elif option==13:
        TREATMENTS()
    elif option==0:
        print("="*60)
        print("Please wear mask -- Be vaccinated")
        print("\nThank you for Visiting")
    else:
        print("\n-> You Entered Invalid option :")
        print("\n-> Try again or Enter '0' to Exit")
        MENU()
MENU()
print("\n"," "*27,f"Last Seen:{date} | {current_time}:{current_minutes}")
print("="*60)
