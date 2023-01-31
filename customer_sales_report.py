import pandas as pd

data = pd.read_csv("sales.csv")

allSales = pd.DataFrame(columns=["Customer", "TotalCharge"])

allSales.Customer = data.CustomerID
allSales.TotalCharge = data.SubTotal + data.TaxAmt + data.Freight

output = pd.DataFrame(columns=["Customer", "TotalCharge"])

currCustomer = allSales["Customer"][0]
currTotal = 0
numbOfCustomers = 0


for x in allSales.index:
    if allSales["Customer"][x] == currCustomer:
        currTotal += allSales["TotalCharge"][x]
    else:

        output.loc[len(output.index)] = [currCustomer, currTotal]

        numbOfCustomers += 1
        currTotal = allSales["TotalCharge"][x]
        currCustomer = allSales["Customer"][x]

# required followup for the last cutomer in the csv
output.loc[len(output.index)] = [currCustomer, currTotal]

output.to_csv("salesreport.csv")
