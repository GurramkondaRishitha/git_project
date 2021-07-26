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

#By using this we can fetch the data from particular URL
API_KEY = "9a8ff12ce0d445a6aa351041212207"
BASE_URL = "http://api.weatherapi.com/v1/astronomy.json"
#Providing the city name and date
DATE ='2021-07-23'
CITY = "London"
URL = BASE_URL + "?key=" + API_KEY + '&q=' + CITY + "&dt=" + DATE
#Fetching the data in the form of json
response = requests.get(URL)
response_body = response.json()

#############################################################################################################

#Creating the logger file 
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()

#############################################################################################################

#Positive testcase for testing the status code of the astronomy api
def test_check_status_astronomy_1():
    assert response.status_code == 200
    logging.info("Status code of astronomy api is 200.Positive testcase passed successfully")

#Negative testcase for testing the status code of the astronomy api
def test_check_status_astronomy_negative_1():
    assert response.status_code != 404
    logging.info("Status code of astronomy api is not 404.Negative testcase passed successfully")

#############################################################################################################

#Positive testcase for testing the headers of the astronomy api
def test_astronomy_2():
    assert response.headers["Content-Type"] == "application/json"
    logging.info("Content type of astronomy api is json.Positive testcase passed successfully")

#Negative testcase for testing the headers of the astronomy api
def test_astronomy_negative_2():
    assert response.headers["Content-Type"] != "XML"
    logging.info("Content type of astronomy api is not XML.Negative testcase passed successfully")

#############################################################################################################

#Positive testcase for testing the country name of the astronomy api
def test_astronomy_3():
    assert response_body["location"]["country"] == "United Kingdom"
    logging.info("Country of astronomy api is United Kingdom.Positive testcase passed successfully")

#Negative testcase for testing the country name of the astronomy api
def test_astronomy_negative_3():
    assert response_body["location"]["country"] != "Belgium"
    logging.info("Country of astronomy api is not a Belgium.Negative testcase passed successfully")

#############################################################################################################

#Positive testcase for testing the moon_phase of the astronomy api
def test_astronomy_4():
    assert response_body["astronomy"]["astro"]["moon_phase"] == "Waxing Gibbous"
    logging.info("Moon phase of astronomy api is Waxing Gibbous.Positive testcase passed successfully")

#Negative testcase for testing the moon_phase of the astronomy api
def test_astronomy_negative_4():
    assert response_body["astronomy"]["astro"]["moon_phase"] != "Gibbous"
    logging.info("Moon phase of astronomy api is not a Gibbous.Negative testcase passed successfully")

#############################################################################################################

#Positive testcase for testing the length of the response_body of astronomy api
def test_astronomy_5():
    assert len(response_body) != 0
    logging.info("Length of astronomy api is not equal to zero.Positive testcase passed successfully")

#Negative testcase for testing the length of the response_body of astronomy api
def test_astronomy_negative_5():
    assert len(response_body) != 3
    logging.info("Length of astronomy api is not equal to three.Negative testcase passed successfully")

#############################################################################################################

#Positive testcase for testing the type of the astronomy of the astronomy api
def test_astronomy_6():
    assert type(response_body['astronomy']) == dict
    logging.info("Type of astronomy is dict.Positive testcase passed successfully")

#Negative testcase for testing the type of the astronomy of the astronomy api
def test_astronomy_negative_6():
    assert type(response_body['astronomy']) != list
    logging.info("Type of astronomy is not a list.Negative testcase passed successfully")

#############################################################################################################

#Positive testcase for testing the astronomy is present in the astronomy api or not
def test_astronomy_7():
    assert "astronomy" in response_body
    logging.info("Astronomy is present in Astronomy api.Positive testcase passed successfully")

#Negative testcase for testing the astronomy is present in the astronomy api or not
def test_astronomy_negative_7():
    assert "condition" not in response_body
    logging.info("Condition is not present in Astronomy api.Negative testcase passed successfully")

    logging.info("#####################################################################################")

#############################################################################################################
############################### Script Details ##############################################################

# Script name               :       test_astronomy.py
# Script version            :       1.0
# Prepared By               :       Rishitha.Gurramkonda@infinite.com
# Create Date               :       22-JULY-2021
# Last Modification Date    :       26-JULY-2021

#############################################################################################################
    