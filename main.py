'''
An example of using pandas
'''

import argparse

from import_dataset import import_dataset
from plot_graph import plot_graph
from print_calculate import print_calculate
from print_info import print_info


def main():
    '''main function'''

    parser = argparse.ArgumentParser(description='A pandas example.')

    parser.add_argument(
        '--calculate',
        action='store_const',
        const=True,
        help='using mathematical function like count, filter etc.')

    parser.add_argument(
        '--filename',
        type=str,
        default='100_Sales_Records.csv',
        help='If you have another file, provide filename with this argument.')
    parser.add_argument('--info',
                        action='store_const',
                        const=True,
                        help='extracting meta information. ')

    parser.add_argument('--plot',
                        action='store_const',
                        const=True,
                        help='plotting dataset into graphs')

    args = vars(parser.parse_args())

    filename = args['filename']
    dataframe = import_dataset(filename)

    print(f'Imported file from ${filename}')
    print()

    if args['calculate']:
        print_calculate(dataframe)

    if args['info']:
        print_info(dataframe)

    if args['plot']:
        plot_graph(dataframe)


if __name__ == '__main__':
    main()
