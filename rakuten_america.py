import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from fbprophet import Prophet

data=pd.DataFrame()
file_name='rakutenindex.csv'
data2=pd.read_csv(file_name,skiprows=1,header=None,names=['ds','y'],dtype={"ds":str, 'y':int})

data=data.append(data2)

data.head()
print(data.dtypes)

#2020年12月30日現在でのデータ量
len(data)

data.describe()


data.head()

#1000日後の予測

future_data = model.make_future_dataframe(periods=1000, freq = 'd')
future_data = future_data[future_data['ds'].dt.weekday < 5]

forecast_data = model.predict(future_data)

fig = model.plot(forecast_data)


model.plot_components(forecast_data)

