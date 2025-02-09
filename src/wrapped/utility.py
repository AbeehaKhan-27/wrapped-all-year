import spotipy

def get_user_playlists(sp, user: str) -> tuple: #TODO Figure out what dtype this is
    playlists = sp.user_playlists('')
    while playlists:
        for i, playlist in enumerate(playlists['items']):
            print("%4d %s %s" % (i + 1 + playlists['offset'], playlist['uri'],  playlist['name']))
        if playlists['next']:
            playlists = sp.next(playlists)
        else:
            playlists = None
    return playlists

