import pyodbc
import json

class MySQLConnector:

    def initialize_connection():
        """Function to initlaize MySQL database connection using pyodbc."""

        driver_name = ''
        driver_names = [x for x in pyodbc.drivers() if x.endswith(' for SQL Server')]
        if driver_names:
            driver_name = driver_names[0]
        
        if driver_name:
            with open('../config.json') as config_file:
                config_data = json.load(config_file)

            conn_str = f"""DRIVER={driver_name};
                        SERVER={config_data['server_name']};
                        DATABASE={config_data['database_name']};
                        UID={config_data['database_uid']};
                        PWD={config_data['pwd']}"""

            cnxn = pyodbc.connect(conn_str)

            cursor = cnxn.cursor()

            return cursor

        else:
            return None