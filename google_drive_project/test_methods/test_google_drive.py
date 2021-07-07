#!/usr/bin/python3.8

#############################################################################################################

#Purpose of the script

#############################################################################################################

#1.This script has been designed to write python test scripts for Google Drive
#to copy, create, delete, emptytrash, export, get, list and update.

#############################################################################################################

#Below points has been considered in the script:

#############################################################################################################

#1.Write test scripts for both positive and negative test cases
#2.Use loggers to print all the information on screen while executing and in log files

#############################################################################################################

#Importing the sys module for importing the file that are present in another folder
import sys
sys.path.append('/home/ubuntu01/rishitha_google_drive_project/methods')
import google_drive_methods
#Importing pytest module
import pytest
#Importing logging
import logging
import requests

#############################################################################################################

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()
logger.info('Execution starts Here.')

#############################################################################################################

#Collecting the ids and file names and storing it in a datas
datas = google_drive_methods.listing_files()
print(datas)
print(type(datas))
print(len(datas))

#############################################################################################################

#POSITIVE TEST CASES

#Checking whether id is present in Google Drive or not
def test_list_files_1():
    id = '1HwnNBVKHd0zD0yxzhWeE5H8adwvZkEx2'
    for i in range(len(datas)):
        if id in datas[i][0]:
            assert id in datas[i][0]
    logger.info("Id present in google drive.Positive testcase passed successfully")

#Checking length of the Id 
def test_list_files_2():
    id = '1MTI-r2fwnns3PZixF0_7EuHAgFU--6Bl'
    assert len(id) != 0
    logger.info("Length of id not equal to zero.Positive testcase passed successfully")

#Checking type of the Id
def test_list_files_3():
    id = '1_xPDbBOQ1IlEsxfu1cSH5JyzX3Oo95x1'
    assert not isinstance('id',list)
    logger.info("Type of id is dictionary.Positive testcase passed successfully")

#NEGATIVE TEST CASE

#Checking Negative testcase
def test_list_files_negative():
    id = 'rrrrrrrrrrrrrrr'
    for i in range(len(datas)):
        if id not in datas[i][0]:
            assert id not in datas[i][0]
    logger.info("Id not present in Google Drive. Negative testcase passed successfully.")

#############################################################################################################

#POSITIVE TEST CASES

#Collecting data from Google Drive
get_file_data = google_drive_methods.get_file()
logger.info('Data collected successfully.')

#Checking whether file is present in Google Drive or not
def test_get_file_1():
    assert 'duplicate.docx' in get_file_data['name']
    logger.info('File present in Google Drive. Positive testcase passed successfully.')

#Checking type of the data
def test_get_file_2():
    assert type(get_file_data) is dict
    logger.info("Type of data is dictionary.Positive testcase passed successfully")

#Checking length of the data 
def test_get_file_3():
    assert len(get_file_data) > 0
    logger.info("Length of data not equal to zero.Positive testcase passed successfully")

#NEGATIVE TEST CASES

#Checking Negative testcase
def test_get_file_negative():
    assert 'resume.docx' not in get_file_data['name']
    assert type(get_file_data) is not list
    logger.info("Type of data is not list. Negative testcase passed successfully")

#############################################################################################################

#POSITIVE TEST CASE

#Checking whether particular file is deleting are not
def test_delete_file():
    id = '1KhWne-QzrBngEKsZxEOoR1FU5rmZoA90'
    for i in range(len(datas)):
        if id not in datas[i][0]:
            print(datas)
            assert id not in datas[i][0] 
    logger.info("File is deleted. Positive testcase passed successfully")


#############################################################################################################

#POSITIVE TEST CASES

#Creating the folder in Google Drive
folder_details = google_drive_methods.create_folder()
logger.info("Folder created in Google Drive")

#Checking type of the folder
def test_create_folder_1():
    assert type(folder_details) is dict
    logger.info("Type of folder is dictionary.Positive testcase passed successfully")

#Checking the particular folder is present in datas or not
def test_create_folder_2():
    for i in range(len(datas)):
        if folder_details['id'] in datas[i][0]:
            assert folder_details['id'] in datas[i][0] 
    logger.info("Folder present in datas.Positive testcase passed successfully.")

#Checking name of the folder    
def test_create_folder_3():
    assert folder_details['name'] == 'rishitha'
    logger.info("Folder name matches.Positive testcase passed successfully.")

#NEGATIVE TEST CASES

#Checking Negative testcase
def test_create_folder_negative():
    assert type(folder_details) is not list
    assert folder_details['name'] != 'rishithaaa'
    logger.info("Folder name not matches and type is not list.Negative testcase passed successfully.")
    
