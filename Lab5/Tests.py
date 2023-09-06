import unittest
from Student import Student


class ClassesTestCase(unittest.TestCase):

    def setUp(self):
        self.name = "Ivan"
        self.age = 23
        self.university = "MIET"
        self.student = Student("Ivan", 26, "MIET")

    def test_name(self):
        self.assertEqual(self.name, self.student.name)

    def test_age(self):
        self.assertTrue(14 < self.student.age < 100)

    def test_university(self):
        self.assertEqual(self.university, self.student.university)


if __name__ == "__main__":
    unittest.main()
