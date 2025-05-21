from App.ConnectDB.Connect import connect_db

def break_projector(projector_id):
    """Установка статуса is_broken = TRUE для выбранного проектора."""
    conn = connect_db()
    if conn:
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE "Projector" 
            SET is_broken = TRUE 
            WHERE id_projector = %s
        """, (projector_id,))
        conn.commit()
        cursor.close()
        conn.close()
        return True
    return False


def check_projector_status(seance_id):
    projector_id=get_projector_id_from_seance(seance_id)
    """Проверяет статус проектора по его ID. Возвращает 0, если сломан, 1, если исправен."""
    conn = connect_db()
    if conn:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT is_broken 
            FROM "Projector" 
            WHERE id_projector = %s
        """, (projector_id,))
        result = cursor.fetchone()
        cursor.close()
        conn.close()
        if result is not None:
            return 0 if result[0] else 1
        else:
            return None  # Если проектор с таким ID не найден
    return None  # Если не удалось подключиться к базе данных


def get_projector_id_from_seance(seance_id):
    """Возвращает первый id_projector для зала, связанного с указанным сеансом."""
    conn = connect_db()
    if conn:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT p.id_projector
            FROM "Projector" p
            JOIN "Seance" s ON p.id_hall = s.id_hall
            WHERE s.id_seance = %s
            LIMIT 1
        """, (seance_id,))
        result = cursor.fetchone()
        cursor.close()
        conn.close()
        if result is not None:
            return result[0]  # Возвращаем первый id_projector
        else:
            return None  # Если проектор или сеанс не найдены
    return None  # Если не удалось подключиться к базе данных