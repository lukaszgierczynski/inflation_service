from django.shortcuts import render
from .mixins import InflationYearlyData, create_graph
from .forms import YearSelectForm, CategorySelectForm


# Create your views here.


def index(request):

    inflation_yearly_data = InflationYearlyData()

    form = YearSelectForm()

    start_year = request.GET.get('start_year')
    end_year = request.GET.get('end_year')

    if start_year and end_year:
        form = YearSelectForm(data=request.GET)
        if form.is_valid():
            fig = create_graph(inflation_yearly_data, ['ogółem'], start_year, end_year)
        else:
            fig = create_graph(inflation_yearly_data, ['ogółem'])
    else:
        fig = create_graph(inflation_yearly_data, ['ogółem'])

    chart = fig.to_html()

    context = {'chart': chart, 'form': form}

    return render(request, 'core/chart.html', context)


def category_inflation(request):

    inflation_yearly_data = InflationYearlyData()

    form = CategorySelectForm()

    categories = request.GET.get('options')
    start_year = request.GET.get('start_year')
    end_year = request.GET.get('end_year')

    if categories is not None and start_year is not None and end_year is not None:
        form = CategorySelectForm(request.GET)
        if form.is_valid():
            selected_categories = form.cleaned_data.get('options')
            fig = create_graph(inflation_yearly_data, selected_categories, start_year, end_year)
        else:
            selected_categories = ['ogółem']
            fig = create_graph(inflation_yearly_data, selected_categories)
    else:
        selected_categories = ['ogółem']
        fig = create_graph(inflation_yearly_data, selected_categories)

    chart = fig.to_html()

    context = {'chart': chart, 'form': form}

    return render(request, 'core/category_inflation.html', context)
