from tabulator2 import tabulate
import csv
def addstn(_row):
    stnstring = ''
    timestring = ''
    stnfile = open("stnlist.csv")
    stncsv = csv.reader(stnfile)
    for row in stncsv:
        if len(row)>1:
            stnstring += row[1]+'-'
            timestring += '('+row[3]+'>'+row[4]+')-'
    stnfile.close()
    _row.append(stnstring)
    _row.append(timestring)
    return _row






a = open('TRtab.csv')
b = open('XTRtab.csv','a')
f1 = csv.reader(a)
f2 = csv.writer(b)
dom = 'https://www.cleartrip.com'
row= f1.next()
row=f1.next()
while str(row[0])!='19943':
    row = f1.next()
    if len(row)<1:
        row = f1.next()

for row in f1:
    if len(row)>1:
        stnURI = dom+row[2]
        try:
            tabulate(stnURI,"stnlist.csv","w")
            print stnURI,"tabulated"
        except:
            errlog = open("Errorlog","w")
            print "station table failed to download",row
            errlog.write(row)
            errlog.write(" \n")
            errlog.close()
            continue

        f2.writerow( addstn(row) )


a.close()
b.close()
