#############################################################################################################
#Purpose of the script
#############################################################################################################
#1.This script has been designed to write python test scripts for google classroom
#to create,list,get,update,patch and delete methods.

#############################################################################################################
#Below points has been considered in the script:
#############################################################################################################
#1.Write test scripts for both positive and negative cases
#2.Use loggers to print all the information on screen while executing and in log files

#############################################################################################################
#importing methods file and logger
import methods
import logging
import exceptions
import pytest
#############################################################################################################

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()
logger.info('Execution starts Here.')

#Listing the ids and storing it into a variable called course_id
course_id = methods.list_courses()
logger.info('collecting the ids and store it into a variable')
print(course_id)

#############################################################################################################
#Testing the create method positively by providing particular id
def test_create():
    res = methods.get_course(course_id[0])
    print(type(res))
    assert str == type(res[0]), 'return type of the function is not dict'
    logger.info('Positive testcase passed successfully in create method')
   
#Testing the create method negatively by providing particular id
def test_create_negative():
    res = methods.get_course(course_id[0])
    print(type(res))
    assert dict != type(res[0]), 'return type of the function is not dict'
    logger.info('Negative test case passed successfully in create method')

#############################################################################################################
#Testing the get method positively by providing particular id
def test_get_positive():
    assert methods.get_course(course_id[0])[0] =='10th Grade Biology',"course not found"
    logger.info('In get method ,positive testcase passed successfully ')

#Testing the get method negatively by providing particular id
def test_get_negative():
    assert methods.get_course(course_id[0])[1] != '10th Grade Biology'
    logger.info('In get method ,negative testcase passed successfully')

#############################################################################################################
#Testing the list method positively ,id is present in course_id or not
def test_list():
    id = '355969960956'
    assert id in course_id 
    exceptions.id_checking(id)
    logger.info('In list method ,positive testcase passed successfully')

#Testing the list method negatively ,id is not present in course_id 
def test_list_negative():
    id = '3559699600000'
    assert id not in course_id
    with pytest.raises(ValueError) as exc_info:
       exceptions.id_checking(id)
    print(str(exc_info.value))
    logger.info('In list method ,negative testcase passed successfully')

#############################################################################################################
#Testing the update method positively, by providing particular id
def test_update():
    update_1 = methods.update_course(course_id[0])
    print(update_1)
    list_roomno = methods.get_course(course_id[0])
    print(list_roomno)
    assert update_1 == list_roomno[2]
    logger.info('In update method ,positive testcase passed successfully')

#Testing the update method negatively, by providing particular id
def test_update_negative():
    update_1 = methods.update_course(course_id[1])
    print(update_1)
    list_roomno = methods.get_course(course_id[1])
    print(list_roomno)
    assert update_1 != list_roomno[2]
    logger.info('In update method ,negative testcase passed successfully')

#############################################################################################################
#Testing the patch method positively, by providing particular id
def test_patch_update():
    update_1 = methods.specific_update_course(course_id[0])
    update_2 = methods.specific_update_course(course_id[1])
    print(update_1)
    print(update_2)
    assert update_1 == update_2
    logger.info('In patch method ,positive testcase passed successfully')

#Testing the patch method negatively, by providing particular id
def test_patch_update_negative():
    update_1 = methods.specific_update_course(course_id[1])
    update_2 = methods.specific_update_course(course_id[2])
    print(update_1)
    print(update_2)
    assert update_1 != update_2
    logger.info('In patch method ,negative testcase passed successfully')

#############################################################################################################

if __name__ == '__main__':
    mylogger.info(' About to start the tests ')
    pytest.main(args=['-s', os.path.abspath(__file__)])
    mylogger.info(' Done executing the tests ')
    
#############################################################################################################
############################### Script Details ##############################################################

# Script name               :       test_googleclassroom.py
# Script version            :       1.0
# Prepared By               :       Rishitha.Gurramkonda@infinite.com
# Create Date               :       09-JUNE-2021
# Last Modification Date    :       14-JUNE-2021

#############################################################################################################