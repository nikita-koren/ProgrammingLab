import unittest
from models import TrendModel

class TestTrendModel(unittest.TestCase):

    def test_previsione_corretta(self):
        trend_model = TrendModel()
        test_data = [50, 52, 60]
        self.assertEqual(trend_model.prevedi(test_data), 65)

    def test_numero_errato_di_mesi(self):
        trend_model = TrendModel()
        wrong_test_data = [50, 52, 60, 70]

        with self.assertRaises(ValueError):
            trend_model.prevedi(wrong_test_data)

if __name__ == '__main__':
    unittest.main()