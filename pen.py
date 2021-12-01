import plotly.express as px
fig = px.treemap(
    names = ["Total","Pension", "AiB", "Hua", "Equity", "Zero", "ask", "avanza"],
    parents = ["", "Total", "Pension", "Pension", "Total", "Equity", "Equity", "Equity"],
    values = [2230000,	410000,	235000,	175000,	1820000,	1095000,	75000,	650000] 
)
fig.update_traces(root_color="lightgrey")
fig.update_layout(margin = dict(t=50, l=25, r=25, b=25))
fig.show()