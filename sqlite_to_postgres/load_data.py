import sqlite3
from dataclasses import fields, astuple
import os

import psycopg2
from psycopg2.extensions import connection as _connection
from psycopg2.extras import DictCursor, execute_values
from dataclass import *


class PostgresSaver:
    def __init__(self, connection, schema):
        self.cur = connection.cursor()
        self._conn = connection
        self._schema = schema

    def truncate_data(self, table_name):
        self.cur.execute(f'TRUNCATE {self._schema}.{table_name}')

    def save_data(self, table_name, field_list, data):
        execute_values(
            self.cur,
            f'INSERT INTO {self._schema}.{table_name} ({field_list}) VALUES %s '
            f'ON CONFLICT (id) DO NOTHING',
            data,
        )


class SQLiteLoader:
    def __init__(self, connection):
        self._conn = connection
        self._conn.row_factory = sqlite3.Row
        self.cur = self._conn.cursor()

    def load_data(self, table_name, field_list):
        self.cur.execute(f'SELECT {field_list} FROM {table_name}')
        return self.cur


def load_from_sqlite(connection: sqlite3.Connection, pg_conn: _connection, default_schema):
    """Основной метод загрузки данных из SQLite в Postgres"""
    postgres_saver = PostgresSaver(pg_conn, default_schema)
    sqlite_loader = SQLiteLoader(connection)

    for table_name, class_obj in tables_dict.items():
        field_list = ', '.join([i.name for i in fields(class_obj)])
        query = sqlite_loader.load_data(table_name, field_list)

        while True:
            data_values = [
                astuple(class_obj(**i)) for i in query.fetchmany(800)
            ]
            if not data_values:
                break
            postgres_saver.save_data(table_name, field_list, data_values)


if __name__ == '__main__':
    dsl = {
        'dbname': os.environ.get('DB_NAME'),
        'user': os.environ.get('DB_USER'),
        'host': os.environ.get('DB_HOST', 'localhost'),
        'password': os.environ.get('DB_PASSWORD'),
        'port': os.environ.get('DB_PORT', 5432),
        'options': '-c search_path=content',
    }
    default_schema = 'content'

    with sqlite3.connect('db.sqlite') as sqlite_conn, psycopg2.connect(**dsl, cursor_factory=DictCursor) as pg_conn:
        load_from_sqlite(sqlite_conn, pg_conn, default_schema)

    sqlite_conn.close()
    pg_conn.close()
