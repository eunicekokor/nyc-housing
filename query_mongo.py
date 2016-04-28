# 'query_mongo.py'

# libraries and tings
from pymongo import MongoClient
import datetime
import sys

# connect & config the mongo store
client = MongoClient()
store  = client['housing']

# use 2nd argument as param
param = int (sys.argv[1])

# create collections for the interval of desired data
if ( param == 3 ):
    collection = store['threemonths']
elif ( param == 6 ):
    collection = store['sixmonths']
elif ( param == 12 ):
    collection = store['oneyear']
elif ( param == 24 ):
    collection = store['twoyears']

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
    # check the interval passed in
    interval  = arg
    arr = []

    for h in arrayOfHoods:
        temp = {}

        data = h["data"]
        temp["neighborhood"] = h["neighborhood"]
        temp["data"] = []

        # calculate data for that interval and place back in arr
        for d in range(0, len(data)-interval, interval):
            data1 = data[d]  # start date
            data2 = data[d + interval] # end end
            delta_price =  data2[1]-data1[1]
            temp["data"].append( (data1[0],data2[0],delta_price) )

        arr.append ( temp )

    # get the size of one element's data in arr
    size = len( arr[0]["data"] )
    print (size)

    top33 = []
    for i in range(0, size-1):

        # get the ith elem. for each hood
        for h in arr:
            name = h["neighborhood"]
            price = h["data"][i][2]

            top33.append ( (name,price) )

        # calculate top 33rd percentile (67th percentile)
        sortedArr = sorted(top33, key=lambda x: x[1])
        index = int( round( 0.67 * len( sortedArr ) ) )
        for j in range(index, len(sortedArr)):
            #break
            print sortedArr[j] # nams of sorted Arr

        #clear the array and repeat
        del top33[:]

        #break # do this for one interval

# call the function w/ param
calcGentrInterval( param )
