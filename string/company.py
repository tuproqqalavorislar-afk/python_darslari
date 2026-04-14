# from db3 import db_connect

# conn  = db_connect()
# cur = conn.cursor()
# conn.autocommit = True

# cur.execute(
#     "CREATE DATABASE company"
# )
# print("Create database")

# cur.execute(
#     """
#     CREATE TABLE worker(
#     id SERIAL PRIMARY KEY,
#     name VARCHAR(100)
#     )
#     """
# )
# print("Create table")

# cur.execute(
#     """
#     CREATE TABLE jobs(
#     id SERIAL PRIMARY KEY,
#     title VARCHAR(100)
#     )

#     """
# )
# print("Create table")

# cur.execute(
#     "INSERT INTO jobs(title) VALUES('Dizayner')"
# )
# print("Add jobs")

# cur.execute(
#     "SELECT "
# )