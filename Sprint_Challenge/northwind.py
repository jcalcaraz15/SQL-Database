import sqlite3


# DB Connect Function
conn = sqlite3.connect('north_small.sqlite3')
curs = conn.cursor()


def execute_query(curs, query):
    curs.execute(query)
    conn.commit()
    return curs.fetchall()


expensive_items = '''
    SELECT *
    FROM Product
    ORDER BY UnitPrice DESC
    LIMIT 10;
'''

avg_hire_age = '''
    SELECT AVG(HireDate - BirthDate) AS avg_hire_age FROM Employee
'''

ten_most_expensive = '''
    SELECT Product.ProductName, Product.UnitPrice, Supplier.CompanyName
    FROM Product
    INNER JOIN Supplier ON Product.SupplierId = Supplier.Id
    ORDER BY UnitPrice DESC
    LIMIT 10;
'''

largest_category = '''
    SELECT Category.CategoryName, COUNT(DISTINCT Product.ProductName)
    FROM Product
    JOIN Category ON Product.CategoryId = Category.Id
    GROUP BY Product.CategoryId
    ORDER BY COUNT(DISTINCT Product.ProductName) DESC
    LIMIT 1;
'''

NORTHWIND_QUERIES = [expensive_items,
                     avg_hire_age,
                     ten_most_expensive,
                     largest_category]


if __name__ == '__main__':
    execute_query(curs, NORTHWIND_QUERIES)
