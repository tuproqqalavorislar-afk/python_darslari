# from db3 import connect

# conn = connect()
# conn.autocommit = True
# cur = conn.cursor()

# cur.execute(
#     "CREATE DATABASE itpark"
# )
# print("👌")

# cur.execute(
#     """CREATE TABLE students(
#     id SERIAL PRIMARY KEY,
#     name VARCHAR(100),
#     grade INT,
#     direction VARCHAR(100)
#     )"""
# )
# print("👌")

# cur.execute(
#     "INSERT INTO students(name,grade,direction) VALUES('Maftuna',9,'backend'),('Zoxira',9,'backend'),('Vali',9,'backend'),('Elbek',9,'backend'),('Sulaymon',9,'backend'),('Yoqubboy',9,'backend'),('Ulugbek',9,'backend'),('Sevinchoy',8,'fullstack')"
# )

# cur.execute(
#     "SELECT * FROM students"
    # "SELECT * FROM students ORDER BY grade"
    # "SELECT * FROM students ORDER BY direction"
    # "SELECT * FROM students LIMIT 4"
    # "SELECT COUNT (id) FROM students "
    # "SELECT * FROM students WHERE name ILIKE'M%'"
# )
# rows = cur.fetchall()
# for row in rows:
#     print(row)