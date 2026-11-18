from rpms.util.db import get_connection

class ApplicationDAO:
    def exists(self, candidate_id, job_id):
        conn = get_connection()
        try:
            cur = conn.cursor()
            cur.execute("SELECT application_id FROM applications WHERE candidate_id=%s AND job_id=%s",
                        (candidate_id,job_id))
            return cur.fetchone() is not None
        finally:
            conn.close()

    def add(self, candidate_id, job_id):
        conn = get_connection()
        try:
            cur = conn.cursor()
            cur.execute("INSERT INTO applications(candidate_id,job_id) VALUES(%s,%s)",
                        (candidate_id,job_id))
            conn.commit()
            return cur.lastrowid
        finally:
            conn.close()

    def all(self):
        conn = get_connection()
        try:
            cur = conn.cursor(dictionary=True)
            cur.execute("""SELECT a.*, c.name candidate_name, j.title job_title, co.name company_name
                FROM applications a JOIN candidates c ON c.candidate_id=a.candidate_id
                JOIN jobs j ON j.job_id=a.job_id JOIN companies co ON co.company_id=j.company_id
                ORDER BY a.application_id DESC""")
            return cur.fetchall()
        finally:
            conn.close()

    def update_status(self, application_id, new_status):
        conn = get_connection()
        allowed = {
            "APPLIED": {"SHORTLISTED","REJECTED"},
            "SHORTLISTED": {"INTERVIEW","REJECTED"},
            "INTERVIEW": {"SELECTED","REJECTED"},
            "SELECTED": {"OFFERED","REJECTED"},
            "OFFERED": {"JOINED","REJECTED"},
            "JOINED": set(), "REJECTED": set()
        }
        try:
            cur = conn.cursor()
            cur.execute("SELECT status FROM applications WHERE application_id=%s", (application_id,))
            row = cur.fetchone()
            if not row:
                raise ValueError("Application not found.")
            current = row[0]
            if new_status not in allowed.get(current, set()):
                raise ValueError(f"Invalid workflow transition: {current} -> {new_status}")
            cur.execute("UPDATE applications SET status=%s WHERE application_id=%s",
                        (new_status,application_id))
            conn.commit()
        finally:
            conn.close()
