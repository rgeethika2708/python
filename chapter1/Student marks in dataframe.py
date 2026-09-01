import pandas as pd

data = {
    "Name": ["Anu", "Ravi", "Kiran", "Sita", "Arun"],
    "Marks": [85, 92, 78, 95, 88]
}

df = pd.DataFrame(data)

print("Student Data:")
print(df)

print("\nHighest Marks:", df["Marks"].max())
print("Lowest Marks:", df["Marks"].min())
print("Average Marks:", df["Marks"].mean())

topper = df.loc[df["Marks"].idxmax(), "Name"]
print("Topper:", topper)
