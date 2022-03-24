# CRUD to use with PostgreSQL

## USAGE
from database import Database

### SELECT
query = """ 
            SELECT * FROM hy_users; 
        """

result = Database.select(query)
print(result)

### INSERT UPDATE DELETE
query = """ 
            UPDATE hy_users SET banned = %s WHERE nickname = %s; 
        """

values = [False, "Krolik"]
Database.update(query, values)