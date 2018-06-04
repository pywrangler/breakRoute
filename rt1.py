import csv

def trimRoute(fullroute):
    for station in fullroute:
        if source in station:
            srcIndex = fullroute.index(station)
        if dest in station:
            dstIndex = fullroute.index(station)
    #trimming the list as per the indexes found
    if srcIndex<dstIndex:
        return fullroute[srcIndex:(dstIndex+1)]
    else:
        #route must be reversed as dstIndex comes b4 srcIndex
        reverseRoute = fullroute[dstIndex:(srcIndex+1)] #trimming
        return reverseRoute[::-1] #reversing


xtr = open("XTRtab.csv","r")
xtrcsv = csv.reader(xtr)

trainlist = [] #holds the list of trains which travel from dest to source
routelist = []
source = raw_input("Give source station code")
dest = raw_input("Give destination station code")

for row in xtrcsv:
    if len(row)>7:
        if source in row[7] and dest in row[7]:
            temp = []
            temp.append(row[0])
            temp.append(row[1])
            trainlist.append(temp)
            #making route list
            temproute = row[7].split("-")
            temproute.pop()
            routelist.append(temproute)
b4 = len(routelist)

#trimming station outside of route
for routeindex in range(len(routelist)):
    routelist[routeindex] = trimRoute(routelist[routeindex])
    
#REMOVING SUBSET routes
for routeA in routelist:
    for routeB in routelist:
        if set(routeA).issubset(routeB) and routeA!=routeB:
            routelist.remove(routeA)
            break

#removing duplicates
unikroutelist = []
for _route in routelist:
    if _route not in unikroutelist:
        unikroutelist.append(_route)
      

#REMOVING SUBSET routes for second time for paranormal reasons!!
for routeA in unikroutelist:
    for routeB in unikroutelist:
        if set(routeA).issubset(routeB) and routeA!=routeB:
            unikroutelist.remove(routeA)
            break

a4 = len(routelist)
a4u = len(unikroutelist)
xtr.close()
print "no of subsets removed", (b4-a4)," \n current no. of routes",a4
print "no of unique routes",a4u


print "No. of trains found",len(trainlist)
print"Unique routes found:"
for unikroute in unikroutelist:
    print unikroute
    print "*************************************************************"
print trainlist
