''' Learning how to use pandas and matplotlib to plot various graph '''
import pandas as pd
import matplotlib.pyplot as plt


def plot_graph(dataframe):
    '''plot graph '''
    plt.close('all')
    plot_line_chat_with_order_date(dataframe)
    plot_bar_chart(dataframe)
    plot_pie_chart(dataframe)
    plt.show()


def get_sum(dataframe, region, is_online):
    ''' helper function get sum of unit price by region and online or not '''
    value = 'Online' if is_online else 'Offline'
    offline_cond = dataframe['Sales Channel'] == value
    return dataframe[(dataframe['Region'] == region)
                     & (offline_cond)]['Unit Price'].sum()


def plot_line_chat_with_order_date(dataframe):
    ''' plot unit price and unit cost to order date line chart '''

    # sort dataframe by date
    dataframe = dataframe.sort_values(by='Order Date')

    # extract unit price as value and date column as index
    unit_price = dataframe['Unit Price'].to_numpy()
    units_sold = dataframe['Units Sold'].to_numpy()
    order_date = dataframe['Order Date']


def plot_bar_chart(dataframe):
    ''' plot bar chart with regions '''
    # get sums
    europe_off_sum = get_sum(dataframe, 'Europe', False)
    asia_off_sum = get_sum(dataframe, 'Asia', False)
    africa_off_sum = get_sum(dataframe, 'Sub-Saharan Africa', False)

    europe_on_sum = get_sum(dataframe, 'Europe', True)
    asia_on_sum = get_sum(dataframe, 'Asia', True)
    africa_on_sum = get_sum(dataframe, 'Sub-Saharan Africa', True)


def plot_pie_chart(dataframe):
    ''' plot pie chart with regions '''
    # get sums
    europe_off_sum = get_sum(dataframe, 'Europe', False)
    asia_off_sum = get_sum(dataframe, 'Asia', False)
    africa_off_sum = get_sum(dataframe, 'Sub-Saharan Africa', False)
