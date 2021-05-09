import pandas as pd

from bokeh.application import Application
from bokeh.application.handlers import FunctionHandler
from bokeh.io import curdoc
from bokeh.layouts import layout
from bokeh.models import (Button, CategoricalColorMapper, ColumnDataSource,
                          HoverTool, Label, SingleIntervalTicker, Slider,)
from bokeh.palettes import Paired12
from bokeh.plotting import figure
from bokeh import sampledata
import numpy as np


def normalize_elem(elem):
    ranger = 250000 - 400
    elem = (elem - 400) / ranger

    range2 = 500 - 20
    return (elem * range2) + 20

def process_data():
    from modeling import final_dict, all_years, countries_list
    
    gdp = final_dict["GDP per capita (current US$)"]
    unemployment = final_dict["Unemployment total (% of total labor force)"]
    labor_force = final_dict["Labor force (% of total)"]

    countries_df = pd.DataFrame({
        'Country': countries_list
    })

    years = list(map(lambda y: int(y), all_years))

    return gdp, unemployment, labor_force, countries_df, countries_list, years

gdp_df, unemployment_df, labor_force_df, countries_df, countries_list, years = process_data()

# Normalize GDP for plotting sizes
for year in years:
    gdp_df[str(year)] = gdp_df[str(year)].apply(normalize_elem)
print(gdp_df)
df = pd.concat({'gdp': gdp_df,
                'unemployment': unemployment_df,
                'labor_force': labor_force_df},
               axis=1)

data = {}
for year in years:
    df_year = df.iloc[:,df.columns.get_level_values(1)==str(year)]
    df_year.columns = df_year.columns.droplevel(1)
    data[year] = df_year.join(countries_df.Country).reset_index().to_dict('series')
    del data[year]['index']
# print(data)
source = ColumnDataSource(data=data[years[0]])

plot = figure(x_range=(0, 10), y_range=(0, 1), title='World Bank Educational Data', height=300)
plot.xaxis.ticker = SingleIntervalTicker(interval=1)
plot.xaxis.axis_label = "Unemployment total (% of total labor force)"
plot.yaxis.ticker = SingleIntervalTicker(interval=10)
plot.yaxis.axis_label = "Labor force (% of total)"

label = Label(x=1.1, y=18, text=str(years[0]), text_font_size='93px', text_color='#eeeeee')
plot.add_layout(label)


color_mapper = CategoricalColorMapper(palette=Paired12, factors=countries_list)
plot.circle(
    x='unemployment',
    y='labor_force',
    size='gdp',
    source=source,
    fill_color={'field': 'Country', 'transform': color_mapper},
    fill_alpha=0.8,
    line_color='#7c7e71',
    line_width=0.5,
    line_alpha=0.5,
    legend_group='Country',
)
plot.add_tools(HoverTool(tooltips="@Country", show_arrow=False, point_policy='follow_mouse'))


def animate_update():
    year = slider.value + 1
    if year > years[-1]:
        year = years[0]
    slider.value = year


def slider_update(attrname, old, new):
    year = slider.value
    label.text = str(year)
    source.data = data[year]

slider = Slider(start=years[0], end=years[-1], value=years[0], step=1, title="Year")
slider.on_change('value', slider_update)

callback_id = None

def animate():
    global callback_id
    if button.label == '► Play':
        button.label = '❚❚ Pause'
        callback_id = curdoc().add_periodic_callback(animate_update, 1000)
    else:
        button.label = '► Play'
        curdoc().remove_periodic_callback(callback_id)

button = Button(label='► Play', width=60)
button.on_click(animate)

layout = layout([
    [plot],
    [slider, button],
], sizing_mode='scale_width')

curdoc().add_root(layout)
curdoc().title = "World Bank Data"
