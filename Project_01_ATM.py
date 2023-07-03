#Project 01 ATM

import mysql.connector
import random

import datetime

mydb = mysql.connector.connect(
  host="localhost",
  user="karthi",
  password="password",
  database="std"
)
mycursor = mydb.cursor()

def create():
	print()
	print("ACCOUNT CREATION".center(40,"-"))
	acc_name = input("\n\tEnter your name: ")
	acc_num = random.randrange(11111111,99999999)
	acc_pw = input("\tEnter your account password: ")
	acc_bal = 0
	sql = "INSERT INTO atm(acc_num, acc_name, acc_pw, acc_bal) VALUES (%s, %s, %s, %s)"
	val = (acc_num, acc_name, acc_pw, acc_bal)
	mycursor.execute(sql, val)
	mydb.commit()
	print("\n\tCongratulations! Account created successfully......\n")
	print(f"\tYour account number is {acc_num}")
	print(f"\tYour account password is {acc_pw}")
	user()

def user():
	try:
		global acc_num, acc_pw
		acc_num = int(input("\n\tEnter your account number: "))
		acc_pw = int(input("\tEnter your account password: "))
		mycursor.execute(f"SELECT * FROM atm where acc_num={acc_num} and acc_pw={acc_pw}")
		myresult = mycursor.fetchall()
		services()
	except IndexError:
		print("\n\tInvalid Credentials")
		user()
	
def services():
	global acc_name, acc_bal
	mycursor.execute(f"SELECT * FROM atm where acc_num={acc_num} and acc_pw={acc_pw}")
	myresult = mycursor.fetchall()
	acc_name=myresult[0][1]
	acc_bal=myresult[0][3]
	print("""
		*********************
			Menu:
			1. Account Detail
			2. Deposit
			3. Withdraw
			4. Exit
		*********************
			""")
	while True:
		opt2=int(input("\tEnter your option : "))
		if opt2 == 1:
			acc_dtl(acc_num, acc_name, acc_bal)
		elif opt2 == 2:
			acc_deposit(acc_num, acc_bal)
		elif opt2 == 3:
			acc_withdraw(acc_num, acc_bal)
		elif opt2 == 4:
			acc_exit()
		else:
			print("\tError: Enter 1, 2, 3, 4, or 5 only!\n")

def acc_dtl(acc_num, acc_name, acc_bal):
	print("\n\t----------ACCOUNT DETAILS----------")
	print(f"\tAccount Holder: {acc_name.capitalize()}")
	print(f"\tAccount Number: {acc_num}")
	print(f"\tAvailable balance: {acc_bal}\n")
	opt3=int(input("\tPress 1 to continue, 0 to exit : "))
	if opt3==1:
		services()
	else:
		acc_exit()

def acc_deposit(acc_num, acc_bal):
	amount = int(input("\n\tHow much you want to deposit : "))
	acc_bal=acc_bal+amount
	sql = f"UPDATE atm SET acc_bal = {acc_bal} WHERE acc_num = {acc_num}"
	mycursor.execute(sql)
	mydb.commit()
	print(f"\t{amount} scuccessfully deposited.")
	print(f"\tAvailable balance: {acc_bal}\n")
	opt3=int(input("\tPress 1 to continue, 0 to exit : "))
	if opt3==1:
		services()
	else:
		acc_exit()

def acc_withdraw(acc_num, acc_bal):
	amount = int(input("\n\tHow much you want to withdraw : "))
	if amount>acc_bal:
		print("\tYou do not have that much money!")
		print(f"\tAvailable balance: {acc_bal}\n")
		services()
	else:
		acc_bal=acc_bal-amount
		sql = f"UPDATE atm SET acc_bal = {acc_bal} WHERE acc_num = {acc_num}"
		mycursor.execute(sql)
		mydb.commit()
		print(f"\t{amount} scuccessfully withdrawed.")
		print(f"\tAvailable balance: {acc_bal}\n")
		opt3=int(input("\tPress 1 to continue, 0 to exit : "))
		if opt3==1:
			services()
		else:
			acc_exit()

def acc_exit():
	print(f"""
\tprinting receipt..............

\t******************************************
\tTransaction is now complete.                         
\tTransaction number: {random.randint(10000, 1000000)}
\tTime of transaction: {datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")}
\tAccount holder: {acc_name.upper()}                  
\tAccount number: {acc_num}                
\tAvailable balance: Nu.{acc_bal}                    
\t******************************************

\tThanks for choosing us as your bank                  
            """)
	exit()

print()
print("WELCOME TO BANK OF KARTHI".center(40,"*"))
print("\n\tIf you have a account enter 1\n\tIf you want to create a account enter 2\n")
while True:
	opt1=input("\tYour option : ")
	if opt1=="1":
		user()
		break
	elif opt1=="2":
		create()
		break
	else:
		print("\tEnter option only between 1 and 2..!")