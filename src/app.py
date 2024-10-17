import os
import pandas as pd
from dotenv import load_dotenv

# pip install spotipy

# load the .env file variables
load_dotenv()

from dotenv import load_dotenv
load_dotenv()

import os

client_id = os.environ.get("CLIENT_ID")
client_secret = os.environ.get("CLIENT_SECRET")



import base64
import requests

# Encode the client credentials
client_credentials = f"{client_id}:{client_secret}"
client_credentials_base64 = base64.b64encode(client_credentials.encode())

# Prepare the token request
token_url = "https://accounts.spotify.com/api/token"
headers = {
    "Authorization": f"Basic {client_credentials_base64.decode()}"
}
data = {
    "grant_type": "client_credentials"
}

# Request access token
response = requests.post(token_url, headers=headers, data=data)

# Check if the request was successful
if response.status_code == 200:
    access_token = response.json()['access_token']
    print("Access token obtained!")
else:
    print(f"Failed to obtain access token. Status code: {response.status_code}")
    print(response.text)

    # Set the access token in the headers
headers = {
    "Authorization": f"Bearer {access_token}"
}

# Define the endpoint and parameters
search_url = "https://api.spotify.com/v1/search"
params = {
    "q": "Travis Scott",  # Artist name to search for
    "type": "artist",
    "limit": 1
}

# Make the API request to search for the artist
response = requests.get(search_url, headers=headers, params=params)

# Check if the request was successful
if response.status_code == 200:
    response_data = response.json()
    # print(f"Response Data: {response_data}")
    artist_id = response_data['artists']['items'][0]['id']
    artist_name = response_data['artists']['items'][0]['name']
    print(f"Found artist: {artist_name} (ID: {artist_id})")
else:
    print(f"Failed to search for artist. Status code: {response.status_code}")
    print(response.text)


    # Define the endpoint for the artist's top tracks
top_tracks_url = f"https://api.spotify.com/v1/artists/{artist_id}/top-tracks"
params = {
    "market": "US"  # Specify the market (country)
}

# Make the API request to get top tracks
response = requests.get(top_tracks_url, headers=headers, params=params)

# Check if the request was successful
if response.status_code == 200:
    top_tracks_data = response.json()
    print(f"Top tracks for {artist_name}:")
    for idx, track in enumerate(top_tracks_data['tracks'], start=1):
        # print(f"Track data: {track}")
        track_name = track['name']
        album_name = track['album']['name']
        print(f"{idx}. {track_name} - Album: {album_name}")
else:
    print(f"Failed to get top tracks. Status code: {response.status_code}")
    print(response.text)


    def get_access_token(client_id, client_secret):
    try:
        # Encoding and token request as before
        client_credentials = f"{client_id}:{client_secret}"
        client_credentials_base64 = base64.b64encode(client_credentials.encode())
        token_url = "https://accounts.spotify.com/api/token"
        headers = {
            "Authorization": f"Basic {client_credentials_base64.decode()}"
        }
        data = {
            "grant_type": "client_credentials"
        }
        response = requests.post(token_url, headers=headers, data=data)
        response.raise_for_status()  # Raises an HTTPError for bad status codes
        access_token = response.json()['access_token']
        return access_token
    except requests.exceptions.HTTPError as err:
        print(f"HTTP error occurred: {err}")
    except Exception as err:
        print(f"An error occurred: {err}")
    return None

# Use the function to get the access token
access_token = get_access_token(client_id, client_secret)
if access_token:
    print("Access token obtained successfully.")
else:
    print("Failed to obtain access token.")
