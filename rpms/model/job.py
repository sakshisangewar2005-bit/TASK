class Job:
    def __init__(self, company_id, title, technology, openings, location, package_lpa,
                 min_percentage, passing_year, max_backlogs, deadline):
        self.company_id = int(company_id)
        self.title = title
        self.technology = technology
        self.openings = int(openings)
        self.location = location
        self.package_lpa = float(package_lpa)
        self.min_percentage = float(min_percentage)
        self.passing_year = int(passing_year)
        self.max_backlogs = int(max_backlogs)
        self.deadline = deadline
