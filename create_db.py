import sqlite3

con = sqlite3.connect(":memory")

cur = con.cursor()

# drop table
cur.execute("DROP TABLE stretches;")

# create database
cur.execute(
    '''CREATE TABLE IF NOT EXISTS stretches(
        excercise text,
        excercise_doublesite integer,
        max_hold_duration integer,
        triggered_part text
    )
    '''
)

# write dummy into db
dummy_excercises = [
    ('pigeon', 0, None, 'it-band'),
    ('forward fold', 1, None, 'backchain'),
    ('saddle', 1, None, 'quads'),
    ('puppy dog', 0, None, 'shoulders')
]

cur.executemany('INSERT INTO stretches VALUES(?,?,?,?);', dummy_excercises)

# commit statement
con.commit()

for row in cur.execute('SELECT * FROM stretches'):
    print(row)
