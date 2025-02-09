from spotipy import Spotify

def get_saved_tracks(sp: Spotify) -> list[tuple[int, str]]:
    results = sp.current_user_saved_tracks()
    tracks = []
    for idx, item in enumerate(results["items"]):
        track = item["track"]
        tracks.append((idx, track["artists"][0]["name"] + " – " + track["name"]))
    return tracks