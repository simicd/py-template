import unittest
import pytemplate

class TestTemplate(unittest.TestCase):

    def test_template_function(self):
        # Input
        name = "World"

        # Expected Output
        expected = "Hello World"

        # Actual Output
        actual = pytemplate.template_function(name)

        # Assert
        self.assertEqual(actual, expected, msg="The two strings do not match")