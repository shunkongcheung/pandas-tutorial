# pandas-tutorial

Introduction to [pandas](https://pandas.pydata.org/).

Using Pandas to analysis data from a CSV file.

## Getting Started

Create virtual environment and install required package.

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

After finishing, run the following to exit virtual environment:
```bash
deactivate
```  

### What is it about?

Inside repository, there is a [100 Sales Records.csv](100_Sales_Records.csv) which is downloaded from [here](http://eforexcel.com/wp/downloads-18-sample-csv-files-data-sets-for-testing-sales/).

We will be working with this file to: 
1. get dataset meta information by running `python main.py --info`
2. learning how to use filter, count and other calculation method by `python main.py --count`
3. deduce information based on existing data with `python main.py --calculate`
4. plot dataset by `python main.py --plot`
