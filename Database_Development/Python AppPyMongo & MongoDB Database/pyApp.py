#!/usr/bin/env python3

#Main App
import pymongo as pm
import datetime

#String parsing from CSV to JSON format
#Converting CSV to JSON format (Prepare JSON)
with open('vocabulary_set.csv', 'r') as input_file:
    wds_list = input_file.readlines()
    #remove the first element of the list
    wds_list.pop(0)
    vocab_list = []
    for ele in wds_list:
        word, definition = ele.split(',',1)
        #remove all characters at the end of the string
        definition = definition.rstrip()
        vocab_list.append({"word":word, "definition":definition})
print (vocab_list)

## Create a MongoDB database
client = pm.MongoClient("mongodb://localhost:27017/")
db = client["vocab"]

#create collection
vocab_col = db["words_list"]

#drop the collection and create a fresh collection
vocab_col.drop()


## Insert documents - there must be documents in the collection for the database to exist
#create JSON entry for collection - Inserting Documents
vb_dict = {'word':'cryptic', 'definition':'secret with hidden meaning'}

#use insert_one() method to insert a single document
res = vocab_col.insert_one(vb_dict)
#obtain id of the document
print ('Inserted_id:',res.inserted_id)

#check for the list of database names
dbs = client.list_database_names()
#Check for the existence of a database
if 'vocab' in dbs:
    print('Database exists')
else:
    print('Database does not exist')

#use insert_many() method to insert multiple documents from the vocab_list above
res = vocab_col.insert_many(vocab_list)

#use inserted_ids mehtod to printed all inserted ids
print (res.inserted_ids)



## Query Collection
#find first document in the collection
first_doc = vocab_col.find_one()
print (first_doc)

#use find() method to find all documents in the collection (exclude id and definition)
for wd_list in vocab_col.find({},{'_id':0, 'definition':0}):
    print (wd_list)

#Query a particular word
wd_bogus = vocab_col.find_one({'word':'bogus'})
print (wd_bogus)


## Update the collection
#update a word's definition
upd = vocab_col.update_one({'word':'bogus'}, {'$set':{'definition':'bogus word'}})
#print modified count
print ("modified count:",upd.modified_count)

#find one document
wd_bogus = vocab_col.find_one({'word':'bogus'})
print (wd_bogus)

#update all documents by setting a last_updated time field using ISO format YYYY-MM-DDTHH:MM:SS.SSSZ
upd_many = vocab_col.update_many({},{"$set": {"last_updated UTC":
datetime.datetime.utcnow().strftime('%Y-%m-%d%H%M%SZ')}})


#print modified count
print ("modified count", upd_many.modified_count)




#Draft code
'''
import pymongo as pm
import datetime

#Converting CSV to JSON format (Prepare JSON)
with open('Vocabulary_set.csv', 'r') as input_file:
    wds_list = input_file.readlines()
    #remove the first element of the list
    wds_list.pop(0)
    vocab_list = []
    for ele in wds_list:
        word, definition = ele.split(',',1)
        #remove all characters at the end of the string
        definition = definition.rstrip()
        vocab_list.append({"word":word, "definition":definition})
##print (vocab_list)


##Create a MongoDB Database
client = pm.MongoClient("mongodb://localhost:27017/")
db = client["vocab"]

#create a collection
vocab_col= db["vocab_list"]
#drop the collection and create a fresh collection
vocab_col.drop()

##Insert Documents
#create JSON entry for collection - Inserting Documents
vb_dict = {'word':'cryptic', 'definition': 'secret with hidden meaning'}

#use insert_one to insert one document
res = vocab_col.insert_one(vb_dict)
#obtain id of the document
print ("Inserted_id:",res.inserted_id)

#check for the list of database names
dbs = client.list_database_names()
#check that th database exist
if 'vocab' in dbs:
    print ("Database exist")
else:
    print ("Database does not exist")

#Insert multiple documents from the vocab_list above
res = vocab_col.insert_many(vocab_list)

#use inserted_ids mehtod to printed all inserted ids
#print(res.inserted_ids)

##Query Collection
#find first document in the collection
data=vocab_col.find_one()
print(data)

#find all the documents in the collection (exclude id and definition)
for wd_data in vocab_col.find({}, {"_id":0, "definition":0}):
    print(wd_data)


#query a particular word
wd_bogus = vocab_col.find_one({'word':'bogus'})
print(wd_bogus)



## Update the Collection
#update a word's definition
upd = vocab_col.update_one({'word':'bogus'},{'$set':{'definition':'factitious; fake; false'}})

#print modified count
print("modified count", upd.modified_count)

#find one document
wd_bogus = vocab_col.find_one({'word':'bogus'})
print(wd_bogus)


#update all documents by setting a last_updated time field
upd_many = vocab_col.update_many({},{"$set": {"last_updated UTC":
datetime.datetime.utcnow().strftime('%Y-%m-%d%H%M%SZ')}})
print ("modified count", upd_many.modified_count)


'''
