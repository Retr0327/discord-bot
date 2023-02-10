from typing import List
from models.sql import query


def create_scheduler(data: List[str]) -> None:
    """The create_scheduler function writes data to the table schedule_message.

    Args:
        data (list): a list of values
    """
    sql_raw = """
    INSERT INTO scheduler (
        message,
        cid,
        next_event_time
    )
    VALUES (?, ?, ?);
    """
    query(sql_raw, data)