#############################################################################################################

#POSITIVE TEST CASES

#Checking whether trash is empty or not
def test_empty_trash():
    empty = ''
    empty_trash = google_drive_methods.empty_trash()
    assert empty_trash == empty
    logger.info("Trash is empty.Positive testcase passed successfully.")

#NEGATIVE TEST CASE

#Checking Negative testcase
def test_empty_trash_negative():
    empty = '        '
    empty_trash = google_drive_methods.empty_trash()
    assert empty_trash != empty
    logger.info("Trash is not empty.Negative testcase passed successfully.")

#############################################################################################################

#POSITIVE TEST CASES

#Checking the length of the ids
def test_generate_ids_1():
    generate_all_ids = google_drive_methods.generate_ids()
    assert len(generate_all_ids) != 0
    logger.info("Length of id is not equal to zero.Positive testcase passed successfully.")

#Checking type of the id
def test_generate_ids_2():
    generate_all_ids = google_drive_methods.generate_ids()
    assert type(generate_all_ids) == dict
    logger.info("Type of the ids are dictionary.Positive testcase passed successfully.")

#NEGATIVE TEST CASES

#Checking Negative testcase
def test_generate_ids_negative():
    generate_all_ids = google_drive_methods.generate_ids()
    assert type(generate_all_ids) != list
    assert len(generate_all_ids) > 0
    logger.info("Type of id is not equal to list and length of id is greater than zero and .Negative testcase passed successfully.")

#############################################################################################################

#POSITIVE TEST CASES

move_data = google_drive_methods.move_file()

#Checking whether file is moved or not
def test_move_file():
    file_id = '1uqE-3hZbRgjxRtLnBmriH8ufxdR1PzRb'
    assert file_id == move_data['id']
    logger.info("Both file_ids are same .Positive testcase passed successfully.")

#Checking whether folder is moved or not
def test_move_file_1():
    folder_id = ['1cZy2PxSiGNpq9NlcU7otJKM67mjBdwqD']
    assert folder_id == move_data['parents']
    logger.info("Both folder_ids are same.Positive testcase passed successfully.")

#NEGATIVE TEST CASES

#Checking Negative testcase
def test_move_file_negative():
    file_id = '1uqE-R1PzRb'
    assert file_id != move_data['id']
    folder_id = ['U7otJKM67mjBdwqD']
    assert folder_id != move_data['parents']
    logger.info("file_id and folder_id are different.Negative testcase passed successfully.")

logger.info("Execution stops Here:")

#############################################################################################################

#POSITIVE TEST CASE

#Checking if a valid status code has being received from the server or not.
def test_status_code():
    response = requests.get('https://drive.google.com/drive/u/1/my-drive')      
    assert response.status_code == 200
    logging.info('Valid Status code')

#NEGATIVE TEST CASE

#Checking if an invalid status code has being received from the server or not.
def test_invalid_status_code():
    response = requests.get('https://drive.google.com/drive/u/1/my-drive')      
    assert response.status_code != 404
    logging.error('Invalid Status code')

#############################################################################################################

#POSITIVE TEST CASE

#Checking if the response time is less than 300 or not.
def test_response_time_less_than_200():
    response = requests.get('https://drive.google.com/drive/u/1/my-drive')
    time = response.elapsed.total_seconds() * 1000
    print(time)
    assert time <= 300

#NEGATIVE TEST CASE

# Checking if the response time is more than 200 or not.
def test_response_time_more_than_200():
    response = requests.get('https://drive.google.com/drive/u/1/my-driv')
    time = response.elapsed.total_seconds() * 1000
    print(time)
    assert time >= 300   

#############################################################################################################

#POSITIVE TEST CASE

#Checking if a valid headers has being received from the server or not.
def test_valid_headers():
    response = requests.get('https://drive.google.com/drive/u/1/my-drive')      
    head = response.headers['Content-Type']
    assert head == 'text/html; charset=UTF-8'
    logging.info('Valid headers has been fetched')

#NEGATIVE TEST CASE
   
#Checking if a valid headers has being received from the server or not.
def test_invalid_headers():
    response = requests.get('https://drive.google.com/drive/u/1/my-driv')      
    head = response.headers['Content-Type']
    assert head != 'text/html; charset=UTF-8'
    logging.error('Invalid Page')

#############################################################################################################
############################### Script Details ##############################################################

# Script name               :       test_google_drive.py
# Script version            :       1.0
# Prepared By               :       Rishitha.Gurramkonda@infinite.com
# Create Date               :       23-JUNE-2021
# Last Modification Date    :       27-JUNE-2021

#############################################################################################################

