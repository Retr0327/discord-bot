import sqlite3
from typing import Optional, Union, List, Dict, Any, Literal
from config import DB_PATH
from .table import SCHEDULER


def connect_db() -> sqlite3.Connection:
    """The connect_db function connects to the database."""

    return sqlite3.connect(
        DB_PATH, detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES
    )


def query(
    script: str,
    params: Optional[Union[List[tuple], Dict[str, Any], None]] = None,
    mode: Optional[Union[Literal["script", "many"], None]] = None,
) -> Union[List, None]:
    """The query function query the database based on `script`, `params` and `mode`."""

    sqlite_cli = connect_db()

    with sqlite_cli:
        if mode == "script":
            return sqlite_cli.executescript(script).fetchall()
        elif mode == "many":
            if params is None:
                raise TypeError("parames must be specified")
            return sqlite_cli.executemany(script, params).fetchall()

        if params is not None:
            return sqlite_cli.execute(script, params).fetchall()

        return sqlite_cli.execute(script).fetchall()


def init_db() -> None:
    """The init_db function initializes the database."""

    sql_script = f"""
    BEGIN TRANSACTION;
    {SCHEDULER}
    COMMIT;
    """
    query(sql_script, mode="script")
