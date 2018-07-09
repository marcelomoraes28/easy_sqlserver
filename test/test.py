import unittest
import os, sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from easy_sqlserver.filters import Filters


class TestTypesMethods(unittest.TestCase):

    def test_integer(self):
        self.assertTrue(Filters().is_integer(45))
        self.assertFalse(Filters().is_integer("45"))

    def test_str(self):
        self.assertTrue(Filters().is_str("45"))
        self.assertFalse(Filters().is_str(45))

    def test_list(self):
        self.assertTrue(Filters().is_list([]))
        self.assertFalse(Filters().is_list(45))
        self.assertFalse(Filters().is_list({}))


class TestSqls(unittest.TestCase):
    filters = Filters()

    def test_order_by(self):
        order_by = "FIELD DESC"
        self.__class__.filters.select("TABLE")
        self.__class__.filters.order_by(order_by)
        self.assertIn("order by " + order_by, self.__class__.filters.sql())

    def test_limit(self):
        limit = 50
        self.__class__.filters.select("TABLE")
        self.__class__.filters.limit(limit)
        self.assertIn("TOP " + str(limit), self.__class__.filters.sql())

    def test_where(self):
        where = 'FIELD1 = "xxxx"'
        where_list = ["FIELD1 = 'xxxx'", "FIELD2 = 'yyyy'"]
        self.__class__.filters.select("TABLE")
        self.__class__.filters.where(where)
        self.assertIn(where, self.__class__.filters.sql())
        self.__class__.filters.where(where_list)
        self.assertIn(" AND ".join(where_list), self.__class__.filters.sql())

    def test_fields(self):
        fields = ['FIELD1', 'FIELD2', 'FIELD3']
        self.__class__.filters.select("TABLE")
        self.__class__.filters.fields(fields)
        self.assertIn(", ".join(fields), self.__class__.filters.sql())

    def test_join(self):
        join = "JOIN TABLE2 on TABLE.id = TABLE2.table_id"
        self.__class__.filters.select("TABLE")
        self.__class__.filters.join("TABLE2", "TABLE.id = TABLE2.table_id")
        self.assertIn(join, self.__class__.filters.sql())


if __name__ == '__main__':
    unittest.main()
