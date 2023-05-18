#!/usr/bin/python3

import json

with open("data.json") as f:
    data = json.loads(f.read())
    playlists = data["playlists"]

    for key in playlists:
        item = playlists[key]

        name = item["name"]
        id = item["id"]
        tracks = item["tracks"]

        print(str(name))

        for track in tracks:
            id = track["id"]
            print("\t" + str(track))
