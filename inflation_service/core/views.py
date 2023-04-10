from django.shortcuts import render
from .mixins import InflationYearlyData
import plotly.express as px
from .forms import YearSelectForm


# Create your views here.


def index(request):

    inflation_yearly_data = InflationYearlyData()
    year_list = inflation_yearly_data.get_year_list()

    form = YearSelectForm()

    x = list(inflation_yearly_data.general_inflation.keys())
    y = list(inflation_yearly_data.general_inflation.values())

    start_year = request.GET.get('start_year')
    end_year = request.GET.get('end_year')

    if start_year and end_year:
        form = YearSelectForm(data=request.GET)
        if form.is_valid():
            index = x.index(int(start_year))
            x = x[index:]
            y = y[index:]

            index = x.index(int(end_year))
            x = x[:index+1]
            y = y[:index+1]

    fig = px.line(
        x=x,
        y=y,
        title="Inflacja ogółem",
        labels={'x': 'Rok', 'y': 'Inflacja r/r [%]'}
    )

    fig.update_layout(title={
        'font_size': 22,
        'xanchor': 'center',
        'x': 0.5
    })
    fig.update_xaxes(tickmode='linear', dtick=1)

    chart = fig.to_html()

    context = {'chart': chart, 'form': form, 'year_list': year_list}

    return render(request, 'core/chart.html', context)