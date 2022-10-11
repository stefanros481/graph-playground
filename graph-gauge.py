import plotly.graph_objects as go
import os

if not os.path.exists("images"):
    os.mkdir("images")

fig = go.Figure(
    go.Indicator(
        mode="gauge",
        value=1100230,        
        title={"text": "Savings Progress"},
        domain={"x": [0, 1], "y": [0, 1]},
    )
)

fig.write_image("images/gauge.png")

# fig.show()
