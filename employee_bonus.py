import pandas as pd

data = pd.read_csv("EmployeePay.csv")
print(data.columns)

print(data.to_string())
