from typing import List
from models.sql import query


def schedule_message(data: List[str]) -> None:
    """The schedule_message function insert data to the table schedule_message.

    Args:
        data (list): a list of values
    """
    sql_raw = """
    INSERT INTO scheduler (
        message,
        cid,
        channel_name,
        next_event_time
    )
    VALUES (?, ?, ?, ?);
    """
    query(sql_raw, data)
