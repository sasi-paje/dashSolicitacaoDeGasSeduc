import pandas as pd
from db import get_connection

def get_gas_requests():
    conn = get_connection('DEV')
    query = "SELECT * FROM vw_bi_gas_request"
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df

def treat_data(df):
    if df.empty:
        return df

    df = df.copy()

    if 'created_at' in df.columns:
        df['created_at'] = pd.to_datetime(df['created_at'])

    return df

if __name__ == '__main__':
    df = get_gas_requests()
    print(f"Linhas carregadas: {len(df)}")
    print(f"Colunas: {list(df.columns)}")
    df_treated = treat_data(df)
    print(f"Linhas tratadas: {len(df_treated)}")