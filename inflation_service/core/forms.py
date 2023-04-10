from django import forms
from .mixins import InflationYearlyData


# class DateForm(forms.Form):
#     start = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
#     end = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

inflation_yearly_data = InflationYearlyData()
year_list = inflation_yearly_data.get_year_list()


class YearSelectForm(forms.Form):
    start_year = forms.IntegerField(widget=forms.Select(choices=[(year, year) for year in year_list]), initial=min(year_list))
    end_year = forms.IntegerField(widget=forms.Select(choices=[(year, year) for year in year_list]), initial=max(year_list))

    def clean(self):
        cleaned_data = super().clean()
        start_year = cleaned_data.get("start_year")
        end_year = cleaned_data.get("end_year")

        if end_year <= start_year:
            raise forms.ValidationError("Rok końcowy musi być rokiem póżniejszym niż rok początkowy!")


# todo: zapytać cgat gpt: jak w django stworzyć widget do wyboru roku z ograniczonej list lat