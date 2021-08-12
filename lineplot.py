import pandas as pd
import plotly.express as px


df = pd.read_csv("data2.csv")
print(df)
linegraph = px.line(df, x = 'Year', y = 'Per capital income', color = 'Country')
linegraph.show()