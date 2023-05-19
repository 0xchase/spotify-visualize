import plotly.express as px
import pandas as pd

with open("dates.csv", "r") as f:
    lines = f.read().splitlines()

    g = {
        "year": [2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022],
        "count": [0, 0, 0, 0, 0, 0, 0, 0, 0]
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

        if add_date == 2023:
            continue

        index = g["year"].index(add_date)
        g["count"][index] += 1

    def genre_time():
        df = pd.DataFrame(data=g)
        df.sort_values(by=["year"], inplace=True)
        fig = px.line(df, x="year", y="count", line_shape="spline", render_mode="svg", labels={"year": "Year", "count": "Number of songs added", "genre": "Genre"}, width=800, height=500, template="plotly_dark")
        fig.show()

    genre_time()
