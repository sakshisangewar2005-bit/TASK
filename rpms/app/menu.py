from rpms.service.candidate_service import CandidateService
from rpms.service.job_service import JobService
from rpms.service.application_service import ApplicationService
from rpms.dao.company_dao import CompanyDAO
from rpms.dao.candidate_dao import CandidateDAO
from rpms.dao.job_dao import JobDAO
from rpms.dao.application_dao import ApplicationDAO
from rpms.dao.interview_dao import InterviewDAO
from rpms.dao.offer_dao import OfferDAO
from rpms.dao.placement_dao import PlacementDAO
from rpms.service import report_service

def ask(prompt):
    return input(prompt).strip()

def show_rows(rows):
    if not rows:
        print("No records found."); return
    for row in rows: print(row)

def run():
    candidates, jobs, apps = CandidateService(), JobService(), ApplicationService()
    companies = CompanyDAO()
    while True:
        print("\n========== RECRUITMENT & PLACEMENT SYSTEM ==========")
        print("1. Candidates  2. Companies  3. Jobs  4. Applications")
        print("5. Interviews  6. Offers  7. Placements  8. Reports  9. Exit")
        choice = ask("Enter choice: ")
        try:
            if choice == "1":
                print("1 Add candidate  2 View all  3 Search by ID  4 Deactivate")
                sub = ask("Choice: ")
                if sub == "1":
                    cid = candidates.create(ask("Name: "),ask("Email: "),ask("Mobile: "),
                        ask("Qualification: "),ask("Percentage: "),ask("Passing year: "),
                        ask("Technology: "),ask("Skills (comma separated): "),ask("Backlogs: ") or 0)
                    print("Candidate created. ID:", cid)
                elif sub == "2": show_rows(CandidateDAO().all())
                elif sub == "3":
                    record = CandidateDAO().get(int(ask("Candidate ID: ")))
                    show_rows([record] if record else [])
                elif sub == "4": print("Deactivated." if CandidateDAO().deactivate(int(ask("Candidate ID: "))) else "Not found.")
            elif choice == "2":
                print("1 Add company  2 View companies")
                sub = ask("Choice: ")
                if sub == "1":
                    cid = companies.add(ask("Company name: "),ask("Industry: "),ask("Location: "),ask("Contact email: "),ask("Phone: "))
                    print("Company created. ID:",cid)
                elif sub == "2": show_rows(companies.all())
            elif choice == "3":
                print("1 Create job  2 View open jobs")
                sub = ask("Choice: ")
                if sub == "1":
                    jid = jobs.create(ask("Company ID: "),ask("Job title: "),ask("Technology: "),
                        ask("Openings: "),ask("Location: "),ask("Package (LPA): "),
                        ask("Minimum percentage: "),ask("Passing year: "),ask("Maximum backlogs: "),ask("Deadline (YYYY-MM-DD): "))
                    print("Job created. ID:",jid)
                elif sub == "2": show_rows(JobDAO().all_open())
            elif choice == "4":
                print("1 Apply for job  2 View applications  3 Update application status")
                sub = ask("Choice: ")
                if sub == "1": print("Application created. ID:",apps.apply(int(ask("Candidate ID: ")),int(ask("Job ID: "))))
                elif sub == "2": show_rows(ApplicationDAO().all())
                elif sub == "3":
                    aid=int(ask("Application ID: "))
                    status=ask("New status (SHORTLISTED/INTERVIEW/SELECTED/OFFERED/JOINED/REJECTED): ").upper()
                    ApplicationDAO().update_status(aid,status); print("Status updated.")
            elif choice == "5":
                iid=InterviewDAO().add(int(ask("Application ID: ")),ask("Round: "),ask("Date (YYYY-MM-DD HH:MM:SS): "),ask("Mode: "),ask("Interviewer: "))
                print("Interview scheduled. ID:",iid)
            elif choice == "6":
                oid=OfferDAO().add(int(ask("Application ID: ")),ask("Designation: "),float(ask("Package LPA: ")),ask("Offer date YYYY-MM-DD: "),ask("Joining date YYYY-MM-DD: "))
                print("Offer saved. ID:",oid)
            elif choice == "7":
                pid=PlacementDAO().add(int(ask("Application ID: ")),int(ask("Company ID: ")),ask("Designation: "),float(ask("Final package LPA: ")),ask("Joining date YYYY-MM-DD: "))
                print("Placement saved. ID:",pid)
            elif choice == "8":
                print("1 Candidates by technology  2 Open jobs  3 Applications by status  4 Company-wise placements  5 Placed candidates  6 Unplaced candidates")
                sub=ask("Choice: ")
                if sub=="1": show_rows(report_service.candidates_by_technology())
                elif sub=="2": show_rows(JobDAO().all_open())
                elif sub=="3": show_rows(report_service.applications_by_status())
                elif sub=="4": show_rows(report_service.company_wise_placements())
                elif sub=="5": show_rows(report_service.placed_candidates())
                elif sub=="6": show_rows(report_service.report_rows("""SELECT candidate_id,name,email FROM candidates
                    WHERE candidate_id NOT IN (SELECT a.candidate_id FROM applications a JOIN placements p ON p.application_id=a.application_id)"""))
            elif choice == "9":
                print("Thank you."); break
            else: print("Invalid choice.")
        except Exception as exc:
            print("Error:", exc)
