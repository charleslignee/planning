# %%
import pandas as pd
import matplotlib.pyplot as plt

years=["2015","2016","2017","2018","2019"]
data={
    "Python":[50,60,70,80,100],
    "JavaScript":[20,20,20,20,0],
    "C++":[30,20,10,0,0],
}

df=pd.DataFrame(data,index=years)

df.plot(kind="bar",stacked=True,figsize=(10,8))
plt.legend(loc="lower left",bbox_to_anchor=(0.8,1.0))
plt.show()


# %%
