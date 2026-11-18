from rpms.util.db import get_connection

def report_rows(sql, params=()):
    conn = get_connection()
    try:
        cur = conn.cursor(dictionary=True)
        cur.execute(sql, params)
        return cur.fetchall()
    finally:
        conn.close()

def candidates_by_technology():
    return report_rows("SELECT technology, COUNT(*) total FROM candidates GROUP BY technology")

def applications_by_status():
    return report_rows("SELECT status, COUNT(*) total FROM applications GROUP BY status")

def company_wise_placements():
    return report_rows("""SELECT c.name company, COUNT(*) placements FROM placements p
                          JOIN companies c ON c.company_id=p.company_id GROUP BY c.name""")

def placed_candidates():
    return report_rows("""SELECT ca.name candidate, co.name company, p.designation, p.final_package
                          FROM placements p JOIN applications a ON a.application_id=p.application_id
                          JOIN candidates ca ON ca.candidate_id=a.candidate_id
                          JOIN companies co ON co.company_id=p.company_id""")
