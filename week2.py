import pandas as md
import matplotlib.pyplot as mano
msd = md.read_csv('gender_submission.csv')
print(msd.head(40))
msd.rename(columns={"PassengerId":"Number"}, inplace=True)
print(msd)
filter=msd[msd["Survived"]==1]
print(filter)
Total_Pass = msd["Survived"].value_counts()
total=len(msd)
a = Total_Pass[0]
perc = (a / total) * 100
print(f"Percentage of non-survivors is: {perc:.2f}%")
Total_Pass.plot(kind = 'bar',color = ["orange","black"])
mano.xlabel("Survived people")
mano.ylabel("non-survived people")
mano.title("survived passenger in the flight")
mano.xticks(rotation = 0)
mano.yticks(rotation = 10)
mano.show()