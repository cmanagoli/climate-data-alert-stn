import numpy as np
import pandas as pd
import datetime as dt
import matplotlib.dates as mdates
import matplotlib.units as munits
import matplotlib.pyplot as plt

# Create Numpy array of 365 days for x-axis
# Year is arbitrary
days = np.arange('2001-01', '2002-01', dtype='datetime64[D]')


# Get mean temperature data
# 1951
data = pd.read_csv(r'Data\1951.csv')
temp1951 = data['Mean Temp (°C)'].values
# 1961
data = pd.read_csv(r'Data\1961.csv')
temp1961 = data['Mean Temp (°C)'].values
# 1971
data = pd.read_csv(r'Data\1971.csv')
temp1971 = data['Mean Temp (°C)'].values
# 1981
data = pd.read_csv(r'Data\1981.csv')
temp1981 = data['Mean Temp (°C)'].values
# 1991
data = pd.read_csv(r'Data\1991.csv')
temp1991 = data['Mean Temp (°C)'].values
# 2001
data = pd.read_csv(r'Data\2001.csv')
temp2001 = data['Mean Temp (°C)'].values
# 2006
data = pd.read_csv(r'Data\2006.csv')
temp2006 = data['Mean Temp (°C)'].values


# Plot data
plt.plot_date(days, temp1951, color = '#4b53e7', linestyle = 'solid', linewidth = 1, marker = ',', label = '1951', xdate = True, ydate = False)
plt.plot_date(days, temp1961, color = '#171ea6', linestyle = 'solid', linewidth = 1, marker = ',', label = '1961', xdate = True, ydate = False)
plt.plot_date(days, temp1971, color = '#1aa5c1', linestyle = 'solid', linewidth = 1, marker = ',', label = '1971', xdate = True, ydate = False)
plt.plot_date(days, temp1981, color = '#1ac17e', linestyle = 'solid', linewidth = 1, marker = ',', label = '1981', xdate = True, ydate = False)
plt.plot_date(days, temp1991, color = '#33c11a', linestyle = 'solid', linewidth = 1, marker = ',', label = '1991', xdate = True, ydate = False)
plt.plot_date(days, temp2001, color = '#ecec13', linestyle = 'solid', linewidth = 1, marker = ',', label = '2001', xdate = True, ydate = False)
plt.plot_date(days, temp2006, color = '#ec1313', linestyle = 'solid', linewidth = 1, marker = ',', label = '2006', xdate = True, ydate = False)

plt.xlabel('Days (Jan - Dec) -->')
plt.ylabel('Mean Daily Temperature (°C)')
plt.title('Mean Daily Temperature Data for Alert Weather Station over 56 Years')
plt.legend()
plt.show()
