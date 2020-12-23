# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import pandas as pd
import numpy as np
from datetime import timedelta
from datetime import datetime

num_agrupado =["10588","10613","10613","10619","10622","10632","10632","10634","10634","10652","10652","10667","10667","10516","10528","10528","10554","10605","10637","10637","10637","10644","10644","10644","10644","10488","10488","10509","10509","10556","10556","10557","10557","10594","10594","10595","10595","10679","10679","10680","10680","10748","10748","10761","10761","10426","10426","10426","10433","10433","10433","10433","10482","10482","10482","10482","10484","10484","10484","10492","10492","10500","10507","10521","10527","10527","10531","10531"]


Radares = [5415,5483,5126,5471,5470,5316,5315,5313,5314,5358,5357,5355,5356,5463,5297,5296,5354,5098,5476,5475,5474,5479,5478,5477,5480,5323,5226,5308,5307,5432,5433,5414,5413,5201,5200,5199,5198,5205,5204,5203,5202,5196,5197,5195,5194,5445,5104,5446,5103,5462,5461,5460,5441,5106,5443,5442,5439,5105,5440,5457,5449,5317,5101,5506,5336,5335,5402,5401]


# cria um dicionário
def faz_dict (keys, values):
    '''
        Cria um dicionário com a correspondência entre 
        chaves e valores. Com a função .map() pode, ser
        adicionadas novas colunas no DF.

        Inputs:
            keys: (list) chaves que estão no presente DF
            values: (list) valores que serão inputados na nova coluna

        Return:
            mapa: (dict) mapa de correspondência
    '''

    mapa = {}
    for i in range(len(keys)):
        mapa[keys[i]] = values[i]

    return mapa


# %%
estacoes = ["BT","BT","BT","BT","BT","BT","BT","BT","BT","BT","BT","BT","BT","CGE","CGE","CGE","CGE","CGE","CGE","CGE","CGE","CGE","VM","CGE","CGE","CGE","CGE","CGE","CGE","CGE","CGE","CGE","CGE","CGE","CGE","CGE","CGE","CGE","CGE","CGE","CGE","CGE","CGE","CGE","CGE","CGE","CGE","CGE","CGE","CGE","CGE","CGE","CGE","CGE","CGE","CGE","CGE","CGE","CGE","CGE","CGE","CGE","CGE","CGE","CGE","CGE","CGE","CGE","CGE","CGE","CGE","CGE","CGE","CGE","CGE","CGE","CGE","CGE","CGE","CGE","CGE","CGE","CGE","CGE","CGE","CGE","CGE","CGE","CGE","CGE","CGE","CGE","CGE","CGE","CGE","CGE","CGE","CGE","CGE","CGE","CGE","CGE","CGE","CGE","IP","IP","IP","IP","IP","IP","IP","IP","IP","IP","IP","IP","IP","IP","IP","IP","IP","IP","IP","IP","IP","IP","JB","JB","JB","JB","JB","JB","JB","JB","JB","JB","LP","LP","LP","LP","LP","LP","LP","LP","LP","PI","PI","PI","PI","PI","PI","PI","PI","PI","PI","PI","PI","PI","PI","PI","PI","PI","PI","PI","PI","PI","PI","PI","PI","PI","PI","PI","PI","PI","PI","PI","PI","PI","PI","PI","PI","PI","PI","PI","PI","PI","PI","PI","PI","PI","PI","PI","PI","PI","PI","PI","PI","PI","PI","PI","PI","PI","PI","PI","PI","PI","PI","PI","PI","PI","PI","PI","PI","PI","PI","PI","PI","PI","PI","PI","PI","PI","PI","PI","PI","PI","PI","PI","PI","PI","PI","PI","PI","PI","PI","PI","PI","PI","PI","PI","PI","PI","PI","PI","PI","PI","PI","PI","PI","PI","PI","PI","PI","PI","PI","SA","SA","SA","SA","SA","SA","SA","SA","SA","SA","SA","SA","SA","SA","SA","SA","SA","SA","SA","SA","SA","SA","SA","ST","ST","ST","ST","ST","ST","ST","ST","ST","ST","ST","ST","ST","ST","ST","ST","ST","ST","VM","VM","VM","VM","VM","VM","VM","VM","VM","VM","VM","VM","VM","VM","VM","VM","VM","VM","VM","VM","VM","VM","VM","VM","VM","VM","VM","VM","VM","VM","VM","VM","VM","VM","VM","VM","VM","VM","VM","VM","VM","VM","VM","VM","VM","VM","VM","VM","VM","VM","VM","VM","VM","VM","VM","VM","VM","VM","VM","VM","VM","VM","VM","VM","VM","VM","VM","VM","VM","VM","VM","VM","VM","VM","VM","VM","VM","VM","VM","VM","VM","VM","VM","VM","VM","VM","VM","VM","VM","VM","VM","VM","VM","VM","VM","VM"]

