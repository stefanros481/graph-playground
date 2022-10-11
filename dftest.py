import pandas as pd

data = {
    "Name": ["Tom", "nick", "krish", "jack"],
    "Age": [20, 21, 19, 18],
    "City": ["Stockholm", "Linkoping", "Malmo", "Malmo"],
}

df = pd.DataFrame(data)

first = df.loc["Name"]

print(first[["Name", "City"]])
