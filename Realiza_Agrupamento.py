import pandas as pd
import numpy as np
import os 

path = r'D:\\Users\\guilh\\Documents\\[POLI]_6_Semestre\\IC\\2021\\dados starima\\dados starima\\TF-STARIMA\\'
dias = [i for i in range (1,31)]
frequencias = ['1Min','2Min','3Min','4Min','5Min']

rad = [5415,5483,5126,5471,5470,5316,5315,5313,5314,5358,5357,5355,5356,5463,5297,5296,5354,5098,5476,5475,5474,5479,5478,5477,5480,5323,5226,5308,5307,5432,5433,5414,5413,5201,5200,5199,5198,5205,5204,5203,5202,5196,5197,5195,5194,5445,5104,5446,5103,5462,5461,5460,5441,5106,5443,5442,5439,5105,5440,5457,5449,5317,5101,5506,5336,5335,5402,5401]

num_agrupado = [10588,10613,10613,10619,10622,10632,10632,10634,10634,10652,10652,10667,10667,10516,10528,10528,10554,10605,10637,10637,10637,10644,10644,10644,10644,10488,10488,10509,10509,10556,10556,10557,10557,10594,10594,10595,10595,10679,10679,10680,10680,10748,10748,10761,10761,10426,10426,10426,10433,10433,10433,10433,10482,10482,10482,10482,10484,10484,10484,10492,10492,10500,10507,10521,10527,10527,10531,10531]

# cria um dicionário
mapa = {}
for i in range(len(num_agrupado)):
    mapa[rad[i]] = num_agrupado[i]


#para cada um dos arquivos
for name in dias:
    #leio cada um dos arquivos
    df_new = pd.read_csv(path + "\\dia_" + str(name) + "_av23maio_numagrup.csv")

    df_new['Número Agrupado'] = df_new['Local'].map(mapa)
    df_new = df_new[['Unnamed: 0', 'Lote', 'Data', 'Local', 'Número Agrupado', 'Faixa', 'Entrefaixa',
       'Registro', 'Tipo de Registro', 'Veiculo', 'Final de Placa', 'Especie',
       'Classe', 'Comprimento', 'Velocidade', 'Ocupacao']]
    df_new.Data=pd.to_datetime(df_new.Data)
    


    # faz uma pasta pra cada dia
    # e coloca 5 csv, um agrupado com uma frequência ['1Min','2Min','3Min','4Min','5Min']    
    directory = str(name)
    parent_dir = os.getcwd()
    path4 = os.path.join(parent_dir, directory) 

    if  os.path.isdir(path4) == False:

        os.mkdir(path4) 
    
    for freq in frequencias:
        df_group = df_new.groupby(['Número Agrupado','Especie','Classe', pd.Grouper(key='Data', freq=freq)]).agg({
                                                                            'Velocidade': 'mean'})

        # Renomeia
        df_group.columns=['Vel_media']
        print(df_group.head())
        
       # df_group.to_csv(path4 + '\\' + str(name) + "_group_"+ freq +".csv")