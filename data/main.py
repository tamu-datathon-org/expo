import pandas as pd

data = pd.read_csv("submissions-tamu-datathon-2019-sensitive-info-2020-10-17-22_01_59.csv")

col = ["table", "project", "sponsors", "link"]
newData = pd.DataFrame(columns=col)
newData["project"] = data["Submission Title"]
newData["sponsors"] = data["Desired Prizes"]
newData["link"] = data["Submission Url"]

newData["table"] = [0 for i in range(len(newData.project))]

newData.to_csv("data.csv", index=False)

print("done")
