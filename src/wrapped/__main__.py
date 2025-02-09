import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv
import utility

def main() -> None:
    load_dotenv()

    auth_manager = SpotifyClientCredentials()
    sp = spotipy.Spotify(auth_manager=auth_manager)

    playlists = utility.get_user_playlists(sp, "bg7vyk7hmq2vz1hrwcdlhvmbq")
    print(playlists)


if __name__ == "__main__":
    main()

