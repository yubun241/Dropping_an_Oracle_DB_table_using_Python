import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy import text
from sqlalchemy.dialects.oracle import NUMBER, VARCHAR2, DATE, TIMESTAMP
import cx_Oracle

HOST = ""
PORT = 
SVS = ""
USER = ""
PASS = "
engine_url = f'oracle+cx_oracle://{USER}:{PASS}@{HOST}:{PORT}/?service_name={SVS}'
engine = create_engine(engine_url)

with engine.connect() as connection:
    # 削除SQL: DROP TABLE テーブル名
    # Oracleの場合、ユーザー名（スキーマ）を指定するとより確実です
    try:
        connection.execute(text('DROP TABLE "TKG201"."MD_TEST"'))
        print("テーブル 'MD_TEST' を正常に削除しました。")
    except Exception as e:
        print(f"エラー（テーブルがない可能性があります）: {e}")
