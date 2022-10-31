import plotly.graph_objects as go
from plotly.subplots import make_subplots

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


fig = make_subplots(
    cols = 2, rows = 1,
    column_widths = [0.4, 0.4],
    subplot_titles = ('branchvalues: <b>remainder<br />&nbsp;<br />', 'branchvalues: <b>total<br />&nbsp;<br />'),
    specs = [[{'type': 'treemap', 'rowspan': 1}, {'type': 'treemap'}]]
)

fig = go.Figure(go.Treemap(
    labels=labels,
    values=values,
    parents=parents,
    textinfo="label+value+percent parent+percent entry",
    root_color="lightgrey",
    pathbar_textfont_size=15,
    ))


fig.update_layout(
    uniformtext=dict(minsize=10, mode='hide'),
    margin = dict(t=50, l=25, r=25, b=25)
    )

fig.write_image("images/dashboard-2.png")
fig.show()