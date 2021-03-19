import psycopg2

CONNECTION_STR = "host='' dbname='' user='' password=''"


def get_all_confessions():
    conn = psycopg2.connect(CONNECTION_STR)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM confession")

    confessions = []

    for c in cursor.fetchall():
        confessions.append({
            'id': c[0],
            'username': c[1],
            'confession': c[2],
            'timestamp': c[3]
        })

    conn.close()
    return confessions


def insert_confession(username, confession):
    conn = psycopg2.connect(CONNECTION_STR)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO confession(username, confession) VALUES (%s, %s)", (username, confession))
    conn.commit()
    conn.close()

    return True
