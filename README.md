:house: NYC Housing Data :house:
================================
###### *"tryna track gentrification out here"*

Uses the [Quandl API](https://www.quandl.com/) to get housing data for all of New York City. Creates a Redis store full of NYC Housing Data. Uses a Flask app to creates a RESTful API that can be used to get relevant statistics on dataset and make visualisations.


### Usage

Note: First make sure you have the following Python libraries installed. 

Run: 
`pip install Quandl requests pandas pymongo`


1. Create file config which holds Quandl API key

	`config.py`
	
2. Put the API key from Quandl into config.py

	`echo apiKey = "YOUR_API_KEY" > config.py`

3. Populate a local Mongo store
	
	`python get_data_from_quandl.py` 
	
4. Query the store, to get gentrification data for a particular interval: `(3,6,12,24)`

	`python query_mongo.py <interval>`


### TODO

+ Use a visualization lib [vega, Seaborn, folium]
+ Write query python scripts and tie together w/ a shell script.
