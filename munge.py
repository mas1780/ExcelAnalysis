# place your code to clean up the data file below.
import csv
#df = open(“data/spain-la-liga-primera-division-2019-to-2020.csv”, “r”)
#read the file on python (CSV reader)
#key vlaues and
input_file = csv.DictReader(open ('data/spain-la-liga-primera-division-2019-to-2020.csv'))
headings = ['HomeTeam', 'AwayTeam', 'FTHG', 'FTAG', 'FTR', 'HTHG', 'HTAG', 'HTR', 'HS', 'AS', 'B365CH', 'B365CA']
headings_joined = (',').join(headings)
#new useful file
outfile = open('data/clean_data.csv', 'w')
outfile.write(headings_joined)
outfile.write('\n')
for line in input_file:
    k = list(line.values())
    write_line = ','.join(k)
    #steps to remove all the values i do not want
    write_line = [] # it is just an emopty line 5,4, barcelona ... we need to add values
    write_line.append(line['HomeTeam'])
    write_line.append(line['AwayTeam'])
    write_line.append(line['FTHG'])
    write_line.append(line['FTAG'])
    write_line.append(line['FTR'])
    write_line.append(line['HTHG'])
    write_line.append(line['HTAG'])
    write_line.append(line['HTR'])
    write_line.append(line['HS'])
    write_line.append(line['AS'])
    write_line.append(line['B365CH'])
    write_line.append(line['B365CA'])
    x = ','.join(write_line)
    #remove columns 4-5
    outfile.write(x)
    outfile.write('\n')