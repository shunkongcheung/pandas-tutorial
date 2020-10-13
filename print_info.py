''' Learn about meta information of a dataframe '''


def print_info(dataframe):
    ''' print_info '''
    print('Meta information of a dataframe:')
    print()
    print()

    print(get_head(dataframe, 2))
    print()

    print(get_tail(dataframe))
    print()

    describe = get_describe(dataframe)
    print(describe)
    print()

    if not isinstance(describe, str):
        unit_sold_mean = describe['Units Sold']['mean']
        print(f'Unit Sold mean is {unit_sold_mean}')
        print()

    datatypes = get_datatypes(dataframe)
    print(datatypes)
    print()
    if not isinstance(datatypes, str):
        ship_date_datatype = datatypes['Ship Date']
        print(f'Data type of Ship Date is {ship_date_datatype}')
        print()

        unit_price_datatype = datatypes['Unit Price']
        print(f'Data type of Unit Price is {unit_price_datatype}')
        print()

    indexes = get_index(dataframe)
    print(indexes)
    if not isinstance(indexes, str):
        head_indexes = set(indexes[0:5])
        print(f'first few indices are {head_indexes}')
    print()


def get_datatypes(dataframe):
    ''' 
    implement this function to learn how to get datatypes of all columns in a dataframe
    '''

    # return all columns datatypes
    return ''


def get_describe(dataframe):
    ''' 
    implement this function to learn how to get description of a dataframe
    '''

    # return description
    return ''


def get_head(dataframe, size=None):
    ''' 
    implement this function to learn how to get head from a dataframe
    '''

    return ''


def get_index(dataframe):
    ''' 
    implement this function to learn how to get index from a dataframe
    '''

    # return indices of a dataframe
    return ''


def get_tail(dataframe, size=None):
    ''' 
    implement this function to learn how to get tail from a dataframe
    '''

    # return tail with default size
    return ''
