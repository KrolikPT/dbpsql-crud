# CRUD to use with PostgreSQL

## REQUIREMENTS
pip install psycopg2    

## USAGE
from dbcrud import Crud

### EXAMPLE: SELECT
query = """ 
            SELECT * FROM table; 
        """

result = Crud.select(query)

print(result)

### EXAMPLE: SELECT WITH VALUES
query = """ 
            SELECT * FROM table WHERE id = %s; 
        """

values = [1]

result = Crud.select(query, values)

print(result)

### EXAMPLE: INSERT UPDATE DELETE
query = """ 
            UPDATE table SET nickname = %s WHERE id = %s; 
        """

values = ["John Doe", 1]

Crud.update(query, values)