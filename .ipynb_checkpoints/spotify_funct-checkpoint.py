# Importing Libraries

import requests
import json 
import base64


# Functions for Creating a Genre and Popularity Column in the DataFrame

client_ID = "002fda1860c7403d8aedd134df4dcc5f"
client_secret = "8b279f8a116142f0a942415f81472fcd"

auth_endpoint = "https://accounts.spotify.com/api/token"
search_API_endpoint = "https://api.spotify.com/v1/search"

def get_access_token():
    message = client_ID + ":" + client_secret
    message_bytes = message.encode("ascii")
    base64_bytes = base64.b64encode(message_bytes)
    encoded_client_details = base64_bytes.decode("ascii")
    
    headers = {"Authorization": "Basic " + encoded_client_details}              
    body = {"grant_type": "client_credentials"}
    response = requests.post(url=auth_endpoint, headers=headers, data=body)
    json_object = json.loads(response.text)
    return json_object["access_token"]
    
def make_request(access_token, full_url):
    headers = {"Accept": "application/json", 
               "Content-Type": "application/json", 
               "Authorization": "Bearer " + access_token}

    response = requests.get(url=full_url, headers=headers)
    json_object = json.loads(response.text)
    return json_object

def search_request(access_token, search_term, search_type):
    search_term = requests.utils.quote(search_term)
    search_type = requests.utils.quote(search_type)
    url = search_API_endpoint + "?q=" + search_term
    url += "&type=" + search_type
    json_obj = make_request(access_token, url)
    return json_obj

def get_popularity(json_obj):
    artists = json_obj["artists"]
    items = artists["items"]
    first_artist_item = items[0] 
    popularity = first_artist_item["popularity"]
    return popularity





    
