#tabwrap2 follows from where tabwrap ended at pulling the table
#as well as the links from the clrtrp page
#tabwrap2 puts them in a csv filename
#be aware that the links are incomplete: no domain prefix
#TODO: write a wrapper around this code to be called every page


from urllib2 import urlopen
from BeautifulSoup import BeautifulSoup
import csv


def tabulate(url_addr,tableFile,flmode): # url_addr is the source
            #tableFile (must be a string with .csv) is the file where the table is saved
    req = urlopen(url_addr, timeout=15)
    soup = BeautifulSoup(req)
    table = soup.findAll('table', {'class': 'results'}) #finds the table with the class results
    csvfile = open(tableFile,flmode)
    writer = csv.writer(csvfile)
    for tab in table:
        for row in tab.findAll("tr"):
             #print "row begins"
             temp = [] #holds the data from current row
             for col in row.findAll("td"):
                    #print col.text
                    temp.append(str(col.text))
             #print "row ends"
             writer.writerow(temp)
    csvfile.close()
