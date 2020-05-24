CREATE TABLE IF NOT EXISTS veiculos (
    id              INTEGER      PRIMARY KEY AUTOINCREMENT,
    placa           VARCHAR (15) UNIQUE
                                 NOT NULL,
    marca           VARCHAR (20),
    modelo          VARCHAR (20),
    cor             VARCHAR (15),
    proprietario_id INTEGER      REFERENCES proprietarios (id) ON DELETE CASCADE
                                                               ON UPDATE CASCADE
);
