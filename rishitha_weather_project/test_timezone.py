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
BASE_URL = "http://api.weatherapi.com/v1/timezone.json"
#Providing the city name
CITY = "London"
URL = BASE_URL + "?key=" + API_KEY + '&q=' + CITY
#Fetching the data in the form of json
response = requests.get(URL)
response_body = response.json()

#############################################################################################################

#Positive testcase for testing the status code of timezone api
def test_check_status_timezone_1():
    assert response.status_code == 200
    logging.info("Status code of timezone api is 200.Positive testcase passed successfully")

#Negative testcase for testing the status code of timezone api
def test_check_status_timezone_negative_1():
    assert response.status_code != 400
    logging.info("Status code of timezone api is not 400.Negative testcase passed successfully")
    
#############################################################################################################

#Positive testcase for testing the headers of the timezone api
def test_timezone_2():
    assert response.headers["Content-Type"] == "application/json"
    logging.info("Content Type of timezone api is a json.Positive testcase passed successfully")

#Negative testcase for testing the headers of the timezone api
def test_timezone_negative_2():
    assert response.headers["Content-Type"] != "XML"
    logging.info("Content Type of timezone api is not a XML.Negative testcase passed successfully")

#############################################################################################################

#Positive testcase for testing the country name of the timezone api
def test_timezone_3():
    assert response_body["location"]["country"] == "United Kingdom"
    logging.info("Country of timezone api is United Kingdom.Positive testcase passed successfully")
    
#Negative testcase for testing the country name of the timezone api
def test_timezone_negative_3():
    assert response_body["location"]["country"] != "England"
    logging.info("Country of timezone api is not England.Negative testcase passed successfully")
    
#############################################################################################################

#Positive testcase for testing the type of the location of the timezone api
def test_timezone_4():
    assert type(response_body['location']) == dict
    logging.info("Type of timezone api Location is dictt.Positive testcase passed successfully")
    
#Negative testcase for testing the type of the location of the timezone api
def test_timezone_negative_4():
    assert type(response_body['location']) != list
    logging.info("Type of timezone api Location is not list.Negative testcase passed successfully")
    
#############################################################################################################

#Positive testcase for testing the location is present in timezone api or not
def test_timezone_5():
    assert "location" in response_body
    logging.info("Location is present in Timezone Api.Positive testcase passed successfully")
    
#Negative testcase for testing the location is present in timezone api or not
def test_timezone_negative_5():
    assert "timezone" not in response_body
    logging.info("Timezone is not present in Timezone Api.Negative testcase passed successfully")
    
#############################################################################################################

#Positive testcase for testing the length of the response_body of the timezone api
def test_timezone_6():
    assert len(response_body) != 0
    logging.info("Length of timezone api is not equal to zero.Positive testcase passed successfully")
    
#Negative testcase for testing the length of the response_body of the timezone api
def test_timezone_negative_6():
    assert len(response_body) != 2
    logging.info("Length of timezone api is not equal to two.Negative testcase passed successfully")
    logging.info("#####################################################################################")

#############################################################################################################
############################### Script Details ##############################################################

# Script name               :       test_timezone.py
# Script version            :       1.0
# Prepared By               :       Rishitha.Gurramkonda@infinite.com
# Create Date               :       22-JULY-2021
# Last Modification Date    :       26-JULY-2021

#############################################################################################################
    
