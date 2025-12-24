import re
import sys
import csv
#importing neccessary modules for this assignment
def displaylines_csv(vals):
    line_blank = ""
    for x in range(len(vals)):
        if x > 0:
           line_blank += ','
        line_blank += vals[x]
    print(line_blank)
#this chunk of code constructs one line (CSV) by iterating over a set of data/values, attaching commas in the middle of them,
# and finally displaying the line (end product)
def main():
    required_columns=sys.argv[3:]
    procedure=sys.argv[2]
    file_csv=sys.argv[1]

    reader_header_rows = open(file_csv, newline='')
    read=csv.reader(reader_header_rows)
    head=next(read)
    row=list(read)
    reader_header_rows.close()
    displaylines_csv(required_columns + ["result"])
#So in this section, the .csv  filename, formula, and requested output columns are all being read, next the .csv is opened,
# the header are displayed and all the values in the rows are put into memort, the file is then terminated and the output header is displayed
    for a in row:
        procedures = procedure
        for column in head:
            original_val = a[head.index(column)]
            try:
                val = str(float(original_val))
            except ValueError:
                val = '"' + original_val + '"'
            sequence = "\\b" + re.escape(column) + "\\b"
            procedures = re.sub(sequence, val, procedures)
#each row in the .csv creates a copy of the formula, changes all the column names within it with the actual value of the row's,
# and a regex is needed to make sure there are correct and proper word complements
        try:
            decision = str(eval(procedures))
        except Exception:
            decision = 'NaN'
        z = []
        for column in required_columns:
            if column in head:
                c = a[head.index(column)]
                if re.search ('[a-zA-Z]', c):
                    c = '"' + c + '"'
                z.append(c)
#so this section here adds the quotes to the name, but doesn't add them to the income numbers
#reference: docs.python.org/3/library/re.html which is one of the links provided for this assignment
            else:
                z.append('NaN')
        z.append(decision)
        displaylines_csv(z)
#finally, this chunk attempts to assess "procedures" to find the answer
#if this fails "NaN" is used and then a list of requested columns is constructed from the rows, the result is attached, and the end product is displayed
if __name__ == "__main__":
    main()
#also, this is needed as this guarantees the program is ran from 
#def main when the file is carried out head on
#In addition, this also ensures the is not brought in by a different script
