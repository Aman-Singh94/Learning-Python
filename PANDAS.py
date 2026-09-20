import pandas as pd
xyz=[100,200,506,346,637,937,873]

#series
print(pd.Series(xyz))


# 1. Basic list se DataFrame banana
data = {
    "naam": ["Aman", "Ravi", "Priya", "Neha"],
    "umar": [22, 25, 21, 24],
    "sheher": ["Delhi", "Mumbai", "Pune", "Jaipur"]
}
df = pd.DataFrame(data)
print(df)
