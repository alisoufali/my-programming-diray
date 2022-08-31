import sqlite3

from pypika import Query, Column, Table, Parameter

from modules.configs import Configs


class Database:

    __connection = None

    @classmethod
    def connect_to_db(cls):
        cls.__connection = sqlite3.connect(database=Configs.DATABASE_PATH)
        cls.__connection.row_factory = sqlite3.Row
        cls.__create_table()

    @classmethod
    def __create_table(cls):
        entries = Table("entries")
        columns = {
            "content": Column(column_name="content", column_type="TEXT"),
            "date": Column(column_name="date", column_type="TEXT")
        }
        query = Query.create_table(table=entries).if_not_exists().columns(
            columns["content"], columns["date"]
        )
        with cls.__connection:
            cls.__connection.execute(query.get_sql())

    @classmethod
    def create_entry(cls, entry_content: str, entry_date: str) -> None:
        entries = Table("entries")
        query = Query.into(table=entries).columns("content", "date").insert(
            Parameter("?"), Parameter("?")
        )
        with cls.__connection:
            cls.__connection.execute(
                query.get_sql(),
                (entry_content, entry_date)
            )

    @classmethod
    def read_entries(cls) -> sqlite3.Cursor:
        entries = Table("entries")
        query = Query.from_(table=entries).select("content", "date")
        cursor = cls.__connection.cursor()
        cursor.execute(query.get_sql())
        return cursor

    @classmethod
    def reset_entries(cls) -> None:
        entries = Table("entries")
        query = Query.drop_table(table=entries)
        with cls.__connection:
            cls.__connection.execute(
                query.get_sql()
            )
        cls.__create_table()
