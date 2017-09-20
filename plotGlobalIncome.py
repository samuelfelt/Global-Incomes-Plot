from bokeh.plotting import figure, output_file, save
from bokeh.models import Legend
import pandas as pd

def generate_chart(data_frame, country, poor_color='#000000',
                    middle_color='#000000', rich_color='#000000',
                   rich_fill='#000000'):
    """
    Given a country name, will generate a chart of the GDP per Capita by Decile

    Takes optional kwargs for coloring the chart

    """

    country_data = data_frame.loc[data_frame.Country == country]
    year_array = country_data.Year.as_matrix()
    dec1 = country_data['Decile 1 Income'].as_matrix()
    dec2 = country_data['Decile 2 Income'].as_matrix()
    dec3 = country_data['Decile 3 Income'].as_matrix()
    dec4 = country_data['Decile 4 Income'].as_matrix()
    dec5 = country_data['Decile 5 Income'].as_matrix()
    dec6 = country_data['Decile 6 Income'].as_matrix()
    dec7 = country_data['Decile 7 Income'].as_matrix()
    dec8 = country_data['Decile 8 Income'].as_matrix()
    dec9 = country_data['Decile 9 Income'].as_matrix()
    dec10 = country_data['Decile 10 Income'].as_matrix()

    output_file(country + ".html", title=country
                                         + " per Capita GDP by Decile Over Time")

    plot = figure(title=country + " GDP per Capita",
                  x_axis_label='Year', y_axis_label='GDP Per Capita')

    poor_line = plot.line(year_array, dec1, line_dash="2 4",
                        line_color=poor_color, line_width=2)
    plot.line(year_array, dec2, line_color=middle_color, line_width=2)
    plot.line(year_array, dec3, line_color=middle_color, line_width=2)
    plot.line(year_array, dec4, line_color=middle_color, line_width=2)
    plot.line(year_array, dec5, line_color=middle_color, line_width=2)
    plot.line(year_array, dec6, line_color=middle_color, line_width=2)
    plot.line(year_array, dec7, line_color=middle_color, line_width=2)
    plot.line(year_array, dec8, line_color=middle_color, line_width=2)
    plot.line(year_array, dec9, line_color=middle_color, line_width=2)
    rich_line = plot.line(year_array, dec10, line_color=rich_color,
                          line_width=2)
    rich_circle = plot.circle(year_array, dec10, fill_color=rich_fill,
                              line_color=rich_color, size=6)

    legend = Legend(items=[
        ('Poorest Decile', [poor_line]),
        ('Richest Decile', [rich_line, rich_circle])
                            ])

    plot.add_layout(legend, 'below')

    save(plot)



data = pd.read_csv('GlobalIncome.csv')

AFG_BLACK = '#000000'
AFG_RED = '#BF0000'
AFG_GREEN = '#009900'

PAK_GREEN= '#006600'

TUR_GREEN = '#28AE66'
TUR_YELLOW = '#FAAE29'
TUR_RED = '#CA3745'

UZB_BLUE = '#0099B5'
UZB_RED = '#CE1126'
UZB_GREEN = '#1EB53A'


generate_chart(data,'Afghanistan', poor_color=AFG_BLACK, middle_color=AFG_RED,
               rich_color=AFG_GREEN, rich_fill=AFG_GREEN)

generate_chart(data,'Pakistan', poor_color=PAK_GREEN, middle_color=PAK_GREEN,
               rich_color=PAK_GREEN, rich_fill='white')

generate_chart(data, 'Uzbekistan', poor_color=UZB_BLUE, middle_color=UZB_RED,
               rich_color=UZB_GREEN, rich_fill='white')

generate_chart(data, 'Turkmenistan', poor_color=TUR_GREEN, middle_color=TUR_YELLOW,
               rich_color=TUR_RED, rich_fill='white')