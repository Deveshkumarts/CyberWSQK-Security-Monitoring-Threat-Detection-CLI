import sqlite3


def save_event(event_type, severity, message):

    conn = sqlite3.connect("database/cyberwsqk.db")

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO security_events
        (event_type, severity, message)
        VALUES (?, ?, ?)
        """,
        (event_type, severity, message)
    )

    conn.commit()
    conn.close()

def get_events():

    conn = sqlite3.connect("database/cyberwsqk.db")

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT id, event_type, severity, message, created_at
        FROM security_events
        ORDER BY id DESC
        """
    )

    events = cursor.fetchall()

    conn.close()

    return events