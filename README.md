# Python-CSV-Evaluator
For this assignment you will practice some basic ideas in Python. Please do not use Libraries like Pandas or NumPy.  The regular expression library may prove useful for this problem, though its use is optional.

The concepts for look ahead and look behind is also useful got get re.sub or re.subn to replace only the column name within the formula string.

Refresher/Tutorial on look ahead and look behind is at the following link: Refresher

For this problem you will deal with CSV files with a heading rows and then data rows.

Name,income,tax_rate,total
"Jimbo James",43.3,0.2,533
"Nimbo Names",50.3,0.5,700
"Party Sylvester",80.9,0.6,900
You do not know the number of columns, headings , data etc.. before hand.

Write a script called script9.py which takes in an unlimited number of parameters.

The first parameter is the filename of the csv file, sys.argv[1]
the second parameter is a string representing formula, , sys.argv[2]
the formula can contain columns names, constants such as -80, 34 etc, and the operators +-/*
You will use this formula to create a results column
If the formula can not be evaluated, insert NaN in the results column
The eval function will be useful for evaluating the formula
The remaining parameters are columns to include in the new table, sys.argv[3:]
Print a new csv table to stdout, containing the selected columns taken from the input table in the order they are specified on the command line.  Add a result column generated from the provided formula. For columns specified on the command-line, but is not in the input table the value in the columns should be NaN.

python3 script9.py dataTable.csv "income*5-1*income*tax_rate" Name income salary
For the above invocation the columns Name and income are in the table and salary is not. The column salary in the new table should contain NaN.  The result column should be calculated from the formula "income*5-1*income*tax_rate".

The output should be:

Name,income,salary,result
"Jimbo James",43.3,NaN,207.84
"Nimbo Names",50.3,NaN,226.35
"Party Sylvester",80.9,NaN,355.96

*Note: Attached is a Python file and CSV if you want to try it for yourselves*
