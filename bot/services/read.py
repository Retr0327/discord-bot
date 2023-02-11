from models.sql import query


def get_schedulers():
    sql_row = "SELECT * FROM scheduler"
    return query(sql_row)


def get_scheduler_by_cid(cid: int):
    sql_row = "SELECT * FROM scheduler WHERE cid=?;"
    return query(sql_row, [cid])
