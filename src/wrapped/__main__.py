import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
from utility import get_saved_tracks

def main() -> None:
    load_dotenv()

    scope = "user-library-read"

    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
    tracks = get_saved_tracks(sp)
    print(tracks)



if __name__ == "__main__":
    main()
