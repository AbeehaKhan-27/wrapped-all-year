import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import utility

def main() -> None:
    load_dotenv(override=True)
    SPOTIPY_CLIENT_ID = os.getenv('SPOTIPY_CLIENT_ID')
    SPOTIPY_CLIENT_SECRET = os.getenv('SPOTIPY_CLIENT_SECRET')
    SPOTIPY_REDIRECT_URI = os.getenv('SPOTIPY_REDIRECT_URI')
    SCOPE = os.getenv('SCOPE')

    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id = SPOTIPY_CLIENT_ID,
                                                   client_secret = SPOTIPY_CLIENT_SECRET,
                                                   redirect_uri=SPOTIPY_REDIRECT_URI,
                                                   scope=SCOPE))

    playlists = utility.get_user_playlists(sp, "bg7vyk7hmq2vz1hrwcdlhvmbq")
    print(playlists)

    top_tracks_short = sp.current_user_top_tracks(limit=20, offset=0, time_range="short_term")
    print(top_tracks_short)
    track_ids = utility.get_track_ids(top_tracks_short)
    print(track_ids)

    track_id = '4iJyoBOLtHqaGxP12qzhQI'
    print(utility.get_track_features(sp, track_id))


if __name__ == "__main__":
    main()

