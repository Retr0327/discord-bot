from models.sql import query


def delete_scheduler(cid: int) -> None:
    """The delete_scheduler function delete a row from the table scheduler
    based on `cid`.

    Args:
        cid (int): a text channel id
    """
    sql_raw = "DELETE FROM scheduler WHERE cid=?;"
    query(sql_raw, [cid])
