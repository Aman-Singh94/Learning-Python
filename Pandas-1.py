import pandas as pd  # pandas ko lao

# STEP 1: Apna data banao (jaise school ki register)
data = {
    "naam":   ["Aman", "Ravi", "Priya", "Neha", "Vikas", "Sneha", "Rahul", "Pooja", "Arjun", "Kiran"],
    "umar":   [22, 25, 21, 24, 23, 26, 22, 25, 24, 23],
    "sheher": ["Delhi", "Mumbai", "Pune", "Jaipur", "Delhi", "Mumbai", "Pune", "Jaipur", "Delhi", "Mumbai"],
    "salary": [50000, 65000, 48000, 55000, 52000, 70000, 51000, 58000, 54000, 62000]
}

# STEP 2: Data ko table (DataFrame) me daalo
df = pd.DataFrame(data)

# STEP 3: Upar se 3 log dikhao (head)
print(df.head(3))

# STEP 4: Neeche se 3 log dikhao (tail)
print(df.tail(3))

# STEP 5: Kitne log aur kitne columns hain? (shape)
print(df.shape)

# STEP 6: Table ki poori jaankari (info)
df.info()

# STEP 7: Numbers ka hisaab — average, min, max (describe)
print(df.describe())

# STEP 8: Column ke naam kya kya hain?
print(list(df.columns))

#kuch  function 
df["salary"].sum()        # sabki total salary
df["salary"].max()        # sabse zyada salary
df[df["salary"] > 55000]  # jin log ki salary 55,000 se zyada hai
