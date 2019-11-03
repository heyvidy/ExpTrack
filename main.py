from app import *

while True:
	print("-"*20)
	print("Welcome to Exp Tracker")
	print("-"*20)


	ch = input("What would you like to do?\n1.Login\n2.Signup\n-->")

	if ch == "1":
		user = login()

		if user is not None: 
			choice = input("Choose Operations:\n1.Add a Transaction\n2.Create Wallet\n3.Check Balance\n")
			
			if choice == "1":
				add_transaction(user)
			elif choice == "2":
				create_wallet(user)
			elif choice == "3":
				check_balance(user)
			elif choice == "4":
				see_transactions(user)
			else:
				continue
		else:
			print("Credentials do not match. Or Create New Account.")

	elif ch == "2":
		signup()

	else: 
		break