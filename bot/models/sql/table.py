SCHEDULER = (
    "CREATE TABLE scheduler ("
    "id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,"
    "cid DECIMAL(22,0) NOT NULL,"
    "message VARCHAR(1000) NOT NULL,"
    "next_event_time INTEGER"
    ");"
)