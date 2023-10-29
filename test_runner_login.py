import unittest
import allure
import pytest


class HtmlTestRunnerTestSuite(unittest.TestCase):

    @allure.feature('Generate Allure Report')
    def test_generate_allure_report_login(self):
        # Generate the report with allure command line
        pytest.main(['-v', '--alluredir', './allure-results-login',
                     './Login/Tests/LoginTest.py'
                     ])


if __name__ == '__main__':
    unittest.main()
