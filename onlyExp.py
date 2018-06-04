import csv

f = open("XTRtab.csv")
fcsv = csv.reader(f)
t = open("XTRexp.csv","w")
tcsv = csv.writer(t)

forbidden = ["Psngr","Pass"]
for row in fcsv:
    if len(row) > 7 and len(row[7])>1:
        flag = 1
        for each in forbidden:
            
            if each in row[1]:
                flag = 0
                break;
        if flag:
            tcsv.writerow(row)
                        
f.close()
t.close()
