import psycopg2
from tkinter import messagebox


def connect_db():
    try:
        conn = psycopg2.connect(
            dbname="Cinema",
            user="postgres",
            password="1234",  # Замените на ваш пароль
            host="localhost",
            port="5432",
            client_encoding="UTF8"
        )
        return conn
    except Exception as e:
        print(f"Ошибка подключения: {e}")
        return None


def get_database_structure():
    conn = connect_db()
    if conn is None:
        return

    try:
        cursor = conn.cursor()

        # Получаем список всех таблиц
        cursor.execute("""
            SELECT table_name 
            FROM information_schema.tables 
            WHERE table_schema = 'public'
        """)
        tables = [row[0] for row in cursor.fetchall()]

        # Выводим структуру каждой таблицы
        for table in tables:
            print(f"\nТаблица: {table}")
            cursor.execute(f"""
                SELECT column_name, data_type, is_nullable, column_default
                FROM information_schema.columns
                WHERE table_schema = 'public' AND table_name = '{table}'
                ORDER BY ordinal_position
            """)
            columns = cursor.fetchall()
            for col in columns:
                col_name, data_type, nullable, default = col
                print(
                    f"  - {col_name} ({data_type}, {'NOT NULL' if nullable == 'NO' else 'NULLABLE'}, Default: {default if default else 'None'})")

            # Проверяем первичные ключи
            cursor.execute(f"""
                SELECT kcu.column_name
                FROM information_schema.table_constraints tc
                JOIN information_schema.key_column_usage kcu
                ON tc.constraint_name = kcu.constraint_name
                WHERE tc.table_schema = 'public' 
                AND tc.table_name = '{table}' 
                AND tc.constraint_type = 'PRIMARY KEY'
            """)
            pk = cursor.fetchall()
            if pk:
                print(f"  Первичный ключ: {', '.join([p[0] for p in pk])}")

            # Проверяем внешние ключи
            cursor.execute(f"""
                SELECT kcu.column_name, ccu.table_name, ccu.column_name
                FROM information_schema.table_constraints tc
                JOIN information_schema.key_column_usage kcu
                ON tc.constraint_name = kcu.constraint_name
                JOIN information_schema.constraint_column_usage ccu
                ON ccu.constraint_name = tc.constraint_name
                WHERE tc.table_schema = 'public' 
                AND tc.table_name = '{table}' 
                AND tc.constraint_type = 'FOREIGN KEY'
            """)
            fk = cursor.fetchall()
            if fk:
                print("  Внешние ключи:")
                for f in fk:
                    col, ref_table, ref_col = f
                    print(f"    - {col} -> {ref_table}({ref_col})")

        cursor.close()
        conn.close()

    except Exception as e:
        print(f"Ошибка при получении структуры: {e}")


if __name__ == "__main__":
    get_database_structure()