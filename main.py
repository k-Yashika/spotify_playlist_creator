import spotipy
from spotipy.oauth2 import SpotifyOAuth

# setting up the authentication
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id='your_client_id',
                                               client_secret='your_client_secret',
                                               redirect_uri='http://localhost:8888/callback',
                                               scope='user-library-read playlist-modify-public'))

# retrieving user's playlist
playlists = sp.current_user_playlists()
for playlist in playlists['items']:
    print(playlist['name'])

# create playlists based on genre, mood, or artist
def create_playlist(name, description):
    playlist = sp.user_playlist_create(sp.current_user()['id'], name=name, description=description)
    return playlist['id']

def search_tracks(criteria):
    results = sp.search(q=criteria, limit=25)
    tracks = results['tracks']['items']
    return [track['uri'] for track in tracks]

def add_tracks_to_playlist(playlist_id, track_uris):
    sp.playlist_add_items(playlist_id, track_uris)

def create_based_on_criteria(criteria, playlist_name, playlist_desc):
    playlist_id = create_playlist(playlist_name, playlist_desc)
    track_uris = search_tracks(criteria)
    add_tracks_to_playlist(playlist_id, track_uris)
    print(f"Playlist '(playlist_name)' has been created successfully!")

# Example Use: creating a playlist with tracks related to a specific artist
artist_name = 'Ariana Grande'
criteria = f'artist:{artist_name}'
playlist_name = f'{artist_name} Favs'
playlist_desc = f'A playlist with popular songs by {artist_name}'

create_based_on_criteria(criteria, playlist_name, playlist_desc)
