''' Learn about methamatical methods of a dataframe '''


def print_calculate(dataframe):
    ''' print calculation results '''
    count = get_count(dataframe)
    europe_count = get_count_where_region_equals_europe(dataframe)
    unit_price_within_count = get_count_where_unit_price_within(dataframe)
    date_count = get_count_where_ship_date_before(dataframe)

    unit_price_mean = get_mean_of_unit_price(dataframe)

    print(f'Total: {count}')
    print(f'Region in Europe count: {europe_count}')
    print(f'Unit Price within range count: {unit_price_within_count}')
    print(f'Shipping date within a range count: {date_count}')
    print(f'Unit Price mean: {unit_price_mean}')
    print()


def get_count(dataframe):
    ''' get total count of a dataframe '''
    # try to use index / a column to count
    return 0


def get_count_where_region_equals_europe(dataframe):
    ''' get total count where a string column equals something '''
    return 0


def get_count_where_unit_price_within(dataframe):
    ''' get total count where a number column within a range '''
    greater_than, smaller_than = 100, 1000
    return 0


def get_count_where_ship_date_before(dataframe):
    ''' get total count where a date column before a date '''
    end_date = '2015-03-09'  # also try '2019/03/09'

    return len(dataframe[dataframe['Ship Date'] < end_date].index)


def get_mean_of_unit_price(dataframe):
    ''' get mean of the unit price '''
    # try execute it on a string column
    return 0
