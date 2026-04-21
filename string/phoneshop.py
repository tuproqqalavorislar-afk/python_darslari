from db3 import db_connect

conn  = db_connect()
cur = conn.cursor()
conn.autocommit = True

# cur.execute(
#     "CREATE DATABASE phoneshop"
# )


# cur.execute(
#     """
#     CREATE TABLE phones (
#     id SERIAL PRIMARY KEY,
#     brand VARCHAR(80),
#     model VARCHAR(100),
#     price NUMERIC(10,2)
#     )

#     """
# )
# print("Create table")
 
# cur.execute(
#     "INSERT INTO phones(brand,model,price) VALUES('Samsung Galaxy',' A07',1500000),('Samsung Galaxy',' A17',2000000),('Samsung Galaxy',' A26 5G',3000000),('Samsung Galaxy',' A37 5G',4500000),('Samsung Galaxy',' A57 5G',5500000),('Samsung Galaxy',' S25',9000000),('Samsung Galaxy',' S25 Plus',11000000),('Samsung Galaxy',' S26 Ultra',15000000),('Samsung Galaxy',' Z Flip 7',13000000),('Samsung Galaxy',' Z Fold 7',20000000),('iPhone','iphone 13',6000000),('iPhone','iphone 14',8000000),('iPhone','iphone 15',10000000),('iPhone','iphone 15 Pro Max',14000000),('Honor','honor X7',2500000),('Honor','honor X8',3000000),('Honor','honor 90',5000000),('Honor','Magic 6',9000000)"
# )
# print('added')

# cur.execute(
#     "SELECT * FROM phones WHERE brand in ('Samsung Galaxy')"
#     # "SELECT * FROM phones"
# )

# cur.execute(
    # "SELECT * FROM phones WHERE price BETWEEN 3000000 AND 10000000"
    # "SELECT * FROM phones WHERE brand BETWEEN 'I' AND 'Z'"
#     "SELECT id AS tartib_raqam FROM phones "
# )

# rows = cur.fetchall()
# for row in rows:
#     print(row)