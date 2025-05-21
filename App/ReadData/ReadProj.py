from App.ConnectDB.Connect import connect_db

def get_projector_id_from_hall(hall_id):
    """Возвращает первый id_projector для указанного зала."""
    conn = connect_db()
    if conn:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT id_projector
            FROM "Projector"
            WHERE id_hall = %s
            LIMIT 1
        """, (hall_id,))
        result = cursor.fetchone()
        cursor.close()
        conn.close()
        if result is not None:
            return result[0]
        else:
            return None
    return None