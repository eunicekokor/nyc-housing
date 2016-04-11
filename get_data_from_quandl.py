# 'get_data_from_quandl.py'
#
#   + parses csv of Zillow Neighborhoods
#   + fetches Zillow stats using Quandl API
#   + creates Flask app, and a REST API to poll

# libraries and tings
import config
import requests
import json
import csv
import Quandl

# some simple setup
apiKey = config.apiKey  # get the api key from config
