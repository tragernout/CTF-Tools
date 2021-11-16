import sys
from datetime import datetime

start = 0
end = 0
sep = ""
form = 0

if sys.argv[1] == "-h" or len(sys.argv) != 5:
    print("Date generator by tragernout(https://github.com/tragernout/):")
    print("Example of using:")
    print("python3 date_gen.py 2019 2021 - 1")
    print("\n")
    print("Where args is:")
    print("python3 date_gen.py <start year> <last year> <separator> <type of output>")
    print("\n")
    print("Outputs types:")
    print("1. yyyy-mm-dd")
    print("2. dd-mm-yyyy")
    print("3. mm-yyyy")
    print("4. yyyy-mm")
else:
    start = int(sys.argv[1])
    end = int(sys.argv[2])
    sep = sys.argv[3] # "Input a separator(like -, for yyyy-mm-dd): "
    form = int(sys.argv[4]) # format: 1. yyyy-mm-dd 2. dd-mm-yyyy 3. mm-yyyy 4. yyyy-mm

def generate(startYear, endYear, separator, formatdata):
    year = range(startYear, endYear + 1)
    month = range(1, 12 + 1)
    day = range(1, 31 + 1)
    if formatdata == 1:
        for y in year:
            for m in month:
                for d in day:
                    print(str(y) + separator + "{:02d}".format(m) + separator + "{:02d}".format(d))
    if formatdata == 2:
        for y in year:
            for m in month:
                for d in day:
                    print("{:02d}".format(d) + separator + "{:02d}".format(m) + separator + str(y))
    if formatdata == 3:
        for y in year:
            for m in month:
                print("{:02d}".format(m) + separator + str(y))
    if formatdata == 4:
        for y in year:
            for m in month:
                print(str(y) + separator + "{:02d}".format(m))
generate(start, end, sep, form)