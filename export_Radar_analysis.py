# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

# %% [markdown]
# # Which lane on a road have the highest speed?
# 
# ## Importing first databases
# 
# Radars.csv contains all cars, trucks, motorcycles and buses that comes thru São Paulo's radar system 
# 

# %%
# to download the data, access https://drive.google.com/file/d/1VG-t8t1mq_HZV-Ue6zkth_3Ne4IfCOrq/view?usp=sharing 

df_base = pd.read_csv(r"Radar_Data_2.03.2018.csv", index_col= "Data")


# %%
df_base.head()

# %% [markdown]
# ### Reading the columns
# 
# * **Radar** is the number of identification of a street section
# * **Lane** goes from 1 to 6 in most radars, low lane number are closer to the center of the freeway, high lane numbers are "local" lanes, to the right
# * **Register** represents each vehicle
# * **Types** are: motorcycle = 0, car = 1, bus = 2 ou truck = 3
# * **Classes** are: *light* (motorcycle and car) = 0 ou *heavy* (bus and truck)  = 1
# * **Speeds** are in kilometer per hour
# * **Radar_Lane** comes to identify each lane on a single radar (will be usefull to merge dataframes)
# 

# %%
# Preprocessing

df = df_base[["Numero Agrupado", "Faixa", "Registro", "Especie", "Classe", "Velocidade"]]
# turns speed from dm/s to km/h
df.loc[:,"Velocidade"] = df.loc[:,"Velocidade"] * 0.36

df.index.names = ["Date"]

df["Radar_Lane"] = df["Numero Agrupado"].astype(str) + df["Faixa"].astype(str)

# renaming columns to english
df.columns = ["Radar", "Lane", "Register", "Type", "Class", "Speed [km/h]", "Radar_Lane"]

df.head()

# %% [markdown]
# ### Lane types database
# 
# Helps to tell the **use of each lane** . 
# 
# "Tipo" contains the information of lanes where all types of vehicycles can use ( *mix_use* ) and other that are for buses only ( *exclusive_bus* )

# %%
lane_types = pd.read_excel(r"Lanes_type.xlsx", usecols = ["Num_agrupado","faixa", "Num_fx","tipo"],engine='openpyxl')


# %%
lane_types.head()

# %% [markdown]
# ### Merge dataframes
# 
# To identify the type of the lane, if it is exclusive for buses, or multipurpose

# %%
df_merged = lane_types[["Num_fx", "tipo"]].merge(df, left_on = "Num_fx", right_on = "Radar_Lane", how="right")

df_merged["Lane_use"] = df_merged["tipo"].map({"mista":"mix_use", "onibus": "exclusive_bus"})

df_merged = df_merged[["Radar", "Lane", "Register", "Type", "Class", "Speed [km/h]", "Lane_use"]]

df_merged.head()

# %% [markdown]
# ### Looking for NaNs
# 
# As shown below, NaNs are less than 1% (actually, less than 0,2%)
# 
# With this information, there will be low loss in dropping NaNs
# 
# 

# %%
print(df_merged.isna().mean() *100)

df_merged.dropna(inplace=True)

# %% [markdown]
# ### Selection of Lanes
# 
# Using only the data from mix_use lanes, select for each lane to create comparison
# 
# The max number of lanes is 6, but only few roads have all 6, so it can be excluded from the analysis

# %%
lanes = df_merged.loc[df_merged["Lane_use"] == "mix_use"]

lane_1 = lanes.loc[lanes["Lane"] == 1]

lane_2 = lanes.loc[lanes["Lane"] == 2]

lane_3 = lanes.loc[lanes["Lane"] == 3]

lane_4 = lanes.loc[lanes["Lane"] == 4]

lane_5 = lanes.loc[lanes["Lane"] == 5]

lane_6 = lanes.loc[lanes["Lane"] == 6]

print(lane_1.shape, lane_2.shape, lane_3.shape, lane_4.shape, lane_5.shape, lane_6.shape)

# %% [markdown]
# ### Plotting the means
# 
# 

# %%
means = []

for lane in [lane_1,lane_2,lane_3,lane_4,lane_5]:
    means.append(lane["Speed [km/h]"].mean())

means = [ round(elem, 2) for elem in means ]


fig, ax = plt.subplots()

rects = ax.bar([1,2,3,4,5],means, width= 0.5)

ax.set_ylabel("Speed [km/h]")
ax.set_xlabel("Lanes")
ax.set_title('Speeds per lane')


def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')

autolabel(rects)


plt.show()

# %% [markdown]
# ## Conclusion
# 
# Center lanes move faster than "local" lanes
# %% [markdown]
# # How does the features correlate?
# 
# The new column is **Length** that represents the size of a vehicycle. Must be turn into meters

# %%
df_corr = df_base[["Numero Agrupado", "Faixa", "Registro", "Especie", "Classe", "Velocidade", "Comprimento"]]

df_corr.loc[:,"Comprimento"] = df_corr.loc[:,"Comprimento"] /10

df_corr.loc[:,"Velocidade"] = df_corr.loc[:,"Velocidade"] * 0.36

df_corr.columns = ["Radar", "Lane", "Register", "Type", "Class", "Speed [km/h]", "Length"]


# %%
corrMatrix = df_corr[["Lane", "Type", "Speed [km/h]","Length"]].corr()
sns.heatmap(corrMatrix, annot=True)
plt.show()


# %%


# %% [markdown]
# ## Conclusion
# 
# Is easy to see that *speed/lane* and *length/type* have the biggest correlations
# 
# High speeds correlates to low lane numbers, that means that center lanes move faster, as seen in other analysis (remembering the lane number grow from left to right)
# 
# Big lengths correlates with greater types that are heavier vehicycles like buses and trucks
# %% [markdown]
# # How can a new car be classified?
# 
# 

# %%
df_regression = df_base[["Numero Agrupado", "Faixa", "Registro", "Especie", "Classe", "Velocidade", "Comprimento"]]

df_regression.loc[:,"Comprimento"] = df_regression.loc[:,"Comprimento"] /10

df_regression.loc[:,"Velocidade"] = df_regression.loc[:,"Velocidade"] * 0.36


# %%
df_regression.columns = ["Radar", "Lane", "Register", "Type", "Class", "Speed [km/h]", "Length"]


Validation = df_regression.loc[df_regression["Speed [km/h]"].isna()]
X = df_regression[["Lane", "Type", "Class", "Length"]].dropna()
X = pd.concat([pd.get_dummies(X[["Lane", "Type", "Class"]].astype("object")),X["Length"]], axis=1)

y = df_regression["Speed [km/h]"].dropna()


X.head()


# %%
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# %%
regr = RandomForestRegressor(n_estimators=50, max_depth=10, random_state=42)
regr.fit(X_train, y_train)

print("R2 score with n_estimators={} and max_depth={} is {} ".format(50,10,regr.score(X_test,y_test)))


