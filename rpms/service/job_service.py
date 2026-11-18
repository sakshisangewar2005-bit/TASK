from rpms.dao.job_dao import JobDAO
from rpms.model.job import Job
from rpms.util.logger import log_activity

class JobService:
    def __init__(self): self.dao = JobDAO()
    def create(self, company_id, title, technology, openings, location, package_lpa,
               min_percentage, passing_year, max_backlogs, deadline):
        if int(openings) <= 0: raise ValueError("Openings must be greater than zero.")
        if not 0 <= float(min_percentage) <= 100: raise ValueError("Minimum percentage must be 0-100.")
        job_id = self.dao.add(Job(company_id,title,technology,openings,location,package_lpa,
                                  min_percentage,passing_year,max_backlogs,deadline))
        log_activity(f"Job Created: {job_id}")
        return job_id
