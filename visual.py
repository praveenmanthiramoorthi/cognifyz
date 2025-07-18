import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

file = input()
df = pd.read_csv(file)

col1 = input()
col2 = input()

sns.scatterplot(data=df, x=col1, y=col2)
plt.show()
