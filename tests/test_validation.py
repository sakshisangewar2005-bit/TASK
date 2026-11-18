import unittest
from rpms.model.candidate import Candidate

class CandidateModelTests(unittest.TestCase):
    def test_candidate_fields(self):
        c = Candidate("Asha", "asha@example.com", "9876543210", "BE", 82, 2026, "Python")
        self.assertEqual(c.name, "Asha")
        self.assertEqual(c.percentage, 82.0)
        self.assertEqual(c.backlogs, 0)

if __name__ == "__main__":
    unittest.main()
