# -*- coding: utf-8 -*-
"""
Script para pegar dados de maré da EPAGRI
Maré observada e astronomica

#@author: Renan Pimentel abr/2021
renan@lma.ufrj.br
"""
import warnings
warnings.filterwarnings("ignore")
import sys
import pandas as pd
import datetime
from datetime import date, timedelta
from pytz import timezone
import numpy as np


df = pd.read_json('https://ciram.epagri.sc.gov.br/graficos/getDataMare6_2963.php',orient='index')

rows = df.iloc[1]
cols = df.iloc[0]

cols.iloc[0] #topping
cols.iloc[1] #Mare Observada
cols.iloc[2] #Mare Astronomica
cols.iloc[3] #Residual
cols.iloc[4] #NMM


data = []
for i in np.arange(0,len(rows)):

    date = rows.iloc[i]['c'][0]['v']

    try:
        mare_obs = float(rows.iloc[i]['c'][1]['v'])
    except:
        mare_obs = float('NaN')

    try:
        mare_astro = float(rows.iloc[i]['c'][2]['v'])
    except:
        mare_astro = float('NaN')

    try:
        resi = float(rows.iloc[i]['c'][3]['v'])
    except:
        resi = float('NaN')

    try:
        nmm = float(rows.iloc[i]['c'][4]['v'])
    except:
        nmm = float('NaN')


    data.append([date,mare_obs,mare_astro,resi,nmm])


df = pd.DataFrame(data, columns=['time', 'mare_obs', 'mare_astro','residual','nmm'])
df['time'] = df['time'].astype('string') 

from datetime import datetime
today = datetime.today()
datem = datetime(today.year, today.month, 1)
year = str(datem.year)
df['year'] = year
df['stid'] = 'Imbutuba_2963'


df['date'] = df['year']+'/'+df['time']
df['time'] = pd.to_datetime(df['date'], format='%Y/%d/%m %H:%M')

df['time'] = df['time'] + pd.Timedelta('03:00:00')

df.index=df.time
df.drop(columns=['time','year','date'],axis=1,inplace=True)

