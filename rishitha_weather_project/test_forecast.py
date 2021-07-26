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
BASE_URL = "http://api.weatherapi.com/v1/forecast.json"
#Providing the city name and number of days
DAYS = '1'
AQI = "yes"
ALERTS = "yes"
CITY = "London"
URL = BASE_URL + "?key=" + API_KEY + '&q=' + CITY + '&days' + DAYS + "&aqi=" + AQI + '&alerts' + ALERTS
#Fetching the data in the form of json
response = requests.get(URL)
response_body = response.json()

#############################################################################################################

#Positive testcase for testing the status code of forecast api
def test_check_status_forecast_1():
    assert response.status_code == 200
    logging.info("Status code of forecast api is 200.Positive testcase passed successfully")
    
#Negative testcase for testing the status code of forecast api
def test_check_status_forecast_negative_1():
    assert response.status_code != 400
    logging.info("Status code of forecast api is not 400.Negative testcase passed successfully")

#############################################################################################################

#Positive testcase for testing the headers of the forecast api
def test_forecast_2():
    assert response.headers["Content-Type"] == "application/json"
    logging.info("Content Type of forecast api is a json.Positive testcase passed successfully")

#Negative testcase for testing the headers of the forecast api
def test_forecast_negative_2():
    assert response.headers["Content-Type"] != "XML"
    logging.info("Content Type of forecast api is not XML.Negative testcase passed successfully")

#############################################################################################################

#Positive testcase for testing the country name of the forecast api
def test_forecast_3():
    assert response_body["location"]["country"] == "United Kingdom"
    logging.info("Country of forecast api is United Kingdom.Positive testcase passed successfully")

#Negative testcase for testing the country name of the forecast api
def test_forecast_negative_3():
    assert response_body["location"]["country"] != "England"
    logging.info("Country of forecast api is not England.Negative testcase passed successfully")

#############################################################################################################

#Positive testcase for testing the region of the forecast api
def test_forecast_4():
    assert response_body["location"]["region"] == "City of London, Greater London"
    logging.info("Region of forecast api is City of London, Greater London.Positive testcase passed successfully")

#Negative testcase for testing the region of the forecast api
def test_forecast_negative_4():
    assert response_body["location"]["region"] != "City of London"
    logging.info("Region of forecast api is not City of London.Negative testcase passed successfully")

#############################################################################################################

#Positive testcase for testing the length of the response_body of the forecast api
def test_forecast_5():
    assert len(response_body) != 0
    logging.info("Length of forecast api is not equal to zero.Positive testcase passed successfully")

#Negative testcase for testing the length of the response_body of the forecast api
def test_forecast_negative_5():
    assert len(response_body) != 4
    logging.info("Length of forecast api is not equal to four.Negative testcase passed successfully")

#############################################################################################################

#Positive testcase for testing the type of forecast in the forecast api
def test_forecast_6():
    assert type(response_body['forecast']) == dict
    logging.info("Type of the forecast is dictt.Positive testcase passed successfully")

#Negative testcase for testing the type of forecast in the forecast api
def test_forecast_negative_6():
    assert type(response_body['forecast']) != list
    logging.info("Type of the forecast is not list.Negative testcase passed successfully")

#############################################################################################################

#Positive testcase for testing the forecast is present in forecast api or not
def test_forecast_7():
    assert "forecast" in response_body
    logging.info("Forecast is present in forecast Api.Positive testcase passed successfully")

#Negative testcase for testing the forecast is present in forecast api or not
def test_forecast_negative_7():
    assert "condition" not in response_body
    logging.info("Condition is not present in forecast Api.Negative testcase passed successfully")
    logging.info("#####################################################################################")

#############################################################################################################
############################### Script Details ##############################################################

# Script name               :       test_forecast.py
# Script version            :       1.0
# Prepared By               :       Rishitha.Gurramkonda@infinite.com
# Create Date               :       22-JULY-2021
# Last Modification Date    :       26-JULY-2021

#############################################################################################################
    