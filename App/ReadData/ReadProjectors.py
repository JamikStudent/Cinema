from App.ConnectDB.Connect import connect_db

def fetch_projectors(hall_id):
    """Получение списка проекторов для выбранного зала."""
    conn = connect_db()
    projectors = []
    if conn:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT id_projector, model 
            FROM "Projector" 
            WHERE id_hall = %s AND is_broken = FALSE
        """, (hall_id,))
        projectors = [(str(row[0]), row[1]) for row in cursor.fetchall()]
        cursor.close()
        conn.close()
    return projectors
