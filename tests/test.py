import datetime
from unittest import TestCase
from forex_python.converter import get_rates, get_rate, convert, get_symbol, get_currency_name, RatesNotAvailableError


class TestGetRates(TestCase):
    """
    Test get_rates with valid(ex: USD) and invalid(ex: XYZ) currency code
    """

    def test_get_rates_valid_code(self):
        all_rates = get_rates('USD')

        # Check if return value of get_rates dictionary
        self.assertTrue(isinstance(all_rates, dict))

        # Test at least one rate value returned
        self.assertTrue(len(all_rates.keys()))

        # Test one rate in returned dict is float value
        self.assertTrue(isinstance(all_rates.get('INR'), float))

    def test_get_rates_with_date(self):
        date_obj = datetime.datetime.strptime('2010-05-10', "%Y-%m-%d").date()
        all_rates = get_rates('USD', date_obj)

        # Check if return value of get_rates dictionary
        self.assertTrue(isinstance(all_rates, dict))

        # Test at least one rate value returned
        self.assertTrue(len(all_rates.keys()))

        # Test one rate in returned dict is float value
        self.assertTrue(isinstance(all_rates.get('INR'), float))

    def test_get_rates_invalid_code(self):
        self.assertRaises(RatesNotAvailableError, get_rates, 'XYZ')


class TestGetRate(TestCase):
    """
    Test get_rate function using valid and invalid currency codes
    """

    def test_get_rate_with_valid_codes(self):
        rate = get_rate('USD', 'INR')

        # check if return value is float
        self.assertTrue(isinstance(rate, float))

    def test_get_rate_with_date(self):
        date_obj = datetime.datetime.strptime('2010-05-10', "%Y-%m-%d").date()
        rate = get_rate('USD', 'INR', date_obj)

        # check if return value is float
        self.assertTrue(isinstance(rate, float))

    def test_get_rate_with_invalid_codes(self):
        # raise exception for invalid currency codes
        self.assertRaises(RatesNotAvailableError, get_rate, 'ABCD', 'XYZ')


class TestAmountConvert(TestCase):
    """
    test amount conversion from one currency to other
    """

    def test_amount_convert_valid_currency(self):
        amount = convert('USD', 'INR', 10)

        # test if amount returned in float
        self.assertTrue(isinstance(amount, float))

    def test_amount_convert_date(self):
        date_obj = datetime.datetime.strptime('2010-05-10', "%Y-%m-%d").date()
        amount = convert('USD', 'INR', 10, date_obj)

        # test if amount returned in float
        self.assertTrue(isinstance(amount, float))

    def test_amount_convert_invalid_currency(self):
        # test if amount returned in float
        self.assertRaises(RatesNotAvailableError, convert, 'ABC', 'XYZ', 10)


class TestCurrencySymbol(TestCase):
    """
    test currency symbols from currency codes
    """

    def test_with_valid_currency_code(self):
        self.assertEqual(str(get_symbol('USD')), 'US$')

    def test_with_invalid_currency_code(self):
        self.assertFalse(get_symbol('XYZ'))


class TestCurrencyName(TestCase):
    """
    test currency name from currency codes
    """

    def test_with_valid_currency_code(self):
        self.assertEqual(str(get_currency_name('USD')), 'United States dollar')

    def test_with_invalid_currency_code(self):
        self.assertFalse(get_currency_name('XYZ'))
