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
BASE_URL = "http://api.weatherapi.com/v1/sports.json"
#Providing the city name
CITY = "London"
URL = BASE_URL + "?key=" + API_KEY + '&q=' + CITY
#Fetching the data in the form of json
response = requests.get(URL)
response_body = response.json()

#############################################################################################################

#Positive testcase for testing the status code of sports api
def test_check_status_sports_1():
    assert response.status_code == 200
    logging.info("Status code of sports api is 200.Positive testcase passed successfully")

#Negative testcase for testing the status code of sports api
def test_check_status_sports_negative_1():
    assert response.status_code != 401
    logging.info("Status code of sports api is not 401.Negative testcase passed successfully")
    
#############################################################################################################

#Positive testcase for testing the headers of the sports api
def test_sports_2():
    assert response.headers["Content-Type"] == "application/json"
    logging.info("Content Type of sports api is a json.Positive testcase passed successfully")
    
#Negative testcase for testing the headers of the sports api
def test_sports_negative_2():
    assert response.headers["Content-Type"] != "XML"
    logging.info("Content Type of sports api is not a XML.Negative testcase passed successfully")
    
#############################################################################################################

#Positive testcase for testing the football region of the sports api
def test_sports_3():
    assert response_body["football"][0]["region"] == ""
    logging.info("Region of sports api is nothing.Positive testcase passed successfully")
    
#Negative testcase for testing the football region of the sports api   
def test_sports_negative_3():
    assert response_body["football"][1]["region"] != "london"
    logging.info("Region of sports api is not london.Negative testcase passed successfully")
    
#############################################################################################################

#Positive testcase for testing the type of the football of the sports api
def test_sports_4():
    assert type(response_body['football']) == list
    logging.info("Type of sports api football is list.Positive testcase passed successfully")
    
#Negative testcase for testing the type of the football of the sports api
def test_sports_negative_4():
    assert type(response_body['football']) != dict
    logging.info("Type of sports api football is not dictt.Negative testcase passed successfully")
    
#############################################################################################################

#Positive testcase for testing football is present in sports api or not
def test_sports_5():
    assert "football" in response_body
    logging.info("Football is present in sports Api.Positive testcase passed successfully")
    
#Negative testcase for testing football is present in sports api or not
def test_sports_negative_5():
    assert "running" not in response_body
    logging.info("Running is not present in sports Api.Negative testcase passed successfully")
    logging.info("#####################################################################################")
      
#############################################################################################################
############################### Script Details ##############################################################

# Script name               :       test_sports.py
# Script version            :       1.0
# Prepared By               :       Rishitha.Gurramkonda@infinite.com
# Create Date               :       22-JULY-2021
# Last Modification Date    :       26-JULY-2021

#############################################################################################################
        


