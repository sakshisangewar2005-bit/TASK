from rpms.util.db import get_connection

class CandidateDAO:
    def add(self, c):
        conn = get_connection()
        try:
            cur = conn.cursor()
            cur.execute("""INSERT INTO candidates
                (name,email,mobile,qualification,percentage,passing_year,technology,skills,backlogs)
                VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)""",
                (c.name,c.email,c.mobile,c.qualification,c.percentage,c.passing_year,
                 c.technology,c.skills,c.backlogs))
            conn.commit()
            return cur.lastrowid
        finally:
            conn.close()

    def all(self):
        conn = get_connection()
        try:
            cur = conn.cursor(dictionary=True)
            cur.execute("SELECT * FROM candidates ORDER BY candidate_id DESC")
            return cur.fetchall()
        finally:
            conn.close()

    def get(self, candidate_id):
        conn = get_connection()
        try:
            cur = conn.cursor(dictionary=True)
            cur.execute("SELECT * FROM candidates WHERE candidate_id=%s", (candidate_id,))
            return cur.fetchone()
        finally:
            conn.close()

    def deactivate(self, candidate_id):
        conn = get_connection()
        try:
            cur = conn.cursor()
            cur.execute("UPDATE candidates SET active=0 WHERE candidate_id=%s", (candidate_id,))
            conn.commit()
            return cur.rowcount > 0
        finally:
            conn.close()
