import mysql.connector

def stream_users_in_batches(batch_size):
    connection = mysql.connector.connect(
        host="localhost",
        user="your_username",        # Replace with your MySQL username
        password="your_password",    # Replace with your MySQL password
        database="ALX_prodev"
    )
    cursor = connection.cursor(dictionary=True)

    batch = []
    cursor.execute("SELECT * FROM user_data")
    for row in cursor:
        batch.append(row)
        if len(batch) == batch_size:
            yield batch
            batch = []
    if batch:
        yield batch

    cursor.close()
    connection.close()


def batch_processing(batch_size):
    def generator():
        for batch in stream_users_in_batches(batch_size):
            for user in batch:
                if user['age'] > 25:
                    yield user
    return generator()
