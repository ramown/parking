#settings
import os

BASEDIR_SCHEMAS = 'banco/schemas_sql'
SCHEMAS = [os.path.join(BASEDIR_SCHEMAS, nome) for nome in os.listdir(BASEDIR_SCHEMAS)]
DATABASE_NAME = 'dados.sqlite3'
