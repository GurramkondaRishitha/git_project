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
BASE_URL = "http://api.weatherapi.com/v1/current.json"
#Providing the city name
AQI = "no"
CITY = "London"
URL = BASE_URL + "?key=" + API_KEY + '&q=' + CITY + "&aqi=" + AQI
#Fetching the data in the form of json
response = requests.get(URL)
response_body = response.json()

#############################################################################################################

#Positive testcase for testing the status code of current api
def test_check_status_current_1():
    assert response.status_code == 200
    logging.info("Status code of current api is 200.Positive testcase passed successfully")

#Negative testcase for testing the status code of current api
def test_check_status_current_1_negative():
    assert response.status_code != 401
    logging.info("Status code of current api is not 401.Negative testcase passed successfully")

#############################################################################################################

#Positive testcase for testing the headers of the current api
def test_current_2():
    assert response.headers["Content-Type"] == "application/json"
    logging.info("Content Type of current api is a json.Positive testcase passed successfully")

#Negative testcase for testing the headers of the current api
def test_current_negative_2():
    assert response.headers["Content-Type"] != "XML"
    logging.info("Content Type of current api is not XML.Negative testcase passed successfully")

#############################################################################################################

#Positive testcase for testing the country name of the current api
def test_current_3():
    assert response_body["location"]["country"] == "United Kingdom"
    logging.info("Country name of current api is United Kingdom.Positive testcase passed successfully")

#Negative testcase for testing the country name of the current api
def test_current_negative_3():
    assert response_body["location"]["country"] != "United State"
    logging.info("Country name of current api is not United State.Negative testcase passed successfully")

#############################################################################################################

#Positive testcase for testing the region of the current api
def test_current_4():
    assert response_body["location"]["region"] == "City of London, Greater London"
    logging.info("Region of current api is City of London, Greater London.Positive testcase passed successfully")

#Negative testcase for testing the region of the current api
def test_current_negative_4():
    assert response_body["location"]["region"] != "Greater London"
    logging.info("Region of current api is not Greater London.Negative testcase passed successfully")

#############################################################################################################

#Positive testcase for testing the length of the response_body of current api
def test_current_5():
    assert len(response_body) != 0
    logging.info("Length of current api is not equal to zero.Positive testcase passed successfully")

#Negative testcase for testing the length of the response_body of current api
def test_current_negative_5():
    assert len(response_body) != 3
    logging.info("Length of current api is not equal to three.Negative testcase passed successfully")

#############################################################################################################

#Positive testcase for testing the type of the location of current api
def test_current_6():
    assert type(response_body['location']) == dict
    logging.info("Type of current api Location is dictt.Positive testcase passed successfully")

#Negative testcase for testing the type of the location of current api
def test_current_negative_6():
    assert type(response_body['location']) != list
    logging.info("Type of current api Location is not list.Negative testcase passed successfully")

#############################################################################################################

#Positive testcase for testing the current present in current api or not
def test_current_7():
    assert "current" in response_body
    logging.info("Current is present in Current Api.Positive testcase passed successfully")

#Negative testcase for testing the current present in current api or not
def test_current_negative_7():
    assert "condition" not in response_body
    logging.info("Condition is not present in Current Api.Negative testcase passed successfully")
    logging.info("#####################################################################################")

#############################################################################################################
############################### Script Details ##############################################################

# Script name               :       test_current.py
# Script version            :       1.0
# Prepared By               :       Rishitha.Gurramkonda@infinite.com
# Create Date               :       22-JULY-2021
# Last Modification Date    :       26-JULY-2021

#############################################################################################################
    