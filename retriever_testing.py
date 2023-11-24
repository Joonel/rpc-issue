from dotenv import load_dotenv
import os
import openai
from supabase import create_client
import requests

load_dotenv()

openai_api_key = os.getenv("OPENAI_KEY", "")
supabase_url = os.getenv("SUPABASE_URL", "")
supabase_anon_key = os.getenv("SUPABASE_SERVICE_KEY", "")

supabase_client = create_client(supabase_url, supabase_anon_key)

openai.api_key = openai_api_key


def fetch_documents(input_query):
    # Generate a one-time embedding for the query
    embedding_response = openai.Embedding.create(
        model="text-embedding-ada-002",
        input=input_query,
        encoding_format="float",
    )

    embedding = embedding_response['data'][0]['embedding']

    # this doesn't work:
    #
    documents = supabase_client.rpc(
        'match_documents',
        {
            "match_count": 3,
            "match_threshold": 0.7,
            "query_embedding": embedding,
        })

    # this works:
    #
    # documents = requests.post(supabase_url + "/rest/v1/rpc/match_documents", json={
    #     "match_count": 3,
    #     "match_threshold": 0.7,
    #     "query_embedding": embedding
    # }, headers={
    #     "apikey": supabase_anon_key
    # })
    # documents = documents.json()

    return documents


# Example usage
input_query = "Hello"
documents = fetch_documents(input_query)
print(documents)
