import re


class Filters:
    """
    Class to generate querys
    """

    q_table = None
    q_fields = []
    q_limit = 10000
    q_where = []
    q_join = []
    q_query = None
    q_order_by = None

    @staticmethod
    def is_integer(var):
        return isinstance(var, int)

    @staticmethod
    def is_str(var):
        return isinstance(var, str)

    @staticmethod
    def is_list(var):
        return isinstance(var, list)

    def valid_query(self):
        errors = []
        if self.__class__.q_table is None and self.__class__.q_query is None:
            errors['table'] = 'Table must be defined'
        if errors:
            raise ValueError(errors)

    def sql(self):
        self.valid_query()
        if self.__class__.q_query:
            return self.__class__.query
        where_clause = " ".join(self.__class__.q_where)
        join_clause = " ".join(self.__class__.q_join)
        order_by_clause = (
                " order by " + self.__class__.q_order_by) if self.__class__.q_order_by else ''
        fields_clause = ", ".join(
            self.__class__.q_fields) if self.__class__.q_fields else '*'
        query = "SELECT TOP %s %s from %s where 1=1 %s %s %s" % (
            self.__class__.q_limit, fields_clause, self.__class__.q_table,
            where_clause, join_clause, order_by_clause) + ";"

        return re.sub(' +', ' ', query)

    def query(self, query):
        """
        Return a query
        :param query:
        :return:
        """
        if not self.is_str(query):
            raise ValueError("query must be a str")
        self.__class__.q_query = query

    def select(self, table):
        self.__class__.q_query = None
        if table is None:
            raise ValueError("Table must be a string")
        self.__class__.q_table = table

    def where(self, cond):
        if self.is_list(cond):
            [self.__class__.q_where.append(" AND %s" % condition) for
             condition in cond]
        if self.is_str(cond):
            self.__class__.q_where.append(" AND  %s " % cond)
        if cond is None:
            raise ValueError("'where' clause must be a str or list")

    def limit(self, limit):
        if not self.is_integer(limit):
            raise ValueError("limit clause must be integer")
        self.__class__.q_limit = limit

    def order_by(self, order_by):
        if not self.is_str(order_by):
            raise ValueError("order_by clause must be str")
        self.__class__.q_order_by = order_by

    def join(self, table, condition):
        errors = []
        if not self.is_str(table) or table is None:
            errors['table'] = "Must be a str"
        if not self.is_str(condition) or condition is None:
            errors['condition'] = "Must be a str"
        if errors:
            raise ValueError(errors)
        self.__class__.q_join.append(" JOIN %s on %s" % (table, condition))

    def fields(self, fields=None):
        if not self.is_list(fields):
            raise ValueError("fields clause must be a list")
        self.__class__.q_fields = fields
