#!/usr/bin/python3.8

#############################################################################################################

#Purpose of the script

#############################################################################################################

#1.This script has been designed to test the weather Api by using Pytest Framework.

#############################################################################################################

#Below points has been considered in the script:

#############################################################################################################

#1.Signup as a new user in Weather app.
#2.Login to that weather app.We get API KEY.
#3.Use this API KEY to check whether API'S are working or not.
#4.Write test scripts for those API'S using Pytest Framework.

#############################################################################################################

#Importing pytest module and requests
import requests
import pytest
#Importing the logger module
import logging

#############################################################################################################

#Creating the logger file 
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()

#############################################################################################################

#By using this we can fetch the data from particular URL
API_KEY = "9a8ff12ce0d445a6aa351041212207"
BASE_URL = "http://api.weatherapi.com/v1/search.json"
#Providing the city name
CITY = "London"
URL = BASE_URL + "?key=" + API_KEY + '&q=' + CITY 
#Fetching the data in the form of json
response = requests.get(URL)
response_body = response.json()

#############################################################################################################

#Positive testcase for testing the status code of search api
def test_check_status_search_1():
    logging.info("Status code of search api is 200.Positive testcase passed successfully")
    assert response.status_code == 200

#Negative testcase for testing the status code of search api
def test_check_status_search_negative_1():
    logging.info("Status code of search api is not 400.Negative testcase passed successfully")
    assert response.status_code != 400
    
#############################################################################################################

#Positive testcase for testing the headers of the search api
def test_search_2():
    assert response.headers["Content-Type"] == "application/json"
    logging.info("Content Type of search api is a json.Positive testcase passed successfully")

#Negative testcase for testing the headers of the search api
def test_search_negative_2():
    assert response.headers["Content-Type"] != "XML"
    logging.info("Content Type of search api is not XML.Negative testcase passed successfully")

#############################################################################################################

#Positive testcase for testing the country name of the search api
def test_search_3():
    assert response_body[0]["country"] == "United Kingdom"
    logging.info("Country of search api is United Kingdom.Positive testcase passed successfully")

#Negative testcase for testing the country name of the search api
def test_search_negative_3():
    assert response_body[0]["country"] != "United States"
    logging.info("Country of search api is not United States.Negative testcase passed successfully")

#############################################################################################################

#Positive testcase for testing the type of the id of the search api
def test_check_search_4():
    assert type(response_body[0]["id"]) == int 
    logging.info("Type of search api id is int.Positive testcase passed successfully")

#Negative testcase for testing the type of the id of the search api
def test_check_search_negative_4():
    assert type(response_body[0]["id"]) != str
    logging.info("Type of search api id is not string.Negative testcase passed successfully")
    logging.info("#####################################################################################")

#############################################################################################################
############################### Script Details ##############################################################

# Script name               :       test_search.py
# Script version            :       1.0
# Prepared By               :       Rishitha.Gurramkonda@infinite.com
# Create Date               :       22-JULY-2021
# Last Modification Date    :       26-JULY-2021

#############################################################################################################
    
