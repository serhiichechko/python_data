from matplotlib import pyplot as plt
import pandas as pd
import matplotlib.dates as mpd
import matplotlib.ticker as ticker

plt.style.use('seaborn')
# import data (value, columns)
data = pd.read_csv('https://gist.githubusercontent.com/serhiichechko/4468779ae9f6ed9069355ba2d1d4b4e4/raw'
                   '/eb7ee691709c1cfcf273dd377c3b020c23e5c4f0/dataset_md0419-20.csv')
dt = data['mmdd']
qnt_19 = data['qnt19']
sum_top_19 = data['sum19']
qnt_20 = data['qnt20']
sum_top_20 = data['sum20']

fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1)

ax1.plot(dt, sum_top_19, marker='.', label='sum_19')
ax1.plot(dt, sum_top_20, marker='.', label='sum_20')
ax2.plot(dt, qnt_19, marker='.', label='qnt_19')
ax2.plot(dt, qnt_20, marker='.', label='qnt_20')


# ax.xaxis.set_major_locator(ticker.MultipleLocator(1))
# ax.xaxis.set_minor_locator(ticker.MultipleLocator(1))
ax1.yaxis.set_major_locator(ticker.MultipleLocator(200000))
ax2.yaxis.set_major_locator(ticker.MultipleLocator(100))

ax1.legend()
# ax1.set_xlabel('month-day')
ax1.set_ylabel('sum (uah)', fontsize=10)
ax1.set_title('Incoming orders per day (sum, qnt)', fontsize=10)

ax2.legend()
ax2.set_xlabel('month-day', fontsize=10)
ax2.set_ylabel('quantity', fontsize=10)
# ax2.set_title('Incoming orders (by quantity)')

plt.grid(True)
plt.tight_layout()

fig.set_figwidth(12)
fig.set_figheight(8)

plt.show()
