import psycopg2, os

##########################################################
# DATABASE ACCESS
##########################################################
class InsertUpdateDelete:

    def __init__(self, query, values):
        try:
            with Database.db_connection() as conn:
                with conn.cursor() as cursor:
                    cursor.execute(query, values)
        except (Exception, psycopg2.DatabaseError) as error:
            return error
        

class Crud:
    def db_connection():
        con = psycopg2.connect(
                        user = "root",
                        password = "",
                        host = "localhost",
                        port = "5432",
                        database = "test")
        return con


    def select(query, values = None):
        try:
            with Database.db_connection() as conn:
                with conn.cursor() as cursor:
                    cursor.execute(query, values)
                    result = cursor.fetchall()
            return result
        except (Exception, psycopg2.DatabaseError) as error:
            return error


    def update(query, values):
        InsertUpdateDelete(query, values)


    def insert(query, values):
        InsertUpdateDelete(query, values)


    def delete(query, values):
        InsertUpdateDelete(query, values)