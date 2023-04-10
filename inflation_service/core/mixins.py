import requests
import json
import pprint

# {217230: 'ogółem', 217231: 'żywność i napoje bezalkoholowe', 217232: 'napoje alkoholowe i wyroby tytoniowe',
# 217233: 'odzież i obuwie', 217234: 'mieszkanie', 217235: 'zdrowie', 217236: 'transport',
# 217237: 'rekreacja i kultura', 217238: 'edukacja'}


class InflationYearlyData:

    def __init__(self):
        self.__categories = InflationYearlyData.__get_categories()
        self.categories_list = list(self.__categories.values())
        self.general_inflation = self.get_general_inflation()

    @staticmethod
    def __get_categories():

        response = requests.get('https://bdl.stat.gov.pl/api/v1/Variables?lang=pl&format=json&subject-id=P2955')
        response_json = json.loads(response.text)
        categories = {}
        for category in response_json['results']:
            categories[category['id']] = category['n1']

        return categories

    def get_category_inflation(self, category_id):

        url = "https://bdl.stat.gov.pl//api/v1/data/by-unit/000000000000?lang=pl&format=json&var-id=" + str(category_id)
        response = requests.get(url)
        response_json = json.loads(response.text)
        category_inflation = {}
        for yearly_inflation in response_json['results'][0]['values']:
            category_inflation[int(yearly_inflation['year'])] = round(yearly_inflation['val'] - 100, 1)

        return category_inflation

    def get_inflation_in_all_categories(self):

        inflation_in_all_categories = {}
        for category_id, category_name in self.__categories.items():
            inflation_in_all_categories[category_name] = self.get_category_inflation(category_id)

        return inflation_in_all_categories

    def get_general_inflation(self):
        category_id = 217230
        general_inflation = self.get_category_inflation(category_id)
        return general_inflation

    def get_year_list(self):
        year_list = [int(year) for year in list(self.general_inflation.keys())]
        return year_list


# a = InflationYearlyData()
# print(pprint.pprint(a.inflation_in_all_categories))
