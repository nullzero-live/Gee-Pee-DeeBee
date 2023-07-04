# Initialize Database for PDF files
import pymongo
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import sys
import tqdm
from pymongo import MongoClient

def upload_database(new_documents: list):
  docs_dic = convert_docs_fordb(pdf_list)

  new_documents = new_documents
  # Provide the mongodb atlas url to connect python to mongodb using pymongo
  CONNECTION_STRING = f"mongodb+srv://nullzeroid:ZFAtWRv38lqdPpQF@inventure-acc.ymxpth9.mongodb.net/?retryWrites=true&w=majority"

  # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
  client = MongoClient(CONNECTION_STRING) #CONNECTION_STRING

  # Create the database for our example (we will use the same database throughout the tutorial
  # use a database named "myDatabase"
  db = client.myDatabase
  print(client.list_database_names())

# use a collection named "my_collection"
  my_collection = db.my_collection
  print("collection created")



  ''' Insert sample documents
  documents = [
  {
      "date_uploaded": datetime.now(),
      "pdf_file_name": "Test"
  },
  {
      "date_uploaded": datetime.now(),
      "pdf_file_name": "Test2"
  },
  {
      "date_uploaded": datetime.now(),
      "pdf_file_name": "/content/drive/MyDrive/projects/gradient_annualreports/c30bca43-0a3e-e911-a97c-000d3ad02a61-e72ed04c-ff1a-456d-8786-082e898ce930-Financial Report-1c425ba2-cf9e-ed11-aad1-00224893b065-Gradient_Institute_Ltd_-_General_Purpose_Financial_Statements_2022_(with_auditor_report).pdf"
  },
  {
      "date_uploaded": datetime.now(),
      "pdf_file_name": "test4"
  }

  ]'''


  for docs in new_documents:

    existing_doc = my_collection.find_one({'pdf_file': docs['pdf_file']})

    if existing_doc is None:
      print(docs)
      result = my_collection.insert_one(docs)
      print(f"Document inserted with id {result.inserted_id}")
    else:
        print("Document already exists in the collection. No action performed.")

  client.close()
