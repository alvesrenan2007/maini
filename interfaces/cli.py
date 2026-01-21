from core import database


def main_loop():
    database.initialize_db()

    print("--- Welcome to Maini ---")
    running = True

    while running:
        print("\n The application succesfuly entered the main loop")
        input("Please input any key to exit.")

        break
