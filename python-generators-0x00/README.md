# Python MySQL Seeder and Query Project

This project demonstrates how to set up a MySQL database, populate it from a CSV file, and fetch data using Python. It is designed to build foundational skills in database interaction, automation, and generator-based data streaming.

## 🧰 Features

- Connect to a MySQL database server using `mysql-connector-python`
- Create a database named `ALX_prodev` if it doesn't exist
- Create a table `user_data` with schema:
  - `user_id` (UUID, primary key, indexed)
  - `name` (VARCHAR, not null)
  - `email` (VARCHAR, not null)
  - `age` (DECIMAL, not null)
- Populate the database from a CSV file (`user_data.csv`)
- Prevents duplicate entries using the primary key (`user_id`)
- Fetch data from the table for verification

## 📂 File Structure

├── seed.py # Script with all database functions
├── user_data.csv # Sample user data to populate the DB
├── 0-main.py # Driver script to set up DB and fetch data
├── README.md # Project documentation


## 🚀 Usage

### 1. Install Dependencies

Make sure you have MySQL running locally and install Python dependencies:

```bash
pip install mysql-connector-python
user_id,name,email,age
uuid-1,John Doe,john@example.com,30
uuid-2,Jane Smith,jane@example.com,45
