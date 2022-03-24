import psycopg2


class InsertUpdateDelete:

    ##########################################################
    # INSERT, UPDATE AND DELETE 
    ##########################################################
    def __init__(self, query, values):
        try:
            with Crud.db_connection() as conn:
                with conn.cursor() as cursor:
                    cursor.execute(query, values)
        except (Exception, psycopg2.DatabaseError) as error:
            return error
        

class Crud:

    ##########################################################
    # DATABASE ACCESS
    ##########################################################
    def db_connection():
        con = psycopg2.connect(
                        user = "root",
                        password = "",
                        host = "localhost",
                        port = "5432",
                        database = "test")
        return con


    ##########################################################
    # SELECT
    ##########################################################
    def select(query, values = None):
        try:
            with Crud.db_connection() as conn:
                with conn.cursor() as cursor:
                    cursor.execute(query, values)
                    result = cursor.fetchall()
            return result
        except (Exception, psycopg2.DatabaseError) as error:
            return error


    ##########################################################
    # INSERT
    ##########################################################
    def insert(query, values):   
        InsertUpdateDelete(query, values)


    ##########################################################
    # UPDATE
    ##########################################################
    def update(query, values):
        InsertUpdateDelete(query, values)


    ##########################################################
    # DELETE
    ##########################################################
    def delete(query, values):
        InsertUpdateDelete(query, values)