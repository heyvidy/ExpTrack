from models import Transaction, Wallet, User, expensedb
from datetime import datetime

expensedb.connect()


def signup():
	username = input("Create username: ")
	password = input("Create Password: ")

	exists = len(User.select().where(User.username == username))

	if not exists: 
		User.create(username=username, password=password)
		print("User created successfully!\n\n")
	else:
		print("Username already exists. Please try new username.")

def login():
	username = input("Enter Username: ")
	password = input("Enter Password: ")

	user = User.select().where(User.username == username)

	if len(user):
		user = user.get()

		if user.password == password:
			return user.get()
		else:
			print("Invalid Password.\n\n")
	else:
		return None



def add_transaction(user):
	wallets = user.wallets
	for wallet in wallets:
		print(wallet.id, wallet.name, wallet.balance)

	ch = int(input("Choose a Wallet ID: "))

	wallet = Wallet.get(Wallet.id == ch)
	is_expense = int(input("Choose Type:\n0. Income\n1.Expense"))

	if not is_expense:
		from_person = input("From Who: ")
	else:
		from_person = "None"

	tranx_name = input("Enter Purpose: ")
	amount = float(input("Enter Amount: "))
	comment = input("Any comments? \n")

	Transaction.create(owner=user, 
		wallet=wallet, 
		name=tranx_name,
		amount=amount,
		comment=comment,
		from_person=from_person,
		timestamp=datetime.now(),
		is_expense=bool(is_expense))



def create_wallet(user):
	name = input("Enter Wallet Name: ")
	bal = input("Enter Starting Balance: ")
	Wallet.create(name=name, balance=bal, owner=user, last_transaction=datetime.now())

def check_balance(user):
	wallets = user.wallets

	for wallet in wallets:
		print(wallet.id, wallet.name, wallet.balance)

def see_transactions(user):
	transactions = user.expenses

	for txn in transactions:
		if txn.is_expense:
			print(txn.wallet, txn.name, f"-{txn.amount}", txn.timestamp)
		else: 
			print(txn.wallet, txn.name, f"+{txn.amount}", txn.timestamp)

