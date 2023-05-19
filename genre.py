import plotly.express as px
import pandas as pd

# Todo:
# - Pie chart of genres
# - Treemap (recursive boxes) of playlists, or genres and artists
# - Correlate popularity and number of songs I have by them

artists = {}

f = open("genres.csv", "r")
data = f.read().splitlines()
for line in data:
    l = line.split(",.,")
    artist = l[0].split(",")[0]
    genres = l[1].split(",")

    if len(genres) > 0 and genres[0] != "":
        artists[artist] = genres

allowed = ["ccm", "indie", "electronic", "instrumental", "pop", "classical", "rock", "ambient", "r&b", "metal", "chill", "cinematic", "other"]

with open("dates.csv", "r") as f:
    lines = f.read().splitlines()

    g = {
        "genre": [],
        "year": [],
        "count": []
    }

    print("Loading data...")
    for line in lines:
        line = line.split(",")

        if len(line) != 6:
            continue

        id = line[0]
        name = line[1]
        playlist = line[2]
        add_date = int(line[3].split("-")[0])
        release_date = int(line[4].split("-")[0])
        artist = line[5]

        try:
            genres = artists[artist]
        except KeyError:
            continue

        for genre in genres:
            if "indie" in genre:
                genre = "indie"            
            if "cinematic" in genre or "soundtrack" in genre or "score" in genre or "movie" in genre or "epic" in genre:
                genre = "cinematic"
            if "ambient" in genre or "drone" in genre or "modular" in genre or "synth" in genre or "sleep" in genre or "mellow" in genre or "slow" in genre or "chill" in genre or "focus" in genre or "background" in genre or "downtempo" in genre or "minimal" in genre or "room" in genre:
                genre = "ambient"
            if "classical" in genre or "gregorian" in genre or "violin" in genre or "middle" in genre or "choral" in genre:
                genre = "classical"
            if "dance" in genre or "house" in genre or "electro" in genre or "trance" in genre or "edm" in genre or "step" in genre:
                genre = "electronic"
            if "instrumental" in genre or "avant" in genre or "piano" in genre or (("christian" in genre or "worship" in genre or "gospel" in genre or "pastoral" in genre) and add_date >= 2019):
                genre = "instrumental"
            if "rock" in genre or "grunge" in genre:
                genre = "rock"
            if "fingerstyle" in genre or "singer-song" in genre or "country" in genre or "roots" in genre or "acoustic" in genre:
                genre = "indie"
            if "pop" in genre:
                genre = "pop"
            if "christian" in genre or "worship" in genre or "gospel" in genre or "ccm" in genre:
                genre = "ccm"
            if "boy" in genre or "jazz" in genre or "blues" in genre or "metal" in genre or "r&b" in genre or "soul" in genre or "funk" in genre:
                genre = "other"

            if genre in allowed:
                if genre not in g["genre"]:
                    g["genre"].append(genre)
                    g["year"].append(add_date)
                    g["count"].append(0)
                
                found = False
                for i in range(len(g["genre"])):
                    if g["genre"][i] == genre and g["year"][i] == add_date:
                        found = True
                        break
                
                if not found:
                    g["genre"].append(genre)
                    g["year"].append(add_date)
                    g["count"].append(0)
                
                for i in range(len(g["genre"])):
                    if g["genre"][i] == genre and g["year"][i] == add_date:
                        g["count"][i] += 1
            else:
                print("Skipping genre " + genre)

    print(g)
    print("Found " + str(len(g["genre"])) + " genres")

    def genre_time():
        min_year = 3000
        max_year = 0

        for year in g["year"]:
            if year < min_year:
                min_year = year
            if year > max_year:
                max_year = year
        
        for y in range(min_year, max_year + 1):
            total = 0
            for i in range(len(g["genre"])):
                if g["year"][i] == y:
                    total += g["count"][i]
            
            for i in range(len(g["genre"])):
                if g["year"][i] == y:
                    g["count"][i] = g["count"][i] / total * 100

        df = pd.DataFrame(data=g)
        df.sort_values(by=["year"], inplace=True)
        fig = px.line(df, x="year", y="count", line_group="genre", color="genre", line_shape="spline", render_mode="svg", labels={"year": "Year", "count": "Percentage of Songs Added", "genre": "Genre"}, width=800, height=500)
        fig.show()
    
    def genre_pie():
        total = 0
        for i in range(len(g["genre"])):
            total += g["count"][i]
        
        for i in range(len(g["genre"])):
            g["count"][i] = g["count"][i] / total * 100

        df = pd.DataFrame(data=g)
        df.sort_values(by=["count"], inplace=True)
        fig = px.pie(df, values="count", names="genre", title="Genres", labels={"count": "Percentage of Songs Added", "genre": "Genre"}, width=800, height=500, template="plotly_dark")
        fig.show()

    # genre_pie()
    #genre_time()
