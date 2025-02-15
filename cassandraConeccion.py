from astrapy import DataAPIClient

# Initialize the client
client = DataAPIClient("AstraCS:QqEnBzCZfCueHaUNkwZarwAh:9d651b17a50bc489f50027ee4393c6d11b0ae9193ef2a565d62b3c9e740d2e37")# "token de AStra "
db = client.get_database_by_api_endpoint(
  "https://d1a4c2f5-b290-4298-bb9b-e8b2745a53a8-us-east-2.apps.astra.datastax.com"
)

print(f"Connected to Astra DB: {db.list_collection_names()}")