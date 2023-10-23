import os
import pprint

from dotenv import load_dotenv
from pymongo import MongoClient

# load config from .env file
load_dotenv()
MONGODB_URI = os.getenv("MONGODB_URI")

# Connect to MongoDB cluster with MongoClient
client = MongoClient(MONGODB_URI)

# get reference to the 'bank' database
db = client.bank

# get reference to the 'accounts' collection
accounts_collection = db.accounts

# calculate teh average balance of checking and savings accounts with balance for each account type.

# select account with balances of less than $1000
select_by_balance = {"$match": {"balance": {"$lt": 1000}}}

# separate document by account type and calculate the average balance for each acount type
separate_by_account_calculate_avg_balance = {
    "$group": {"_id": "$account_type", "avg_balance": {"$avg": "$balance"}}
}

# create an aggregation pipeline using 'stage_match_balance' and 'stage_group_account_type'
pipeline = [
    select_by_balance,
    separate_by_account_calculate_avg_balance,
]

# perform the aggregation
result = accounts_collection.aggregate(pipeline)

print()
print(
    "Average balance of checking and savings accounts with balances of less than $1000:", "\n"
)

for item in result:
    pprint.pprint(item)
    
# close connection
client.close()