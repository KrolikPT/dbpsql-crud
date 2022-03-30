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
    
    ##########################################################
    # INSERT, UPDATE AND DELETE 
    ##########################################################
    def __init__(self, query, values):
        try:
            with db_connection() as conn:
                with conn.cursor() as cursor:
                    cursor.execute(query, values)
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            exit()


class Crud:
    
    ##########################################################
    # SELECT
    ##########################################################
    def __init__(self, query, values):
        self.values = values
        self.query = query

    def select(self):
        try:
            with db_connection() as conn:
                with conn.cursor() as cursor:
                    cursor.execute(self.query, self.values)
                    result = cursor.fetchall()
            return result
        except (Exception, psycopg2.DatabaseError) as error:
            return error
    
    ##########################################################
    # INSERT
    ##########################################################
    def insert(self):
        InsertUpdateDelete(self.query, self.values)
    
    ##########################################################
    # UPDATE
    ##########################################################
    def update(self):
        InsertUpdateDelete(self.query, self.values)
    
    ##########################################################
    # DELETE
    ##########################################################
    def delete(self):
        InsertUpdateDelete(self.query, self.values)
