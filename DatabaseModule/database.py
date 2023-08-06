import mysql.connector
import bcrypt
import re

# MySQL configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'crime_reporting_db',
}


def connect_to_database():
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()
        return connection, cursor
    except mysql.connector.Error as err:
        pass
        # print("Error connecting to MySQL: ", err)
        return None, None


def fetch_users():
    connection, cursor = connect_to_database()
    if connection and cursor:
        try:
            query = "SELECT * FROM login_table"
            cursor.execute(query)
            columns = [column[0] for column in cursor.description]
            users = []
            for row in cursor.fetchall():
                user_dict = {}
                for i, col in enumerate(columns):
                    user_dict[col] = row[i]
                users.append(user_dict)
            return users
        except mysql.connector.Error as err:
            # print("Error executing query: ", err)
            pass
        finally:
            cursor.close()
            connection.close()
    return None


def register_user(phone, full_name, pin):
    connection, cursor = connect_to_database()
    if connection and cursor:
        try:
            query = "INSERT INTO login_table (phone, full_name, pin) VALUES (%s, %s, %s)"
            values = (phone, full_name, password_to_hash(pin))
            cursor.execute(query, values)
            connection.commit()
            return True  # Return True to indicate successful insertion
        except mysql.connector.Error as err:
            # print("Error executing query: ", err)
            connection.rollback()  # Rollback the changes in case of an error
        finally:
            cursor.close()
            connection.close()
    return False  # Return False to indicate failure in insertion


def login_user(phone):
    connection, cursor = connect_to_database()
    if connection and cursor:
        try:
            query = "SELECT pin FROM login_table WHERE phone = %s"
            values = (phone,)
            cursor.execute(query, values)
            result = cursor.fetchone()
            if result:
                return result[0]  # Return the hashed password
            else:
                return None  # Return None if the phone number is not found
        except mysql.connector.Error as err:
            pass
            # print("Error executing query: ", err)
        finally:
            cursor.close()
            connection.close()
    return None  # Return None if there's an issue with the database connection


def get_username(phone):
    connection, cursor = connect_to_database()
    if connection and cursor:
        try:
            query = "SELECT full_name FROM login_table WHERE phone = %s"
            values = (phone,)
            cursor.execute(query, values)
            result = cursor.fetchone()
            if result:
                return result[0]  # Return the hashed password
            else:
                return None  # Return None if the phone number is not found
        except mysql.connector.Error as err:
            pass
            # print("Error executing query: ", err)
        finally:
            cursor.close()
            connection.close()
    return None  # Return None if there's an issue with the database connection


def password_to_hash(password):
    hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    return hashed.decode('utf-8')


def hash_to_password(password, hashed):
    return bcrypt.checkpw(password.encode('utf-8'), hashed.encode('utf-8'))


def validate_phone_number(phone):
    # Regular expression pattern for matching the phone number format
    pattern = r'^(01|07|\+2541|\+2547)\d{8}$'

    # Use re.match to check if the phone number matches the pattern
    if re.match(pattern, phone):
        return True
    else:
        return False
