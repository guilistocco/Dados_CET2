import numpy as np
import pandas as pd

rad_Rebou = [5323,5226,5308,5307,5432,5433,5414,5413,5201,5200,5199,5198,5205,5204,5203,5202,5196,5197,5195,5194]
rad_23 = [5445,5104,5446,5103,5462,5461,5460,5441,5106,5443,5442,5439,5105,5440,5457,5449,5317,5101,5506,5336,5335,5402,5401]
rad_Sum_Brasil = [5415,5483,5126,5471,5470,5316,5315,5313,5314,5358,5357,5355,5356,5463,5297,5296,5354,5098,5476,5475,5474,5479,5478,5477,5480]

### ------------ ESCOLHER AQUI ---------------- ###

## os limites se referem ao intervalo de horas 
Limite_inf_inclusive = 7
Limite_sup = 9

## os radares devem ser escolhidos entre:       rad_Rebou      rad_23     rad_Sum_Brasil

radares = rad_23

### ------------------------------------------- ###
## colocar o caminho até a a pasta em que estão os CSVs



df = pd.read_csv(r'D:\\Users\\guilh\\Documents\\GitHub\\Dados_CET\\csv_radares-20200426T211130Z-001\\28_selec.csv', index_col=0) 
df['Data'] = pd.to_datetime(df['Data'])

df_n = df[(df.Data.dt.hour >=Limite_inf_inclusive) & (df.Data.dt.hour <Limite_sup)]
df_n.reset_index(drop=True,inplace=True)


data_frame = pd.DataFrame()
for loc in radares:
    data_frame = pd.concat([data_frame,df_n.loc[df_n["Local"]== loc]])


## data_frame resultado dessa operação recorte do arquivo original

