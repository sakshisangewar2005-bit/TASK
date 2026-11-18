import re
from rpms.dao.candidate_dao import CandidateDAO
from rpms.model.candidate import Candidate
from rpms.util.logger import log_activity

class CandidateService:
    def __init__(self): self.dao = CandidateDAO()

    def create(self, name, email, mobile, qualification, percentage, passing_year,
               technology, skills="", backlogs=0):
        if not 0 <= float(percentage) <= 100: raise ValueError("Percentage must be between 0 and 100.")
        if int(backlogs) < 0: raise ValueError("Backlog count cannot be negative.")
        if not re.fullmatch(r"[^@]+@[^@]+\.[^@]+", email): raise ValueError("Enter a valid email.")
        if not re.fullmatch(r"[0-9]{10}", mobile): raise ValueError("Mobile must contain 10 digits.")
        candidate = Candidate(name,email,mobile,qualification,percentage,passing_year,
                              technology,skills,backlogs)
        candidate_id = self.dao.add(candidate)
        log_activity(f"Candidate Created: {candidate_id}")
        return candidate_id
