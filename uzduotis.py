import sqlite3


def open_connection():
    connection = sqlite3.connect("exercise.db")
    cursor = connection.cursor()
    return connection, cursor


def close_connection(connection):
    connection.close()


def db_query(query, query_parameters=None):
    try:
        connect, cursor = open_connection()
        if query_parameters:
            cursor.execute(query, query_parameters)
            connect.commit()
        else:
            for i in cursor.execute(query):
                print(i)
    except sqlite3.DataError as error:
        print(error)
    finally:
        close_connection(connect)

def exercise1_1():
    query = """ SELECT first_name, last_name, salary
                FROM employees
                WHERE salary NOT BETWEEN 10000 AND 15000"""
    db_query(query)


def exercise1_2():
    query = """SELECT first_name, last_name, department_id
                FROM employees
                WHERE department_id IN (30, 100)
                ORDER BY department_id ASC """
    db_query(query)


def exercise1_3():
    query = """SELECT first_name, last_name, salary
                FROM employees 
                WHERE salary NOT BETWEEN 10000 AND 15000 AND department_id IN (30, 100)"""
    db_query(query)


def exercise1_4():
    query = """SELECT first_name
                FROM employees
                WHERE first_name LIKE '%b%
                AND first_name LIKE '%c%'"""
    db_query(query)


def exercise1_5():
    query = """ SELECT last_name, job_id, salary
                FROM employees 
                WHERE job_id IN ('IT_PROG','ST_CLERK') and
                salary NOT IN (4500, 10000, 15000)"""
    db_query(query)


def exercise1_6():
    query = """SELECT last_name
                FROM employees 
                WHERE last_name LIKE '______'"""
    db_query(query)

def exercise1_7():
    query = """SELECT last_name
                FROM employees 
                WHERE last_name LIKE '__e%'"""
    db_query(query)

def exercise2_1():
    query = """ SELECT COUNT (DISTINCT job_id)
                FROM employees"""
    db_query(query)

def exercise2_2():
    query = """ SELECT SUM(salary)
                FROM employees"""
    db_query(query)

def exercise2_3():
    query = """ SELECT MIN(salary)
                FROM employees"""
    db_query(query)

def exercise2_4():
    query = """ SELECT MAX(salary)
                FROM employees"""
    db_query(query)

def exercise2_5():
    query = """ SELECT AVG(salary), COUNT(employee_id)
                FROM employees
                WHERE department_id = 90"""
    db_query(query)

def exercise2_6():
    query = """ SELECT MAX(salary), MIN(salary), AVG(salary), SUM(salary)
                FROM employees"""
    db_query(query)

def exercise2_7():
    query = """ SELECT  COUNT(DISTINCT job_id)
               FROM employees"""
    db_query(query)

def exercise2_8():
    query = """SELECT MAX(salary) - MIN(salary)
               FROM employees """
    db_query(query)

def exercise2_9():
    query = """ SELECT department_id, SUM(salary)
                FROM employees
                GROUP BY department_id"""
    db_query(query)

def exercise2_10():
    query = """ SELECT job_id, AVG(salary)
                FROM employees
                WHERE job_id <> 'IT_PROG'
                GROUP BY job_id"""
    db_query(query)

def exercise2_11():
    query = """ SELECT manager_id, MIN(salary)
                FROM employees
                GROUP BY manager_id"""
    db_query(query)

def exercise3_01():
    query = """ SELECT first_name, last_name, salary
                FROM employees
                WHERE salary > 
                (SELECT salary FROM employees WHERE last_name='Bull')"""
    db_query(query)

def exercise3_02():
    query = """SELECT first_name, last_name
                FROM employees
                WHERE (employee_id IN (SELECT manager_id FROM employees))"""
    db_query(query)

def exercise3_03():
    query = """SELECT First_name, last_name, salary
                FROM employees
                WHERE salary > (SELECT AVG(salary) FROM employees)"""
    db_query(query)

def exercise3_04():
    query = """ SELECT first_name, last_name, salary
                FROM employees
                WHERE salary = (SELECT MIN(salary) FROM employees)"""
    db_query(query)

def exercise3_05():
    query = """ SELECT first_name, last_name, salary
                FROM employees 
                WHERE salary > (SELECT AVG(salary) FROM employees) AND 
                department_id IN (SELECT department_id FROM departments WHERE depart_name LIKE "%IT%")"""
    db_query(query)

def exercise3_06():
    query = """SELECT salary 
               FROM employees
               ORDER BY salary DESC 
               LIMIT 3"""
    db_query(query)

def exercise3_07():
    query = """SELECT first_name, last_name
               FROM employees
               WHERE manager_id IN (SELECT manager_id FROM departments WHERE location_id IN 
               (SELECT location_id FROM locations WHERE country_id LIKE "%US%"))              
               """
    db_query(query)

#Write a query to get the department name and number of employees in the department
def exercise4_01():
    query = """SELECT departments.depart_name, COUNT(employees.employee_id)
               FROM employees
               INNER JOIN departments
                    ON employees.department_id = departments.department_id
                GROUP BY depart_name"""
    db_query(query)

#Write a query to display the department ID, department name, and managers first name.
def exercise4_02():
    query = """ SELECT employees.first_name, employees.manager_id, departments.depart_name, employees.department_id
                FROM employees
                INNER JOIN departments
                    ON employees.department_id = departments.department_id"""
    db_query(query)

#Write a query to display the department name, manager name, and city.
def exercise4_03():
    query = """ SELECT employees.first_name, locations.city, departments.depart_name
                FROM employees
                JOIN departments
                    ON employees.manager_id = departments.manager_id
                JOIN locations ON departments.Location_ID = locations.location_id
                 """
    db_query(query)

#Write a query to display the job history that was done by any employee who is currently drawing more than 10000 of salary.
def exercise4_04():
    query = """SELECT job_history.*
               FROM job_history
               JOIN employees
                  ON job_history.employee_id = employees.employee_id
               WHERE salary > 10000"""
    db_query(query)


#Write a query to display the job title and average salary of employees.
def exercise4_05():
    query = """SELECT Job_Title, AVG(salary)
                FROM employees
                JOIN jobs
                    ON employees.job_id = jobs.Job_ID
                GROUP BY job_Title"""
    db_query(query)

def exercise4_06():
    query = """SELECT employee_ID, Job_Title, end_date - start_date
                FROM job_history
                JOIN Jobs
                    ON jobs.Job_ID = job_history.job_id
                WHERE department_id = 90"""
    db_query(query)

#Write a query to find the names (first_name, last_name) and hire date of the employees who were hired after 'Jones'
def exercise4_07():
    query = """ SELECT employees.first_name, employees.last_name, employees.hire_date
                FROM employees
                JOIN employees Jones
                    ON Jones.last_name = "Jones"
                WHERE employees.hire_date > Jones.hire_date """
    db_query(query)


open_connection()
exercise4_07()
close_connection(sqlite3.connect("exercise.db"))