numeros_agrupados = ["10875","10862","10874","10858","10858","10893","10893","10864","10848","10906","10900","10904","10905","10605","10433","10426","10468","10508","10508","10613","10538","10616","10631","10505","10533","10607","10524","10479","10565","10586","10583","10587","10587","10584","10584","10514","10514","10513","10513","10595","10595","10594","10594","10582","10582","10585","10585","10555","10552","10488","10615","10464","10560","10543","10543","10540","10542","10512","10509","10509","10438","10497","10532","10532","10488","10502","10459","10454","10480","10591","10540","10591","10520","10554","10590","10537","10609","10609","10506","10506","10490","10490","10557","10557","10517","10556","10556","10426","10426","10568","10596","10596","10433","10433","10433","10628","10622","10619","10613","10538","10616","10468","10476","10476","10276","10306","10305","10348","10348","10337","10337","10309","10309","10310","10310","10302","10302","10293","10352","10262","10262","10353","10235","10269","10291","10292","10434","10434","10408","10371","10368","10380","10381","10434","10381","10381","10933","10940","10881","10877","10947","10911","10933","10894","10895","10770","10725","10655","10655","10702","10702","10701","10701","10630","10630","10674","10675","10670","10656","10654","10654","10720","10692","10732","10684","10709","10672","10788","10715","10807","10807","10683","10683","10762","10762","10834","10834","10761","10761","10748","10748","10680","10680","10679","10679","10635","10635","10808","10658","10664","10653","10820","10815","10815","10724","10713","10712","10711","10810","10689","10634","10634","10632","10632","10745","10800","10800","10670","10689","10742","10742","10747","10747","10798","10798","10665","10665","10830","10667","10667","10652","10652","10669","10669","10698","10698","10697","10697","10640","10640","10686","10686","10736","10736","10731","10731","10789","10703","10829","10729","10656","10764","10678","10763","10637","10637","10637","10644","10644","10644","10644","10658","10767","10704","10673","10627","10627","10625","10625","10592","10592","10578","10578","10650","10527","10527","10534","10474","10474","10471","10471","10531","10531","10589","10511","10511","10521","10623","10564","10564","10614","10614","10577","10577","10536","10620","10620","10477","10498","10498","10526","10526","10588","10530","10536","10645","10325","10323","10507","10356","10484","10482","10277","10431","10478","10606","10606","10539","10539","10487","10452","10458","10475","10384","10374","10566","10398","10357","10304","10544","10544","10375","10440","10334","10363","10363","10344","10344","10431","10321","10321","10351","10317","10529","10541","10541","10528","10528","10563","10500","10410","10410","10451","10525","10457","10346","10346","10496","10496","10489","10489","10361","10361","10358","10358","10367","10367","10420","10420","10421","10421","10465","10465","10561","10377","10290","10314","10486","10413","10413","10356","10356","10484","10484","10482","10482","10482","10357","10492","10492","10516","10572","10572","10410","10420","10421","10377","10486","10413","10413","10374","10374"]

mapa_estacoes = faz_dict(numeros_agrupados, estacoes)
# 0,L3,2018-02-28 23:56:22,5323,3,0,1095514,0,1,0,048,136,00649,84956
# 54,L3,2018-08-03 00:00:12,5323,2,0,283530,0,1,0,118,053,03039,95040


# %%
labels = np.array(["P1","P2","P3","P4","P5","P6","P7"])

intervalos = pd.IntervalIndex.from_tuples([(0,5),(5,7),(7,10),(10,14),(14,17),(17,20),(20,24)], closed="left")

inter = ["[0, 5)","[5, 7)","[7, 10)","[10, 14)","[14, 17)","[17, 20)","[20, 24)"]
# "P1","P2","P3","P4","P5","P6","P7"

