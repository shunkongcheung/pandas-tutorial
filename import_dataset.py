''' importing dataset from 100_Sales_Records.csv '''

import pandas as pd


def import_dataset(filename):
    '''
    import_dataset based on filename and return a pandas dataframe

    To learn more about importing dataset from various source, visit:
    https://pandas.pydata.org/pandas-docs/stable/reference/io.html
    '''
    return pd.read_csv(filename)
