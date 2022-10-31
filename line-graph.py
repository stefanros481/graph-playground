import plotly.express as px
import pandas as pd

# values = [274.01, 275.1, 274.5]
# labels = ["1", "2", "3", "4"]

price = [274.01, 275.1, 274.5, 274.9]
tt = ["15:32", "15:34", "15:36", "15:38"]


price.append(275)
tt.append("15:40")

print(price)
df = pd.DataFrame(dict(price=price, tt=tt))

fig = px.line(
    df,
    x="tt",
    y="price",
    title="Price",
    markers=True,
    color_discrete_sequence=px.colors.sequential.Greys,
)

fig.update_traces(marker=dict(line=dict(color="#000000", width=2)))

fig.write_image("images/quote.png")

# fig.show()
