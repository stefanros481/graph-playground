import plotly.express as px
import pandas as pd

""" fig = px.treemap(
    names = ["Total", "Pen", "AiB", "Hua", "Equity", "Zero", "ask", "avanza"],
    parents = ["", "Total", "Pension", "Pen", "Total", "Equity", "Equity", "Equity"],
    values = [1051275,	410000,	235000,	175000,	1820000, 1095000, 75000, 650000] 
) """

types = ["Debt", "Debt", "Debt", "Debt"]
names = ["Zero", "TM3", "i13promax", "sb"]
values = [-60250, -205000, -7500, -15000]

df = pd.DataFrame(dict(types=types, names=names, values=values))

df["all"] = "all"

fig = px.treemap(df, path=["all", "types", "names"], values="values")

fig.update_traces(root_color="lightgrey")
fig.update_layout(margin=dict(t=50, l=25, r=25, b=25))
fig.show()
