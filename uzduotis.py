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
                WHERE last_name LIKE '__e___'"""
    db_query(query)

open_connection()
exercise1_7()
close_connection(sqlite3.connect("exercise.db"))