sentidos = ["Sumare_N","Sumare_S","Sumare_S","Sumare_S","Sumare_N","Sumare_N","Sumare_N","Sumare_S","Sumare_S","Sumare_S","Sumare_S","Sumare_N","Sumare_N","Brasil_N","Brasil_S","Brasil_S","Brasil_S","Brasil_S","Brasil_S","Brasil_S","Brasil_S","Brasil_N","Brasil_N","Brasil_N","Brasil_N","Reboucas_C","Reboucas_C","Reboucas_B","Reboucas_B","Reboucas_B","Reboucas_B","Reboucas_C","Reboucas_C","Reboucas_B","Reboucas_B","Reboucas_C","Reboucas_C","Reboucas_B","Reboucas_B","Reboucas_C","Reboucas_C","Reboucas_B","Reboucas_B","Reboucas_C","Reboucas_C","23deMaio_B","23deMaio_B","23deMaio_B","23deMaio_C","23deMaio_C","23deMaio_C","23deMaio_C","23deMaio_C","23deMaio_C","23deMaio_C","23deMaio_C","23deMaio_B","23deMaio_B","23deMaio_B","23deMaio_B","23deMaio_B","23deMaio_C","23deMaio_B","23deMaio_B","23deMaio_B","23deMaio_B","23deMaio_C","23deMaio_C"]


tip_faixa = ["mista","mista","mista","onibus","mista","mista","mista","mista","onibus","mista","mista","mista","mista","onibus","mista","mista","mista","mista","onibus","onibus","mista","mista","mista","mista","mista","mista","mista","mista","mista","mista","mista","onibus","mista","mista","mista","mista","mista","mista","onibus","mista","mista","onibus","mista","mista","mista","onibus","mista","mista","mista","onibus","mista","mista","mista","onibus","mista","mista","mista","onibus","mista","mista","mista","mista","mista","mista","mista","onibus","mista","mista","onibus","mista","mista","mista","mista","mista","mista","mista","mista","mista","mista","mista","mista","onibus","mista","mista","onibus","mista","mista","mista","mista","mista","onibus","mista","mista","mista","mista","mista","mista","mista","mista","mista","mista","mista","mista","mista","mista","mista","onibus","mista","mista","mista","onibus","onibus","mista","mista","onibus","mista","mista","onibus","mista","mista","onibus","mista","mista"]

num_faixa = ["104261","104262","104263","104264","104331","104332","104333","104334","104335","104821","104822","104823","104824","104825","104841","104842","104843","104844","104845","104881","104882","104883","104884","104921","104922","104923","105001","105002","105003","105071","105072","105091","105092","105093","105094","105161","105162","105163","105164","105211","105212","105213","105281","105282","105283","105284","105311","105312","105313","105314","105541","105542","105543","105561","105562","105563","105564","105571","105572","105573","105574","105881","105882","105883","105884","105941","105942","105943","105951","105952","105953","106051","106052","106053","106131","106132","106133","106134","106135","106191","106192","106193","106221","106222","106223","106321","106322","106323","106341","106342","106343","106371","106372","106373","106374","106375","106376","106441","106442","106443","106444","106445","106446","106521","106522","106523","106524","106671","106672","106673","106674","106791","106792","106793","106801","106802","106803","107481","107482","107483","107611","107612","107613"]


mapfaixas = faz_dict(num_faixa,tip_faixa)


mapa_intervalos  = {}
for i in range(len(labels)):
    mapa_intervalos[inter[i]] = labels[i]



mapa_sentidos = {}
for i in range(len(num_agrupado)):
    mapa_sentidos[numeros_agrupados[i]] = sentidos[i]


# %%
df_base = pd.read_csv(r'D:\Users\guilh\Documents\GitHub\Dados_CET\csv_radares-20200426T211130Z-001_selecionados/'+"01_selecionado.csv", index_col=["Unnamed: 0"], parse_dates=True, dayfirst= True)

# cria a coluna de numeros agrupados
df_base['Numero Agrupado'] = df_base['Local'].map(faz_dict(Radares,num_agrupado))


#coloca a Data e datetime object para facilitar manipulacao
df_base["Data"] = pd.to_datetime(df_base["Data"],format='%Y-%d-%m %H:%M:%S', errors='coerce')


