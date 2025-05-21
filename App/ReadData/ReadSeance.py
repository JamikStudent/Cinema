from App.ConnectDB.Connect import connect_db

def fetch_seances_without_film(hall_id):
    """Получение списка сеансов без загруженного фильма для выбранного зала."""
    conn = connect_db()
    seances = []
    if conn:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT s.id_seance, f.name 
            FROM "Seance" s
            JOIN "Film" f ON s.id_film = f.id_film
            WHERE s.id_hall = %s AND s.has_film = FALSE
        """, (hall_id,))
        seances = [(str(row[0]), row[1]) for row in cursor.fetchall()]
        cursor.close()
        conn.close()
    return seances
