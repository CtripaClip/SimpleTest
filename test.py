from main import get_formated_name
import unittest

class Test(unittest.TestCase):
    """Tests for main.py"""

    def test_firsst_name(self):
        formated_name = get_formated_name('Jenis', 'Jopin')
        self.assertEqual(formated_name, 'Jenis Jopin')

if __name__ == '__main__':
    unittest.main()
