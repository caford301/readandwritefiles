import pandas as pd

data = pd.read_csv("customers.csv")

newData = pd.DataFrame(columns=["Customer", "Country"])

newData.Customer = data.FirstName + " " + data.LastName
newData.Country = data.Country

newData.to_csv("customer_country.csv")
