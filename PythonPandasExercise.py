import pandas  as pd
df = pd.read_csv(r"C:\Users\90538\Desktop\PythonExercises\Automobile_data.csv")
pd.set_option("display.max_columns", None)
pd.set_option("display.width", 500)

# Exercise 1: From the given dataset print the first and last five rows
df.head()
df.tail()

# Exercise 2: Clean the dataset and update the CSV file
# Replace all column values which contain ?, n.a, or NaN.
df = pd.read_csv(r"C:\Users\90538\Desktop\PythonExercises\Automobile_data.csv", na_values={
'price': ["?", "n.a"],
'stroke': ["?", "n.a"],
'horsepower': ["?", "n.a"],
'peak-rpm': ["?", "n.a"],
'average-mileage': ["?","n.a"]})
print(df)
df.to_csv(r"C:\Users\90538\Desktop\PythonExercises\Automobile_data.csv")
df = df.dropna()

# Exercise 3: Find the most expensive car company name
# Print most expensive car’s company name and price.

var = df[["company", "price"]][df["price"] == df["price"].max()]
print(var)

# Exercise 4: Print All Toyota Cars details
var = df[df["company"] == "toyota"]
print(var)

# Exercise 5: Count total cars per company
df["company"].value_counts()


# Exercise 6: Find each company’s Higesht price car
df.groupby("company").agg({"price": "max"})

# Exercise 7: Find the average mileage of each car making company
df.groupby("company").agg({"average-mileage": "mean"})

# Exercise 8: Sort all cars by Price column
df.sort_values("price", ascending=False)

# Exercise 9: Concatenate two data frames using the following conditions
# Create two data frames using the following two dictionaries.

GermanCars = {'Company': ['Ford', 'Mercedes', 'BMV', 'Audi'], 'Price': [23845, 171995, 135925, 71400]}
carsDf1 = pd.DataFrame.from_dict(GermanCars)
japaneseCars = {'Company': ['Toyota', 'Honda', 'Nissan', 'Mitsubishi '], 'Price': [29995, 23600, 61500, 58900]}
carsDf2 = pd.DataFrame.from_dict(japaneseCars)
carsDf = pd.concat([carsDf1, carsDf2], keys=["Germany", "Japan"])
carsDf


# Exercise 10: Merge two data frames using the following condition Create two data frames using the following two
# Dicts, Merge two data frames, and append the second data frame as a new column to the first data frame.
# Car_Price = {'Company': ['Toyota', 'Honda', 'BMV', 'Audi'], 'Price': [23845, 17995, 135925 , 71400]}
# car_Horsepower = {'Company': ['Toyota', 'Honda', 'BMV', 'Audi'], 'horsepower': [141, 80, 182 , 160]}

Car_Price = {'Company': ['Toyota', 'Honda', 'BMV', 'Audi'], 'Price': [23845, 17995, 135925, 71400]}
carsDf1 = pd.DataFrame.from_dict(Car_Price)
car_Horsepower = {'Company': ['Toyota', 'Honda', 'BMV', 'Audi'], 'horsepower': [141, 80, 182, 160]}
carsDf2 = pd.DataFrame.from_dict(car_Horsepower)

pd.merge(carsDf1, carsDf2, on="Company")