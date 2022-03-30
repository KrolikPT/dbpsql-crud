import psycopg2


##########################################################
# DATABASE ACCESS
##########################################################
def db_connection():
    con = psycopg2.connect(
        user="root",
        password="",
        host="localhost",
        port="5432",
        database="test")
    return con


class InsertUpdateDelete:
    
    def __init__(self, query, values):
        self.query = query
        self.values = values
    
        try:
            with db_connection() as conn:
                with conn.cursor() as cursor:
                    cursor.execute(self.query, self.values)
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            exit()


class Crud:

    def select(query, values):
        try:
            with db_connection() as conn:
                with conn.cursor() as cursor:
                    cursor.execute(query, values)
                    result = cursor.fetchall()
            return result
        except (Exception, psycopg2.DatabaseError) as error:
            return error
    
    
    def insert(query, values):
        InsertUpdateDelete(query, values)
        
    
    def update(query, values):
        InsertUpdateDelete(query, values)
        
        
    def delete(query, values):
        InsertUpdateDelete(query, values)
