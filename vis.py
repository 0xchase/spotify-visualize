import plotly.express as px
import pandas as pd

# Todo:
# - Pie chart of genres
# - Treemap (recursive boxes) of playlists, or genres and artists
# - Correlate popularity and number of songs I have by them

with open("data_cleaned.csv", "r") as f:
    lines = f.read().splitlines()
    m = {
        "uri": [], "name": [], "playlist": [], "artist": [], 
        "album": [], "popularity": [], "energy": [], "loudness": [], 
        "speechiness": [], "acousticness": [], "instrumentalness": [],
        "liveness": [], "valence": [], "tempo": [], "duration": []
    }

    a = {
        "artist": [],
        "average_popularity": [],
        "number_of_songs": [],
    }

    print("Loading data...")
    for line in lines:
        line = line.split(",")

        uri = line[0]
        name = line[1]
        playlist = line[2]
        artist = line[3]
        album = line[4]
        popularity = int(line[5])

        energy = float(line[6])
        loudness = float(line[7])
        speechiness = float(line[8])
        acousticness = float(line[9])
        intrumentalness = float(line[10])
        liveness = float(line[11])
        valence = float(line[12])
        tempo = float(line[13])
        duration = float(line[14])

        m["uri"].append(uri)
        m["name"].append(name)
        m["playlist"].append(playlist)
        m["artist"].append(artist)
        m["album"].append(album)
        m["popularity"].append(popularity)
        m["energy"].append(energy)
        m["loudness"].append(loudness)
        m["speechiness"].append(speechiness)
        m["acousticness"].append(acousticness)
        m["instrumentalness"].append(intrumentalness)
        m["liveness"].append(liveness)
        m["valence"].append(valence)
        m["tempo"].append(tempo)
        m["duration"].append(duration)

        if artist not in a["artist"]:
            a["artist"].append(artist)
            a["average_popularity"].append(popularity)
            a["number_of_songs"].append(1)
        else:
            index = a["artist"].index(artist)
            a["average_popularity"][index] = (a["average_popularity"][index] * len(a["artist"]) + popularity) / (len(a["artist"]) + 1)
            a["number_of_songs"][index] += 1
    

    # Plot speechiness against acousticness and loudness
    # df = pd.DataFrame(data=m)
    # fig = px.scatter(df, x="speechiness", y="acousticness", color="loudness", width=800, height=500)

    def top_artists():
        a_filtered = {
            "artist": [],
            "average_popularity": [],
            "number_of_songs": [],
        }

        exclude = ["Colton Dixon", "Hillsong Young & Free", "", "Elevation Worship", "Planetshakers", "Britt Nicole", "Hillsong Kids Jr.", "Hillsong Worship"]

        for artist in a["artist"]:
            index = a["artist"].index(artist)
            if a["number_of_songs"][index] >= 10:
                if not artist in exclude:
                    a_filtered["artist"].append(artist)
                    a_filtered["average_popularity"].append(a["average_popularity"][index])
                    a_filtered["number_of_songs"].append(a["number_of_songs"][index])

        df = pd.DataFrame(data=a_filtered)
        df.sort_values(by=["number_of_songs"], inplace=True, ascending=True)
        fig = px.bar(df, x="number_of_songs", y="artist", width=800, height=1600, log_x=True)

        fig.show()
    
    top_artists()
