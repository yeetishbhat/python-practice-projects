import pandas as pd

df = pd.read_csv("50_states.csv")
states = df.state.to_list()

x = df[df.state == "Ohio"]
y = df[df.state == "Ohio"]

print(x)
