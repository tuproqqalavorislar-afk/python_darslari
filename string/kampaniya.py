from db3 import db_connect

conn  = db_connect()
cur = conn.cursor()
conn.autocommit = True

# cur.execute(
#     "CREATE DATABASE kompaniya"
# )
# print("Create database")

# cur.execute(
#     """
#     CREATE TABLE worker(
#     id SERIAL PRIMARY KEY,
#     name VARCHAR(100),
#     duty VARCHAR(100)
#     )
#     """
# )
# print("Create table")

# cur.execute(
#     """
#     CREATE TABLE company(
#     id SERIAL PRIMARY KEY,
#     name VARCHAR(100)
#     )

#     """
# )
# print("Create table")

# cur.execute(
#     """
#     CREATE TABLE staff(   
#     worker_id INTEGER,
#     company_id INTEGER,
#     duty_id INTEGER
#     )

#     """
# )
# print("Create table")

# cur.execute(
#     "INSERT INTO worker(name,duty) VALUES('Zoxira','frontend')"
# )
# print("Add worker")

# cur.execute(
#     "INSERT INTO company(name) VALUES('HYPE')"
# )
# print("Success")

# cur.execute(
#     "SELECT * FROM staff"
# )
# rows = cur.fetchall()
# print(rows)

# cur.execute(
#     "INSERT INTO staff(worker_id,company_id) VALUES(1,1)"
# )


# cur.execute(
#     "SELECT worker.name,company.name,worker.duty FROM staff JOIN worker ON worker.id=staff.worker_id JOIN company ON company.id=staff.company_id"
# )
# rows = cur.fetchall()
# for row in rows:
#     print(row)