import sqlite3, os

def get_db_connection():
    conn = sqlite3.connect(os.path.dirname(os.path.abspath(__file__)) + '/database.db')
    conn.row_factory = sqlite3.Row
    return conn

def clear_db_connection():
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("DROP TABLE IF EXISTS tarefa;")
        conn.commit()
    finally:
        conn.close()

def criar_banco():
    cursor = get_db_connection().cursor()

    cursor.execute("""
        CREATE TABLE tarefa (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            descricao TEXT NOT NULL,
            data TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            status INTEGER DEFAULT 0
        );
    """)

def main():
    clear_db_connection()
    criar_banco()

if __name__ == '__main__':
    main()