import random
import re
from sqlalchemy.orm import Session
from parte_1.models import User
from parte_1.models import Agency
from parte_1.models import UserAccount
from sqlalchemy import inspect
from parte_1.models import engine
from sqlalchemy import text


inspect_engine = inspect(engine)


class DatabaseHandler:

    def __init__(
            self, name, surname, cpf, agency_number, agency_city, agency_state,
            agency_country, account_number, account_type
    ):

        self.name = name
        self.surname = surname
        self.cpf = re.sub(pattern='[^\w$]', repl='', string=cpf)
        self.agency_number = agency_number
        self.agency_city = agency_city
        self.agency_state = agency_state
        self.agency_country = agency_country
        self.account_number = account_number
        self.account_type = account_type

    def create_records(self):
        with Session(engine) as session:
            user = User(
                name=self.name,
                surname=self.surname,
                cpf=self.cpf
            )
            agency = session.query(Agency).filter_by(
                agency_number=self.agency_number).first()

            if not agency:
                agency = Agency(
                    agency_number=self.agency_number,
                    agency_city=self.agency_city,
                    agency_state=self.agency_state,
                    agency_country=self.agency_country
                )
                session.add(agency)

            session.add(user)
            session.flush()

            user_account = UserAccount(
                account_number=self.account_number,
                account_type=self.account_type,
                user_id=user.id,
                agency_id=agency.id
            )
            session.add(user_account)
            session.commit()


def bulk_add_account(names, surnames, cpfs,
                     agencies_number, agencies_city, agencies_state, agencies_country,
                     accounts_number, accounts_type):
    for name, surname, cpf, agency_number, agency_city, agency_state, agency_country, account_number, account_type in zip(
            names, surnames, cpfs, agencies_number, agencies_city, agencies_state, agencies_country, accounts_number, accounts_type
    ):
        data_handler = DatabaseHandler(
            name=name,
            surname=surname,
            cpf=cpf,
            agency_number=agency_number,
            agency_city=agency_city,
            agency_state=agency_state,
            agency_country=agency_country,
            account_number=account_number,
            account_type=account_type
        )
        data_handler.create_records()


names = [
    'John', 'Alice', 'Bob', 'Emma', 'Michael', 'Olivia', 'William', 'Sophia', 'James', 'Ava'
]

surnames = [
    'Doe', 'Smith', 'Johnson', 'Brown', 'Taylor', 'Miller', 'Anderson', 'Wilson', 'Moore', 'Jackson'
]

cpfs = [
    '12345678900', '98765432100', '56789012300', '13579246800', '86420975300', '24681357900', '97531086400', '86427531000', '53108642700', '42753108600'
]

numbers = [1234, 5678, 9101]
agencies_number = [random.choice(numbers) for _ in range(10)]
cities = ['New York', 'Los Angeles', 'Chicago', 'San Francisco']
agencies_city = [random.choice(cities) for _ in range(10)]
states = ['NY', 'CA', 'IL', 'CA']
agencies_states = [random.choice(states) for _ in range(10)]

countries = ['USA', 'CA', 'MEX']
agencies_countries = [random.choice(countries) for _ in range(10)]
accounts_number = random.sample(range(10000, 100000), 10)
types = ['Savings', 'Checking', 'Investment']
accounts_type = [random.choice(types) for _ in range(10)]

bulk_add_account(names, surnames, cpfs, agencies_number, agencies_city,
                 agencies_states, agencies_countries, accounts_number, accounts_type)

with Session(engine) as session:
    user_accounts = session.query(UserAccount).join(
        Agency).filter(Agency.agency_city == "Los Angeles").all()

    for user_account in user_accounts:
        print(f"User ID: {user_account.user_id}")
        print(f"Account Number: {user_account.account_number}")
        print(f"Account Type: {user_account.account_type}")
        print(f"Agency ID: {user_account.agency_id}")
        print("\n")

with engine.begin() as conn:
    query = text("SELECT account_number, account_type, agency_city FROM user_account INNER JOIN agency ON user_account.agency_id = agency.id WHERE agency_id = :agency_id")
    result = conn.execute(query, {'agency_id': 1})
    for row in result:
        print(row)