df_base = df_base[df_base.Data.dt.day == 1]
# df_base.head()

# %% [markdown]
# ## Limpeza inicial do df
# 
# * tiramos os NaNs, 
# * os vazios,
# * adicionamos o Numero agrupado (str),
# * Coloca data em datetime,
# * Cria as colunas "Numero Agrupado", "Dia_Sem"

# %%

# cria a coluna do dia da semana
# ###############IMPORTANTE############# segunda = 0
df_base["Dia_Sem"] =  df_base["Data"].dt.dayofweek


########## UPDATE ###########
# transforma todos radares 5479 na faixa 3, (5479,3) em radares 5478 na faixa 3 (5478,3)
# pode ficar tranquilo por que eles tem o mesmo numero agrupado
df_base.loc[(df_base["Local"]==5479) & (df_base["Faixa"] == 3), "Local"] = 5478

# limpa a ocupacao
df_base.drop(df_base.loc[df_base['Ocupacao'] =='     ','Ocupacao'].index, inplace=True)
df_base.Ocupacao = df_base.Ocupacao.astype(float)

#dropa vazios
df_base.drop(df_base.loc[df_base['Velocidade'] =='   ','Velocidade'].index, inplace=True)

#dropa não válidos (nan)
df_base.loc[:,'Velocidade'].dropna(inplace=True)

#coloca tudo no mesmo formato de dado int
df_base.loc[:,'Velocidade'] = pd.to_numeric(df_base.loc[:,'Velocidade'])

# colocar faixa no formato int
df_base.loc[:,'Faixa'] = pd.to_numeric(df_base.loc[:,'Faixa'])

# colocar Especie no formato int
df_base.loc[:,'Especie'] = pd.to_numeric(df_base.loc[:,'Especie'])

###### Numero Agrupado é uma String

df_base.reset_index(drop=True,inplace=True)


df_base = df_base[['Lote', 'Data', "Dia_Sem", 'Local', 'Numero Agrupado', 'Faixa', 'Entrefaixa',
       'Registro', 'Tipo de Registro', 'Especie',
      'Classe', 'Comprimento', 'Velocidade', 'Ocupacao']]
# df_base.head()

# %% [markdown]
# ## Cria o df agrupado
# 
# df agrupado a cada 5 minutos
# adiciona Volume, velocidade media, mediana e desvio padrao
# adiciona ocupação media mediana e desvio padrao
# 

# %%
df_agregado = df_base.copy()

df_agregado.loc[:,'V1'] = df_agregado.loc[:,'Velocidade'].copy()
df_agregado.loc[:,'V2'] = df_agregado.loc[:,'Velocidade'].copy()
df_agregado.loc[:,'Oc1'] = df_agregado.loc[:,'Ocupacao'].copy()
df_agregado.loc[:,'Oc2'] = df_agregado.loc[:,'Ocupacao'].copy()
df_agregado = df_agregado.groupby([ 'Numero Agrupado',"Faixa",'Especie',pd.Grouper(key='Data', freq='5Min')]).agg({'Dia_Sem': "mean",
                                                                        "Registro": "count",
                                                                        'Velocidade': 'mean',
                                                                        'V1':'median',
                                                                        'V2':'std',
                                                                        'Ocupacao':'mean',
                                                                        'Oc1':'median',
                                                                        'Oc2':'std',
                                                                        })
df_agregado.columns=['Dia_Sem',
            "Volume",
            'Vel_media',
            'Vel_mediana',
            'Vel_desvpad',
            'Ocu_media',
            'Ocu_mediana',
            'Ocu_desvpad'
            ] # Renomeia

df_agregado.reset_index(inplace=True)
# df_agregado.head()

# %% [markdown]
# ## Criando dicionarios
# 
# Aqui são dicionarios que serão utilizados para gerar colunas via mapeamento

# %%

# Criando a coluna Periodo (no lugar de y pode ser qualquer coisa, menos numero)
df_agregado["Periodo"] = "y"


df_agregado['aux'] = pd.cut(np.array(df_agregado.Data.dt.hour), intervalos)

try:
    df_agregado['aux'] = df_agregado['aux'].astype(str)
    df_agregado['Periodo'] = df_agregado['aux'].map(mapa_intervalos)
    df_agregado.drop(columns=["aux"],inplace=True, axis = 0)
