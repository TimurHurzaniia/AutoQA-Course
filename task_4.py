import unittest
from task_1 import ITEmployee


class Tests(unittest.TestCase):
    def setUp(self):
        self.emp1 = ITEmployee(1986, 'Tester', 1, 600, ['Friendly'])
        self.emp2 = ITEmployee()


    def test_get_satus(self):
        self.assertNotEqual(self.emp2.get_status(), 'Middle ' + str(self.emp2.post))

    def test_ITEmployee(self):
        self.assertEqual(self.emp2.skills, [])

    def test_ITEmployee_class(self):
        self.assertIsInstance(self.emp1, ITEmployee)

    def test_add_skill(self):
        self.emp2.add_skill('Sexy')
        self.assertEqual(self.emp2.skills, ['Sexy'])

    def test_add_skills(self):
        self.emp1.add_skills('Perfect Tester', 'Always Smiled')
        self.assertEqual(self.emp1.skills, ['Friendly', 'Perfect Tester', 'Always Smiled'])

    def test_sal_raise_minus(self):
        self.assertRaises(Exception, lambda: self.emp1.sal_raise(-1))

    def test_sal_raise_char(self):
        self.assertRaises(Exception, lambda: self.emp1.sal_raise('qwerty'))


if __name__ == '__main__':
    unittest.main()
