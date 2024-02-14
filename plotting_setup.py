import matplotlib.ticker as ticker
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams.update(matplotlib.rcParamsDefault)
plt.style.use('bmh')

plt.rcParams['xtick.major.size'] = 5.0
plt.rcParams['xtick.minor.size'] = 3.0
plt.rcParams['axes.facecolor'] =  'white'
plt.rcParams['axes.grid'] = False
plt.rcParams['axes.edgecolor'] = 'black'
plt.rcParams['patch.edgecolor'] =  'black'
plt.rcParams['axes.linewidth'] = 2.5
plt.rcParams['ytick.minor.visible'] = True
plt.rcParams['ytick.minor.width'] = 2
plt.rcParams['ytick.minor.size'] = 4
plt.rcParams['ytick.major.size'] = 6
plt.rcParams['ytick.major.width'] = 2

plt.rcParams['xtick.minor.visible'] = True
plt.rcParams['xtick.minor.width'] = 2
plt.rcParams['xtick.minor.size'] = 4
plt.rcParams['xtick.major.size'] = 6
plt.rcParams['xtick.major.width'] = 2

plt.rcParams['xtick.top'] = False