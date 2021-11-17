import unittest
import Leccion_01
import pandas as pd


class UnitTest(unittest.TestCase):

    df = pd.DataFrame({'Enero': [100, 350, -450, 500],
                       'Febrero': [200, 300, -500, 100],
                       'Marzo': [150, -200, 300, -500],
                       'Abril': [200, 300, -600, 200],
                       'Mayo': [150, -800, 500, 50],
                       'Junio': [650, -500, -50, 100],
                       'Julio': [100, 300, -100, -100],
                       'Agosto': [-500, -300, -100, 150],
                       'Septiembre': [100, 500, -400, -100],
                       'Octubre': [200, 840, -40, -200],
                       'Noviembre': [100, -700, 500, -100],
                       'Diciembre': [300, 150, -250, -50]})

    def test_monthly_expenses(self):
        result = [-450, -500, -700, -600, -800,
                  -550, -200, -900, -500, -240, -800, -300]
        self.assertEqual(Leccion_01.monthly_expenses(self.df), result)

    def test_monthly_savings(self):
        result = [950, 600, 450, 700, 700, 750,
                  400, 150, 600, 1040, 600, 450]
        self.assertEqual(Leccion_01.monthly_savings(self.df), result)


if __name__ == '__main__':
    unittest.main()
