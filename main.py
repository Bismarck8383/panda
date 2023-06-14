import os
import pandas as pd
import mysql.connector
from configuracion import DATABASE_CONFIG


def insert_data_to_database(data, table_name):
    cnx = mysql.connector.connect(**DATABASE_CONFIG)
    cursor = cnx.cursor()
    cols = ", ".join([f"`{i}`" for i in data.columns.tolist()])
    for i, row in data.iterrows():
        sql = f"INSERT INTO {table_name} ({cols}) VALUES (" + "%s," * (len(row) - 1) + "%s)"
        cursor.execute(sql, tuple(row))
        cnx.commit()
    cursor.close()
    cnx.close()


def main():
    path_to_files = "archivos"
    table_name = "clientes"
    for file in os.listdir(path_to_files):
        if file.endswith(".xlsx"):
            print(f"Leyendo el archivo {file}...")
            data = pd.read_excel(os.path.join(path_to_files, file), sheet_name="data_21042023_104337", engine="openpyxl")
            insert_data_to_database(data, table_name)
            print(f"Datos del archivo {file} insertados en la tabla {table_name}.")
            assert cursor.rowcount > 0, f"No se insertaron datos del archivo {file}."


if __name__ == '__main__':
    main()
