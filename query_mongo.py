# 'query_mongo.py'

# libraries and tings
from pymongo import MongoClient
import datetime
import sys

# connect & config the mongo store
client = MongoClient()
store  = client['housing']

# create an array of the neighborhood names
hoodList = store.collection_names()

# create a dict of years for each neighborhood
arrayOfHoods = []

# iterate through each neighborhood and get all data for 2010->2015
for hood in hoodList:

    dataPoints = store.get_collection(hood).find({"year": {"$gt": 2009}})

    # create a temp obj.
    temp = {}
    temp["data"] = []
    temp["neighborhood"] = hood

    # for each datapoint, add tuple to hood data
    for datapoint in dataPoints:

        date = datapoint["date"]
        price = datapoint["price"]

        temp["data"].append( (date, price) )

    # append the temp nhood obj to the glbl array
    arrayOfHoods.append( temp )

# clean garbage values in array
for item in arrayOfHoods:
    if len(item["data"]) < 1:
        arrayOfHoods.remove( item )


def calcGentrInterval( arg ):
    """calculations for a given interval:
        + 3 month (3)
        + 6 month (6)
        + 1 year  (12)
        + 2 years (24)"""
    # create collections for the interval of desired data
    if ( arg == 3 ):
        collection = store['threemonths']
    elif ( arg == 6 ):
        collection = store['sixmonths']
    elif ( arg == 12 ):
        collection = store['oneyear']
    elif ( arg  == 24 ):
        collection = store['twoyears']

    interval = arg
    arr = []

    # calc the change over this interval
    for h in arrayOfHoods:
        temp = {}

        data = h["data"]
        temp["neighborhood"] = h["neighborhood"]
        temp["data"] = []

        # calculate data for that interval and place back in arr
        for d in range(0, len(data)-interval, interval):
            data1 = data[d]  # start date
            data2 = data[d + interval] # end end
            percentChange =  ((data2[1]-data1[1]) / data1[1])
            price = data1[1] # start price
            temp["data"].append( (data1[0],data2[0],percentChange, price) )

        arr.append ( temp )


    # get the size of one element's data in arr
    size = len( arr[0]["data"] )

    filterSet = []
    for i in range(0, size-1):

        # get the ith elem. for each hood
        for h in arr:
            try:  # ignore garbage data
                name = h["neighborhood"]
                percent = h["data"][i][2]
                start = h["data"][i][0]
                end = h["data"][i][1]
                startprice = h["data"][i][3]
            except IndexError:
                continue

            filterSet.append ( (name, percent, start, end, startprice) )

        # using filterSet, calculate bottom 40th percent -> top33
        bottom40 = sorted(filterSet, key=lambda x: x[4])
        threshold = int( round ( 0.50 * len(filterSet) ))
        start_prices = [(x[0], x[-1]) for x in bottom40]


        top33 = []
        for i in range(0, threshold):
            top33.append( bottom40[i] )

        # calculate top 33rd percentile (67th percentile)
        sortedArr = sorted(top33, key=lambda x: x[1])
        index = int( round( 0.67 * len( sortedArr ) ) )
        for j in range(index, len(sortedArr)):
            name = sortedArr[j][0]
            percChange = sortedArr[j][1]
            startdate = sortedArr[j][2]
            enddate = sortedArr[j][3]
            # insert into appr. mongo collection
            data_point = collection.insert_one(
            {
                "name": name,
                "percent": percChange,
                "start": startdate,
                "end": enddate,
            })
            print "name: " + name
            print "startdate: " + str(startdate)
            print "Object Added."

        #clear the arrays and repeat
        del top33[:]
        del filterSet[:]

        #break # do this for one interval

# call the function w/ param
calcGentrInterval( 3 )
calcGentrInterval( 6 )
calcGentrInterval( 12 )
calcGentrInterval( 24 )
