import unittest
from unittest import mock

from airflow.models import Connection, Variable


class Test(unittest.TestCase):
    def test_env(self):
        with mock.patch.dict("os.environ", AIRFLOW_VAR_KEY="env-value"):
            assert "env-value" == Variable.get("key")

    def test(self):
        conn = Connection(
            conn_type="gcpssh",
            login="cat",
            host="conn-host",
        )
        conn_uri = conn.get_uri()
        with mock.patch.dict("os.environ", AIRFLOW_CONN_MY_CONN=conn_uri):
            assert "cat" == Connection.get("my_conn").login


if __name__ == '__main__':
    unittest.main()