from rpms.util.db import get_connection

class JobDAO:
    def add(self, j):
        conn = get_connection()
        try:
            cur = conn.cursor()
            cur.execute("""INSERT INTO jobs(company_id,title,technology,openings,location,package_lpa,
                min_percentage,passing_year,max_backlogs,deadline)
                VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",
                (j.company_id,j.title,j.technology,j.openings,j.location,j.package_lpa,
                 j.min_percentage,j.passing_year,j.max_backlogs,j.deadline))
            conn.commit()
            return cur.lastrowid
        finally:
            conn.close()

    def all_open(self):
        conn = get_connection()
        try:
            cur = conn.cursor(dictionary=True)
            cur.execute("""SELECT j.*, c.name AS company_name FROM jobs j
                           JOIN companies c ON c.company_id=j.company_id
                           WHERE j.status='OPEN' AND j.deadline >= CURDATE()
                           ORDER BY j.deadline""")
            return cur.fetchall()
        finally:
            conn.close()

    def get(self, job_id):
        conn = get_connection()
        try:
            cur = conn.cursor(dictionary=True)
            cur.execute("SELECT * FROM jobs WHERE job_id=%s", (job_id,))
            return cur.fetchone()
        finally:
            conn.close()
