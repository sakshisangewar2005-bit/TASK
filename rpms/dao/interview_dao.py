from rpms.util.db import get_connection

class InterviewDAO:
    def add(self, application_id, round_name, interview_date, mode, interviewer):
        conn = get_connection()
        try:
            cur = conn.cursor()
            cur.execute("""INSERT INTO interviews(application_id,round_name,interview_date,mode,interviewer)
                           VALUES(%s,%s,%s,%s,%s)""",
                        (application_id,round_name,interview_date,mode,interviewer))
            conn.commit()
            return cur.lastrowid
        finally:
            conn.close()
