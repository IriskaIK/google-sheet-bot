from settings.bot_init import conn



def create_user(username, tg_id, table_url):
    with conn:
        with conn.cursor() as cur:
            cur.execute(f"SELECT * FROM client WHERE tg_id='{tg_id}'")
            data = cur.fetchall()
            if not data:
                cur.execute(f"INSERT INTO client (name, tg_id, table_url) VALUES ('{username}', {tg_id}, '{table_url}')")
                return True
            else:
                return data




def get_user(tg_id):
    with conn:
        with conn.cursor() as cur:
            cur.execute(f"SELECT * FROM client WHERE tg_id='{tg_id}'")
            data = cur.fetchall()
            if not data:
                return False
            return data
