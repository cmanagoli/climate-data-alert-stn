# converter = mdates.ConciseDateConverter()
# munits.registry[np.datetime64] = converter
# munits.registry[datetime.date] = converter
# munits.registry[datetime.datetime] = converter


# Convert to Numpy array
xvals = data['Date/Time'].values
yvals = data['Mean Temp (°C)'].values

fig = plt.figure(dpi=100, figsize=(14, 7))
ax = fig.add_axes([0,0,1,1])
l1 = ax.plot(xvals, yvals, 'ys--', label='1961')
ax.xaxis.set_major_formatter(mdates.DateFormatter('%m-%d'))
plt.tick_params(axis='both', which='major', labelsize=5)
ax.legend()
plt.show()

import matplotlib.dates as mdates
import matplotlib.pyplot as plt 

fig = plt.figure()
ax = fig.add_subplot(111)
plt.plot(date, price , label="Price")
ax.xaxis.set_major_formatter(mdates.DateFormatter('%m-%d'))