except:
    pass

# Criando a colua Eixo usando o mapa de sentidos das vias criado acimma
df_agregado["Eixo"] = df_agregado["Numero Agrupado"].map(mapa_sentidos)

# Criando a coluna Numero agregado + faixa, somando as strings
df_agregado["NumAg_fx"] = df_agregado["Numero Agrupado"] + df_agregado['Faixa'].astype(str)

# Criando a coluna Faixa tipo que, para cada NumAg_fx determina qual o tipo de faixa
df_agregado["Fx_tipo"] = df_agregado["NumAg_fx"].map(mapfaixas)

#criando coluna de estação meteorologica, será retirada mais a frente
df_agregado['Estacao Meteorol'] = df_agregado["Numero Agrupado"].map(mapa_estacoes)


# reorganiza a ordem das colunas
df_agregado = df_agregado[["Data", "Dia_Sem", "Periodo", "Numero Agrupado", "Faixa", "NumAg_fx","Fx_tipo","Eixo","Especie","Volume", "Vel_media", "Vel_mediana", "Vel_desvpad", "Ocu_media", "Ocu_mediana", "Ocu_desvpad", 'Estacao Meteorol']] # 17 sao as que vao ficar, mas ai tem 18



# display(df_agregado.shape[1], df_agregado.head())

# %% [markdown]
# ### ate aqui temos 17 colunas finais
# 
# Foram adicionadas o 
# 
# * Período
# * Eixo
# * NumAg_fx
# * Fx_tipo
# * Estacao Meteorol

# %%
#to fazendo pra um radar de exemplo mas preciso fazer o mesmo processo para
# cada numero agrupado
# cada Especie
# Cada Faixa
# 24 horas do dia * 60 minutos por hora / 5 minutos = 288 registros por cada um dos 
# 288 * 4 especies * 3 faixas(em media) = 3456 por numero agrupado
# 3456 * 34 Num agrup = 117.504 linhas por dia
# 117504 * 30 dias = 35 milhoes
# por dia ate que nao esta muito nao, é um tamanho parecido com o DF que entra

# radar10680 = df_agregado.loc[(df_agregado["Numero Agrupado"] == "10468")
#             &   (df_agregado["Faixa"] == 1)
#             &   (df_agregado["Especie"] == "1")

#                 ].sort_values(by="Data")

# radar10680 = radar10680.set_index("Data").asfreq("5 min")

# radar10680[["Numero Agrupado","Faixa","Especie","Dia_Sem","NumAg_fx","Fx_tipo","Eixo"]] = radar10680[["Numero Agrupado","Faixa","Especie","Dia_Sem","NumAg_fx", "Fx_tipo",	"Eixo"]].fillna(method="ffill")

# radar10680.head()

# %% [markdown]
# ## Adiciona as colunas de chuva
# 
# A depender do qual radar estamos tratando, usamos uma estação meteorológica para computar os dados de chuva por 5 minutos
# 
# O timedelta faz o trabalho de defasar o df da chuva para ficar alinhado com o df_agregado 

# %%
chuva = pd.read_excel(r"D:\Users\guilh\Documents\[POLI]_6_Semestre\IC\2021\codigos olimpio\Radar X Chuva.xlsx", sheet_name = "Chuva", parse_dates=True)
chuva["DATA"] = pd.to_datetime(chuva["DATA"],format='%Y-%d-%m %H:%M:%S', errors='coerce').astype("datetime64[s]")
chuva = chuva[chuva.DATA.dt.month == 3]

chuva["DATA"] = chuva["DATA"] -timedelta(minutes = 5)

for estacao in ["JB","CGE","ST","PI","BT", "IP","LA","SA"]: 
    chuva[estacao] = pd.to_numeric(chuva[estacao])


chuva.reset_index(drop=True, inplace=True)

# chuva.head()

# %% [markdown]
# aqui tem um pequeno exemplo caso queira computar para apenas um radar, sem iterações

# %%
# merged_radar10680 = radar10680.merge(chuva[["DATA", "CGE"]],how="left",right_on= "DATA", left_on="Data")

# merged_radar10680["Chuva 1h"] = merged_radar10680["CGE"].rolling(12).sum()

