import os
from .filters import filters
from .con import Connection
import pymssql

SERVER = os.getenv("SQLSERVER_SERVER")
PORT = os.getenv("SQLSERVER_PORT")
USERNAME = os.getenv("SQLSERVER_USERNAME")
PASSWD = os.getenv("SQLSERVER_PASSWD")
DATABASE = os.getenv("SQLSERVER_DATABASE")


class EasySQLServer(filters.Filters):
    """
    Easy SQL Server library
    """
    def __init__(self):
        self.con = Connection(SERVER, PORT, USERNAME, PASSWD,
                              DATABASE)

    def execute(self):
        try:
            connection = self.con.connect()
            cursor = connection.cursor(as_dict=True)
            cursor.execute(self.sql())
            rows = cursor.fetchall()
        except pymssql.ProgrammingError as e:
            raise e.args
        except ValueError as e:
            raise e
        connection.close()
        return rows
