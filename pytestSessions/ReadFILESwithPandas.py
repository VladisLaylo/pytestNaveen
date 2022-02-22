import pandas
import pandas as pd

df = pandas.read_csv('C:\\Users\\User QA\\PycharmProjects\\NumberProvisioning\\errors\\orders__errors (1).csv')
print(df)

count_row = df.shape[0]
print(count_row - 1)

a = len(df)-len(df.drop_duplicates())  # for duplicate numbers
print(a)

item_counts = df["message"].value_counts()  # count of unique messages
print(f"""Messages found: \n{item_counts.to_string()}""")  # to_string() removes Name: message, dtype: int64 from print

"""

# Suppose df is your dataframe then:

count_row = df.shape[0]  # Gives number of rows
count_col = df.shape[1]  # Gives number of columns

# Or, more succinctly
r, c = df.shape

"""

"""
GOOD MANUAL: https://appdividend.com/2020/04/28/python-how-to-select-rows-from-pandas-dataframe/

Supported file formats:

Comma-separated values (CSV)
XLSX
ZIP
Plain Text (txt)
JSON
XML
HTML
Images
Hierarchical Data Format
PDF
DOCX
MP3
MP4
SQL
"""