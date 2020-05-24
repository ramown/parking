CREATE TABLE IF NOT EXISTS proprietarios (
    id        INTEGER PRIMARY KEY AUTOINCREMENT,
    categoria INTEGER NOT NULL,
    pessoa_id INTEGER REFERENCES pessoas (id) ON DELETE CASCADE
                                              ON UPDATE CASCADE
);
