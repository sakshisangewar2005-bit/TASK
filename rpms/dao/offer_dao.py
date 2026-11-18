from rpms.util.db import get_connection

class OfferDAO:
    def add(self, application_id, designation, package_lpa, offer_date, joining_date):
        conn = get_connection()
        try:
            cur = conn.cursor()
            cur.execute("""INSERT INTO offers(application_id,designation,package_lpa,offer_date,joining_date)
                           VALUES(%s,%s,%s,%s,%s)""",
                        (application_id,designation,package_lpa,offer_date,joining_date))
            conn.commit()
            return cur.lastrowid
        finally:
            conn.close()
