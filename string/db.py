# import psycopg2

# ulash = psycopg2.connect(
#     host = "localhost",
#     database = "market",
#     user = "postgres",
#     password = "VORISLAR2026"

# )
# ishlatish = ulash.cursor()

# ishlatish.execute(
#     "INSERT INTO mahsulot(name,number,price) VALUES ('orik',35,'10000')"
# )
# ulash.commit()

# ishlatish.execute(
#     "SELECT * FROM mahsulot"
# )
# ustunlar = ishlatish.fetchall()
# for ustun in ustunlar:
#     print(ustun)

# ishlatish.execute(
#     "UPDATE mahsulot SET number = 15000 WHERE id=9"
# )
# ulash.commit()

# ishlatish.execute(
#     "DELETE FROM mahsulot WHERE id=15"
# )
# ulash.commit()