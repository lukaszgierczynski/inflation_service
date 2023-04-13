import requests
import json
import pprint
import plotly.express as px
import pandas as pd

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


def create_graph(inflation_yearly_data, selected_categories, start_year=None, end_year=None):

    x = inflation_yearly_data.get_year_list()
    if start_year is not None and end_year is not None:
        index = x.index(int(start_year))
        x = x[index:]
        index = x.index(int(end_year))
        x = x[:index + 1]

    inflation_in_all_categories = inflation_yearly_data.get_inflation_in_all_categories()
    inflation_in_selected_categories = {k: v for k, v in inflation_in_all_categories.items() if k in selected_categories}
    inflation_in_selected_cat_and_years = {}

    for category, inflation in inflation_in_selected_categories.items():
        inflation_in_selected_cat_and_years[category] = {}
        for year, value in inflation.items():
            if year in x:
                inflation_in_selected_cat_and_years[category][year] = value

    data_dict = {'x': x}

    for category, inflation in inflation_in_selected_cat_and_years.items():
        data_dict[category] = list(inflation.values())

    df = pd.DataFrame(data_dict)

    fig = px.line(df, x='x', y=selected_categories,
        title="Wartość inflacji w wybranym okresie",
        labels={'x': 'Rok', 'y': 'Inflacja r/r [%]'})

    fig.update_layout(title={
        'font_size': 22,
        'xanchor': 'center',
        'x': 0.5
    })
    fig.update_xaxes(tickmode='linear', dtick=1)

    return fig
