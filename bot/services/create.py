from typing import List, Union
from models.sql import query


def create_scheduler(data: List[str]) -> List[Union[tuple, None]]:
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
    return query(sql_raw, data)
