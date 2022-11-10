import csv
import sys

'''
cmdline args are multiple filenames --
In the CSV output:
* Filename will be column name
* File lines will be column rows
'''

columns = sys.argv[1:]
data = {}
for infile in columns:
    with open(infile, encoding='utf-8') as fd:
        data[infile] = fd.readlines()
# List of dicts (rows)
rows = []
# Iterate over values of the first column with enumerated index
col1_header = list(data.keys())[0]
for index, value in enumerate(data[col1_header]):
    # Create row with the header:value of the first column
    row = {col1_header: value.rstrip()}
    # Iterate over other column values
    for col_header, column in data.items():
        if col_header == col1_header:
            continue
        # Add other column header and value to row
        row[col_header] = column[index].rstrip()
    rows.append(row)
with open('out.csv', encoding='utf-8', mode='w', newline='') as fd:
    writer = csv.DictWriter(fd, fieldnames=columns)
    writer.writeheader()
    writer.writerows(rows)