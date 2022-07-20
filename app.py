import sqlite3
import time

con = sqlite3.connect(":memory")

cur = con.cursor()


for row in cur.execute('SELECT * FROM stretches'):
    print(row)


# ask user for input - how long should the stretch be?
user_input = input("How long do you want to stretch in minutes?")

# transform user input into seconds
user_input = int(user_input) * 60

# select random excercise from stretches table
# cur.execute("SELECT * FROM stretches ORDER BY RANDOM() LIMIT 1;").fetchall()[0]

# select random excersis as long as there is time left
time_elapsed = 0
while(time_elapsed < user_input):
    excercise = cur.execute(
        "SELECT * FROM stretches ORDER BY RANDOM() LIMIT 1;").fetchall()[0]
    excercise_stretch = excercise[0]
    # time_to_stretch should get value from an function that selects random time based on restrictions
    time_to_stretch = 60
    print(
        f"Do the excercise {excercise_stretch} for {str(time_to_stretch)} seconds")
    while (time_to_stretch > 0):
        print(time_to_stretch)
        time.sleep(1)
        time_to_stretch -= 1
    time_elapsed += time_to_stretch


# close connection to the database
con.close()
