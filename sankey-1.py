import plotly.graph_objects as go
"""
labels  = [
    "Gjensidige",
    "NordnetPension",
    "Zero",
    "ASK",
    "Avanza",
    "DeGiro",
    "Pension",
    "Equity",
    "Total",
    ]
parents =[
    "Pension",
    "Pension",
    "Equity",
    "Equity",
    "Equity",
    "Equity",
    "Total",
    "Total",
    "",
    ]

values = [
    332812,
    223045,
    868078,
    12283,
    439225,
    14257,
    555857,
    1333843,
    1889700,
]
"""

label = [
    "0Avanza",
    "1Zero",
    "2Gjen",
    "3equity",
    "4Pension accnt",
    "5Total"
]

source = [0, 1, 2, 3, 4]
target = [3, 3, 4, 5, 5]
values = [1, 2, 3, 4, 5]

fig = go.Figure(data=[go.Sankey(
    node = dict(
      pad = 15,
      thickness = 20,
      line = dict(color = "black", width = 0.5),
      label = label,
      color = "blue"
    ),
    link = dict(
      source = source, # indices correspond to labels, eg A1, A2, A1, B1, ...
      target = target,
      value = values
  ))])

fig.update_layout(title_text="Basic Sankey Diagram", font_size=10)

fig.write_image("images/sankey-1.png")
#fig.show()