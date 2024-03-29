from peewee import *

expensedb = SqliteDatabase("exptracker.db")

class User(Model):
	username = CharField()
	password = CharField()

	class Meta:
		database = expensedb


class Wallet(Model):
	owner = ForeignKeyField(User, backref="wallets")
	name = CharField()
	balance = FloatField()
	last_transaction = DateTimeField()

	class Meta:
		database = expensedb


class Transaction(Model):
	owner = ForeignKeyField(User, backref="expenses")
	wallet = ForeignKeyField(Wallet, backref="wallet_expenses")
	name = CharField()
	from_person = CharField()
	amount = FloatField()
	timestamp = DateTimeField()
	comment = TextField()
	is_expense = BooleanField()

	class Meta:
		database = expensedb

if __name__ == '__main__':
	expensedb.connect()
	expensedb.create_tables([User, Wallet, Transaction])