import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()

def get_connection(env='DEV'):
    host = os.getenv(f'HOST_{env}')
    db_name = os.getenv(f'DB_NAME_{env}')
    db_user = os.getenv(f'DB_USER_{env}')
    db_password = os.getenv(f'DB_PASSWORD_{env}')
    port = os.getenv(f'PORT_{env}', 5432)

    return psycopg2.connect(
        host=host,
        database=db_name,
        user=db_user,
        password=db_password,
        port=port
    )

if __name__ == '__main__':
    try:
        conn = get_connection('DEV')
        print(f'Conexão estabelecida com sucesso!')
        print(f'Host: {conn.info.host}')
        print(f'Database: {conn.info.dbname}')
        print(f'User: {conn.info.user}')
        conn.close()
    except Exception as e:
        print(f'Erro ao conectar: {e}')