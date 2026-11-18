from rpms.util.db import get_connection

class CompanyDAO:
    def add(self, name, industry, location, email, phone):
        conn = get_connection()
        try:
            cur = conn.cursor()
            cur.execute("""INSERT INTO companies(name,industry,location,contact_email,phone)
                           VALUES(%s,%s,%s,%s,%s)""",
                        (name,industry,location,email,phone))
            conn.commit()
            return cur.lastrowid
        finally:
            conn.close()

    def all(self):
        conn = get_connection()
        try:
            cur = conn.cursor(dictionary=True)
            cur.execute("SELECT * FROM companies ORDER BY company_id DESC")
            return cur.fetchall()
        finally:
            conn.close()
