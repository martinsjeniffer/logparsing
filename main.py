# 1 -> read file
# 2 -> extract ip address and error and success logs
# 3 -> save the output in csv/excel file

import pprint
import pandas as pd

file = open("serverlogs.log", "r")

list_ip_address = []
list_success = []
list_failed = []

for log in file:
  splitLog = log.split(" ")

  list_ip_address.append(splitLog[0])

  list_success.append(int(splitLog[-4]))
  list_failed.append(int(splitLog[-1]))

list_ip_address.append("Total")
list_success.append(sum(list_success))
list_failed.append(sum(list_failed))


df = pd.DataFrame(columns=["IP Address", "Success", "Failed"])

df["IP Address"] = list_ip_address
df["Success"] = list_success
df["Failed"] = list_failed

df.to_csv("output.csv", index=False)

pprint.pprint(df)