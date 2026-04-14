# import psycopg2
# def db_connect():
#     conn = psycopg2.connect(
#         host = "localhost",
#         database = "learning_center",
#         user = "postgres",
#         password = "VORISLAR2026"
#     )
#     return conn
# import psycopg2
# def db_connect():
#     conn = psycopg2.connect(
#         host = "localhost",
#         database = "kompaniya",
#         user = "postgres",
#         password = "VORISLAR2026"
#     )
#     return conn

# import psycopg2
# def db_connect():
#     conn = psycopg2.connect(
#         host = "localhost",
#         database = "clinic",
#         user = "postgres",
#         password = "VORISLAR2026"
#     )
#     return conn

# import psycopg2
# def db_connect():
#     conn = psycopg2.connect(
#         host = "localhost",
#         database = "postgres",
#         user = "postgres",
#         password = "VORISLAR2026"
#     )
#     return conn

import psycopg2
def db_connect():
    conn = psycopg2.connect(
        host = "localhost",
        database = "inner_join",
        user = "postgres",
        password = "VORISLAR2026"
    )
    return conn