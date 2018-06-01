import pymssql


class Connection(object):
    def __init__(self, server, port, user, passwd, database):
        self.server = server
        self.port = port
        self.user = user
        self.passwd = passwd
        self.database = database
        self.validate()

    def connect(self):
        try:
            conn = pymssql.connect(
                server=self.server,
                user=self.user, password=self.passwd,
                port=self.port,
                database=self.database)
        except pymssql.InterfaceError as e:
            raise e
        except pymssql.DatabaseError as e:
            raise e
        return conn

    def validate(self):
        errors = []
        if self.server is None:
            errors.append("SERVER is required, please set SQLSERVER_SERVER env")
        if self.port is None:
            errors.append(
                "PORT is required, please set SQLSERVER_PORT env")
        if self.passwd is None:
            errors.append(
                "PASSWORD is required, please set SQLSERVER_PASSWD env")
        if self.user is None:
            errors.append(
                "USER is required, please set SQLSERVER_USER env")
        if self.database is None:
            errors.append(
                "DATABASE is required, please set SQLSERVER_DATABASE env")
        if errors:
            raise ValueError(errors)
