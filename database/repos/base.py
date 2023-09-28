from typing import Any, Protocol, Iterable
from contextlib import closing
import sqlite3


class DbContext(Protocol):
    def create_connection():
        """Return connection to database else raise sqlite3.Error."""

class BaseRepository:
    def __init__(self, db_context: DbContext) -> None:
        self.db_context = db_context
    
    def _create_row_from_values(self, command: str, values: Iterable[Any]) -> int:
        with closing(self.db_context.create_connection()) as connection:
            cursor = connection.cursor()
            try:
                cursor.execute(command, values)
                connection.commit()
                return cursor.lastrowid
            except (TypeError, sqlite3.Error) as error:
                raise(error)
            
    def _read_row_by_id(self, query: str, id: int | tuple[int]) -> Iterable[Any] | None:
        try:
            with closing(self.db_context.create_connection()) as connection:
                cursor = connection.cursor()
                cursor.execute(query, (id,))
                row = cursor.fetchone()
                return row
        except sqlite3.Error as error:
            raise error
        
    def _read_rows_fetchall(self, query: str) -> Iterable[Any] | None:
        try:
            with closing(self.db_context.create_connection()) as connection:
                cursor = connection.cursor()
                cursor.execute(query)
                rows = cursor.fetchall()
                return rows
        except sqlite3.Error as error:
            raise error
        
    def _search_by_term(self, query, search_term) -> Iterable[Any]:
        try:
            with closing(self.db_context.create_connection()) as connection:
                cursor = connection.cursor()
                cursor.execute(query, (f"%{search_term}%",))
                rows = cursor.fetchall()
                return rows
        except sqlite3.Error as error:
            raise error
        
    def _update_row_with_values(self, query: str, values: Iterable[Any]) -> None:
        try:
            with closing(self.db_context.create_connection()) as connection:
                cursor = connection.cursor()
                cursor.execute(query, values)
                connection.commit()
        except sqlite3.Error as error:
            raise error
    
    def _delete_row_by_id(self, query: str, id: int) -> None:
        try:
            with closing(self.db_context.create_connection()) as connection:
                cursor = connection.cursor()
                cursor.execute(query, (id,))
                connection.commit()
        except sqlite3.Error as error:
            raise error