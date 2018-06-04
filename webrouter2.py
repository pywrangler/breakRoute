import csv
from operator import itemgetter
from flask import Flask,jsonify

rengFlobj = Flask(__name__)
@rengFlobj.route('/<qstryng>', methods=['GET'])


def starter(qstryng):
    msource,mdest = qstryng.split("-")
    xtr = open("XTRnoblank.csv","r")
    xtrcsv = csv.reader(xtr)

    #making level 1 routelist from csv
    routelist = getRlistfromCSV(xtrcsv,msource,mdest)

    #trimming station outside of route
    #WARNING the source and dest are also trimmed:only stns in b/w remain
    for routeindex in range(len(routelist)):
        routelist[routeindex] = trimRoute(routelist[routeindex],msource,mdest)


    midStnlist = getUnikstn(routelist)
    dirTrains = getTrains(msource, mdest,xtr,xtrcsv)
    midstnswithtrains = getStnandTrains(msource, mdest,midStnlist,xtr,xtrcsv,dirTrains)
    rankinds = rankbytrains(midstnswithtrains)
    rankinds =  rankinds[::-1] #reversing rankinds because its in ascending order
    # for ind in rankinds:
    #     print midstnswithtrains[ind][0]
    #     print "part A",midstnswithtrains[ind][1],"part B",midstnswithtrains[ind][2]

    xtr.close()
    sortedmids = []
    for rank in rankinds:
        sortedmids.append(midstnswithtrains[rank])
    return jsonify(sortedmids)

def getRlistfromCSV(CSVobj,source,dest):
    _routelist = []
    for row in CSVobj:
        if len(row)>7:
            if source in row[7] and dest in row[7]:
                temproute = row[7].split("-")
                temproute.pop()
                _routelist.append(temproute)
    return _routelist

def trimRoute(fullroute,source,dest):
    for station in fullroute:
        if source in station:
            srcIndex = fullroute.index(station)
        if dest in station:
            dstIndex = fullroute.index(station)
    #trimming the list as per the indexes found
    #WARNING the source and dest are also trimmed:only stns in b/w remain
    if srcIndex<dstIndex:
        return fullroute[(srcIndex+1):dstIndex]
    else:
        #route must be reversed as dstIndex comes b4 srcIndex
        reverseRoute = fullroute[(dstIndex+1):srcIndex] #trimming
        return reverseRoute[::-1] #reversing

def getUnikstn(fullroute):
    stnlist = []
    for route in fullroute:
        for station in route:
            if station not in stnlist:
                stnlist.append(station)
    return stnlist

def getTrains(trsource,trdest,xtr,xtrcsv):
    xtr.seek(0)
    _trainlist =[]
    for row in xtrcsv:
        if len(row)>7:
            if trsource in row[7] and trdest in row[7]:
                temp = []
                temp.append(row[0])
                temp.append(row[1])
                _trainlist.append(temp)
    return _trainlist
def getStnandTrains(source,dest,_midStnlist,xtr,xtrcsv,dirTrains): #returns [ <[ [midstation][partA][partB] ]>..<>..<>]
    stnAndtrains = []
    for midstation in _midStnlist:
        temp = []
        temp.append(midstation)
        atrn = getTrains(source, midstation,xtr,xtrcsv)
        btrn = getTrains(midstation, dest,xtr,xtrcsv)
        uatrn = [i for i in atrn if i not in dirTrains] #checking halfroute trains
        ubtrn = [i for i in btrn if i not in dirTrains]
        Luatrn = len(uatrn)
        Lubtrn = len(ubtrn)
        if Luatrn>0 and Lubtrn>0 :#adding extra points to stations with more halroute trains
            temp.append(Luatrn*100 )
            temp.append( Lubtrn*100 )
        else:
            temp.append( Luatrn  ) #appending lengths instead of full trainlist
            temp.append( Lubtrn  )
        stnAndtrains.append(temp)
    return stnAndtrains

def rankbytrains(stnparts):
    indsizelist = []
    for stnSet in stnparts:
        indsize = []
        indsize.append(stnparts.index(stnSet))
        indsize.append( stnSet[1] + stnSet[2] ) #these are sizes of trainlist and not the actual trainlsit
        indsizelist.append(indsize)
    #sorting indsizelist by size
    indsizelist = sorted(indsizelist, key=itemgetter(1))
    onlyinds = []
    for each in indsizelist:
        onlyinds.append(each[0])
    return onlyinds
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#function defs ends script begins
rengFlobj.run(debug=False)
