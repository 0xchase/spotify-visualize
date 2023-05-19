import plotly.express as px
import pandas as pd
category = ["North", "North", "North", "North", "North",
           "South", "South", "South", "South", "South",
           "Highlights", "Highlights", "Highlights", "Highlights", "Highlights", "Highlights", "Highlights", "Highlights", "Highlights", "Highlights", "Highlights", "Highlights"
           "Instrumental", "Instrumental", "Instrumental", "Instrumental", "Instrumental", "Instrumental", "Instrumental", "Instrumental", "Instrumental" 
            ]
sectors = ["Tech", "Tech", "Finance", "Finance", "Other",
           "Tech", "Tech", "Finance", "Finance", "Other",
           "Meaningful", "Neo-classical", "Post-rock", "Pop", "Indie", "Ambient", "Chill Electronic", "EDM", "Cinematic", "String Section", "Choir", "Modern Piano"
           "Ambient", "Neo-classical", "Post-rock", "Acoustic", "Bethel", "Downtempo Electronic", "Inspire", "Electro", "Ambient Piano"
           ]
vendors = ["A", "B", "C", "D", None,
           "E", "F", "G", "H", None,
           None, None, None, None, None, None, None, None, None, None, None, None,
           None, None, None, None, None, None, None, None
           ]
sales = [1, 3, 2, 4, 1,
         2, 2, 1, 4, 1,
         5, 5, 4, 4, 4, 3, 2, 2, 3, 4, 4, 4,
         1, 1, 1, 1, 1, 1, 1, 1]

print(len(category), len(sectors), len(vendors), len(sales))
df = pd.DataFrame(
    dict(vendors=vendors, sectors=sectors, category=category, sales=sales)
)
df["Root"] = "Root" # in order to have a single root node
print(df)
fig = px.treemap(df, path=['Root', 'category', 'sectors', 'vendors'], values='sales')
fig.update_traces(root_color="lightgrey")
fig.update_layout(margin = dict(t=50, l=25, r=25, b=25))
fig.show()