# Spotify Playlist Creator

This Python script allows you to create playlists on Spotify based on specific criteria such as artist, genre or mood. It utilizes the Spotify API and the Spotify library to authenticate users, search for tracks and create playlists.

# Features
- Authenticate with Spotify using OAuth2 authentication
- Retrieve user's playlists
- Create playlists based on artist, genre or mood criteria
- Add tracks to newly created playlists

# Getting Started
## Prerequisites
- Python 3 installed on your machine
- A Spotify Developer account with client ID and client secret

## Installation
1. Clone this repository to your local machine
2. Install the required dependencies using pip

## Usage
1. Open the .py file in a text editor
2. Replace 'your_client_id' and 'your_client_secret' with your actual Spotify Client ID and Client Secret obtained from the Spotify Developer Dashboard
3. Run the script
4. Follow the prompts to crete playlists based on your preferred criteria

# Documentation
### 'create_playlist(name, description)'
This function creates a new playlist on the user's Spotify account
- 'name': The name of the playlist
- 'description': The description of the playlist

### 'search_tracks(criteria)'
This function searches for tracks on Spotify based on the given criteria
- 'criteria': The search criteria (e.g. artist, genre)

### 'add_tracks_to_playlist(playlist_id, track_uris)'
This function adds tracks to a specified playlist on Spotify
- 'playlist_id': The ID of the playlist
- 'track_uris': List of URIs of the tracks to be added to the playlist

### 'create_based_on_criteria(criteria, playlist_name, playlist_desc)'
This function creates a new playlist based on the given criteria and adds tracks to it
- 'criteria': The search criteria (e.g. artist, genre)
- 'playlist_name': The name of the playlist to be created
- 'playlist_desc': The description of the playlist

# License
This project is licensed under the MIT License 
