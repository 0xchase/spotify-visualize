#!/usr/bin/python3

import json
from spotipy import *

class Features:
    def __init__(self, danceability, energy, loudness, speechiness, acousticness, intrumentalness, liveness, valence, tempo, duration):
        self.danceability = danceability
        self.energy = energy
        self.loudness = loudness
        self.speechiness = speechiness
        self.acousticness = acousticness
        self.intrumentalness = intrumentalness
        self.liveness = liveness
        self.valence = valence
        self.tempo = tempo
        self.duration = duration
    
    def csv(self) -> str:
        return str(self.energy) + "," + str(self.loudness) + "," + str(self.speechiness) + "," + str(self.acousticness) + "," + str(self.intrumentalness) + "," + str(self.liveness) + "," + str(self.valence) + "," + str(self.tempo) + "," + str(self.duration)

class Track:
    def __init__(self, name, playlist, artist, album, popularity, uri, features):
        self.name = name
        self.playlist = playlist
        self.artist = artist
        self.album = album
        self.popularity = popularity
        self.uri = uri
        self.features = features
    
    def __str__(self) -> str:
        return "Uri: " + str(self.uri) + " | Track: " + self.name + " | Playlist: " + self.playlist + " | Artist: " + self.artist + " | Album: " + self.album + " | Popularity: " + str(self.popularity)
    
    def csv(self) -> str:
        return self.uri + "," + self.name + "," + self.playlist + "," + self.artist + "," + self.album + "," + str(self.popularity) + "," + self.features.csv()

class Playlist:
    def __init__(self, name, id, tracks):
        self.name = name
        self.id = id
        self.tracks = tracks

skip = True

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

            if playlist_name == "Pianos":
                skip = False
            
            if playlist_name == "totallytori724 + 1635321":
                continue
            
            if skip:
                continue

            print(str(playlist_name))

            for track in sp.playlist_tracks(id)["items"]:
                #URI
                track_uri = track["track"]["uri"]
                
                #Track name
                track_name = track["track"]["name"]
                
                #Main Artist
                artist_uri = track["track"]["artists"][0]["uri"]
                artist_info = sp.artist(artist_uri)
                
                #Name, popularity, genre
                artist_name = track["track"]["artists"][0]["name"]
                artist_pop = artist_info["popularity"]
                artist_genres = artist_info["genres"]
                
                #Album
                album = track["track"]["album"]["name"]
                
                #Popularity of the track
                track_pop = track["track"]["popularity"]

                # Track features
                f = sp.audio_features(track_uri)[0]
                try:
                    features = Features(f["danceability"], f["energy"], f["loudness"], f["speechiness"], f["acousticness"], f["instrumentalness"], f["liveness"], f["valence"], f["tempo"], f["duration_ms"])
                except:
                    print("Couldn't extract features for song " + track_name + " by " + artist_name)
                    f = open("data.csv", "a")
                    f.write("ERROR for " + track_name + " by " + artist_name + "\n")
                    continue

                track = Track(track_name, playlist_name, artist_name, album, track_pop, track_uri, features)

                print(track)

                f = open("data.csv", "a")
                f.write(track.csv() + "\n")
