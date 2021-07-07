#!/usr/bin/python3.8

#############################################################################################################

#Purpose of the script

#############################################################################################################

#1.This script has been designed to write python test scripts for Google Drive
#to copy, create, delete, emptytrash, export, get, list and update.

#############################################################################################################

#Below points has been considered in the script:

#############################################################################################################

#1.Writing the methods for copy, create, delete, emptytrash, export, get, list and update.
#2.Use loggers to print all the information on screen while executing and in log files

#############################################################################################################

#Importing the sys module for importing the file that are present in another folder
import sys
sys.path.append('/home/ubuntu01/rishitha_google_drive_project/quickstart_method')
from quickstart import main
#This module is used to Uploading the files
from apiclient.http import MediaFileUpload, MediaIoBaseDownload
#Importing loggers 
import logging
#############################################################################################################

#Creating the logger file with date and time format
logging.basicConfig(filename="methods.log",filemode = 'w', level=logging.INFO, format='%(asctime)s %(message)s', datefmt='%d/%m/%Y %H:%M:%S')
logging.info('Execution starts Here.')

#############################################################################################################

#Calling the main function and store that in a variable calles services
service = main()
logging.info("Calling the main methods from quickstart.py")

#############################################################################################################

#Creating folder in Google Drive
def create_folder():
    #Giving the folder name and type of the folder
    file_metadata = {
        'name': 'rishitha',
        'mimeType': 'application/vnd.google-apps.folder'
    }
    logging.info("Giving the folder name and type of the folder")
    #Creating the folder by using files.create method
    file = service.files().create(body=file_metadata).execute()
    print(file)
    print('Folder ID: ', file.get('id'))
    logging.info("Folder created successfully in Google Drive.")
    return file

#############################################################################################################

#Uploading the file in a folder in Google Drive
def upload_folder_file():

    #Giving the particular Folder Id along with giving the file name
    folder_id = '1cZy2PxSiGNpq9NlcU7otJKM67mjBdwqD'
    file_metadata = {
        'name': 'photo.jpg',
        'parents': [folder_id]
    }
    logging.info("Giving the particular Folder Id along with file name.")

    #Uploading the existing image/jpeg 
    media = MediaFileUpload('/home/ubuntu01/Downloads/rishitha_photo.jpg',
                            mimetype='image/jpeg',    
                            resumable=True)
    logging.info("Uploading the existing image/jpeg and storing it a variable")

    #Creating the uploaded file in Google Drive
    file = service.files().create(body=file_metadata,
                                        media_body=media,
                                        fields='id').execute()
    print ('File ID: ' ,file.get('id'))
    logging.info("Successfully uploaded the file in a folder.")

#############################################################################################################

#Uploading the file in a Google Drive
def upload_file():
    #Uploading existing file in a Google Drive
    file_metadata = {'name': 'google_drive_quickstart.py'}
    media = MediaFileUpload('/home/ubuntu01/rishitha_google_drive_project/quickstart_method/quickstart.py', mimetype='text/python')
    file = service.files().create(body=file_metadata,
                                        media_body=media,
                                        fields='id').execute()
    print('File ID: ', file.get('id'))
    logging.info("Successfully uploaded the file in Google Drive")

#############################################################################################################

#Listing all the files along with ids
def listing_files():
    #Creating the empty list to store the ids and file names
    lst = []
    # Call the Drive v3 API
    results = service.files().list(
        pageSize=60, fields="nextPageToken, files(id, name)").execute()
    items = results.get('files', [])

    #If files are not there in Drive it will print no files found else it list out all the files.
    if not items:
        print('No files found.')
        logging.info('Files are not present')
    else:
        print('Files:')
        for item in items:
            lst.append([item['id'],item['name']])
        print(lst)
        logging.info("Successfully listing all the files that are present in Google Drive.")
        return lst
           # print(u'{0} ({1})'.format(item['name'], item['id']))
            
#############################################################################################################

#Fetching the specific data by providing specific id
def get_file():
    results = service.files().get(fileId = '19UfJyNCbfz3GGXwgKY8QuOjapkaV1hqVUMtUTKcYhx8').execute()
    print(results)
    logging.info("Successfully returning the data that are present in particulat id.")
    return results

#############################################################################################################

#Deleting the specific file from Google Drive
def delete_file():
    results = service.files().delete(fileId = '1qdCQ_d5Rlh10tE69wE41jvW1q0kNxzEz').execute()
    print(results)
    logging.info("Successfully deleting the file in Google Drive.")
    return results

#############################################################################################################

#Deleting all the files/folders in Trash from Google Drive
def empty_trash():
    results = service.files().emptyTrash().execute()
    print(results)
    logging.info("Successfully empty the trash.")
    return results

#############################################################################################################

#Copied particular file in Google Drive
def copy_file():
    results = service.files().copy(fileId = '0B75N3OTbg-9ySXZydGxJUVYxM1lHNHJxeThqRU9taHBXd2dR').execute()
    print(results)
    logging.info("Successfully copying the file.")

#############################################################################################################

#Generating all the file ids
def generate_ids():
    results = service.files().generateIds().execute()
    print(results)
    logging.info("Successfully generating all the file ids.")
    return results

#############################################################################################################

#Converting document file to pdf/text file
def export_file():
    #Providing the specific fileid
    fileid = '19UfJyNCbfz3GGXwgKY8QuOjapkaV1hqVUMtUTKcYhx8'
    logging.info("Providing the specific fileid.")

    #Exporting that document file to pdf format
    results = service.files().export(fileId = fileid,mimeType='application/pdf'
                                    ).execute()
    logging.info("Exporting that document file to pdf format")

    #Opening and creating the file with pdf format and storing the results
    with open("/home/ubuntu01/rishi_duplicate.pdf", "wb") as fw:
        fw.write(results)
        print("doc exported successfully")
    logging.info("Successfully exporting the file from decument to pdf format.")

#############################################################################################################

#Moving and Upating the specific file
def move_file():
    #Providing the specific fileid and folder id
    fileid = '1uqE-3hZbRgjxRtLnBmriH8ufxdR1PzRb'
    folder_id = '1cZy2PxSiGNpq9NlcU7otJKM67mjBdwqD'
    logging.info("#Providing the specific fileid and folder id")

    #Getting all the parent files
    results = service.files().get(fileId=fileid,fields='parents').execute()
    print(results)
    previous_parents = ",".join(results.get('parents'))
    print(previous_parents)
    #Updating the file to a specific folder
    file = service.files().update(fileId=fileid,
                                    addParents=folder_id,
                                    removeParents=previous_parents,
                                    fields='id, parents').execute()
    print('moved')
    logging.info("Updating the file successfully.")
    print(file)
    return file


#############################################################################################################

if __name__ == '__main__':
    #create_folder()
    #upload_folder_file()
    #upload_file()
    listing_files()
    #get_file()
    #delete_file()
    #empty_trash()
    #copy_file()
    #generate_ids()
    #export_file()
    move_file()

logging.info("Execution stops Here:")

#############################################################################################################
############################### Script Details ##############################################################

# Script name               :       google_drive_methods.py
# Script version            :       1.0
# Prepared By               :       Rishitha.Gurramkonda@infinite.com
# Create Date               :       23-JUNE-2021
# Last Modification Date    :       27-JUNE-2021

#############################################################################################################


