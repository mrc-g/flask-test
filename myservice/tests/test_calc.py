import unittest
from myservice import app

app.testing = True

# TODO: Extend these component tests for the calc view
#       and THEN implement all 4 operations!
# DO NOT REMOVE EXISTING TESTS!


class TestCalc(unittest.TestCase):

    def test_sum1(self):
        tested_app = app.test_client()
        reply = tested_app.get('/calc/sum?m=3&n=5').get_json()
        self.assertEqual(reply['result'], '8')

    def test_div1(self):
        tested_app = app.test_client()
        reply = tested_app.get('/calc/div?m=6&n=2').get_json()
        self.assertEqual(reply['result'], '3')

    def test_mul1(self):
        tested_app = app.test_client()
        reply = tested_app.get('/calc/mul?m=3&n=2').get_json()
        self.assertEqual(reply['result'], '6')

    def test_sub1(self):
        tested_app = app.test_client()
        reply = tested_app.get('/calc/sub?m=5&n=2').get_json()
        self.assertEqual(reply['result'], '3')

    def test_sum_missing_n(self):
        tested_app = app.test_client()
        reply = tested_app.get('/calc/sum?m=3').get_json()
        self.assertEqual(reply['result'], 'MissingArgument')

    def test_div_missing_n(self):
        tested_app = app.test_client()
        reply = tested_app.get('/calc/div?m=3').get_json()
        self.assertEqual(reply['result'], 'MissingArgument')

    def test_mul_missing_n(self):
        tested_app = app.test_client()
        reply = tested_app.get('/calc/mul?m=3').get_json()
        self.assertEqual(reply['result'], 'MissingArgument')

    def test_sub_missing_n(self):
        tested_app = app.test_client()
        reply = tested_app.get('/calc/sub?m=5').get_json()
        self.assertEqual(reply['result'], 'MissingArgument')

    def test_sum_value_n(self):
        tested_app = app.test_client()
        reply = tested_app.get('/calc/sum?m=3&n=a').get_json()
        self.assertEqual(reply['result'], 'ValueError')

    def test_div_value_n(self):
        tested_app = app.test_client()
        reply = tested_app.get('/calc/div?m=3&n=a').get_json()
        self.assertEqual(reply['result'], 'ValueError')

    def test_mul_value_n(self):
        tested_app = app.test_client()
        reply = tested_app.get('/calc/mul?m=3&n=a').get_json()
        self.assertEqual(reply['result'], 'ValueError')

    def test_sub_value_n(self):
        tested_app = app.test_client()
        reply = tested_app.get('/calc/sub?m=5&n=a').get_json()
        self.assertEqual(reply['result'], 'ValueError')

    def test_sum_missing_m(self):
        tested_app = app.test_client()
        reply = tested_app.get('/calc/sum?m=3').get_json()
        self.assertEqual(reply['result'], 'MissingArgument')

    def test_div_missing_m(self):
        tested_app = app.test_client()
        reply = tested_app.get('/calc/div?n=3').get_json()
        self.assertEqual(reply['result'], 'MissingArgument')

    def test_mul_missing_m(self):
        tested_app = app.test_client()
        reply = tested_app.get('/calc/mul?n=3').get_json()
        self.assertEqual(reply['result'], 'MissingArgument')

    def test_sub_missing_m(self):
        tested_app = app.test_client()
        reply = tested_app.get('/calc/sub?n=5').get_json()
        self.assertEqual(reply['result'], 'MissingArgument')

    def test_sum_value_m(self):
        tested_app = app.test_client()
        reply = tested_app.get('/calc/sum?m=a&n=3').get_json()
        self.assertEqual(reply['result'], 'ValueError')

    def test_div_value_m(self):
        tested_app = app.test_client()
        reply = tested_app.get('/calc/div?m=a&n=3').get_json()
        self.assertEqual(reply['result'], 'ValueError')

    def test_mul_value_m(self):
        tested_app = app.test_client()
        reply = tested_app.get('/calc/mul?m=a&n=3').get_json()
        self.assertEqual(reply['result'], 'ValueError')

    def test_sub_value_m(self):
        tested_app = app.test_client()
        reply = tested_app.get('/calc/sub?m=a&n=3').get_json()
        self.assertEqual(reply['result'], 'ValueError')

    def test_div_zero(self):
        tested_app = app.test_client()
        reply = tested_app.get('/calc/div?m=3&n=0').get_json()
        self.assertEqual(reply['result'], 'DivisionByZeroError')
