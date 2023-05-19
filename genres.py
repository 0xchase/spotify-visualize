import json
from spotipy import *

artists = []

with open("creds.txt", "r") as f:
    values = f.read().splitlines()
    cid = values[0]
    secret = values[1]

    client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
    sp = Spotify(client_credentials_manager = client_credentials_manager)

    with open("data.json") as f:
        data = json.loads(f.read())
        playlists = data["playlists"]

        for key in playlists:
            item = playlists[key]

            playlist_name = item["name"]
            id = item["id"]
            tracks = item["tracks"]

            if playlist_name == "totallytori724 + 1635321" or playlist_name == "Philosophy":
                continue

            print(playlist_name)
            tracks = sp.playlist_tracks(id)["items"]
            for track in tracks:
                try:
                    artist_name = track["track"]["artists"][0]["name"]
                    artist_id = track["track"]["artists"][0]["id"]

                    if not artist_name in artists:
                        artists.append(artist_name)
                        artist = sp.artist(track["track"]["artists"][0]["external_urls"]["spotify"])
                        genres = artist["genres"]
                        print(genres)
                    
                        with open("genres.csv", "a") as f:
                            f.write(artist_name + "," + artist_id + ",.," + ",".join(genres) + "\n")
                except:
                    print("Skipping podcasts")