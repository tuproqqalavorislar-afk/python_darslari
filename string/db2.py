import psycopg2

ulash = psycopg2.connect(
    host = "localhost",
    database = "it_park",
    user = "postgres",
    password = "VORISLAR2026"
)
ulash.autocommit = True
ishlatish = ulash.cursor()
# ishlatish.execute("CREATE DATABASE it_park")
# ishlatish.execute(
#     """
#     CREATE TABLE students(
#     id SERIAL PRIMARY KEY,
#     name VARCHAR(100),
#     age INTEGER ,
#     subject VARCHAR(100)
#     )
#     """
# )
# ishlatish.execute(
#     "INSERT INTO students(name,age,subject) VALUES ('Sevinchoy',12,'fullstack')"
# )

# ishlatish.execute(
#     "INSERT INTO students(name,age,subject) VALUES ('Zoxira',15,'frontend')"
# )

# ishlatish.execute(
#     "INSERT INTO students(name,age,subject) VALUES ('Maftuna',16,'AI')"
# )

# ishlatish.execute(
#     "INSERT INTO students(name,age,subject) VALUES ('Rayhona',14,'mobil')"
# )

# ishlatish.execute(
#     "INSERT INTO students(name,age,subject) VALUES ('Shohrux',10,'savodxonlik')"
# )

# ishlatish.execute(
#     "INSERT INTO students(name,age,subject) VALUES ('Rayhona',14,'backend')"
# )

# ishlatish.execute(
#     "SELECT * FROM students"
# )
# ustunlar = ishlatish.fetchall()
# for ustun in ustunlar:
#     print(ustun)

# ishlatish.execute(
#     "UPDATE students SET age=age+1 WHERE id=1",
#     "UPDATE students SET subject ='backend' WEHERE id=2"
# )

# ishlatish.execute(
#     "DELETE FROM students WHERE id=6"
# )
# ishlatish.execute("CREATE DATABASE it_park")
# ishlatish.execute(
#     """
#     CREATE TABLE teachers(
#     id SERIAL PRIMARY KEY,
#     name VARCHAR(100),
#     subject VARCHAR(100)
#     )
#     """
# )
# ishlatish.execute(
#     "INSERT INTO teachers(name,subject) VALUES ('Mirzabek','fullstack')"
# )

# ishlatish.execute(
#     "INSERT INTO teachers(name,subject) VALUES ('Vali','frontend')"
# )

# ishlatish.execute(
#     "INSERT INTO teachers(name,subject) VALUES ('Sevinchoy','AI')"
# )

# ishlatish.execute(
#     "INSERT INTO teachers(name,subject) VALUES ('Laylo','mobil')"
# )

# ishlatish.execute(
#     "INSERT INTO teachers(name,subject) VALUES ('Shohrux','savodxonlik')"
# )

# ishlatish.execute(
#     "INSERT INTO teachers(name,subject) VALUES ('Rayhona','frontend')"
# )

# ishlatish.execute(
#     "SELECT * FROM teachers"
# )
# ustunlar = ishlatish.fetchall()
# for ustun in ustunlar:
#     print(ustun)

# ishlatish.execute(
#     "UPDATE teachers SET name = 'Murod' WHERE id=5",
#     "UPDATE teachers SET subject ='backend' WEHERE id=2"
# )

# ishlatish.execute(
#     "DELETE FROM teachers WHERE id=6"
# )