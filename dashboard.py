import plotly.express as px


names  = [
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


fig = px.treemap(
    names=names,
    parents=parents,
    values=values,
)

fig.update_traces(
    root_color="lightgrey",
    )

fig.update_layout(margin=dict(t=50, l=25, r=25, b=25))
fig.write_image("images/dashboard.png")
fig.show()