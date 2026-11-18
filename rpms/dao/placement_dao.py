from rpms.util.db import get_connection

class PlacementDAO:
    def add(self, application_id, company_id, designation, final_package, joining_date):
        conn = get_connection()
        try:
            cur = conn.cursor()
            cur.execute("""INSERT INTO placements(application_id,company_id,designation,final_package,actual_joining_date)
                           VALUES(%s,%s,%s,%s,%s)""",
                        (application_id,company_id,designation,final_package,joining_date))
            conn.commit()
            return cur.lastrowid
        finally:
            conn.close()
