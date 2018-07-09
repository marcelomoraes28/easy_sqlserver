import os
from .filters import filters
from .con import Connection
from argparse import Namespace

import pymssql

# Database configurations with environments
CONFIGS = {
    "SQLSERVER_SERVER": os.getenv("SQLSERVER_SERVER"),
    "SQLSERVER_PORT": os.getenv("SQLSERVER_PORT"),
    "SQLSERVER_USERNAME": os.getenv("SQLSERVER_USERNAME"),
    "SQLSERVER_PASSWD": os.getenv("SQLSERVER_PASSWD"),
    "SQLSERVER_DATABASE": os.getenv("SQLSERVER_DATABASE")
}


class EasySQLServer(filters.Filters):
    """
    Easy SQL Server library
    """

    def __init__(self, configs={}):
        if configs:
            CONFIGS.update(configs)
        conf = Namespace(**CONFIGS)
        self.con = Connection(conf.SQLSERVER_SERVER, conf.SQLSERVER_PORT,
                              conf.SQLSERVER_USERNAME, conf.SQLSERVER_PASSWD,
                              conf.SQLSERVER_DATABASE)

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
