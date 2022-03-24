# CRUD to use with PostgreSQL

## REQUIREMENTS
pip install psycopg2    

## USAGE
from database import Database

### EXAMPLE: SELECT
query = """ 
            SELECT * FROM hy_users; 
        """

result = Database.select(query)

print(result)

### EXAMPLE: INSERT UPDATE DELETE
query = """ 
            UPDATE hy_users SET banned = %s WHERE nickname = %s; 
        """

values = [False, "Krolik"]

Database.update(query, values)