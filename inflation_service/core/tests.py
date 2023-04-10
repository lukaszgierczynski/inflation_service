from django.test import TestCase
from .mixins import InflationYearlyData


class InflationYearlyDataTestCase(TestCase):

    def setUp(self):
        self.inflation_yearly_data = InflationYearlyData()
        self.categories = ['ogółem', 'żywność i napoje bezalkoholowe', 'napoje alkoholowe i wyroby tytoniowe',
                           'odzież i obuwie', 'mieszkanie', 'zdrowie', 'transport', 'rekreacja i kultura', 'edukacja']

    def test_categories_list(self):
        for category in self.categories:
            self.assertIn(category, self.inflation_yearly_data.categories_list)

    def test_general_inflation(self):
        self.assertEqual(self.inflation_yearly_data.general_inflation[2003], 0.8)
        self.assertEqual(self.inflation_yearly_data.general_inflation[2004], 3.5)
        self.assertEqual(self.inflation_yearly_data.general_inflation[2012], 3.7)
        self.assertEqual(self.inflation_yearly_data.general_inflation[2015], -0.9)
        self.assertEqual(self.inflation_yearly_data.general_inflation[2021], 5.1)
        self.assertEqual(self.inflation_yearly_data.general_inflation[2022], 14.4)

    def test_get_category_inflation(self):
        food_inflation = self.inflation_yearly_data.get_category_inflation(217231)
        self.assertEqual(food_inflation[2003], -1.0)
        self.assertEqual(food_inflation[2004], 6.3)
        self.assertEqual(food_inflation[2012], 4.3)
        self.assertEqual(food_inflation[2015], -1.7)
        self.assertEqual(food_inflation[2021], 3.2)
        self.assertEqual(food_inflation[2022], 15.4)

    def test_get_inflation_in_all_categories(self):
        inflation_in_all_categories = self.inflation_yearly_data.get_inflation_in_all_categories()
        for category in self.categories:
            self.assertIn(category, inflation_in_all_categories.keys())

        education_inflation = inflation_in_all_categories['edukacja']
        self.assertEqual(education_inflation[2003], 2.3)
        self.assertEqual(education_inflation[2004], 2.7)
        self.assertEqual(education_inflation[2012], 4.2)
        self.assertEqual(education_inflation[2015], 1.1)
        self.assertEqual(education_inflation[2021], 5.0)
        self.assertEqual(education_inflation[2022], 8.7)



