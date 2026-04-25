from db3 import db_connect

conn  = db_connect()
cur = conn.cursor()
conn.autocommit = True


# cur.execute(
#     "CREATE DATABASE inner_join"
# )

# cur.execute(
#     """
#     CREATE TABLE talaba (
#     id SERIAL PRIMARY KEY,
#     name VARCHAR(100)
#     )

#     """
# )
# print("Create table") 

cur.execute(
    """
    CREATE TABLE kursi(
    id SERIAL PRIMARY KEY,
    kurs VARCHAR(100)
    )

    """
)
print("Create table")

# cur.execute(
#     "INSERT INTO talaba(name) VALUES('Jasur') "
# )
# print("Add talabalar") 

# cur.execute(
# "INSERT INTO kursi(kurs) VALUES('Dizayner')"
# )
# print("Success") 

# cur.execute(
#     "SELECT talaba.name , kursi.kurs FROM talaba LEFT JOIN kursi ON talaba.id = kursi.id"
# )

# rows = cur.fetchall()
# for row in rows:
#     print(row)