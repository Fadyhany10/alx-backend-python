import mysql.connector
import csv
import os

DB_NAME = "ALX_prodev"
TABLE_NAME = "user_data"

def connect_db():
    """Connect to MySQL server (not to a specific DB)."""
    try:
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password=""
        )
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

def create_database(connection):
    """Create the ALX_prodev database if it doesn't exist."""
    try:
        cursor = connection.cursor()
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")
        cursor.close()
    except mysql.connector.Error as err:
        print(f"Failed to create database: {err}")

def connect_to_prodev():
    """Connect directly to ALX_prodev database."""
    try:
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database=DB_NAME
        )
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

def create_table(connection):
    """Create user_data table if it doesn't exist."""
    create_table_query = f"""
    CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
        user_id VARCHAR(36) PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        email VARCHAR(255) NOT NULL,
        age DECIMAL(5,2) NOT NULL,
        INDEX (user_id)
    );
    """
    try:
        cursor = connection.cursor()
        cursor.execute(create_table_query)
        connection.commit()
        cursor.close()
        print("Table user_data created successfully")
    except mysql.connector.Error as err:
        print(f"Failed to create table: {err}")

def insert_data(connection, csv_file):
    """Insert data into user_data table from CSV file."""
    if not os.path.exists(csv_file):
        print(f"File '{csv_file}' not found")
        return

    try:
        cursor = connection.cursor()
        with open(csv_file, newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                cursor.execute(f"""
                INSERT IGNORE INTO {TABLE_NAME} (user_id, name, email, age)
                VALUES (%s, %s, %s, %s)
                """, (row['user_id'], row['name'], row['email'], row['age']))
        connection.commit()
        cursor.close()
    except mysql.connector.Error as err:
        print(f"Failed to insert data: {err}")
