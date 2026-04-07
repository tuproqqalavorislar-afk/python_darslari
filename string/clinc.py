from db3 import db_connect

conn  = db_connect()
cur = conn.cursor()
conn.autocommit = True

# cur.execute(
#     "CREATE DATABASE clinic"
# )
# print("Create database")

# cur.execute(
#     """
#     CREATE TABLE patients(
#     id SERIAL PRIMARY KEY,
#     name VARCHAR(100)
#     )
#     """
# )
# print("Create table")

# cur.execute(
#     """
#     CREATE TABLE doctors(
#     id SERIAL PRIMARY KEY,
#     name VARCHAR(100)
#     )
#     """
# )
# print("Create table")

# cur.execute(
#     """
#     CREATE TABLE clinc(   
#     patients_id INTEGER,
#     doctors_id INTEGER
#     )
#     """
# )
# print("Create table")

# cur.execute(
#     "INSERT INTO patients(name) VALUES('Zoxira')"
# )
# print("Add patients")

# cur.execute(
#     "INSERT INTO patients(name) VALUES('Sevinchoy')"
# )
# print("Add patients")

# cur.execute(
#     "INSERT INTO patients(name) VALUES('Egamberdi')"
# )
# print("Add patients")

# cur.execute(
#     "INSERT INTO doctors(name) VALUES('Mirzabek')"
# )
# print("Add doctors")

# cur.execute(
#     "INSERT INTO doctors(name) VALUES('Kamoladdin')"
# )
# print("Add doctors")

# cur.execute(
#     "INSERT INTO clinic(name) VALUES('GRAND CLINIC')"
# )
# print("Successlly add")

# cur.execute(
#     "INSERT INTO clinc (patients_id,doctors_id) VALUES(1,2),(2,1),(3,2)"
# )
# print('added')

# cur.execute(
#     "SELECT patients.name,doctors.name FROM clinc JOIN patients ON patients.id=clinc.patients_id JOIN doctors ON doctors.id=clinc.doctors_id "
# )
# rows = cur.fetchall()
# for row in rows:
#     print(rows)
