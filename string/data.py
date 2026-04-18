# from db3 import db_connect

# conn  = db_connect()
# cur = conn.cursor()
# conn.autocommit = True

# # cur.execute(
# #     "CREATE DATABASE dokon"
# # )

# cur.execute(
#     """
#     CREATE TABLE product (
#     id SERIAL PRIMARY KEY,
#     name VARCHAR(100),
#     price NUMERIC(10,2)
#     )

#     """
# )
# print("Create table") 


# cur.execute(
#     "INSERT INTO product (name,price) VALUES('olma',10000),('non', 3000), ('sut', 10000), ('guruch', 18000), ('shakar', 14000), ('tuxum', 22000), ('kartoshka', 6000), ('piyoz', 5000), ('sabzi', 4000), ('tovuq goshti', 35000), ('mol goshti', 90000), ('olma', 12000), ('banan', 20000)"
# )
# print("added") 

# cur.execute(
#     # "SELECT * FROM product WHERE price >= 10000"
#     # "SELECT max(price) FROM product"
#     # "SELECT min(price) FROM product"
#     # "SELECT AVG(price) FROM product"
#     # "SELECT COUNT(id) FROM product"
#     # "SELECT SUM(price) FROM product"
# )
# rows = cur.fetchall()
# for row in rows:
#     print(row)