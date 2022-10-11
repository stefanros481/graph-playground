import plotly.graph_objects as go
import os

if not os.path.exists("images"):
    os.mkdir("images")

fig = go.Figure(go.Indicator(
    domain = {'x': [0, 1], 'y': [0, 1]},
    value = 1300000,
    mode = "gauge+number+delta",
    title = {'text': "Savings Progress"},
    delta = {'reference': 10000000},
    gauge = {'axis': {'range': [None, 12000000]},
             'steps' : [
                 {'range': [0, 5000000], 'color': "lightgray"},
                 {'range': [5000000, 10000000], 'color': "gray"}],
             }))

fig.write_image("images/gauge-2.png")

# fig.show()
