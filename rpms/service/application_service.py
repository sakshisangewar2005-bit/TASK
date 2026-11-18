from datetime import date
from rpms.dao.candidate_dao import CandidateDAO
from rpms.dao.job_dao import JobDAO
from rpms.dao.application_dao import ApplicationDAO
from rpms.exception.errors import CandidateNotFoundError, JobNotFoundError, DuplicateApplicationError, CandidateNotEligibleError
from rpms.util.logger import log_activity

class ApplicationService:
    def __init__(self):
        self.candidates, self.jobs, self.apps = CandidateDAO(), JobDAO(), ApplicationDAO()

    def apply(self, candidate_id, job_id):
        candidate = self.candidates.get(candidate_id)
        if not candidate: raise CandidateNotFoundError("Candidate not found.")
        job = self.jobs.get(job_id)
        if not job: raise JobNotFoundError("Job not found.")
        reasons = []
        if not candidate["active"]: reasons.append("candidate is inactive")
        if job["status"] != "OPEN": reasons.append("job is not open")
        if job["deadline"] < date.today(): reasons.append("application deadline has passed")
        if candidate["percentage"] < job["min_percentage"]: reasons.append("percentage criteria not satisfied")
        if candidate["passing_year"] != job["passing_year"]: reasons.append("passing year criteria not satisfied")
        if candidate["backlogs"] > job["max_backlogs"]: reasons.append("backlog criteria not satisfied")
        if candidate["technology"].lower() != job["technology"].lower(): reasons.append("technology criteria not satisfied")
        if self.apps.exists(candidate_id, job_id): raise DuplicateApplicationError("Candidate has already applied.")
        if reasons: raise CandidateNotEligibleError("NOT ELIGIBLE: " + ", ".join(reasons))
        application_id = self.apps.add(candidate_id, job_id)
        log_activity(f"Candidate Applied: APP{application_id}")
        return application_id
