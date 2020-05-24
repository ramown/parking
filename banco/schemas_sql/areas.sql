CREATE TABLE IF NOT EXISTS areas  (
    id               INTEGER      PRIMARY KEY AUTOINCREMENT,
    nome             VARCHAR (20) NOT NULL,
    vagas_max        INTEGER      NOT NULL,
    vagas_livres     INTEGER      NOT NULL,
    vagas_bloqueadas INTEGER      NOT NULL
);
