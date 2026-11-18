class Candidate:
    def __init__(self, name, email, mobile, qualification, percentage,
                 passing_year, technology, skills="", backlogs=0, active=True):
        self.name = name
        self.email = email
        self.mobile = mobile
        self.qualification = qualification
        self.percentage = float(percentage)
        self.passing_year = int(passing_year)
        self.technology = technology
        self.skills = skills
        self.backlogs = int(backlogs)
        self.active = bool(active)
