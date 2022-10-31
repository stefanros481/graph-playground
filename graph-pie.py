import plotly.express as px

# colors = ['gold', 'mediumturquoise', 'darkorange', 'lightgreen']
# df = px.data.tips()

labels = ["Zero", "Avanza", "Gjensidige"]
values = [1005000, 480000, 250000]

fig = px.pie(
    labels=labels,
    names=labels,
    values=values,
    color_discrete_sequence=px.colors.sequential.Greys,
)
# fig = px.pie(labels=labels, values=values, values='tip', names='day', color_discrete_sequence=px.colors.sequential.Greys)

# fig = px.pie(df, values='tip', names='day')

fig.update_traces(
    hoverinfo="label+percent",
    textinfo="label+value+percent",
    textfont_size=20,
    marker=dict(line=dict(color="#000000", width=2)),
)
# fig.update_traces(hoverinfo='label+percent', textinfo='value', textfont_size=20,
#                  marker=dict(line=dict(color='#000000', width=2)))

fig.write_image("images/pie.png")
# fig.show()
