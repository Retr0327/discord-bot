from typing import List, Union
from models.sql import query


def get_schedulers() -> List[Union[tuple, None]]:
    """The get_schedulers function get all the rows from the table `scheduler`.

    Returns:
        a list of tuples if the table is not empty, an empty list otherwise
    """
    sql_row = "SELECT * FROM scheduler"
    return query(sql_row)


def get_scheduler_by_cid(cid: int) -> List[Union[tuple, None]]:
    """The get_scheduler_by_cid function get the row based on channel id.

    Args:
        cid (int): the channel id
    Returns:
        a list of tuples if the table is not empty, an empty list otherwise
    """
    sql_row = "SELECT * FROM scheduler WHERE cid=?;"
    return query(sql_row, [cid])
