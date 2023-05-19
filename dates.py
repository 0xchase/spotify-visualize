import json
from spotipy import *

with open("dates.csv", "w+") as f:
    f.write("")

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
                    id = track["track"]["id"]
                    name = track["track"]["name"]
                    add_date = track["added_at"].split("T")[0]
                    release_date = track["track"]["album"]["release_date"]
                    print("Id: " + id + " | Name: " + name + " | Playlist: " + playlist_name + " | Add Date: " + add_date + " | Release Date: " + release_date)

                    with open("dates.csv", "a") as f:
                        f.write(id + "," + name + "," + playlist_name + "," + add_date + "," + release_date + "\n")
                except:
                    print("Ignoring podcasts")
                    continue