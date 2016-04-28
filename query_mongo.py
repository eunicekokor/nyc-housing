# 'query_mongo.py'
#
# TO DO
#   + order in list and get top 40%.
#   + make visualisation [optional]

# libraries and tings
from pymongo import MongoClient
import datetime
import sys

# connect & config the mongo store
client = MongoClient()
store  = client['housing']

# create collections for each interval of desired data
three  = store['threemonths']
six    = store['sixmonths']
one    = store['oneyear']
two    = store['twoyears']


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

def calcInterval():
    """calculations for a given interval:
        + 3 month (3)
        + 6 month (6)
        + 1 year  (12)
        + 2 years (24)"""

    arr = []

    for h in arrayOfHoods:
        temp = {}

        data = h["data"]
        temp["neighborhood"] = h["neighborhood"]
        temp["data"] = []

        # calculate data for that interval and place back in arr
        for d in range(0, len(data)-3, 3):
            data1 = data[d]  # start date
            data2 = data[d+3] # end end
            delta_price =  data2[1]-data1[1]
            temp["data"].append( (data1[0],data2[0],delta_price) )

        arr.append ( temp )

    # clean up arr [weird garbage value from mongo]
    for item in arr:
        if len(item["data"]) < 1:
            arr.remove( item )

    # get the size of one element's data in arr
    size = len( arr[0]["data"] )

    fortyPer = []
    for i in range(0, size):

        # get the ith elem. for each hood
        for h in arr:
            name = h["neighborhood"]
            price = h["data"][i][2]

            fortyPer.append ( (name,price) )

        # calculate top 40th percentile (60th percentile)
        sortedArr = sorted(fortyPer, key=lambda x: x[1])
        count = len( sortedArr )
        index = int( round( 0.60 * count ) )
        for j in range(index, len(sortedArr)):
            print sortedArr[j][0]
        
        break
            # put the first tuple in arr
            # calculate 40th percentile. put those objects in output array
            #   + sort by keys (ascending)
            #   + calculate
            #   return
            # repeat


calcInterval()

# calculations for 6-month period
#for h in arrayOfHoods:
#    data = h["data"]
#    for d in range(0, len(data)-6, 6):
#        data1 = data[d]  # start
#        data2 = data[d+6] # end
#        delta_price =  data2[1]-data1[1]
#        print h["neighborhood"],data1[0],data2[0],delta_price
#    break


# calculations for 1 year period
#for h in arrayOfHoods:
#    data = h["data"]
#    for d in range(0, len(data)-12, 12):
#        data1 = data[d]  # start
#        data2 = data[d+12] # end
#        delta_price =  data2[1]-data1[1]
#        print h["neighborhood"],data1[0],data2[0],delta_price
#    break


# calculations for 2 year period
#for h in arrayOfHoods:
#    data = h["data"]
#    for d in range(0, len(data)-24, 24):
#        data1 = data[d]  # start
#        data2 = data[d+24] # end
#        delta_price =  data2[1]-data1[1]
#        print h["neighborhood"],data1[0],data2[0],delta_price
#    break

