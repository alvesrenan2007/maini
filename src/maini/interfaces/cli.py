from src.maini.core import database
from src.maini.core import config_manager


def initial_routine():
    database.initialize_db()

    print("--- Welcome to Maini ---")
    print("\n The application succesfuly entered the initial routine")
    input("Please input any key to exit.")
