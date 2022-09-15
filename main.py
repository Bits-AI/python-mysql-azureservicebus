import os
from modules.mysql_connector import MySQLConnector
from modules.asb_client import ASBClient

def get_table_data(cursor):
    """Sample function for select query."""

    cursor.execute("""
                SELECT TOP 1 *
                FROM dbo.TestTable
                """)
    
    for row in cursor:
        data = {
            'key1': row.value1,
            'key2': row.value2
        }

    return data

def main():
    cursor = MySQLConnector.initialize_connection()

    data = get_table_data(cursor)

    response = ASBClient.send(data)

    print(response)

if __name__ == "__main__":
    while True:
        main()

        os.sleep(1)