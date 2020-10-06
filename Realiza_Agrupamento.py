import pandas as pd
import numpy as np
import os 

path = r'D:\\Users\\guilh\\Documents\\[POLI]_6_Semestre\\IC\\2021\\dados starima\\dados starima\\TF-STARIMA\\'
dias = [i for i in range (1,31)]
frequencias = ['1Min','2Min','3Min','4Min','5Min']

#para cada um dos arquivos
for name in dias:
    #leio cada um dos arquivos
    df_new = pd.read_csv(path + "\\dia_" + str(name) + "_av23maio_numagrup.csv")
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

        df_group.to_csv(path4 + '\\' + str(name) + "_group_"+ freq +".csv")