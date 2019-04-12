import predictionio
import pandas as pd
engine_client = predictionio.EngineClient(url="http://localhost:8000")

def getAllItems(df):
    return set(df[0])

def getAllUsers(df):
    return set(df[0])

df = pd.read_csv("./other-engines/customize/ur/data/nlt-data.txt", sep=",", header=None)

user_df = df[0:650]
item_df = df[650:]
users = getAllUsers(user_df)
items = getAllItems(item_df)

print("---------------------------")
print("|    Querying   Users     |")
print("---------------------------")
for user in users:
    print("User: " + user + " | ", engine_client.send_query({"user": user}))

print("---------------------------")
print("|    Querying   Items     |")
print("---------------------------")
for item in items:
    print("Item: " + item + " | ", engine_client.send_query({"item": item}))

"""
Commands:

curl -H "Content-Type: application/json" -d '
{
    "item": "4",
    "fields": [{
        "name": "categories",
        "values": ["ca1", "ca2"],
        "bias": 20
    }]
}' http://localhost:8000/queries.json

curl -H "Content-Type: application/json" -d '
{
    "user": "u1",
    "fields": [{
        "name": "categories",
        "values": ["ca1", "ca2"],
        "bias": 20
    }]
}' http://localhost:8000/queries.json
"""