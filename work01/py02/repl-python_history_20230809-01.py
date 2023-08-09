1
2
dir()
1+123
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
x = [1,2,3,4,5]
y = [1,3,2,4,5]
sns.set() # おまじない
# グラフの可視化
plt.plot(x,y)
plt.title("lineplot matplotlib")
plt.xlabel("x")
plt.ylabel("y")
plt.show()