# merged_radar10680 = merged_radar10680 [["DATA", "Dia_Sem", "Periodo", "Numero Agrupado", "Faixa", "NumAg_fx","Fx_tipo","Eixo","Especie","Volume", "Vel_media", "Vel_mediana", "Vel_desvpad", "Ocu_media", "Ocu_mediana", "Ocu_desvpad", "CGE", "Chuva 1h"]]

# merged_radar10680.columns = ["Data", "Dia_Sem", "Periodo", "Numero Agrupado", "Faixa", "NumAg_fx","Fx_tipo","Eixo","Especie","Volume", "Vel_media", "Vel_mediana", "Vel_desvpad", "Ocu_media", "Ocu_mediana", "Ocu_desvpad", "Chuva", "Chuva 1h"]


# merged_radar10680.head()

# %% [markdown]
# # Iteração para todos os radares

# %%

df = pd.DataFrame()
df_reduzido = df_agregado.copy()

# for radar in list(set(df_agregado["Numero Agrupado"])):


# caso queira testar para so alguns radares
for radar in ["10488", '10582', '10514', '10513', '10587']:


    for especie in list(set(df_reduzido["Especie"])):


        for faixa in list(set(df_reduzido["Faixa"])):
            
            # faz um pequeno subset do df buscando criar uma configuração de radar, faixa e especie especifica
            radar_especifico = df_reduzido.loc[(df_reduzido["Numero Agrupado"] == radar)
                                            &   (df_reduzido["Especie"] == especie)
                                            &   (df_reduzido["Faixa"] == faixa)].sort_values(by="Data").reset_index(drop=True)
      
            
            #adiciona linhas nos intervalos de 5 minutos que nao tem registro de veiculo, portanto, linhas vazias
            radar_especifico = radar_especifico.set_index("Data").asfreq("5 min")

            #o seguinte preenchimento deve ser feito apos as novas linhas de 5 minutos que
            # que nao tem registros serem adicionadas, e 
            # somente nas colunas selecionadas, que sao as que sabemos os parametros

            colunas_preenchiveis = ["Numero Agrupado","Faixa","Especie","Dia_Sem","NumAg_fx","Fx_tipo","Eixo", "Periodo", "Estacao Meteorol"]
            radar_especifico[colunas_preenchiveis] = radar_especifico[colunas_preenchiveis].fillna(method="ffill")

            #o metodo de preenchimento é forward fill, o NaN é preenchido com o conteudo de cima
            # poderia ser backward fill (backfill) ja que para essas colunas nao faz diferença


            # esse try existe para que seja possivel rodar o codigo mesmo que um radar nao esteja no arquivo 
            try:
                # seleciona qual é a estação meteorologica para esse radar especifico
                estac_metero = radar_especifico["Estacao Meteorol"][0]

                # merge entre as duas tabelas, com prevalencia da tabela de radares (left)
                radar_com_chuva = radar_especifico.merge(chuva[["DATA", estac_metero]],how="left",right_on= "DATA", left_on="Data")

                # Cria a coluna com a soma rolante da ultima hora (por isso os ultimos 12 registros)
                radar_com_chuva["Chuva 1h"] = radar_com_chuva["CGE"].rolling(12).sum()

                # reorganiza a ordem das colunas
                radar_com_chuva = radar_com_chuva [["DATA", "Dia_Sem", "Periodo", "Numero Agrupado", "Faixa", "NumAg_fx","Fx_tipo","Eixo","Especie","Volume", "Vel_media", "Vel_mediana", "Vel_desvpad", "Ocu_media", "Ocu_mediana", "Ocu_desvpad", estac_metero, "Chuva 1h"]]

                # reorganiza o nome das colunas
                radar_com_chuva.columns = ["Data", "Dia_Sem", "Periodo", "Numero Agrupado", "Faixa", "NumAg_fx","Fx_tipo","Eixo","Especie","Volume", "Vel_media", "Vel_mediana", "Vel_desvpad", "Ocu_media", "Ocu_mediana", "Ocu_desvpad", "Chuva_5min", "Chuva_1h"]

                #concatena os dataframes em uma unica tabela
                df = pd.concat([df, radar_com_chuva])
            except:
                print("radar:",radar, "     Especie",especie,"      Faixa:",faixa,"     //        radar,faixa ou especie nao presente no dataframe")


df.to_excel("tabela nova.xlsx")


# %%
#df


# %%



