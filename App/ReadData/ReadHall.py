from App.ConnectDB.Connect import connect_db

def fetch_halls():
    """Получение списка залов."""
    conn = connect_db()
    halls = []
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT id_hall, number FROM \"Hall\"")
        halls = [(str(row[0]), str(row[1])) for row in cursor.fetchall()]
        cursor.close()
        conn.close()
    return halls