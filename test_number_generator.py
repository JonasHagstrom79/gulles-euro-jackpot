import unittest
from unittest.mock import patch
from number_generator import generate_series

class TestNumberGenerator(unittest.TestCase):

    @patch('number_generator.print')
    def test_generate_series(self, mock_print):
        # Test with count = 1
        generate_series(1)
        self.assertEqual(mock_print.call_count, 3)  # Expect 3 print calls (2 series prints + 1 newline)
        mock_print.reset_mock()

        # Test with count = 2
        generate_series(2)
        self.assertEqual(mock_print.call_count, 6)  # Expect 6 print calls (2 series prints + 1 newline) * 2

        # Test with count = 0 (should not print anything)
        generate_series(0)
        self.assertEqual(mock_print.call_count, 0)

if __name__ == '__main__':
    unittest.main()
