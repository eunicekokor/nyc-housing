:house: NYC Housing Data :house:
================================
###### *"tryna track gentrification out here"*

Uses the [Quandl API](https://www.quandl.com/) to get housing data for all of New York City. Creates a Redis store full of NYC Housing Data. Uses a Flask app to creates a RESTful API that can be used to get relevant statistics on dataset and make visualisations.


### Usage

Note: First make sure you have the following Python libraries installed. Run: 
`pip install Quandl requests pandas)`


1. Create file config which holds Quandl API key

	`config.py`
	
2. Put the API key from Quandl into config.py

	`echo apiKey = "YOUR_API_KEY" > config.py`
	
