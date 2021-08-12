import pandas as pd
import plotly.express as px


df = pd.read_csv("data.csv")
print(df)
scattergraph = px.scatter(df, x = 'Population', y = 'Per capital', color = 'Country', size = 'Percentage', size_max = 60)
scattergraph.show()