# Using graph_objects
import plotly.graph_objects as go
import pandas as pd

df = pd.read_csv('tsla-copy.csv')

fig = go.Figure([go.Scatter(x=df['tt'], y=df['TSLA.Price'])])

fig.write_image("images/quote-2.png")

#fig.show()