# docstring - Kevin_Tang - GPU Database Application
# imports
import sqlite3

# constants and variables
DATABASE = "gpu_database.db"

# functions
def print_all_gpus():
    '''prints all the gpus nicely'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM gpus"
    cursor.execute(sql)
    results = cursor.fetchall()
    # loop through all the results
    print(f"name                          manufacturer speed_mhz price_nzd")
    for gpu in results:
        print(f"{gpu[1]:<30}{gpu[2]:<13}{gpu[3]:<10}{gpu[4]:<19}")
    # loop finished here
    db.close()

def print_all_gpus_by_speed():
    '''prints all gpus sorted by speed'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    # sort by speed_mhz in descending order
    sql = "SELECT * FROM gpus ORDER BY speed_mhz DESC"
    cursor.execute(sql)
    results = cursor.fetchall()
    # loop through all the results
    print(f"name                          manufacturer speed_mhz price_nzd")
    for gpu in results:
        print(f"{gpu[1]:<30}{gpu[2]:<13}{gpu[3]:<10}{gpu[4]:<19}")
    # loop finished here
    db.close()

def print_all_gpus_by_price():
    '''prints all gpus sorted by price'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    # sort by price_nzd in descending order
    sql = "SELECT * FROM gpus ORDER BY price_nzd DESC"
    cursor.execute(sql)
    results = cursor.fetchall()
    # loop through all the results
    print(f"name                          manufacturer speed_mhz price_nzd")
    for gpu in results:
        print(f"{gpu[1]:<30}{gpu[2]:<13}{gpu[3]:<10}{gpu[4]:<19}")
    # loop finished here
    db.close()

# main code
while True:
    user_input = input("""What would you like to do.
1. Print all aircraft
2. Print all aircraft sorted by speed
3. Print all aircraft sorted by cost
4. Exit
""")

    if user_input == "1":
        print_all_gpus()
    elif user_input == "2":
        print_all_gpus_by_speed()
    elif user_input == "3":
        print_all_gpus_by_price()
    elif user_input == "4":
        print("Goodbye!")
        break
    else:
        print("That was not an option\n")